from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

class _RaggedCrossOutput(NamedTuple):
    output_values: Any
    output_row_splits: Any

def ragged_cross(ragged_values, ragged_row_splits, sparse_indices, sparse_values, sparse_shape, dense_inputs, input_order, hashed_output, num_buckets, hash_key, out_values_type, out_row_splits_type, name: Any | None = ...): ...

RaggedCross: Any

def ragged_cross_eager_fallback(ragged_values, ragged_row_splits, sparse_indices, sparse_values, sparse_shape, dense_inputs, input_order, hashed_output, num_buckets, hash_key, out_values_type, out_row_splits_type, name, ctx): ...

class _RaggedGatherOutput(NamedTuple):
    output_nested_splits: Any
    output_dense_values: Any

def ragged_gather(params_nested_splits, params_dense_values, indices, OUTPUT_RAGGED_RANK, name: Any | None = ...): ...

RaggedGather: Any

def ragged_gather_eager_fallback(params_nested_splits, params_dense_values, indices, OUTPUT_RAGGED_RANK, name, ctx): ...
