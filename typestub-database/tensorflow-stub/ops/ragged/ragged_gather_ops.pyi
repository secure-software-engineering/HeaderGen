from tensorflow.python.framework import dtypes as dtypes, indexed_slices as indexed_slices, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, gen_ragged_array_ops as gen_ragged_array_ops, math_ops as math_ops
from tensorflow.python.ops.ragged import ragged_array_ops as ragged_array_ops, ragged_math_ops as ragged_math_ops, ragged_tensor as ragged_tensor
from tensorflow.python.util import dispatch as dispatch
from typing import Any

def gather(params: ragged_tensor.RaggedOrDense, indices: ragged_tensor.RaggedOrDense, validate_indices: Any | None = ..., axis: Any | None = ..., batch_dims: int = ..., name: Any | None = ...): ...
def gather_nd(params: ragged_tensor.RaggedOrDense, indices: ragged_tensor.RaggedOrDense, batch_dims: int = ..., name: Any | None = ...): ...
