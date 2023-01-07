from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

class _RaggedTensorFromVariantOutput(NamedTuple):
    output_nested_splits: Any
    output_dense_values: Any

def ragged_tensor_from_variant(encoded_ragged, input_ragged_rank, output_ragged_rank, Tvalues, Tsplits=..., name: Any | None = ...): ...

RaggedTensorFromVariant: Any

def ragged_tensor_from_variant_eager_fallback(encoded_ragged, input_ragged_rank, output_ragged_rank, Tvalues, Tsplits, name, ctx): ...

class _RaggedTensorToSparseOutput(NamedTuple):
    sparse_indices: Any
    sparse_values: Any
    sparse_dense_shape: Any

def ragged_tensor_to_sparse(rt_nested_splits, rt_dense_values, name: Any | None = ...): ...

RaggedTensorToSparse: Any

def ragged_tensor_to_sparse_eager_fallback(rt_nested_splits, rt_dense_values, name, ctx): ...
def ragged_tensor_to_tensor(shape, values, default_value, row_partition_tensors, row_partition_types, name: Any | None = ...): ...

RaggedTensorToTensor: Any

def ragged_tensor_to_tensor_eager_fallback(shape, values, default_value, row_partition_tensors, row_partition_types, name, ctx): ...
def ragged_tensor_to_variant(rt_nested_splits, rt_dense_values, batched_input, name: Any | None = ...): ...

RaggedTensorToVariant: Any

def ragged_tensor_to_variant_eager_fallback(rt_nested_splits, rt_dense_values, batched_input, name, ctx): ...
def ragged_tensor_to_variant_gradient(encoded_ragged_grad, row_splits, dense_values_shape, Tvalues, name: Any | None = ...): ...

RaggedTensorToVariantGradient: Any

def ragged_tensor_to_variant_gradient_eager_fallback(encoded_ragged_grad, row_splits, dense_values_shape, Tvalues, name, ctx): ...
