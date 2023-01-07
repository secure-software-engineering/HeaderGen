from tensorflow.python.ops import array_ops as array_ops
from tensorflow.python.ops.ragged import ragged_gather_ops as ragged_gather_ops, ragged_tensor as ragged_tensor
from tensorflow.python.util import dispatch as dispatch
from typing import Any

def batch_gather(params: ragged_tensor.RaggedOrDense, indices: ragged_tensor.RaggedOrDense, name: Any | None = ...): ...
