#
# Copyright (c) 2020 Vitalis Salis.
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
import ast
import os
import re

from pycg_extended import utils
from pycg_extended.machinery.definitions import Definition
from pycg_extended.processing.usedef_processor import UseDefProcessor

disable_for_testing_other_implementaions = False


class ProcessingBase(ast.NodeVisitor):
    def __init__(self, filename, modname, modules_analyzed):
        self.modname = modname

        self.modules_analyzed = modules_analyzed
        self.modules_analyzed.add(self.modname)

        self.filename = os.path.abspath(filename)

        self.contents = utils.read_input_file(self.filename)

        self.name_stack = []
        self.method_stack = []
        self.last_called_names = None

        # NOTE: Flow Sensitive
        self.usedefprocessor = UseDefProcessor(filename)
        # self.usedefprocessor.analyze()

    def get_modules_analyzed(self):
        return self.modules_analyzed

    def merge_modules_analyzed(self, analyzed):
        self.modules_analyzed = self.modules_analyzed.union(analyzed)

    @property
    def current_ns(self):
        return ".".join(self.name_stack)

    @property
    def current_method(self):
        return ".".join(self.method_stack)

    def visit_Module(self, node):
        self.name_stack.append(self.modname)
        self.method_stack.append(self.modname)
        self.scope_manager.get_scope(self.modname).reset_counters()
        self.generic_visit(node)
        self.method_stack.pop()
        self.name_stack.pop()

    def visit_FunctionDef(self, node):
        # NOTE: Flow Sensitive
        self.name_stack.append("{}:{}".format(node.name, node.lineno))
        self.method_stack.append("{}:{}".format(node.name, node.lineno))
        self.scope_manager.get_scope(self.current_ns).reset_counters()
        for stmt in node.body:
            self.visit(stmt)
        self.method_stack.pop()
        self.name_stack.pop()

    def visit_Lambda(self, node, lambda_name=None):
        lambda_ns = utils.join_ns(
            self.current_ns, "{}:{}".format(lambda_name, node.lineno)
        )
        if not self.scope_manager.get_scope(lambda_ns):
            self.scope_manager.create_scope(
                lambda_ns, self.scope_manager.get_scope(self.current_ns)
            )
        self.name_stack.append("{}:{}".format(lambda_name, node.lineno))
        self.method_stack.append("{}:{}".format(lambda_name, node.lineno))
        self.visit(node.body)
        self.method_stack.pop()
        self.name_stack.pop()

    def visit_For(self, node):
        for item in node.body:
            self.visit(item)

    def visit_Dict(self, node):
        counter = self.scope_manager.get_scope(self.current_ns).inc_dict_counter()
        dict_name = utils.get_dict_name(counter)

        sc = self.scope_manager.get_scope(utils.join_ns(self.current_ns, dict_name))
        if not sc:
            return
        self.name_stack.append(dict_name)
        sc.reset_counters()
        for key, val in zip(node.keys, node.values):
            if key:
                self.visit(key)
            if val:
                self.visit(val)
        self.name_stack.pop()

    def visit_List(self, node):
        counter = self.scope_manager.get_scope(self.current_ns).inc_list_counter()
        list_name = utils.get_list_name(counter)

        sc = self.scope_manager.get_scope(utils.join_ns(self.current_ns, list_name))
        if not sc:
            return
        self.name_stack.append(list_name)
        sc.reset_counters()
        for elt in node.elts:
            self.visit(elt)
        self.name_stack.pop()

    def visit_ListComp(self, node):
        counter = self.scope_manager.get_scope(self.current_ns).inc_list_counter()
        list_name = utils.get_list_name(counter)

        sc = self.scope_manager.get_scope(utils.join_ns(self.current_ns, list_name))
        if not sc:
            return
        self.name_stack.append(list_name)
        sc.reset_counters()
        self.visit(node.elt)
        for _node in list(ast.walk(node)):
            self.visit(_node)
        self.name_stack.pop()

    def visit_BinOp(self, node):
        self.visit(node.left)
        self.visit(node.right)

    def visit_ClassDef(self, node):
        # NOTE: Flow Sensitive
        self.name_stack.append("{}:{}".format(node.name, node.lineno))
        self.method_stack.append("{}:{}".format(node.name, node.lineno))
        self.scope_manager.get_scope(self.current_ns).reset_counters()
        for stmt in node.body:
            self.visit(stmt)
        self.method_stack.pop()
        self.name_stack.pop()

    def visit_Tuple(self, node):
        for elt in node.elts:
            self.visit(elt)

    def _handle_assign(self, targetns, decoded):
        defi = self.def_manager.get(targetns)
        if not defi:
            defi = self.def_manager.create(targetns, utils.constants.NAME_DEF)

        # check if decoded is iterable
        try:
            iter(decoded)
        except TypeError:
            return defi

        if self.current_method == self.modname:
            defi.get_name_pointer().clear_pointers()

        for d in decoded:
            if isinstance(d, Definition):
                # if self.current_method == self.modname:
                #     defi.get_name_pointer().add(d.get_ns())
                # else:
                if (
                    targetns.startswith("pandas.core.series.Series")
                    and d.class_ref == "numpy.ndarray"
                ):
                    pass
                else:
                    defi.get_name_pointer().add(d.get_ns())
            else:
                defi.get_lit_pointer().add(d)
        return defi

    def _visit_return(self, node):
        if not node or not node.value:
            return

        self.visit(node.value)

        return_ns = utils.join_ns(self.current_ns, utils.constants.RETURN_NAME)
        self._handle_assign(return_ns, self.decode_node(node.value))

    def _get_target_ns(self, target):
        if isinstance(target, ast.Name):
            # NOTE: Flow Sensitive
            # return [utils.join_ns(self.current_ns, target.id)]
            return [
                utils.join_ns(
                    self.current_ns, "{}:{}".format(target.id, str(target.lineno))
                )
            ]
        if isinstance(target, ast.Attribute):
            bases = self._retrieve_base_names(target)
            res = []
            for base in bases:
                res.append(utils.join_ns(base, target.attr))
            return res
        if isinstance(target, ast.Subscript):
            return self.retrieve_subscript_names(target)
        return []

    def _visit_assign(self, value, targets):
        self.visit(value)

        decoded = self.decode_node(value)

        def do_assign(decoded, target):
            self.visit(target)
            if isinstance(target, ast.Tuple):
                for pos, elt in enumerate(target.elts):
                    if decoded:
                        if not isinstance(decoded, Definition) and pos < len(decoded):
                            do_assign(decoded[pos], elt)
            else:
                targetns = self._get_target_ns(target)
                for tns in targetns:
                    if not tns:
                        continue
                    defi = self._handle_assign(tns, decoded)
                    splitted = tns.split(".")
                    self.scope_manager.handle_assign(
                        ".".join(splitted[:-1]), splitted[-1], defi
                    )

        for target in targets:
            do_assign(decoded, target)

    def decode_node(self, node):
        # NOTE: Debug
        if hasattr(node, "end_lineno"):
            if node.end_lineno == 12:
                a = True

        if isinstance(node, ast.Name):
            if self.is_builtin(node.id):
                _decoded = []
                _obj_sensitive_name = f"{node.id}<{node.lineno}>"
                obj_defi = self.def_manager.get(_obj_sensitive_name)
                if not obj_defi:
                    obj_defi = self.def_manager.create(
                        _obj_sensitive_name,
                        utils.constants.EXT_DEF,
                        "builtins",
                    )
                _decoded.append(obj_defi)
                return _decoded

            # NOTE: Flow Sensitive
            # if _call not in _call_sites_lineno[_line]:
            if node.lineno in self.usedefprocessor.line_uses:
                _decoded = []
                for _use in self.usedefprocessor.line_uses[node.lineno]:
                    if utils.get_ns_without_last_lineno(_use) == node.id:
                        defi = self.scope_manager.get_def(self.current_ns, _use)
                        if defi:
                            if defi.get_type() == utils.constants.CLS_DEF:
                                regex = f"^({node.id}?)"
                                _obj_sensitive_name = re.sub(
                                    regex,
                                    f"{self.current_ns}.{node.id}<{node.lineno}>",
                                    _use,
                                )
                                obj_defi = self.def_manager.get(_obj_sensitive_name)
                                if not obj_defi:
                                    obj_defi = self.def_manager.create(
                                        _obj_sensitive_name,
                                        utils.constants.OBJ_DEF,
                                        defi,
                                    )
                                _decoded.append(obj_defi)
                                _decoded.append(defi)
                            else:
                                _decoded.append(defi)
                        else:
                            _decoded.append(defi)

                return _decoded
            # HACK: what about this return?
            return [self.scope_manager.get_def(self.current_ns, node.id)]
        elif isinstance(node, ast.Call):
            decoded = self.decode_node(node.func)
            return_defs = []
            for called_def in decoded:
                if not isinstance(called_def, Definition):
                    continue

                return_ns = utils.constants.INVALID_NAME
                if called_def.get_type() == utils.constants.FUN_DEF:
                    return_ns = utils.join_ns(
                        called_def.get_ns(), utils.constants.RETURN_NAME
                    )
                elif called_def.get_type() == utils.constants.CLS_DEF:
                    return_ns = called_def.get_ns()
                elif called_def.get_type() == utils.constants.OBJ_DEF:
                    return_ns = called_def.get_ns()

                if called_def.get_type() == utils.constants.EXT_FUN_DEF:
                    return_ns = called_def.get_ns()
                    ext_info = self.typestub_manager.lookup_return_type(
                        called_def.get_ns(),
                        self.import_manager.module_imports,
                        node=node.func,
                        filename=self.filename,
                    )
                    if ext_info:
                        if ext_info["return_type"]:
                            for _ext_ret_type in ext_info["return_type"]:
                                _obj_sensitive_name = f"{_ext_ret_type}<{node.lineno}>"
                                if not self.def_manager.get(_obj_sensitive_name):
                                    ext_ret_info = (
                                        self.typestub_manager.lookup_return_type(
                                            _ext_ret_type,
                                            self.import_manager.module_imports,
                                            node=node.func,
                                            filename=self.filename,
                                        )
                                    )
                                    if ext_ret_info:
                                        self.def_manager.create(
                                            _obj_sensitive_name,
                                            utils.constants.EXT_DEF,
                                            class_ref=ext_ret_info["return_name"],
                                            ext_def_type=ext_ret_info["type_of_def"],
                                        )

                                defi = self.def_manager.get(_obj_sensitive_name)
                                if defi:
                                    return_defs.append(defi)
                    else:
                        return_ns = called_def.get_ns()
                        defi = self.def_manager.get(return_ns)
                        if defi:
                            return_defs.append(defi)

                # Investigate: how the definitions are changing here from ext_def for normal call
                # NOTE: Assign extdef should be handled here. Approximation
                elif called_def.get_type() == utils.constants.EXT_DEF:
                    if not getattr(self, "closured", None):
                        # ext_info = self.typestub_manager.lookup_return_type(called_def.get_ns(), self.import_manager.module_imports)

                        # if ext_info:

                        #     if ext_info['return_type']:
                        #         for _ext_ret_type in ext_info['return_type']:
                        #             if not self.def_manager.get(_ext_ret_type):
                        #                 self.def_manager.create(_ext_ret_type, utils.constants.EXT_DEF)

                        #             defi = self.def_manager.get(_ext_ret_type)
                        #             if defi:
                        #                 return_defs.append(defi)

                        # else:
                        #     return_ns = called_def.get_ns()
                        #     defi = self.def_manager.get(return_ns)
                        #     if defi:
                        #         return_defs.append(defi)
                        pass
                    else:
                        for name in self.closured.get(called_def.get_ns(), []):
                            ext_info = self.typestub_manager.lookup_return_type(
                                re.sub(r"<\d+>$", "", name),
                                self.import_manager.module_imports,
                                node=node.func,
                                filename=self.filename,
                            )

                            if ext_info:
                                if ext_info["return_type"]:
                                    for _ext_ret_type in ext_info["return_type"]:
                                        _obj_sensitive_name = (
                                            f"{_ext_ret_type}<{node.lineno}>"
                                        )
                                        if not self.def_manager.get(
                                            _obj_sensitive_name
                                        ):
                                            defi = self.def_manager.create(
                                                _obj_sensitive_name,
                                                utils.constants.EXT_DEF,
                                                class_ref=_ext_ret_type,
                                                ext_def_type=ext_info["type_of_def"],
                                            )

                                        defi = self.def_manager.get(_obj_sensitive_name)
                                        if defi:
                                            return_defs.append(defi)

                            if not (ext_info and ext_info["return_type"]):
                                return_ns = name
                                defi = self.def_manager.get(return_ns)
                                if defi:
                                    return_defs.append(defi)
                elif called_def.get_type() == utils.constants.NAME_DEF:
                    if getattr(self, "closured", None) and self.closured.get(
                        called_def.get_ns(), None
                    ):
                        for name in self.closured.get(called_def.get_ns(), []):
                            called_name_defi = self.def_manager.get(name)
                            name_return_ns = utils.constants.INVALID_NAME

                            if called_name_defi.get_type() == utils.constants.FUN_DEF:
                                name_return_ns = utils.join_ns(
                                    called_name_defi.get_ns(),
                                    utils.constants.RETURN_NAME,
                                )
                            elif called_name_defi.get_type() == utils.constants.CLS_DEF:
                                name_return_ns = called_name_defi.get_ns()

                            name_defi = self.def_manager.get(name_return_ns)
                            if name_defi:
                                return_defs.append(name_defi)

                else:
                    defi = self.def_manager.get(return_ns)
                    if defi:
                        return_defs.append(defi)

            return return_defs
        elif isinstance(node, ast.Lambda):
            lambda_counter = self.scope_manager.get_scope(
                self.current_ns
            ).get_lambda_counter()
            lambda_name = utils.get_lambda_name(lambda_counter)
            return [self.scope_manager.get_def(self.current_ns, lambda_name)]
        elif isinstance(node, ast.Tuple):
            decoded = []
            for elt in node.elts:
                decoded.append(self.decode_node(elt))
            return decoded
        elif isinstance(node, ast.UnaryOp):
            decoded_operand = self.decode_node(node.operand)
            return decoded_operand

        elif isinstance(node, ast.BinOp):
            decoded_left = self.decode_node(node.left)
            decoded_right = self.decode_node(node.right)
            # return the non definition types if we're talking about a binop
            # since we only care about the type of the return (num, str, etc)
            # TODO: APSV: Check if literals exist and prefer that
            if not isinstance(decoded_left, Definition):
                return decoded_left
            if not isinstance(decoded_right, Definition):
                return decoded_right
        elif isinstance(node, ast.Attribute):
            names = self._retrieve_attribute_names(node)
            defis = []
            for name in names:
                defi = self.def_manager.get(name)
                if defi:
                    defis.append(defi)
            return defis
        elif isinstance(node, ast.Constant) and isinstance(node.value, bool):
            return [node.value]
        elif isinstance(node, ast.Num):
            return [node.n]
        elif isinstance(node, ast.Str):
            return [node.s]
        elif self._is_literal(node):
            return [node]
        elif isinstance(node, ast.Dict):
            dict_counter = self.scope_manager.get_scope(
                self.current_ns
            ).get_dict_counter()
            dict_name = utils.get_dict_name(dict_counter)
            scope_def = self.scope_manager.get_def(self.current_ns, dict_name)
            return [self.scope_manager.get_def(self.current_ns, dict_name)]
        elif isinstance(node, ast.List):
            list_counter = self.scope_manager.get_scope(
                self.current_ns
            ).get_list_counter()
            list_name = utils.get_list_name(list_counter)
            scope_def = self.scope_manager.get_def(self.current_ns, list_name)
            return [self.scope_manager.get_def(self.current_ns, list_name)]
        elif isinstance(node, ast.ListComp):
            list_counter = self.scope_manager.get_scope(
                self.current_ns
            ).get_list_counter()
            list_name = utils.get_list_name(list_counter)
            scope_def = self.scope_manager.get_def(self.current_ns, list_name)
            return [self.scope_manager.get_def(self.current_ns, list_name)]
        elif isinstance(node, ast.Subscript):
            names = self.retrieve_subscript_names(node)
            defis = []
            for name in names:
                defi = self.def_manager.get(name)
                if defi:
                    defis.append(defi)
            return defis
        elif isinstance(node, ast.Compare):
            # HACK: finish this
            defis = []
            decoded_left = self.decode_node(node.left)
            for defi in decoded_left:
                # if defi.
                defis.append(defi)
            return defis
        return []

    def _is_literal(self, item):
        return (
            isinstance(item, int)
            or isinstance(item, str)
            or isinstance(item, float)
            or isinstance(item, bool)
        )

    def _retrieve_base_names(self, node):
        if not isinstance(node, ast.Attribute):
            raise Exception("The node is not an attribute")

        if not getattr(self, "closured", None):
            return set()

        decoded = self.decode_node(node.value)
        if not decoded:
            return set()

        names = set()
        for name in decoded:
            if not name or not isinstance(name, Definition):
                continue

            for base in self.closured.get(name.get_ns(), []):
                cls = self.class_manager.get(base)
                if not cls:
                    continue

                for item in cls.get_mro():
                    names.add(item)
        return names

    def _retrieve_parent_names(self, node):
        if not isinstance(node, ast.Attribute):
            raise Exception("The node is not an attribute")

        decoded = self.decode_node(node.value)
        if not decoded:
            return set()

        names = set()
        for parent in decoded:
            if not parent or not isinstance(parent, Definition):
                continue
            if getattr(self, "closured", None) and self.closured.get(
                parent.get_ns(), None
            ):
                names = names.union(self.closured.get(parent.get_ns()))
            else:
                names.add(parent.get_ns())
        return names

    def _retrieve_attribute_names(self, node):
        if not getattr(self, "closured", None):
            return set()

        # if node.attr == "values":
        #     print()

        parent_names = self._retrieve_parent_names(node)
        names = set()
        for parent_name in parent_names:
            for name in self.closured.get(parent_name, []):
                defi = self.def_manager.get(name)
                if not defi:
                    continue
                if defi.get_type() == utils.constants.CLS_DEF:
                    cls_names = self.find_cls_fun_ns(defi.get_ns(), node.attr)
                    if cls_names:
                        names = names.union(cls_names)
                if defi.get_type() in [
                    utils.constants.FUN_DEF,
                    utils.constants.MOD_DEF,
                ]:
                    # NOTE: find funtion definition line.
                    # HACK: Do this better? should change to "." in logic?
                    _func_full_ns = utils.join_ns(name, node.attr)
                    for _def in self.def_manager.get_defs().keys():
                        if utils.get_ns_without_last_lineno(_def) == (_func_full_ns):
                            if (
                                len(_def.split(_func_full_ns)) == 2
                                and not _def.split(_func_full_ns)[0]
                            ):
                                if (
                                    len(_def.split(_func_full_ns)[1].split(":")) == 2
                                    and not _def.split(_func_full_ns)[1].split(":")[0]
                                ):
                                    # because "func_1" split func --> '', 1
                                    defi = self.def_manager.get(_def)
                                    names.add(_def)
                                    break

                if defi.get_type() == utils.constants.OBJ_DEF:
                    cls_names = self.find_cls_fun_ns(defi.class_ref.get_ns(), node.attr)
                    if cls_names:
                        names = names.union(cls_names)
                    # names.add(utils.join_ns(name, node.attr))
                if defi.get_type() == utils.constants.EXT_DEF:
                    # HACK: extenral attributes can lead to infinite loops
                    # Identify them here
                    # if node.attr in name:
                    #     continue
                    # ext_name = utils.join_ns(name, node.attr)
                    # ext_info = self.typestub_manager.lookup_return_type(ext_name)

                    # if defi.fullns == 'pandas.core.frame.DataFrame':
                    #     class_funcs = self.typestub_manager.get_methods_of_class(defi.fullns)
                    #     if node.attr not in class_funcs:
                    #         # trying to access the dataframe column as attribute
                    #         ext_name = "pandas.core.series.Series"
                    #     else:
                    #         ext_name = utils.join_ns("pandas.core.frame.DataFrame", node.attr)

                    # else:
                    #     ext_name = utils.join_ns(name, node.attr)

                    if (
                        defi.ext_def_type == "class"
                        and not disable_for_testing_other_implementaions
                    ):
                        if defi.class_ref in [
                            "pandas.core.frame.DataFrame",
                            "pandas.core.groupby.generic.DataFrameGroupBy",
                        ]:
                            class_funcs = self.typestub_manager.get_methods_of_class(
                                defi.class_ref
                            )
                            if node.attr not in class_funcs:
                                # trying to access the dataframe column as attribute
                                ext_name = (
                                    "pandas.core.series.Series"
                                    if (defi.class_ref == "pandas.core.frame.DataFrame")
                                    else "pandas.core.groupby.generic.SeriesGroupBy"
                                )

                            else:
                                if node.attr in ["iloc", "loc", "values"]:
                                    ext_name = (
                                        "pandas.core.frame.DataFrame"
                                        if (
                                            defi.class_ref
                                            == "pandas.core.frame.DataFrame"
                                        )
                                        else "pandas.core.groupby.generic.DataFrameGroupBy"
                                    )
                                else:
                                    _ext_name = (
                                        "pandas.core.frame.DataFrame"
                                        if (
                                            defi.class_ref
                                            == "pandas.core.frame.DataFrame"
                                        )
                                        else "pandas.core.groupby.generic.DataFrameGroupBy"
                                    )
                                    ext_name = utils.join_ns(_ext_name, node.attr)
                        elif defi.class_ref in ["pandas.core.series.Series"]:
                            if node.attr in ["values"]:
                                ext_name = "numpy.ndarray"
                            else:
                                ext_name = utils.join_ns(defi.class_ref, node.attr)
                        elif defi.class_ref in ["numpy.ndarray"]:
                            class_funcs = self.typestub_manager.get_methods_of_class(
                                defi.class_ref
                            )
                            if node.attr not in class_funcs:
                                ext_name = "numpy.ndarray"
                            else:
                                ext_name = utils.join_ns(defi.class_ref, node.attr)

                        else:
                            ext_name = utils.join_ns(defi.class_ref, node.attr)
                    else:
                        obj_ins_name = re.sub(r"<\d+>$", "", name)
                        ext_name = utils.join_ns(obj_ins_name, node.attr)

                    # if ext_name in ['pandas.core.frame.DataFrame.values', 'pandas.core.series.Series.values']:
                    #     ext_name = "pandas.core.frame.DataFrame.to_numpy"

                    ext_info = self.typestub_manager.lookup_return_type(
                        ext_name,
                        self.import_manager.module_imports,
                        node=node,
                        filename=self.filename,
                    )
                    # if not ext_info:
                    #     print("No ext_info", ext_name)
                    # else:
                    #     if not ext_info['return_type']:
                    #         print("No return_type ext_info", ext_name)

                    # if node.attr == "drop":
                    #     print("debug")
                    if ext_info:
                        if ext_info["type_of_def"] in ["class", "alias"]:
                            # HACK: approximating dataframe series access as both ndarray and series
                            # if ext_name == "numpy.ndarray" and defi.class_ref in [
                            #     "pandas.core.series.Series"
                            # ]:
                            #     ext_info["return_type"].append(
                            #         "pandas.core.series.Series"
                            #     )

                            for _ext_ret_type in ext_info["return_type"]:
                                _obj_sensitive_name = f"{_ext_ret_type}<{node.lineno}>"
                                if not self.def_manager.get(_obj_sensitive_name):
                                    defi = self.def_manager.create(
                                        _obj_sensitive_name,
                                        utils.constants.EXT_DEF,
                                        class_ref=_ext_ret_type,
                                        ext_def_type=ext_info["type_of_def"],
                                    )

                                names.add(_obj_sensitive_name)

                        elif ext_info["type_of_def"] in [
                            "function",
                            "constant",
                            "instance",
                        ]:
                            # ext_name = utils.join_ns(_ext_type_def_ret, node.attr)
                            # ext_name = _ext_type_def_name

                            # _obj_sensitive_name = f"{ext_info['return_name']}<{node.lineno}>"

                            _obj_sensitive_name = ext_info["return_name"]
                            if _obj_sensitive_name:
                                if not self.def_manager.get(_obj_sensitive_name):
                                    self.def_manager.create(
                                        _obj_sensitive_name,
                                        utils.constants.EXT_FUN_DEF,
                                        class_ref=ext_info["return_name"],
                                        ext_def_type=ext_info["type_of_def"],
                                    )

                                names.add(_obj_sensitive_name)
                        elif ext_info["type_of_def"] == None:
                            _obj_sensitive_name = (
                                f"{ext_info['return_name']}<{node.lineno}>"
                            )
                            if not self.def_manager.get(_obj_sensitive_name):
                                self.def_manager.create(
                                    _obj_sensitive_name,
                                    utils.constants.EXT_DEF,
                                    class_ref=ext_info["return_name"],
                                    ext_def_type=ext_info["type_of_def"],
                                )

                            names.add(_obj_sensitive_name)
                    # else:
                    #     if not self.def_manager.get(ext_name):
                    #         self.def_manager.create(ext_name, utils.constants.EXT_DEF)
                    #     names.add(ext_name)

                # if defi.get_type() == utils.constants.NAME_DEF:
                #     if name.startswith("pandas.core.frame.DataFrame") and name != "pandas.core.frame.DataFrame":
                #         # a pandas column access pandas.core.frame.DataFrame.<col>
                #         # class_funcs = self.typestub_manager.get_methods_of_class(defi.fullns)
                #         ext_name = utils.join_ns("pandas.core.series.Series", node.attr)
                #         ext_info = self.typestub_manager.lookup_return_type(ext_name, self.import_manager.module_imports)
                #         if ext_info:
                #             ext_name = ext_info['return_name']
                #         if not self.def_manager.get(ext_name):
                #             self.def_manager.create(ext_name, utils.constants.EXT_DEF)
                #         names.add(ext_name)

        return names

    def iterate_call_args(self, defi, node):
        for pos, arg in enumerate(node.args):
            self.visit(arg)
            decoded = self.decode_node(arg)
            if defi.is_function_def():
                pos_arg_names = defi.get_name_pointer().get_pos_arg(pos)
                # if arguments for this position exist update their namespace
                if not pos_arg_names:
                    continue
                for name in pos_arg_names:
                    arg_def = self.def_manager.get(name)
                    if not arg_def:
                        continue
                    for d in decoded:
                        if isinstance(d, Definition):
                            arg_def.get_name_pointer().add(d.get_ns())
                        else:
                            arg_def.get_lit_pointer().add(d)
            else:
                for d in decoded:
                    if isinstance(d, Definition):
                        defi.get_name_pointer().add_pos_arg(pos, None, d.get_ns())
                    else:
                        defi.get_name_pointer().add_pos_lit_arg(pos, None, d)

        for keyword in node.keywords:
            self.visit(keyword.value)
            decoded = self.decode_node(keyword.value)
            if defi.is_function_def():
                arg_names = defi.get_name_pointer().get_arg(keyword.arg)
                if not arg_names:
                    continue
                for name in arg_names:
                    arg_def = self.def_manager.get(name)
                    if not arg_def:
                        continue
                    for d in decoded:
                        if isinstance(d, Definition):
                            arg_def.get_name_pointer().add(d.get_ns())
                        else:
                            arg_def.get_lit_pointer().add(d)
            else:
                for d in decoded:
                    if isinstance(d, Definition):
                        defi.get_name_pointer().add_arg(keyword.arg, d.get_ns())
                    else:
                        defi.get_name_pointer().add_lit_arg(keyword.arg, d)

    def retrieve_subscript_names(self, node):
        if not isinstance(node, ast.Subscript):
            raise Exception("The node is not an subcript")

        if not getattr(self, "closured", None):
            return set()

        if getattr(node.slice, "value", None) and self._is_literal(node.slice.value):
            sl_names = [node.slice.value]
        else:
            sl_names = self.decode_node(node.slice)

        val_names = self.decode_node(node.value)

        decoded_vals = set()
        keys = set()
        full_names = set()
        # get all names associated with this variable name
        for n in val_names:
            if n and isinstance(n, Definition) and self.closured.get(n.get_ns(), None):
                decoded_vals |= self.closured.get(n.get_ns())
        for s in sl_names:
            if isinstance(s, Definition) and self.closured.get(s.get_ns(), None):
                # we care about the literals pointed by the name
                # not the namespaces, so retrieve the literals pointed
                for name in self.closured.get(s.get_ns()):
                    defi = self.def_manager.get(name)
                    if not defi:
                        continue
                    keys |= defi.get_lit_pointer().get()
            elif isinstance(s, str):
                keys.add(s)
            elif isinstance(s, int):
                keys.add(utils.get_int_name(s))

        # NOTE
        for d in decoded_vals:
            if d.startswith("pandas.core.frame.DataFrame") or d.startswith(
                "pandas.core.groupby.generic.DataFrameGroupBy"
            ):
                if (
                    isinstance(node.slice, (ast.ListComp, ast.ExtSlice))
                    or isinstance(node.slice, ast.List)
                    or isinstance(node.slice, ast.Slice)
                    or isinstance(node.slice, ast.Tuple)
                ):
                    if d.startswith("pandas.core.frame.DataFrame"):
                        full_ns = "pandas.core.frame.DataFrame"
                    elif d.startswith("pandas.core.groupby.generic.DataFrameGroupBy"):
                        full_ns = "pandas.core.groupby.generic.DataFrameGroupBy"
                    _obj_sensitive_name = f"{full_ns}<{node.lineno}>"
                    if not self.def_manager.get(_obj_sensitive_name):
                        ext_info = self.typestub_manager.lookup_return_type(
                            full_ns,
                            self.import_manager.module_imports,
                            node=node.value,
                            filename=self.filename,
                        )
                        if ext_info:
                            self.def_manager.create(
                                _obj_sensitive_name,
                                utils.constants.EXT_DEF,
                                class_ref=full_ns,
                                ext_def_type=ext_info["type_of_def"],
                            )

                    if self.def_manager.get(_obj_sensitive_name):
                        full_names.add(_obj_sensitive_name)

                elif isinstance(node.slice, ast.Compare):
                    # handle statements of the form: survived = train[train['Survived']==1]['Survived'].value_counts()
                    if isinstance(node.slice.left, (ast.Subscript, ast.Attribute)):
                        nested_sub_decode = self.decode_node(node.slice.left.value)
                        for _nd in nested_sub_decode:
                            if self.closured.get(_nd.get_ns(), None):
                                for nd_vals in self.closured.get(_nd.get_ns(), None):
                                    if nd_vals.startswith(
                                        "pandas.core.frame.DataFrame"
                                    ):
                                        full_ns = "pandas.core.frame.DataFrame"
                                        _obj_sensitive_name = (
                                            f"{full_ns}<{node.lineno}>"
                                        )
                                        if not self.def_manager.get(
                                            _obj_sensitive_name
                                        ):
                                            ext_info = self.typestub_manager.lookup_return_type(
                                                full_ns,
                                                self.import_manager.module_imports,
                                                node=node.slice,
                                                filename=self.filename,
                                            )
                                            if ext_info:
                                                self.def_manager.create(
                                                    _obj_sensitive_name,
                                                    utils.constants.EXT_DEF,
                                                    class_ref=full_ns,
                                                    ext_def_type=ext_info[
                                                        "type_of_def"
                                                    ],
                                                )

                                        if self.def_manager.get(_obj_sensitive_name):
                                            full_names.add(_obj_sensitive_name)

                elif isinstance(node.slice, ast.Name):
                    # Handle cases where slice is a Name pointing to a list
                    full_ns = None
                    for s in sl_names:
                        if isinstance(s, Definition) and self.closured.get(
                            s.get_ns(), None
                        ):
                            for name in self.closured.get(s.get_ns()):
                                if re.search("<list\d+>$", name):
                                    full_ns = "pandas.core.frame.DataFrame"
                                elif re.search("numpy.ndarray<\d+>$", name):
                                    full_ns = "pandas.core.frame.DataFrame"

                    # not a list, could be Series. HACK: maybe return both when not sure?
                    if not full_ns:
                        full_ns = "pandas.core.series.Series"

                    _obj_sensitive_name = f"{full_ns}<{node.lineno}>"
                    if not self.def_manager.get(_obj_sensitive_name):
                        ext_info = self.typestub_manager.lookup_return_type(
                            full_ns,
                            self.import_manager.module_imports,
                            node=node.slice,
                            filename=self.filename,
                        )
                        if ext_info:
                            self.def_manager.create(
                                _obj_sensitive_name,
                                utils.constants.EXT_DEF,
                                class_ref=full_ns,
                                ext_def_type=ext_info["type_of_def"],
                            )

                    if self.def_manager.get(_obj_sensitive_name):
                        full_names.add(_obj_sensitive_name)
                elif isinstance(node.slice, ast.Constant):
                    if "DataFrameGroupBy" in d:
                        full_ns = "pandas.core.groupby.generic.SeriesGroupBy"
                    else:
                        full_ns = "pandas.core.series.Series"
                    _obj_sensitive_name = f"{full_ns}<{node.lineno}>"
                    if not self.def_manager.get(_obj_sensitive_name):
                        ext_info = self.typestub_manager.lookup_return_type(
                            full_ns,
                            self.import_manager.module_imports,
                            node=node.slice,
                            filename=self.filename,
                        )
                        if ext_info:
                            self.def_manager.create(
                                _obj_sensitive_name,
                                utils.constants.EXT_DEF,
                                class_ref=full_ns,
                                ext_def_type=ext_info["type_of_def"],
                            )

                    if self.def_manager.get(_obj_sensitive_name):
                        full_names.add(_obj_sensitive_name)
                elif isinstance(node.slice, ast.Index):
                    # Dataframe access with Index will return a series
                    if d.startswith("pandas.core.frame.DataFrame") or d.startswith(
                        "pandas.core.groupby.generic.DataFrameGroupBy"
                    ):
                        if isinstance(node.slice.value, ast.Compare):
                            full_ns = (
                                "pandas.core.frame.DataFrame"
                                if d.startswith("pandas.core.frame.DataFrame")
                                else "pandas.core.groupby.generic.DataFrameGroupBy"
                            )
                        elif isinstance(node.slice.value, ast.Name):
                            _val_def = self.decode_node(node.slice.value)
                            if _val_def:
                                # HACK: only one of points-to
                                if not _val_def[0]:
                                    # Could be a for loop reference, approximate as series
                                    full_ns = (
                                        "pandas.core.series.Series"
                                        if d.startswith("pandas.core.frame.DataFrame")
                                        else "pandas.core.groupby.generic.SeriesGroupBy"
                                    )
                                else:
                                    # df[["features",..]] returns a dataframe
                                    is_list = any(
                                        [
                                            x if "list" in x else False
                                            for x in self.closured.get(
                                                _val_def[0].get_ns(), None
                                            )
                                        ]
                                    )
                                    is_numpy = any(
                                        [
                                            x if "numpy" in x else False
                                            for x in self.closured.get(
                                                _val_def[0].get_ns(), None
                                            )
                                        ]
                                    )
                                    if any([is_list, is_numpy]):
                                        full_ns = (
                                            "pandas.core.frame.DataFrame"
                                            if d.startswith(
                                                "pandas.core.frame.DataFrame"
                                            )
                                            else "pandas.core.groupby.generic.DataFrameGroupBy"
                                        )
                                    else:
                                        full_ns = (
                                            "pandas.core.series.Series"
                                            if d.startswith(
                                                "pandas.core.frame.DataFrame"
                                            )
                                            else "pandas.core.groupby.generic.SeriesGroupBy"
                                        )

                            else:
                                full_ns = (
                                    "pandas.core.series.Series"
                                    if d.startswith("pandas.core.frame.DataFrame")
                                    else "pandas.core.groupby.generic.SeriesGroupBy"
                                )
                        if isinstance(node.slice.value, ast.Tuple):
                            # list with more than 1 element will return a Dataframe
                            if len(node.slice.value.elts) > 1:
                                full_ns = (
                                    "pandas.core.frame.DataFrame"
                                    if d.startswith("pandas.core.frame.DataFrame")
                                    else "pandas.core.groupby.generic.DataFrameGroupBy"
                                )
                            else:
                                full_ns = (
                                    "pandas.core.series.Series"
                                    if d.startswith("pandas.core.frame.DataFrame")
                                    else "pandas.core.groupby.generic.SeriesGroupBy"
                                )

                        elif isinstance(node.slice.value, ast.Constant):
                            if "DataFrameGroupBy" in d:
                                full_ns = "pandas.core.groupby.generic.SeriesGroupBy"
                            else:
                                full_ns = "pandas.core.series.Series"
                            _obj_sensitive_name = f"{full_ns}<{node.lineno}>"
                            if not self.def_manager.get(_obj_sensitive_name):
                                ext_info = self.typestub_manager.lookup_return_type(
                                    full_ns,
                                    self.import_manager.module_imports,
                                    node=node.slice,
                                    filename=self.filename,
                                )
                                if ext_info:
                                    self.def_manager.create(
                                        _obj_sensitive_name,
                                        utils.constants.EXT_DEF,
                                        class_ref=full_ns,
                                        ext_def_type=ext_info["type_of_def"],
                                    )

                            if self.def_manager.get(_obj_sensitive_name):
                                full_names.add(_obj_sensitive_name)

                        else:
                            approx_ns = (
                                [
                                    "pandas.core.series.Series",
                                    "pandas.core.frame.DataFrame",
                                ]
                                if d.startswith("pandas.core.frame.DataFrame")
                                else [
                                    "pandas.core.groupby.generic.DataFrameGroupBy",
                                    "pandas.core.groupby.generic.SeriesGroupBy",
                                ]
                            )
                            for _ns in approx_ns:
                                _obj_sensitive_name = f"{_ns}<{node.lineno}>"
                                if not self.def_manager.get(_obj_sensitive_name):
                                    ext_info = self.typestub_manager.lookup_return_type(
                                        _ns,
                                        self.import_manager.module_imports,
                                        node=node.slice,
                                        filename=self.filename,
                                    )
                                    if ext_info:
                                        self.def_manager.create(
                                            _obj_sensitive_name,
                                            utils.constants.EXT_DEF,
                                            class_ref=_ns,
                                            ext_def_type=ext_info["type_of_def"],
                                        )

                                if self.def_manager.get(_obj_sensitive_name):
                                    full_names.add(_obj_sensitive_name)
                            continue

                    # elif d.startswith('pandas.core.groupby.generic.DataFrameGroupBy'):
                    #     full_ns = "pandas.core.groupby.generic.SeriesGroupBy"
                    else:
                        continue

                    _obj_sensitive_name = f"{full_ns}<{node.lineno}>"
                    if not self.def_manager.get(_obj_sensitive_name):
                        ext_info = self.typestub_manager.lookup_return_type(
                            full_ns,
                            self.import_manager.module_imports,
                            node=node.slice,
                            filename=self.filename,
                        )
                        if ext_info:
                            self.def_manager.create(
                                _obj_sensitive_name,
                                utils.constants.EXT_DEF,
                                class_ref=full_ns,
                                ext_def_type=ext_info["type_of_def"],
                            )

                    if self.def_manager.get(_obj_sensitive_name):
                        full_names.add(_obj_sensitive_name)
                elif isinstance(node.slice, ast.Call):
                    approx_ns = (
                        ["pandas.core.series.Series", "pandas.core.frame.DataFrame"]
                        if d.startswith("pandas.core.frame.DataFrame")
                        else [
                            "pandas.core.groupby.generic.DataFrameGroupBy",
                            "pandas.core.groupby.generic.SeriesGroupBy",
                        ]
                    )
                    for _ns in approx_ns:
                        _obj_sensitive_name = f"{_ns}<{node.lineno}>"
                        if not self.def_manager.get(_obj_sensitive_name):
                            ext_info = self.typestub_manager.lookup_return_type(
                                _ns,
                                self.import_manager.module_imports,
                                node=node.slice,
                                filename=self.filename,
                            )
                            if ext_info:
                                self.def_manager.create(
                                    _obj_sensitive_name,
                                    utils.constants.EXT_DEF,
                                    class_ref=_ns,
                                    ext_def_type=ext_info["type_of_def"],
                                )

                        if self.def_manager.get(_obj_sensitive_name):
                            full_names.add(_obj_sensitive_name)
                    continue

                elif isinstance(node.slice, ast.Subscript):
                    approx_ns = (
                        ["pandas.core.series.Series", "pandas.core.frame.DataFrame"]
                        if d.startswith("pandas.core.frame.DataFrame")
                        else [
                            "pandas.core.groupby.generic.DataFrameGroupBy",
                            "pandas.core.groupby.generic.SeriesGroupBy",
                        ]
                    )
                    for _ns in approx_ns:
                        _obj_sensitive_name = f"{_ns}<{node.lineno}>"
                        if not self.def_manager.get(_obj_sensitive_name):
                            ext_info = self.typestub_manager.lookup_return_type(
                                _ns,
                                self.import_manager.module_imports,
                                node=node.slice,
                                filename=self.filename,
                            )
                            if ext_info:
                                self.def_manager.create(
                                    _obj_sensitive_name,
                                    utils.constants.EXT_DEF,
                                    class_ref=_ns,
                                    ext_def_type=ext_info["type_of_def"],
                                )

                        if self.def_manager.get(_obj_sensitive_name):
                            full_names.add(_obj_sensitive_name)
                    continue

            else:
                for key in keys:
                    # check for existence of var name and key combination
                    str_key = str(key)
                    if isinstance(key, int):
                        str_key = utils.get_int_name(key)
                    full_ns = utils.join_ns(d, str_key)
                    # # NOTE
                    # if not self.def_manager.get(full_ns):
                    #     self.def_manager.create(full_ns, utils.constants.NAME_DEF)
                    full_names.add(full_ns)

        return full_names

    def retrieve_call_names(self, node):
        names = set()
        if isinstance(node.func, ast.Name):
            # NOTE: Flow Sensitive
            if node.lineno in self.usedefprocessor.line_uses:
                for _use in self.usedefprocessor.line_uses[node.lineno]:
                    if utils.get_ns_without_last_lineno(_use) == node.func.id:
                        defi = self.scope_manager.get_def(self.current_ns, _use)
                        if defi:
                            names |= self.closured.get(defi.get_ns(), None)
                    elif _use == "*":
                        # all_ns = utils.join_ns(self.current_method, node.func.id)
                        all_ns = node.func.id
                        for _defi in self.scope_manager.get_scope(
                            self.current_method
                        ).defs:
                            if utils.get_ns_without_last_lineno(_defi) == all_ns:
                                if (
                                    len(_defi.split(all_ns)) == 2
                                    and not _defi.split(all_ns)[0]
                                ):
                                    if (
                                        len(_defi.split(all_ns)[1].split(":")) == 2
                                        and "."
                                        not in _defi.split(all_ns)[1].split(":")[1]
                                    ):
                                        # HACK: Do this better?
                                        # defi = self.def_manager.get(_defi)
                                        # self.call_sites.add_edge(self.current_method, _defi, node)
                                        defi = self.scope_manager.get_def(
                                            self.current_ns, _defi
                                        )
                                        if defi:
                                            names |= self.closured.get(
                                                defi.get_ns(), None
                                            )
                                        break
            else:
                # NOTE: HACK: Handle lambda cases
                defi = self.scope_manager.get_def(
                    self.current_ns, "{}:{}".format(node.func.id, node.lineno)
                )
                if defi:
                    names = self.closured.get(defi.get_ns(), None)

            if not names:
                # NOTE: beniget does not capture function arguments? how to handle this?
                defi = self.scope_manager.get_def(self.current_ns, node.func.id)
                if defi:
                    names = self.closured.get(defi.get_ns(), None)

        elif isinstance(node.func, ast.Call) and self.last_called_names:
            for name in self.last_called_names:
                return_ns = utils.join_ns(name, utils.constants.RETURN_NAME)
                returns = self.closured.get(return_ns)
                if not returns:
                    continue
                for ret in returns:
                    defi = self.def_manager.get(ret)
                    names.add(defi.get_ns())
        elif isinstance(node.func, ast.Attribute):
            names = self._retrieve_attribute_names(node.func)
        elif isinstance(node.func, ast.Subscript):
            # Calls can be performed only on single indices, not ranges
            full_names = self.retrieve_subscript_names(node.func)
            for n in full_names:
                if self.closured.get(n, None):
                    names |= self.closured.get(n)

        return names

    def analyze_submodules(self, cls, *args, **kwargs):
        imports = self.import_manager.get_imports(self.modname)

        for imp in imports:
            self.analyze_submodule(cls, imp, *args, **kwargs)

    def analyze_submodule(self, cls, imp, *args, **kwargs):
        if imp in self.get_modules_analyzed():
            return

        fname = self.import_manager.get_filepath(imp)

        if (
            not fname
            or not self.import_manager.get_mod_dir() in fname
            or "site-packages" in fname
        ):
            return

        self.import_manager.set_current_mod(imp, fname)

        visitor = cls(fname, imp, *args, **kwargs)
        visitor.analyze()
        self.merge_modules_analyzed(visitor.get_modules_analyzed())

        self.import_manager.set_current_mod(self.modname, self.filename)

    def find_cls_fun_ns(self, cls_name, fn):
        cls = self.class_manager.get(cls_name)
        if not cls:
            return set()

        ext_names = set()
        for item in cls.get_mro():
            # NOTE: Flow Sensitive
            _ns = utils.join_ns(item, fn)
            ns = None
            if _ns not in self.def_manager.defs.keys():
                for _def in self.def_manager.defs.keys():
                    if len(_def.split(_ns)) > 1:
                        # NOTE: HACK: obviously better way to find the line number
                        if (
                            "." not in _def.split(_ns)[1]
                            and _def.split(_ns)[1].startswith(":")
                            and utils.is_int_str(_def.split(_ns)[1].split(":")[1])
                        ):
                            ns = _def
                            break

                # NOTE: HACK: getting external module
                if ns is None:
                    ns = _ns

            else:
                ns = _ns

            # if "__init__" in _ns and not _ns:
            #     ns = _ns

            names = set()
            if getattr(self, "closured", None) and self.closured.get(ns, None):
                names = self.closured[ns]
            else:
                names.add(ns)

            if self.def_manager.get(ns):
                return names

            parent = self.def_manager.get(item)
            if parent and parent.get_type() == utils.constants.EXT_DEF:
                ext_names.add(ns)

        for name in ext_names:
            self.def_manager.create(name, utils.constants.EXT_DEF)
            self.add_ext_mod_node(name)
        return ext_names

    def add_ext_mod_node(self, name):
        ext_modname = name.split(".")[0]
        ext_mod = self.module_manager.get(ext_modname)
        if not ext_mod:
            ext_mod = self.module_manager.create(ext_modname, None, external=True)
            ext_mod.add_method(ext_modname)

        ext_mod.add_method(name)

    def is_builtin(self, name):
        return name in __builtins__
