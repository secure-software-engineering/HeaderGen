import re

import gast as ast
from intervaltree import Interval, IntervalTree

from framework_models import PHASES as PIPELINE_PHASES

disable_for_testing_other_implementaions = False


def get_ns_without_last_lineno(ns):
    return re.sub(r"(?s)(?!:.*?(?=\.)):.*?(?=$)", "", ns)


class HeaderGenVisitor(ast.NodeVisitor):
    def __init__(self, analysis_info):
        self.source_code_tags = {}
        self.function_tags = {}
        self.body_intervals = IntervalTree()

        self.analysis_info = analysis_info
        self.pattern_single_statement = {}

        self.pattern_matches = {}

        self.context_library_calls = analysis_info["context_library_calls"]
        self.defined_calls = analysis_info["defined_calls"]
        self.call_args = analysis_info["call_args"]

        self.call_args_line_no = {}
        for k, v in self.call_args.items():
            _func = k.split(":")[0]
            _line = int(k.split(":")[1].split(".")[0])
            if _line not in self.call_args_line_no:
                self.call_args_line_no[_line] = {}

            self.call_args_line_no[_line][_func] = v

        self.defined_function_summaries = {}

        # self.function_def_stack = []

    # def _get_current_function_def(self):
    #     if len(self.function_def_stack) != 0:
    #         return self.function_def_stack[-1]

    def is_name_dataframe(self, node):
        is_value_dataframe = False
        if node.lineno in self.analysis_info["line_uses"]:
            _decoded = []
            for _use in self.analysis_info["line_uses"][node.lineno]:
                if get_ns_without_last_lineno(_use) == node.id:
                    _var_name = f"{self.analysis_info['file_name']}.{_use}"
                    if _var_name in self.analysis_info["eag"]:
                        is_value_dataframe = any(
                            [
                                x.startswith(
                                    (
                                        "pandas.core.frame.DataFrame",
                                        "numpy.ndarray",
                                        "pandas.core.series.Series",
                                    )
                                )
                                for x in self.analysis_info["eag"][_var_name]["names"]
                            ]
                        )

        return is_value_dataframe

    def is_dataframe_access(self, node):
        is_dataframe_access = False
        if isinstance(node, (ast.Subscript, ast.Attribute)):
            if isinstance(node.value, ast.Name):
                if node.lineno in self.analysis_info["line_uses"]:
                    for _use in self.analysis_info["line_uses"][node.lineno]:
                        if get_ns_without_last_lineno(_use) == node.value.id:
                            _var_name = f"{self.analysis_info['file_name']}.{_use}"
                            if _var_name in self.analysis_info["eag"]:
                                is_dataframe_access = any(
                                    [
                                        x.startswith(
                                            (
                                                "pandas.core.frame.DataFrame",
                                                "numpy.ndarray",
                                                "pandas.core.series.Series",
                                            )
                                        )
                                        for x in self.analysis_info["eag"][_var_name][
                                            "names"
                                        ]
                                    ]
                                )

        return is_dataframe_access

    def is_list_access(self, node):
        is_dataframe_access = False
        if isinstance(node, ast.Name):
            if node.lineno in self.analysis_info["line_uses"]:
                for _use in self.analysis_info["line_uses"][node.lineno]:
                    if get_ns_without_last_lineno(_use) == node.id:
                        _var_name = f"{self.analysis_info['file_name']}.{_use}"
                        if _var_name in self.analysis_info["eag"]:
                            is_dataframe_access = any(
                                [
                                    re.search("<list\d+>$", x)
                                    for x in self.analysis_info["eag"][_var_name][
                                        "names"
                                    ]
                                ]
                            )
        elif isinstance(node, ast.List):
            is_dataframe_access = True

        return is_dataframe_access

    def add_pattern_match(self, node, phase):
        if disable_for_testing_other_implementaions:
            return
        if node.lineno not in self.pattern_matches:
            self.pattern_matches[node.lineno] = {
                "dl_pipeline_tag": [],
                "doc_string": {},
            }

        self.pattern_matches[node.lineno]["dl_pipeline_tag"].extend([phase])

    def generate_function_summaries(self):
        # TODO: Get lineno intervals and summarize from context_library_calls
        for body_interval in self.body_intervals:
            if body_interval.data["node_type"] == "FunctionDef":
                for _iv in range(body_interval[0] + 1, body_interval[1]):
                    if (
                        body_interval.data["name"]
                        not in self.defined_function_summaries
                    ):
                        self.defined_function_summaries[body_interval.data["name"]] = {
                            "dl_pipeline_tag": [],
                            "doc_string": {},
                            "call_args": {},
                        }
                    if _iv in self.source_code_tags:
                        self.defined_function_summaries[body_interval.data["name"]][
                            "dl_pipeline_tag"
                        ].extend(self.source_code_tags[_iv]["dl_pipeline_tag"])
                        self.defined_function_summaries[body_interval.data["name"]][
                            "doc_string"
                        ] = (
                            self.defined_function_summaries[body_interval.data["name"]][
                                "doc_string"
                            ]
                            | self.source_code_tags[_iv]["doc_string"]
                        )

                    if _iv in self.call_args_line_no:
                        self.defined_function_summaries[body_interval.data["name"]][
                            "call_args"
                        ][_iv] = self.call_args_line_no[_iv]

    # https://julien.danjou.info/finding-definitions-from-a-source-file-and-a-line-number-in-python/
    def _compute_interval(self, node):
        min_lineno = node.lineno
        max_lineno = node.lineno
        for _node in ast.walk(node):
            if hasattr(_node, "lineno"):
                if not _node.lineno:
                    continue
                min_lineno = min(min_lineno, _node.lineno)
                max_lineno = max(max_lineno, _node.lineno)
        return (min_lineno, max_lineno + 1)

    def _body_visitor(self, node, body=[]):
        # Add body interval and type
        # TODO: reuse this code instead of copies
        if node.lineno not in self.source_code_tags:
            self.source_code_tags[node.lineno] = {
                "dl_pipeline_tag": [],
                "doc_string": {},
            }

        if node.lineno in self.context_library_calls:
            for _func_call_dict in self.context_library_calls[node.lineno]:
                self.source_code_tags[node.lineno]["dl_pipeline_tag"].extend(
                    _func_call_dict["dl_pipeline_tag"]
                )
                if "doc_string" in _func_call_dict:
                    self.source_code_tags[node.lineno]["doc_string"][
                        _func_call_dict["func_call"]
                    ] = _func_call_dict["doc_string"]

        if isinstance(node, ast.FunctionDef):
            _node_name = "{}:{}".format(node.name, node.lineno)
            self.source_code_tags[node.lineno]["dl_pipeline_tag"].extend(
                [PIPELINE_PHASES["FUNCTION_DEFINITION"]]
            )
            # self.function_def_stack.append(node)

        else:
            _node_name = "{}:{}".format(type(node).__name__, node.lineno)

        _body_int_start, _body_int_end = self._compute_interval(node)

        self.body_intervals[_body_int_start:_body_int_end] = {
            "name": _node_name,
            "node_type": type(node).__name__,
        }

        # if isinstance(node, ast.If) or isinstance(node, ast.IfExp):
        #     self.visit(node.orelse)

        for stmt in body:
            if hasattr(stmt, "body"):
                self.visit(stmt)

            elif hasattr(stmt, "lineno"):
                self.visit(stmt)

                if stmt.lineno not in self.source_code_tags:
                    self.source_code_tags[stmt.lineno] = {
                        "dl_pipeline_tag": [],
                        "doc_string": {},
                    }

                if stmt.lineno in self.context_library_calls:
                    for _func_call_dict in self.context_library_calls[stmt.lineno]:
                        self.source_code_tags[stmt.lineno]["dl_pipeline_tag"].extend(
                            _func_call_dict["dl_pipeline_tag"]
                        )
                        if "doc_string" in _func_call_dict:
                            self.source_code_tags[stmt.lineno]["doc_string"][
                                _func_call_dict["func_call"]
                            ] = _func_call_dict["doc_string"]

    def visit_Module(self, node):
        # Entry point
        # print(node)
        for stmt in node.body:
            if hasattr(stmt, "body"):
                self.visit(stmt)

            elif hasattr(stmt, "lineno"):
                self.visit(stmt)

                for _lineno in range(stmt.lineno, stmt.end_lineno + 1):
                    if _lineno not in self.source_code_tags:
                        self.source_code_tags[_lineno] = {
                            "dl_pipeline_tag": [],
                            "doc_string": {},
                        }

                    if _lineno in self.context_library_calls:
                        for _func_call_dict in self.context_library_calls[_lineno]:
                            self.source_code_tags[_lineno]["dl_pipeline_tag"].extend(
                                _func_call_dict["dl_pipeline_tag"]
                            )
                            if "doc_string" in _func_call_dict:
                                self.source_code_tags[_lineno]["doc_string"][
                                    _func_call_dict["func_call"]
                                ] = _func_call_dict["doc_string"]

        self.generate_function_summaries()

    def visit_FunctionDef(self, node):
        # print(node)
        self._body_visitor(node, node.body)

    def visit_ClassDef(self, node):
        # print(node)
        self._body_visitor(node, node.body)

    def visit_If(self, node):
        # print(node)
        # self._body_visitor(node)
        self._body_visitor(node, node.body)
        self._body_visitor(node, node.orelse)

    def visit_For(self, node):
        # print(node)
        # P7 --> for i in df:
        if isinstance(node.iter, (ast.Subscript, ast.Attribute)):
            is_dataframe_access = self.is_dataframe_access(node.iter)
            if is_dataframe_access:
                self.add_pattern_match(
                    node, PIPELINE_PHASES["DATA_CLEANING_PREPARATION"]
                )
                self.add_pattern_match(node, PIPELINE_PHASES["FEATURE_ENGINEERING"])

        self._body_visitor(node, node.body)
        self._body_visitor(node, node.orelse)

    def visit_While(self, node):
        # print(node)
        self._body_visitor(node, node.body)
        self._body_visitor(node, node.orelse)

    def visit_IfExp(self, node):
        # print(node)
        self.visit(node.body)
        self.visit(node.orelse)

    def visit_Try(self, node):
        # print(node)
        self._body_visitor(node)

    def visit_TryFinally(self, node):
        # print(node)
        self._body_visitor(node)

    def visit_TryExcept(self, node):
        # print(node)
        self._body_visitor(node)

    def visit_ExceptHandler(self, node):
        # print(node)
        self._body_visitor(node)

    def visit_With(self, node):
        # print(node)
        self._body_visitor(node)

    def visit_Lambda(self, node):
        # print(node)
        self._body_visitor(node)

    def visit_AsyncFunctionDef(self, node):
        # print(node)
        self._body_visitor(node)

    def visit_AsyncFor(self, node):
        # print(node)
        self._body_visitor(node)

    def visit_AsyncWith(self, node):
        # print(node)
        self._body_visitor(node)

    def visit_Import(self, node):
        if node.lineno not in self.source_code_tags:
            self.source_code_tags[node.lineno] = {
                "dl_pipeline_tag": [],
                "doc_string": {},
            }

        self.source_code_tags[node.lineno]["dl_pipeline_tag"].extend(
            [PIPELINE_PHASES["LIBRARY_LOADING"]]
        )

        # print(node)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        if node.lineno not in self.source_code_tags:
            self.source_code_tags[node.lineno] = {
                "dl_pipeline_tag": [],
                "doc_string": {},
            }

        self.source_code_tags[node.lineno]["dl_pipeline_tag"].extend(
            [PIPELINE_PHASES["LIBRARY_LOADING"]]
        )
        # print(node)
        self.generic_visit(node)

    # Undefined

    def visit_Num(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Str(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_FormattedValue(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_JoinedStr(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Bytes(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_List(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Tuple(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Set(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Dict(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Ellipsis(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_NameConstant(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Name(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Load(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Store(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Del(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Starred(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Expr(self, node):
        node_value_chain = []

        def nested_value(node, arr):
            if hasattr(node, "value"):
                arr.append(node.value)
                nested_value(node.value, arr)

        if disable_for_testing_other_implementaions:
            return
        # PATTERN Search - single statement
        try:
            is_dataframe_access = False
            is_dataframe_column_access = False

            if isinstance(node.value, (ast.Subscript, ast.Attribute, ast.Name)):
                if node.lineno in self.analysis_info["line_uses"]:
                    _decoded = []
                    for _use in self.analysis_info["line_uses"][node.lineno]:
                        nested_value(node, node_value_chain)
                        if get_ns_without_last_lineno(_use) == node_value_chain[-1].id:
                            _var_name = f"{self.analysis_info['file_name']}.{_use}"
                            if _var_name in self.analysis_info["eag"]:
                                # P9 --> np.ndarray
                                # P9 --> df
                                is_dataframe_access = any(
                                    [
                                        x.startswith(
                                            (
                                                "pandas.core.frame.DataFrame",
                                                "numpy.ndarray",
                                            )
                                        )
                                        for x in self.analysis_info["eag"][_var_name][
                                            "names"
                                        ]
                                    ]
                                )

            if any([is_dataframe_access, is_dataframe_column_access]):
                self.add_pattern_match(
                    node,
                    PIPELINE_PHASES["DATA_PROFILING_AND_EXPLORATORY_DATA_ANALYSIS"],
                )

            if isinstance(node.value, ast.Call):
                if hasattr(node.value.func, "id"):
                    if node.value.func.id == "len":
                        self.add_pattern_match(
                            node,
                            PIPELINE_PHASES[
                                "DATA_PROFILING_AND_EXPLORATORY_DATA_ANALYSIS"
                            ],
                        )

            # print(node)
            self.generic_visit(node)
            if hasattr(node, "value"):
                if hasattr(node.value, "attr"):
                    if node.value.attr in [
                        "shape",
                        "values",
                        "columns",
                        "dtypes",
                        "iloc",
                        "loc",
                    ]:
                        if node.lineno not in self.source_code_tags:
                            self.source_code_tags[node.lineno] = {
                                "dl_pipeline_tag": [],
                                "doc_string": {},
                            }

                        self.source_code_tags[node.lineno]["dl_pipeline_tag"].extend(
                            [
                                PIPELINE_PHASES[
                                    "DATA_PROFILING_AND_EXPLORATORY_DATA_ANALYSIS"
                                ]
                            ]
                        )

                    if node.value.attr in ["iloc", "loc"]:
                        if node.lineno not in self.source_code_tags:
                            self.source_code_tags[node.lineno] = {
                                "dl_pipeline_tag": [],
                                "doc_string": {},
                            }

                        self.source_code_tags[node.lineno]["dl_pipeline_tag"].extend(
                            [PIPELINE_PHASES["FEATURE_SELECTION"]]
                        )

        except:
            print("Pattern matching error: Expr")

    def visit_UnaryOp(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_UAdd(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_USub(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Not(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Invert(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_BinOp(self, node):
        # print(node)
        # P1 --> df['xy'] = df.x * df.y
        try:
            is_left_dataframe_access = self.is_dataframe_access(node.left)
            is_right_dataframe_access = self.is_dataframe_access(node.right)
            if any([is_left_dataframe_access, is_right_dataframe_access]):
                self.add_pattern_match(node, PIPELINE_PHASES["FEATURE_TRANSFORMATION"])
        except:
            print("Pattern matching error: BinOp")

        self.generic_visit(node)

    def visit_Add(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Sub(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Mult(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Div(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_FloorDiv(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Mod(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Pow(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_LShift(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_RShift(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_BitOr(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_BitXor(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_BitAnd(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_MatMult(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_And(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Or(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Compare(self, node):
        # print(node)
        try:
            is_dataframe_access = False
            is_dataframe_column_access = False

            # P5 --> df.x[df.x == 1] = 1
            is_left_dataframe_access = self.is_dataframe_access(node.left)
            is_right_dataframe_access = self.is_dataframe_access(node.left)
            if any([is_left_dataframe_access, is_right_dataframe_access]):
                self.add_pattern_match(node, PIPELINE_PHASES["DATA_CLEANING_FILTERING"])
                self.add_pattern_match(node, PIPELINE_PHASES["FEATURE_TRANSFORMATION"])
        except:
            print("Pattern matching error: Expr")

        self.generic_visit(node)

    def visit_Eq(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_NotEq(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Lt(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_LtE(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Gt(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_GtE(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Is(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_IsNot(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_In(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_NotIn(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Call(self, node):
        # print(node)
        # PATTERN Search - print dataframe
        try:
            is_dataframe_access = False
            is_dataframe_column_access = False
            if isinstance(node.func, ast.Name):
                if node.func.id in ["print", "map"]:
                    for _arg in node.args:
                        if isinstance(_arg, (ast.Subscript, ast.Attribute)):
                            is_dataframe_column_access = self.is_dataframe_access(_arg)
                            if is_dataframe_column_access:
                                break

                        elif isinstance(_arg, ast.Name):
                            if node.lineno in self.analysis_info["line_uses"]:
                                _decoded = []
                                for _use in self.analysis_info["line_uses"][
                                    node.lineno
                                ]:
                                    if get_ns_without_last_lineno(_use) == _arg.id:
                                        _var_name = (
                                            f"{self.analysis_info['file_name']}.{_use}"
                                        )
                                        if _var_name in self.analysis_info["eag"]:
                                            is_dataframe_access = any(
                                                [
                                                    x.startswith(
                                                        (
                                                            "pandas.core.frame.DataFrame",
                                                            "numpy.ndarray",
                                                        )
                                                    )
                                                    for x in self.analysis_info["eag"][
                                                        _var_name
                                                    ]["names"]
                                                ]
                                            )

            if any([is_dataframe_access, is_dataframe_column_access]):
                self.add_pattern_match(
                    node,
                    PIPELINE_PHASES["DATA_PROFILING_AND_EXPLORATORY_DATA_ANALYSIS"],
                )

        except:
            print("Pattern matching error: Expr")

        self.generic_visit(node)

    def visit_keyword(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Attribute(self, node):
        if disable_for_testing_other_implementaions:
            return
        # print(node)
        self.generic_visit(node)
        if hasattr(node, "attr"):
            if node.attr in ["shape", "values", "columns", "dtypes", "iloc", "loc"]:
                if node.lineno not in self.source_code_tags:
                    self.source_code_tags[node.lineno] = {
                        "dl_pipeline_tag": [],
                        "doc_string": {},
                    }

                self.source_code_tags[node.lineno]["dl_pipeline_tag"].extend(
                    [PIPELINE_PHASES["DATA_PROFILING_AND_EXPLORATORY_DATA_ANALYSIS"]]
                )

                if node.attr in ["iloc", "loc"]:
                    if node.lineno not in self.source_code_tags:
                        self.source_code_tags[node.lineno] = {
                            "dl_pipeline_tag": [],
                            "doc_string": {},
                        }

                    self.source_code_tags[node.lineno]["dl_pipeline_tag"].extend(
                        [PIPELINE_PHASES["FEATURE_SELECTION"]]
                    )

    def visit_Subscript(self, node):
        if isinstance(node.value, ast.Attribute):
            is_value_dataframe_column_access = self.is_dataframe_access(node.value)
            is_list_access = self.is_list_access(node.slice)
            is_slice = False

            if isinstance(node.slice, (ast.Tuple, ast.Slice)):
                is_slice = True

            if is_value_dataframe_column_access and (is_list_access or is_slice):
                self.add_pattern_match(node, PIPELINE_PHASES["FEATURE_SELECTION"])
                self.add_pattern_match(
                    node, PIPELINE_PHASES["DATA_CLEANING_PREPARATION"]
                )
        # print(node)
        self.generic_visit(node)

    def visit_Index(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Slice(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_ExtSlice(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_ListComp(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_SetComp(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_GeneratorExp(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_DictComp(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_comprehension(self, node):
        if isinstance(node.iter, (ast.Subscript, ast.Attribute)):
            is_dataframe_access = self.is_dataframe_access(node.iter)
            if is_dataframe_access:
                self.add_pattern_match(
                    node.iter, PIPELINE_PHASES["DATA_CLEANING_PREPARATION"]
                )
        elif isinstance(node.iter, ast.Name):
            is_dataframe_access = self.is_name_dataframe(node.iter)
            if is_dataframe_access:
                self.add_pattern_match(
                    node.iter, PIPELINE_PHASES["DATA_CLEANING_PREPARATION"]
                )

        # print(node)
        self.generic_visit(node)

    def visit_Assign(self, node):
        # print(node)
        try:
            is_dataframe_access = False
            is_dataframe_column_access = False
            is_target_dataframe_access = False
            is_target_dataframe_column_access = False
            is_value_dataframe_access = False
            is_value_dataframe_column_access = False

            # Analyze LHS
            for _target in node.targets:
                if isinstance(_target, ast.Name):
                    if node.lineno in self.analysis_info["line_uses"]:
                        _decoded = []
                        for _use in self.analysis_info["line_uses"][node.lineno]:
                            if get_ns_without_last_lineno(_use) == _target.id:
                                _var_name = f"{self.analysis_info['file_name']}.{_use}"
                                if _var_name in self.analysis_info["eag"]:
                                    is_target_dataframe_access = any(
                                        [
                                            x.startswith(
                                                (
                                                    "pandas.core.frame.DataFrame",
                                                    "numpy.ndarray",
                                                )
                                            )
                                            for x in self.analysis_info["eag"][
                                                _var_name
                                            ]["names"]
                                        ]
                                    )

                elif isinstance(_target, (ast.Subscript, ast.Attribute)):
                    # P2 --> df[] = 1
                    # P4 --> df.x = 1
                    if isinstance(_target.value, ast.Name):
                        if node.lineno in self.analysis_info["line_uses"]:
                            _decoded = []
                            for _use in self.analysis_info["line_uses"][node.lineno]:
                                if get_ns_without_last_lineno(_use) == _target.value.id:
                                    _var_name = (
                                        f"{self.analysis_info['file_name']}.{_use}"
                                    )
                                    if _var_name in self.analysis_info["eag"]:
                                        is_target_dataframe_column_access = any(
                                            [
                                                x.startswith(
                                                    (
                                                        "pandas.core.frame.DataFrame",
                                                        "numpy.ndarray",
                                                    )
                                                )
                                                for x in self.analysis_info["eag"][
                                                    _var_name
                                                ]["names"]
                                            ]
                                        )

            # Analyze RHS
            if isinstance(node.value, (ast.Subscript, ast.Attribute)):
                if isinstance(node.value.value, ast.Name):
                    if node.lineno in self.analysis_info["line_uses"]:
                        _decoded = []
                        for _use in self.analysis_info["line_uses"][node.lineno]:
                            if get_ns_without_last_lineno(_use) == node.value.value.id:
                                _var_name = f"{self.analysis_info['file_name']}.{_use}"
                                if _var_name in self.analysis_info["eag"]:
                                    is_value_dataframe_column_access = any(
                                        [
                                            x.startswith(
                                                (
                                                    "pandas.core.frame.DataFrame",
                                                    "numpy.ndarray",
                                                )
                                            )
                                            for x in self.analysis_info["eag"][
                                                _var_name
                                            ]["names"]
                                        ]
                                    )

                    # P3 --> x = df[]
                    if is_value_dataframe_column_access:
                        self.add_pattern_match(
                            node, PIPELINE_PHASES["DATA_CLEANING_PREPARATION"]
                        )
                        self.add_pattern_match(
                            node, PIPELINE_PHASES["FEATURE_ENGINEERING"]
                        )

                # P6 --> x = df.x[[]]
                elif isinstance(node.value.value, ast.Attribute):
                    is_value_dataframe_column_access = self.is_dataframe_access(
                        node.value.value
                    )
                    if isinstance(node.value, ast.Subscript):
                        is_list_access = self.is_list_access(node.value.slice)

                        if is_value_dataframe_column_access and is_list_access:
                            self.add_pattern_match(
                                node, PIPELINE_PHASES["FEATURE_SELECTION"]
                            )
                            self.add_pattern_match(
                                node, PIPELINE_PHASES["DATA_CLEANING_PREPARATION"]
                            )

                elif isinstance(node.value.value, ast.Subscript):
                    is_value_dataframe_column_access = self.is_dataframe_access(
                        node.value.value
                    )
                    if hasattr(node.value.value.slice, "value"):
                        # if hasattr()
                        is_list_access = self.is_list_access(
                            node.value.value.slice.value
                        )

                        if is_value_dataframe_column_access and is_list_access:
                            self.add_pattern_match(
                                node, PIPELINE_PHASES["FEATURE_SELECTION"]
                            )
                            self.add_pattern_match(
                                node, PIPELINE_PHASES["DATA_CLEANING_PREPARATION"]
                            )

            elif isinstance(node.value, (ast.Constant, ast.Name, ast.List)):
                # P2 --> df[] = 1
                # P4 --> df.x = 1
                if is_target_dataframe_column_access:
                    self.add_pattern_match(
                        node, PIPELINE_PHASES["FEATURE_TRANSFORMATION"]
                    )
                    self.add_pattern_match(
                        node, PIPELINE_PHASES["DATA_CLEANING_PREPARATION"]
                    )
                else:
                    if isinstance(node.value, ast.Name):
                        if self.is_name_dataframe(node.value):
                            self.add_pattern_match(
                                node, PIPELINE_PHASES["DATA_CLEANING_PREPARATION"]
                            )

        except:
            print("Pattern matching error: Expr")

        self.generic_visit(node)

    def visit_AnnAssign(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_AugAssign(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Print(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Raise(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Assert(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Delete(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Pass(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_alias(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Break(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Continue(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_withitem(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_arguments(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_arg(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Return(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Yield(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_YieldFrom(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Global(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Nonlocal(self, node):
        # print(node)
        self.generic_visit(node)

    def visit_Await(self, node):
        # print(node)
        self.generic_visit(node)


SOURCE = """
def hello(msg):
    a = 21 * 2
    print(msg, a)
"""

if __name__ == "__main__":
    root = ast.parse(SOURCE)
    visitor = HeaderGenVisitor()
    visitor.visit(root)
