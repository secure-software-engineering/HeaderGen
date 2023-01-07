from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.util import nest as nest
from tensorflow.python.util.lazy_loader import LazyLoader as LazyLoader
from typing import Any

map_fn_lib: Any

def map_fn(fn, elems, dtype: Any | None = ..., parallel_iterations: Any | None = ..., back_prop: bool = ..., swap_memory: bool = ..., infer_shape: bool = ..., name: Any | None = ...): ...
