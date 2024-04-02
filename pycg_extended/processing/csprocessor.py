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

from pycg_extended import utils
from pycg_extended.machinery.callgraph import CallGraph
from pycg_extended.machinery.callsites import CallSites
from pycg_extended.machinery.definitions import Definition
from pycg_extended.processing.base import ProcessingBase


class CallSiteProcessor(ProcessingBase):
    def __init__(
        self,
        filename,
        modname,
        import_manager,
        scope_manager,
        def_manager,
        class_manager,
        module_manager,
        typestub_manager,
        modules_analyzed=None,
        call_sites=None,
        call_args=None,
    ):
        super().__init__(filename, modname, modules_analyzed)
        # parent directory of file
        self.parent_dir = os.path.dirname(filename)

        self.import_manager = import_manager
        self.scope_manager = scope_manager
        self.def_manager = def_manager
        self.class_manager = class_manager
        self.module_manager = module_manager
        self.typestub_manager = typestub_manager

        # self.call_graph = call_graph

        self.call_sites = call_sites
        self.call_args = call_args

        self.closured = self.def_manager.transitive_closure()

    def visit_Module(self, node):
        self.call_sites.add_node(self.modname, self.modname)
        super().visit_Module(node)

    def visit_For(self, node):
        self.visit(node.iter)
        self.visit(node.target)
        # assign target.id to the return value of __next__ of node.iter.it
        # we need to have a visit for on the postprocessor also
        iter_decoded = self.decode_node(node.iter)
        for item in iter_decoded:
            if not isinstance(item, Definition):
                continue
            names = self.closured.get(item.get_ns(), [])
            for name in names:
                iter_ns = utils.join_ns(name, utils.constants.ITER_METHOD)
                next_ns = utils.join_ns(name, utils.constants.NEXT_METHOD)

                # if self.def_manager.get(iter_ns):
                #     self.call_sites.add_edge(self.current_method, iter_ns, node)
                # NOTE: HACK: checking if init exists, remove init lineno from analysis? but python doesnt raise error for multi init.
                for _defi in self.def_manager.get_defs():
                    if utils.get_ns_without_last_lineno(_defi) == iter_ns:
                        if (
                            len(_defi.split(iter_ns)) == 2
                            and not _defi.split(iter_ns)[0]
                        ):
                            if (
                                len(_defi.split(iter_ns)[1].split(":")) == 2
                                and "." not in _defi.split(iter_ns)[1].split(":")[1]
                            ):
                                # HACK: Do this better?
                                # defi = self.def_manager.get(_defi)
                                self.call_sites.add_edge(
                                    self.current_method, _defi, node
                                )
                                break

                # if self.def_manager.get(next_ns):
                #     self.call_sites.add_edge(self.current_method, next_ns, node)
                for _defi in self.def_manager.get_defs():
                    if utils.get_ns_without_last_lineno(_defi) == next_ns:
                        if (
                            len(_defi.split(next_ns)) == 2
                            and not _defi.split(next_ns)[0]
                        ):
                            if (
                                len(_defi.split(next_ns)[1].split(":")) == 2
                                and "." not in _defi.split(next_ns)[1].split(":")[1]
                            ):
                                # HACK: Do this better?
                                # defi = self.def_manager.get(_defi)
                                self.call_sites.add_edge(
                                    self.current_method, _defi, node
                                )
                                break

        super().visit_For(node)

    def visit_Lambda(self, node):
        counter = self.scope_manager.get_scope(self.current_ns).inc_lambda_counter()
        lambda_name = utils.get_lambda_name(counter)
        lambda_fullns = utils.join_ns(self.current_ns, lambda_name)

        self.call_sites.add_node(lambda_fullns, self.modname)

        super().visit_Lambda(node, lambda_name)

    def visit_Raise(self, node):
        if not node.exc:
            return
        self.visit(node.exc)
        decoded = self.decode_node(node.exc)
        for d in decoded:
            if not isinstance(d, Definition):
                continue
            names = self.closured.get(d.get_ns(), [])
            for name in names:
                pointer_def = self.def_manager.get(name)
                if pointer_def.get_type() == utils.constants.CLS_DEF:
                    init_ns = self.find_cls_fun_ns(name, utils.constants.CLS_INIT)
                    for ns in init_ns:
                        self.call_sites.add_edge(self.current_method, ns, node)
                if pointer_def.get_type() == utils.constants.EXT_DEF:
                    self.call_sites.add_edge(self.current_method, name, node)

    def visit_AsyncFunctionDef(self, node):
        self.visit_FunctionDef(node)

    def visit_FunctionDef(self, node):
        for decorator in node.decorator_list:
            self.visit(decorator)
            decoded = self.decode_node(decorator)
            for d in decoded:
                if not isinstance(d, Definition):
                    continue
                names = self.closured.get(d.get_ns(), [])
                for name in names:
                    self.call_sites.add_edge(self.current_method, name, node)

        self.call_sites.add_node(
            utils.join_ns(self.current_ns, "{}:{}".format(node.name, node.lineno)),
            self.modname,
        )
        super().visit_FunctionDef(node)

    def visit_Call(self, node):
        def create_ext_edge(name, ext_modname):
            self.add_ext_mod_node(name)
            self.call_sites.add_node(name, ext_modname)
            self.call_sites.add_edge(self.current_method, name, node)

        # First visit the child function so that on the case of
        #       func()()()
        # we first visit the call to func and then the other calls
        for arg in node.args:
            self.visit(arg)

        for keyword in node.keywords:
            self.visit(keyword.value)

        self.visit(node.func)

        names = self.retrieve_call_names(node)
        if not names:
            # Investigate: could be a case for adding attributes?
            if isinstance(node.func, ast.Attribute) and self.has_ext_parent(node.func):
                # TODO: This doesn't work for cases where there is an assignment of an attribute
                # i.e. import os; lala = os.path; lala.dirname()
                for name in self.get_full_attr_names(node.func):
                    ext_modname = name.split(".")[0]
                    create_ext_edge(name, ext_modname)
                    # Investigate: should add edge to external here?
            elif isinstance(node.func, ast.Attribute):
                for name in self.get_builtin_type_method_calls(node.func):
                    ext_modname = name.split(".")[0]
                    create_ext_edge(name, utils.constants.BUILTIN_NAME)

            elif getattr(node.func, "id", None) and self.is_builtin(node.func.id):
                name = utils.join_ns(utils.constants.BUILTIN_NAME, node.func.id)
                create_ext_edge(name, utils.constants.BUILTIN_NAME)
            return

        self.last_called_names = names
        for pointer in names:
            pointer_def = self.def_manager.get(pointer)
            if not pointer_def or not isinstance(pointer_def, Definition):
                continue
            if pointer_def.is_callable():
                # Fetch args and kwargs
                self.call_args[
                    f"{utils.get_ns_without_obj_lineno(pointer_def.get_ns())}:{node.lineno}"
                ] = {
                    "args": [x.value for x in node.args if isinstance(x, ast.Constant)]
                    + [
                        [y.value for y in x.elts if isinstance(y, ast.Constant)]
                        for x in node.args
                        if isinstance(x, ast.List)
                    ],
                    "kwargs": {
                        x.arg: x.value.value
                        for x in node.keywords
                        if isinstance(x.value, ast.Constant)
                    }
                    | {
                        x.arg: [
                            y.value for y in x.value.elts if isinstance(y, ast.Constant)
                        ]
                        for x in node.keywords
                        if isinstance(x.value, ast.List)
                    },
                }
                if pointer_def.get_type() in [
                    utils.constants.EXT_DEF,
                    utils.constants.EXT_FUN_DEF,
                ]:
                    ext_modname = pointer.split(".")[0]
                    create_ext_edge(pointer, ext_modname)
                    if isinstance(node, ast.Call):
                        if hasattr(node.func, "attr"):
                            if node.func.attr == "apply":
                                for _p in self._retrieve_parent_names(node.func):
                                    if _p.startswith(
                                        "pandas.core.frame.DataFrame"
                                    ) or _p.startswith("pandas.core.series.Series"):
                                        for _arg_node in node.args:
                                            for _d in self.decode_node(_arg_node):
                                                if _d:
                                                    ext_modname = _d.fullns.split(".")[
                                                        0
                                                    ]
                                                    create_ext_edge(
                                                        _d.fullns, ext_modname
                                                    )

                    continue
                self.call_sites.add_edge(self.current_method, pointer, node)

                # TODO: This doesn't work and leads to calls from the decorators
                #    themselves to the function, creating edges to the first decorator
                # for decorator in pointer_def.decorator_names:
                #    dec_names = self.closured.get(decorator, [])
                #    for dec_name in dec_names:
                #        if self.def_manager.get(dec_name).get_type() == utils.constants.FUN_DEF:
                #            self.call_sites.add_edge(self.current_ns, dec_name)

            if pointer_def.get_type() == utils.constants.CLS_DEF:
                init_ns = self.find_cls_fun_ns(pointer, utils.constants.CLS_INIT)

                for ns in init_ns:
                    self.call_sites.add_edge(self.current_method, ns, node)

    def analyze_submodules(self):
        super().analyze_submodules(
            CallSiteProcessor,
            self.import_manager,
            self.scope_manager,
            self.def_manager,
            self.class_manager,
            self.module_manager,
            self.typestub_manager,
            call_sites=self.call_sites,
            modules_analyzed=self.get_modules_analyzed(),
            call_args=self.call_args,
        )

    def analyze(self):
        self.visit(ast.parse(self.contents, self.filename))
        self.analyze_submodules()
        # print()

    def get_all_reachable_functions(self):
        reachable = set()
        names = set()
        current_scope = self.scope_manager.get_scope(self.current_ns)
        while current_scope:
            for name, defi in current_scope.get_defs().items():
                if defi.is_function_def() and not name in names:
                    closured = self.closured.get(defi.get_ns())
                    for item in closured:
                        reachable.add(item)
                    names.add(name)
            current_scope = current_scope.parent

        return reachable

    def has_ext_parent(self, node):
        if not isinstance(node, ast.Attribute):
            return False

        while isinstance(node, ast.Attribute):
            parents = self._retrieve_parent_names(node)
            for parent in parents:
                for name in self.closured.get(parent, []):
                    defi = self.def_manager.get(name)
                    # Investigate: definition marked as not external. but its parent could be
                    if defi and defi.is_ext_def():
                        return True
            node = node.value
        return False

    def get_full_attr_names(self, node):
        name = ""
        while isinstance(node, ast.Attribute):
            if not name:
                name = node.attr
            else:
                name = node.attr + "." + name
            node = node.value

        names = []
        if getattr(node, "id", None) == None:
            return names

        defi = self.scope_manager.get_def(self.current_ns, node.id)
        if defi and self.closured.get(defi.get_ns()):
            for id in self.closured.get(defi.get_ns()):
                names.append(id + "." + name)

        return names

    def is_builtin(self, name):
        return name in __builtins__

    def get_builtin_type_method_calls(self, node):
        name = ""
        while isinstance(node, ast.Attribute):
            if not name:
                name = node.attr
            else:
                name = node.attr + "." + name
            node = node.value

        names = []
        if getattr(node, "id", None) == None:
            return names

        if node.lineno in self.usedefprocessor.line_uses:
            for _use in self.usedefprocessor.line_uses[node.lineno]:
                if utils.get_ns_without_last_lineno(_use) == node.id:
                    defi = self.scope_manager.get_def(self.current_ns, _use)
                    if defi and self.closured.get(defi.get_ns()):
                        id_defs = self.def_manager.transitive_closure().get(defi.fullns)
                        if id_defs:
                            # Prepare type_fact dict
                            for _def in id_defs:
                                if utils.is_dict(_def):
                                    names.append("<dict>" + "." + name)
                                elif utils.is_list(_def):
                                    names.append("<list>" + "." + name)

        return names

        # for id in self.closured.get(defi.get_ns()):
        #     names.append(id + "." + name)
