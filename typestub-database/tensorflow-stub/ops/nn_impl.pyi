from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, candidate_sampling_ops as candidate_sampling_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, custom_gradient as custom_gradient, embedding_ops as embedding_ops, gen_array_ops as gen_array_ops, gen_nn_ops as gen_nn_ops, gen_sparse_ops as gen_sparse_ops, linalg_ops as linalg_ops, math_ops as math_ops, nn_ops as nn_ops, variables as variables
from tensorflow.python.platform import device_context as device_context
from tensorflow.python.util import dispatch as dispatch
from tensorflow.python.util.deprecation import deprecated_args as deprecated_args, deprecated_argument_lookup as deprecated_argument_lookup
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def log_poisson_loss(targets, log_input, compute_full_loss: bool = ..., name: Any | None = ...): ...
def sigmoid_cross_entropy_with_logits(_sentinel: Any | None = ..., labels: Any | None = ..., logits: Any | None = ..., name: Any | None = ...): ...
def sigmoid_cross_entropy_with_logits_v2(labels: Any | None = ..., logits: Any | None = ..., name: Any | None = ...): ...
def weighted_cross_entropy_with_logits_v2(labels, logits, pos_weight, name: Any | None = ...): ...
def weighted_cross_entropy_with_logits(labels: Any | None = ..., logits: Any | None = ..., pos_weight: Any | None = ..., name: Any | None = ..., targets: Any | None = ...): ...
def compute_average_loss(per_example_loss, sample_weight: Any | None = ..., global_batch_size: Any | None = ...): ...
def scale_regularization_loss(regularization_loss): ...
def relu_layer(x, weights, biases, name: Any | None = ...): ...
def swish(features): ...
def normalize(tensor, ord: str = ..., axis: Any | None = ..., name: Any | None = ...): ...
def l2_normalize(x, axis: Any | None = ..., epsilon: float = ..., name: Any | None = ..., dim: Any | None = ...): ...
def zero_fraction(value, name: Any | None = ...): ...
def depthwise_conv2d(input, filter, strides, padding, rate: Any | None = ..., name: Any | None = ..., data_format: Any | None = ..., dilations: Any | None = ...): ...
def depthwise_conv2d_v2(input, filter, strides, padding, data_format: Any | None = ..., dilations: Any | None = ..., name: Any | None = ...): ...
def separable_conv2d(input, depthwise_filter, pointwise_filter, strides, padding, rate: Any | None = ..., name: Any | None = ..., data_format: Any | None = ..., dilations: Any | None = ...): ...
def separable_conv2d_v2(input, depthwise_filter, pointwise_filter, strides, padding, data_format: Any | None = ..., dilations: Any | None = ..., name: Any | None = ...): ...
def sufficient_statistics(x, axes, shift: Any | None = ..., keep_dims: Any | None = ..., name: Any | None = ..., keepdims: Any | None = ...): ...
def sufficient_statistics_v2(x, axes, shift: Any | None = ..., keepdims: bool = ..., name: Any | None = ...): ...
def normalize_moments(counts, mean_ss, variance_ss, shift, name: Any | None = ...): ...
def moments(x, axes, shift: Any | None = ..., name: Any | None = ..., keep_dims: Any | None = ..., keepdims: Any | None = ...): ...
def moments_v2(x, axes, shift: Any | None = ..., keepdims: bool = ..., name: Any | None = ...): ...
def weighted_moments(x, axes, frequency_weights, name: Any | None = ..., keep_dims: Any | None = ..., keepdims: Any | None = ...): ...
def weighted_moments_v2(x, axes, frequency_weights, keepdims: bool = ..., name: Any | None = ...): ...
def batch_normalization(x, mean, variance, offset, scale, variance_epsilon, name: Any | None = ...): ...
def fused_batch_norm(x, scale, offset, mean: Any | None = ..., variance: Any | None = ..., epsilon: float = ..., data_format: str = ..., is_training: bool = ..., name: Any | None = ..., exponential_avg_factor: float = ...): ...
def batch_norm_with_global_normalization(t: Any | None = ..., m: Any | None = ..., v: Any | None = ..., beta: Any | None = ..., gamma: Any | None = ..., variance_epsilon: Any | None = ..., scale_after_normalization: Any | None = ..., name: Any | None = ..., input: Any | None = ..., mean: Any | None = ..., variance: Any | None = ...): ...
def batch_norm_with_global_normalization_v2(input, mean, variance, beta, gamma, variance_epsilon, scale_after_normalization, name: Any | None = ...): ...
def nce_loss_v2(weights, biases, labels, inputs, num_sampled, num_classes, num_true: int = ..., sampled_values: Any | None = ..., remove_accidental_hits: bool = ..., name: str = ...): ...
def nce_loss(weights, biases, labels, inputs, num_sampled, num_classes, num_true: int = ..., sampled_values: Any | None = ..., remove_accidental_hits: bool = ..., partition_strategy: str = ..., name: str = ...): ...
def sampled_softmax_loss_v2(weights, biases, labels, inputs, num_sampled, num_classes, num_true: int = ..., sampled_values: Any | None = ..., remove_accidental_hits: bool = ..., seed: Any | None = ..., name: str = ...): ...
def sampled_softmax_loss(weights, biases, labels, inputs, num_sampled, num_classes, num_true: int = ..., sampled_values: Any | None = ..., remove_accidental_hits: bool = ..., partition_strategy: str = ..., name: str = ..., seed: Any | None = ...): ...
