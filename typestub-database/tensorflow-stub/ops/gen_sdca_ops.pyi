from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

def sdca_fprint(input, name: Any | None = ...): ...

SdcaFprint: Any

def sdca_fprint_eager_fallback(input, name, ctx): ...

class _SdcaOptimizerOutput(NamedTuple):
    out_example_state_data: Any
    out_delta_sparse_weights: Any
    out_delta_dense_weights: Any

def sdca_optimizer(sparse_example_indices, sparse_feature_indices, sparse_feature_values, dense_features, example_weights, example_labels, sparse_indices, sparse_weights, dense_weights, example_state_data, loss_type, l1, l2, num_loss_partitions, num_inner_iterations, adaptative: bool = ..., name: Any | None = ...): ...

SdcaOptimizer: Any

def sdca_optimizer_eager_fallback(sparse_example_indices, sparse_feature_indices, sparse_feature_values, dense_features, example_weights, example_labels, sparse_indices, sparse_weights, dense_weights, example_state_data, loss_type, l1, l2, num_loss_partitions, num_inner_iterations, adaptative, name, ctx): ...

class _SdcaOptimizerV2Output(NamedTuple):
    out_example_state_data: Any
    out_delta_sparse_weights: Any
    out_delta_dense_weights: Any

def sdca_optimizer_v2(sparse_example_indices, sparse_feature_indices, sparse_feature_values, dense_features, example_weights, example_labels, sparse_indices, sparse_weights, dense_weights, example_state_data, loss_type, l1, l2, num_loss_partitions, num_inner_iterations, adaptive: bool = ..., name: Any | None = ...): ...

SdcaOptimizerV2: Any

def sdca_optimizer_v2_eager_fallback(sparse_example_indices, sparse_feature_indices, sparse_feature_values, dense_features, example_weights, example_labels, sparse_indices, sparse_weights, dense_weights, example_state_data, loss_type, l1, l2, num_loss_partitions, num_inner_iterations, adaptive, name, ctx): ...
def sdca_shrink_l1(weights, l1, l2, name: Any | None = ...): ...

SdcaShrinkL1: Any

def sdca_shrink_l1_eager_fallback(weights, l1, l2, name, ctx) -> None: ...
