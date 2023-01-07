from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

class _DenseCountSparseOutputOutput(NamedTuple):
    output_indices: Any
    output_values: Any
    output_dense_shape: Any

def dense_count_sparse_output(values, weights, binary_output, minlength: int = ..., maxlength: int = ..., name: Any | None = ...): ...

DenseCountSparseOutput: Any

def dense_count_sparse_output_eager_fallback(values, weights, binary_output, minlength, maxlength, name, ctx): ...

class _RaggedCountSparseOutputOutput(NamedTuple):
    output_indices: Any
    output_values: Any
    output_dense_shape: Any

def ragged_count_sparse_output(splits, values, weights, binary_output, minlength: int = ..., maxlength: int = ..., name: Any | None = ...): ...

RaggedCountSparseOutput: Any

def ragged_count_sparse_output_eager_fallback(splits, values, weights, binary_output, minlength, maxlength, name, ctx): ...

class _SparseCountSparseOutputOutput(NamedTuple):
    output_indices: Any
    output_values: Any
    output_dense_shape: Any

def sparse_count_sparse_output(indices, values, dense_shape, weights, binary_output, minlength: int = ..., maxlength: int = ..., name: Any | None = ...): ...

SparseCountSparseOutput: Any

def sparse_count_sparse_output_eager_fallback(indices, values, dense_shape, weights, binary_output, minlength, maxlength, name, ctx): ...
