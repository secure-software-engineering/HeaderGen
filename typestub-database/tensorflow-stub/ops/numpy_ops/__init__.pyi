from tensorflow.python.ops.numpy_ops.np_array_ops import *
from tensorflow.python.ops.numpy_ops.np_config import *
from tensorflow.python.ops.numpy_ops.np_dtypes import *
from tensorflow.python.ops.numpy_ops.np_math_ops import *
from tensorflow.python.ops.array_ops import newaxis as newaxis
from tensorflow.python.ops.numpy_ops import np_utils as np_utils
from tensorflow.python.ops.numpy_ops.np_arrays import ndarray as ndarray
from tensorflow.python.ops.numpy_ops.np_utils import finfo as finfo, promote_types as promote_types, result_type as result_type
from typing import Any

def max(a, axis: Any | None = ..., keepdims: Any | None = ...): ...
def min(a, axis: Any | None = ..., keepdims: Any | None = ...): ...
def round(a, decimals: int = ...): ...
