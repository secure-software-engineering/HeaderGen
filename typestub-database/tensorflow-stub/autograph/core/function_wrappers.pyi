from tensorflow.python.autograph.core import ag_ctx as ag_ctx, converter as converter
from tensorflow.python.autograph.operators import variables as variables
from tensorflow.python.framework import auto_control_deps as auto_control_deps, ops as ops, tensor_util as tensor_util
from tensorflow.python.util import nest as nest
from typing import Any

class FunctionScope:
    name: Any
    options: Any
    autograph_ctx: Any
    callopts: Any
    use_name_scope: Any
    name_scope: Any
    use_auto_deps: Any
    autodeps_scope: Any
    def __init__(self, function_name, scope_name, options) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def ret(self, value, did_return): ...

def with_function_scope(thunk, scope_name, options): ...
