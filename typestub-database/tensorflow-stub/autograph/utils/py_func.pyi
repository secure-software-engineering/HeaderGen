from tensorflow.python.framework import dtypes as dtypes, tensor_util as tensor_util
from tensorflow.python.ops import script_ops as script_ops
from typing import Any

class MatchDType: ...

def wrap_py_func(f, return_dtypes, args, kwargs: Any | None = ..., use_dummy_return: bool = ...): ...
