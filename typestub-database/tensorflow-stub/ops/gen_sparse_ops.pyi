from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

def add_many_sparse_to_tensors_map(sparse_indices, sparse_values, sparse_shape, container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

AddManySparseToTensorsMap: Any

def add_many_sparse_to_tensors_map_eager_fallback(sparse_indices, sparse_values, sparse_shape, container, shared_name, name, ctx): ...
def add_sparse_to_tensors_map(sparse_indices, sparse_values, sparse_shape, container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

AddSparseToTensorsMap: Any

def add_sparse_to_tensors_map_eager_fallback(sparse_indices, sparse_values, sparse_shape, container, shared_name, name, ctx): ...

class _DeserializeManySparseOutput(NamedTuple):
    sparse_indices: Any
    sparse_values: Any
    sparse_shape: Any

def deserialize_many_sparse(serialized_sparse, dtype, name: Any | None = ...): ...

DeserializeManySparse: Any

def deserialize_many_sparse_eager_fallback(serialized_sparse, dtype, name, ctx): ...

class _DeserializeSparseOutput(NamedTuple):
    sparse_indices: Any
    sparse_values: Any
    sparse_shape: Any

def deserialize_sparse(serialized_sparse, dtype, name: Any | None = ...): ...

DeserializeSparse: Any

def deserialize_sparse_eager_fallback(serialized_sparse, dtype, name, ctx): ...
def serialize_many_sparse(sparse_indices, sparse_values, sparse_shape, out_type=..., name: Any | None = ...): ...

SerializeManySparse: Any

def serialize_many_sparse_eager_fallback(sparse_indices, sparse_values, sparse_shape, out_type, name, ctx): ...
def serialize_sparse(sparse_indices, sparse_values, sparse_shape, out_type=..., name: Any | None = ...): ...

SerializeSparse: Any

def serialize_sparse_eager_fallback(sparse_indices, sparse_values, sparse_shape, out_type, name, ctx): ...

class _SparseAddOutput(NamedTuple):
    sum_indices: Any
    sum_values: Any
    sum_shape: Any

def sparse_add(a_indices, a_values, a_shape, b_indices, b_values, b_shape, thresh, name: Any | None = ...): ...

SparseAdd: Any

def sparse_add_eager_fallback(a_indices, a_values, a_shape, b_indices, b_values, b_shape, thresh, name, ctx): ...

class _SparseAddGradOutput(NamedTuple):
    a_val_grad: Any
    b_val_grad: Any

def sparse_add_grad(backprop_val_grad, a_indices, b_indices, sum_indices, name: Any | None = ...): ...

SparseAddGrad: Any

def sparse_add_grad_eager_fallback(backprop_val_grad, a_indices, b_indices, sum_indices, name, ctx): ...

class _SparseConcatOutput(NamedTuple):
    output_indices: Any
    output_values: Any
    output_shape: Any

def sparse_concat(indices, values, shapes, concat_dim, name: Any | None = ...): ...

SparseConcat: Any

def sparse_concat_eager_fallback(indices, values, shapes, concat_dim, name, ctx): ...

class _SparseCrossOutput(NamedTuple):
    output_indices: Any
    output_values: Any
    output_shape: Any

def sparse_cross(indices, values, shapes, dense_inputs, hashed_output, num_buckets, hash_key, out_type, internal_type, name: Any | None = ...): ...

SparseCross: Any

def sparse_cross_eager_fallback(indices, values, shapes, dense_inputs, hashed_output, num_buckets, hash_key, out_type, internal_type, name, ctx): ...

class _SparseCrossHashedOutput(NamedTuple):
    output_indices: Any
    output_values: Any
    output_shape: Any

def sparse_cross_hashed(indices, values, shapes, dense_inputs, num_buckets, strong_hash, salt, name: Any | None = ...): ...

SparseCrossHashed: Any

def sparse_cross_hashed_eager_fallback(indices, values, shapes, dense_inputs, num_buckets, strong_hash, salt, name, ctx): ...

class _SparseCrossV2Output(NamedTuple):
    output_indices: Any
    output_values: Any
    output_shape: Any

def sparse_cross_v2(indices, values, shapes, dense_inputs, sep, name: Any | None = ...): ...

SparseCrossV2: Any

def sparse_cross_v2_eager_fallback(indices, values, shapes, dense_inputs, sep, name, ctx): ...
def sparse_dense_cwise_add(sp_indices, sp_values, sp_shape, dense, name: Any | None = ...): ...

SparseDenseCwiseAdd: Any

def sparse_dense_cwise_add_eager_fallback(sp_indices, sp_values, sp_shape, dense, name, ctx): ...
def sparse_dense_cwise_div(sp_indices, sp_values, sp_shape, dense, name: Any | None = ...): ...

SparseDenseCwiseDiv: Any

def sparse_dense_cwise_div_eager_fallback(sp_indices, sp_values, sp_shape, dense, name, ctx): ...
def sparse_dense_cwise_mul(sp_indices, sp_values, sp_shape, dense, name: Any | None = ...): ...

SparseDenseCwiseMul: Any

def sparse_dense_cwise_mul_eager_fallback(sp_indices, sp_values, sp_shape, dense, name, ctx): ...

class _SparseFillEmptyRowsOutput(NamedTuple):
    output_indices: Any
    output_values: Any
    empty_row_indicator: Any
    reverse_index_map: Any

def sparse_fill_empty_rows(indices, values, dense_shape, default_value, name: Any | None = ...): ...

SparseFillEmptyRows: Any

def sparse_fill_empty_rows_eager_fallback(indices, values, dense_shape, default_value, name, ctx): ...

class _SparseFillEmptyRowsGradOutput(NamedTuple):
    d_values: Any
    d_default_value: Any

def sparse_fill_empty_rows_grad(reverse_index_map, grad_values, name: Any | None = ...): ...

SparseFillEmptyRowsGrad: Any

def sparse_fill_empty_rows_grad_eager_fallback(reverse_index_map, grad_values, name, ctx): ...
def sparse_reduce_max(input_indices, input_values, input_shape, reduction_axes, keep_dims: bool = ..., name: Any | None = ...): ...

SparseReduceMax: Any

def sparse_reduce_max_eager_fallback(input_indices, input_values, input_shape, reduction_axes, keep_dims, name, ctx): ...

class _SparseReduceMaxSparseOutput(NamedTuple):
    output_indices: Any
    output_values: Any
    output_shape: Any

def sparse_reduce_max_sparse(input_indices, input_values, input_shape, reduction_axes, keep_dims: bool = ..., name: Any | None = ...): ...

SparseReduceMaxSparse: Any

def sparse_reduce_max_sparse_eager_fallback(input_indices, input_values, input_shape, reduction_axes, keep_dims, name, ctx): ...
def sparse_reduce_sum(input_indices, input_values, input_shape, reduction_axes, keep_dims: bool = ..., name: Any | None = ...): ...

SparseReduceSum: Any

def sparse_reduce_sum_eager_fallback(input_indices, input_values, input_shape, reduction_axes, keep_dims, name, ctx): ...

class _SparseReduceSumSparseOutput(NamedTuple):
    output_indices: Any
    output_values: Any
    output_shape: Any

def sparse_reduce_sum_sparse(input_indices, input_values, input_shape, reduction_axes, keep_dims: bool = ..., name: Any | None = ...): ...

SparseReduceSumSparse: Any

def sparse_reduce_sum_sparse_eager_fallback(input_indices, input_values, input_shape, reduction_axes, keep_dims, name, ctx): ...

class _SparseReorderOutput(NamedTuple):
    output_indices: Any
    output_values: Any

def sparse_reorder(input_indices, input_values, input_shape, name: Any | None = ...): ...

SparseReorder: Any

def sparse_reorder_eager_fallback(input_indices, input_values, input_shape, name, ctx): ...

class _SparseReshapeOutput(NamedTuple):
    output_indices: Any
    output_shape: Any

def sparse_reshape(input_indices, input_shape, new_shape, name: Any | None = ...): ...

SparseReshape: Any

def sparse_reshape_eager_fallback(input_indices, input_shape, new_shape, name, ctx): ...

class _SparseSliceOutput(NamedTuple):
    output_indices: Any
    output_values: Any
    output_shape: Any

def sparse_slice(indices, values, shape, start, size, name: Any | None = ...): ...

SparseSlice: Any

def sparse_slice_eager_fallback(indices, values, shape, start, size, name, ctx): ...
def sparse_slice_grad(backprop_val_grad, input_indices, input_start, output_indices, name: Any | None = ...): ...

SparseSliceGrad: Any

def sparse_slice_grad_eager_fallback(backprop_val_grad, input_indices, input_start, output_indices, name, ctx): ...
def sparse_softmax(sp_indices, sp_values, sp_shape, name: Any | None = ...): ...

SparseSoftmax: Any

def sparse_softmax_eager_fallback(sp_indices, sp_values, sp_shape, name, ctx): ...

class _SparseSparseMaximumOutput(NamedTuple):
    output_indices: Any
    output_values: Any

def sparse_sparse_maximum(a_indices, a_values, a_shape, b_indices, b_values, b_shape, name: Any | None = ...): ...

SparseSparseMaximum: Any

def sparse_sparse_maximum_eager_fallback(a_indices, a_values, a_shape, b_indices, b_values, b_shape, name, ctx): ...

class _SparseSparseMinimumOutput(NamedTuple):
    output_indices: Any
    output_values: Any

def sparse_sparse_minimum(a_indices, a_values, a_shape, b_indices, b_values, b_shape, name: Any | None = ...): ...

SparseSparseMinimum: Any

def sparse_sparse_minimum_eager_fallback(a_indices, a_values, a_shape, b_indices, b_values, b_shape, name, ctx): ...

class _SparseSplitOutput(NamedTuple):
    output_indices: Any
    output_values: Any
    output_shape: Any

def sparse_split(split_dim, indices, values, shape, num_split, name: Any | None = ...): ...

SparseSplit: Any

def sparse_split_eager_fallback(split_dim, indices, values, shape, num_split, name, ctx): ...
def sparse_tensor_dense_add(a_indices, a_values, a_shape, b, name: Any | None = ...): ...

SparseTensorDenseAdd: Any

def sparse_tensor_dense_add_eager_fallback(a_indices, a_values, a_shape, b, name, ctx): ...
def sparse_tensor_dense_mat_mul(a_indices, a_values, a_shape, b, adjoint_a: bool = ..., adjoint_b: bool = ..., name: Any | None = ...): ...

SparseTensorDenseMatMul: Any

def sparse_tensor_dense_mat_mul_eager_fallback(a_indices, a_values, a_shape, b, adjoint_a, adjoint_b, name, ctx): ...
def sparse_to_dense(sparse_indices, output_shape, sparse_values, default_value, validate_indices: bool = ..., name: Any | None = ...): ...

SparseToDense: Any

def sparse_to_dense_eager_fallback(sparse_indices, output_shape, sparse_values, default_value, validate_indices, name, ctx): ...

class _TakeManySparseFromTensorsMapOutput(NamedTuple):
    sparse_indices: Any
    sparse_values: Any
    sparse_shape: Any

def take_many_sparse_from_tensors_map(sparse_handles, dtype, container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

TakeManySparseFromTensorsMap: Any

def take_many_sparse_from_tensors_map_eager_fallback(sparse_handles, dtype, container, shared_name, name, ctx): ...
