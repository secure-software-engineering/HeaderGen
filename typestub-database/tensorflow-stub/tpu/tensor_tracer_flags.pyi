from tensorflow.python.ops import linalg_ops as linalg_ops, math_ops as math_ops
from typing import Any

TRACE_MODE_PART_TENSOR: str
TRACE_MODE_FULL_TENSOR: str
TRACE_MODE_FULL_TENSOR_SUMMARY: str
TRACE_MODE_NAN_INF: str
TRACE_MODE_NORM: str
TRACE_MODE_MAX_ABS: str
TRACE_MODE_SUMMARY: str
FLAGS_ENV_VAR: str
FLAG_NAME_ENABLE: str
FLAG_NAME_TRACE_MODE: str
FLAG_NAME_TRACE_SCALAR_OPS: str
FLAG_NAME_SUBMODE: str
FLAG_NAME_EXCLUDED_OPNAMES: str
FLAG_NAME_EXCLUDED_OPTYPES: str
FLAG_NAME_INCLUDED_OPNAMES: str
FLAG_NAME_INCLUDED_OPTYPES: str
FLAG_NAME_TRACE_LEVEL: str
FLAG_NAME_TRACE_DIR: str
FLAG_NAME_REPORT_FILE: str
FLAG_NAME_USE_TEST_UNDECLARED_OUTPUTS_DIR: str
FLAG_NAME_OP_RANGE: str
FLAG_NAME_DUMP_BEFORE_AFTER_GRAPHS: str
FLAG_NAME_SUMMARY_SIGNATURES: str
FLAG_NAME_SUMMARY_PER_CORE: str
FLAG_NAME_TEMP_CACHE_VAR: str
FLAG_NAME_INSPECT_TRACE: str
FLAG_NAME_FINGERPRINT_DIR: str
FLAG_FLUSH_SUMMARY: str
FLAG_SUMMARY_MODE_TYPE: str
UI_MODE: str
TEXT_MODE: str
SAFE_MODE: str
TT_SUMMARY_NORM: Any
TT_SUMMARY_MAX: Any
TT_SUMMARY_MAX_ABS: Any
TT_SUMMARY_MIN: Any
TT_SUMMARY_MEAN: Any
TT_SUMMARY_VAR: Any
TT_SUMMARY_SIZE: Any
TT_SUMMARY_SIGNATURES: Any

class TTParameters:
    trace_mode: Any
    submode: Any
    trace_dir: Any
    report_file_path: Any
    op_range: Any
    excluded_opname_re_list: Any
    excluded_optype_re_list: Any
    included_opname_re_list: Any
    included_optype_re_list: Any
    trace_scalar_ops: Any
    use_compact_trace: Any
    use_temp_cache_var: Any
    inspect_trace: Any
    use_fingerprint_subdir: Any
    trace_level: Any
    summary_signatures: Any
    collect_summary_per_core: Any
    flush_summaries_with_outside_compile: Any
    summary_mode: Any
    def __init__(self, env: Any | None = ...) -> None: ...
    def is_brief_mode(self): ...
    @staticmethod
    def match_next_flag(flags, pos): ...
    def get_signature_to_agg_fn_map(self): ...
    def get_flag_value(self, wanted_flag_name): ...
    def is_flag_on(self, flag_name): ...
    def is_enabled(self): ...
    def use_test_undeclared_outputs_dir(self): ...
