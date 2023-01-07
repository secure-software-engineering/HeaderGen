from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

class _DenseToDenseSetOperationOutput(NamedTuple):
    result_indices: Any
    result_values: Any
    result_shape: Any

def dense_to_dense_set_operation(set1, set2, set_operation, validate_indices: bool = ..., name: Any | None = ...): ...

DenseToDenseSetOperation: Any

def dense_to_dense_set_operation_eager_fallback(set1, set2, set_operation, validate_indices, name, ctx): ...

class _DenseToSparseSetOperationOutput(NamedTuple):
    result_indices: Any
    result_values: Any
    result_shape: Any

def dense_to_sparse_set_operation(set1, set2_indices, set2_values, set2_shape, set_operation, validate_indices: bool = ..., name: Any | None = ...): ...

DenseToSparseSetOperation: Any

def dense_to_sparse_set_operation_eager_fallback(set1, set2_indices, set2_values, set2_shape, set_operation, validate_indices, name, ctx): ...
def set_size(set_indices, set_values, set_shape, validate_indices: bool = ..., name: Any | None = ...): ...

SetSize: Any

def set_size_eager_fallback(set_indices, set_values, set_shape, validate_indices, name, ctx): ...

class _SparseToSparseSetOperationOutput(NamedTuple):
    result_indices: Any
    result_values: Any
    result_shape: Any

def sparse_to_sparse_set_operation(set1_indices, set1_values, set1_shape, set2_indices, set2_values, set2_shape, set_operation, validate_indices: bool = ..., name: Any | None = ...): ...

SparseToSparseSetOperation: Any

def sparse_to_sparse_set_operation_eager_fallback(set1_indices, set1_values, set1_shape, set2_indices, set2_values, set2_shape, set_operation, validate_indices, name, ctx): ...
