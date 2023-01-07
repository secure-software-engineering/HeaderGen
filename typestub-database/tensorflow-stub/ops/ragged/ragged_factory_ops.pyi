from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor, ragged_tensor_value as ragged_tensor_value
from tensorflow.python.util import dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def constant(pylist, dtype: Any | None = ..., ragged_rank: Any | None = ..., inner_shape: Any | None = ..., name: Any | None = ..., row_splits_dtype=...): ...
def constant_value(pylist, dtype: Any | None = ..., ragged_rank: Any | None = ..., inner_shape: Any | None = ..., row_splits_dtype: str = ...): ...
def placeholder(dtype, ragged_rank, value_shape: Any | None = ..., name: Any | None = ...): ...
