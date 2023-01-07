from tensorflow.python.framework import constant_op as constant_op, ops as ops
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, math_ops as math_ops
from tensorflow.python.ops.ragged import ragged_array_ops as ragged_array_ops, ragged_dispatch as ragged_dispatch, ragged_operators as ragged_operators, ragged_tensor as ragged_tensor, ragged_tensor_shape as ragged_tensor_shape, ragged_where_op as ragged_where_op
from typing import Any

def batch_gather_with_default(params, indices, default_value: str = ..., name: Any | None = ...): ...
