from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

def avg_pool(value, ksize, strides, padding, data_format: str = ..., name: Any | None = ...): ...

AvgPool: Any

def avg_pool_eager_fallback(value, ksize, strides, padding, data_format, name, ctx): ...
def avg_pool3d(input, ksize, strides, padding, data_format: str = ..., name: Any | None = ...): ...

AvgPool3D: Any

def avg_pool3d_eager_fallback(input, ksize, strides, padding, data_format, name, ctx): ...
def avg_pool3d_grad(orig_input_shape, grad, ksize, strides, padding, data_format: str = ..., name: Any | None = ...): ...

AvgPool3DGrad: Any

def avg_pool3d_grad_eager_fallback(orig_input_shape, grad, ksize, strides, padding, data_format, name, ctx): ...
def avg_pool_grad(orig_input_shape, grad, ksize, strides, padding, data_format: str = ..., name: Any | None = ...): ...

AvgPoolGrad: Any

def avg_pool_grad_eager_fallback(orig_input_shape, grad, ksize, strides, padding, data_format, name, ctx): ...

BatchNormWithGlobalNormalization: Any

class _BatchNormWithGlobalNormalizationGradOutput(NamedTuple):
    dx: Any
    dm: Any
    dv: Any
    db: Any
    dg: Any

def batch_norm_with_global_normalization_grad(t, m, v, gamma, backprop, variance_epsilon, scale_after_normalization, name: Any | None = ...): ...

BatchNormWithGlobalNormalizationGrad: Any

def batch_norm_with_global_normalization_grad_eager_fallback(t, m, v, gamma, backprop, variance_epsilon, scale_after_normalization, name, ctx): ...
def bias_add(value, bias, data_format: str = ..., name: Any | None = ...): ...

BiasAdd: Any

def bias_add_eager_fallback(value, bias, data_format, name, ctx): ...
def bias_add_grad(out_backprop, data_format: str = ..., name: Any | None = ...): ...

BiasAddGrad: Any

def bias_add_grad_eager_fallback(out_backprop, data_format, name, ctx): ...
def bias_add_v1(value, bias, name: Any | None = ...): ...

BiasAddV1: Any

def bias_add_v1_eager_fallback(value, bias, name, ctx): ...
def conv2d(input, filter, strides, padding, use_cudnn_on_gpu: bool = ..., explicit_paddings=..., data_format: str = ..., dilations=..., name: Any | None = ...): ...

Conv2D: Any

def conv2d_eager_fallback(input, filter, strides, padding, use_cudnn_on_gpu, explicit_paddings, data_format, dilations, name, ctx): ...
def conv2d_backprop_filter(input, filter_sizes, out_backprop, strides, padding, use_cudnn_on_gpu: bool = ..., explicit_paddings=..., data_format: str = ..., dilations=..., name: Any | None = ...): ...

Conv2DBackpropFilter: Any

def conv2d_backprop_filter_eager_fallback(input, filter_sizes, out_backprop, strides, padding, use_cudnn_on_gpu, explicit_paddings, data_format, dilations, name, ctx): ...
def conv2d_backprop_input(input_sizes, filter, out_backprop, strides, padding, use_cudnn_on_gpu: bool = ..., explicit_paddings=..., data_format: str = ..., dilations=..., name: Any | None = ...): ...

Conv2DBackpropInput: Any

def conv2d_backprop_input_eager_fallback(input_sizes, filter, out_backprop, strides, padding, use_cudnn_on_gpu, explicit_paddings, data_format, dilations, name, ctx): ...
def conv3d(input, filter, strides, padding, data_format: str = ..., dilations=..., name: Any | None = ...): ...

Conv3D: Any

def conv3d_eager_fallback(input, filter, strides, padding, data_format, dilations, name, ctx): ...
def conv3d_backprop_filter(input, filter, out_backprop, strides, padding, dilations=..., name: Any | None = ...): ...

Conv3DBackpropFilter: Any

def conv3d_backprop_filter_eager_fallback(input, filter, out_backprop, strides, padding, dilations, name, ctx): ...
def conv3d_backprop_filter_v2(input, filter_sizes, out_backprop, strides, padding, data_format: str = ..., dilations=..., name: Any | None = ...): ...

Conv3DBackpropFilterV2: Any

def conv3d_backprop_filter_v2_eager_fallback(input, filter_sizes, out_backprop, strides, padding, data_format, dilations, name, ctx): ...
def conv3d_backprop_input(input, filter, out_backprop, strides, padding, dilations=..., name: Any | None = ...): ...

Conv3DBackpropInput: Any

def conv3d_backprop_input_eager_fallback(input, filter, out_backprop, strides, padding, dilations, name, ctx): ...
def conv3d_backprop_input_v2(input_sizes, filter, out_backprop, strides, padding, data_format: str = ..., dilations=..., name: Any | None = ...): ...

Conv3DBackpropInputV2: Any

def conv3d_backprop_input_v2_eager_fallback(input_sizes, filter, out_backprop, strides, padding, data_format, dilations, name, ctx): ...
def data_format_dim_map(x, src_format: str = ..., dst_format: str = ..., name: Any | None = ...): ...

DataFormatDimMap: Any

def data_format_dim_map_eager_fallback(x, src_format, dst_format, name, ctx): ...
def data_format_vec_permute(x, src_format: str = ..., dst_format: str = ..., name: Any | None = ...): ...

DataFormatVecPermute: Any

def data_format_vec_permute_eager_fallback(x, src_format, dst_format, name, ctx): ...
def depthwise_conv2d_native(input, filter, strides, padding, explicit_paddings=..., data_format: str = ..., dilations=..., name: Any | None = ...): ...

DepthwiseConv2dNative: Any

def depthwise_conv2d_native_eager_fallback(input, filter, strides, padding, explicit_paddings, data_format, dilations, name, ctx): ...
def depthwise_conv2d_native_backprop_filter(input, filter_sizes, out_backprop, strides, padding, explicit_paddings=..., data_format: str = ..., dilations=..., name: Any | None = ...): ...

DepthwiseConv2dNativeBackpropFilter: Any

def depthwise_conv2d_native_backprop_filter_eager_fallback(input, filter_sizes, out_backprop, strides, padding, explicit_paddings, data_format, dilations, name, ctx): ...
def depthwise_conv2d_native_backprop_input(input_sizes, filter, out_backprop, strides, padding, explicit_paddings=..., data_format: str = ..., dilations=..., name: Any | None = ...): ...

DepthwiseConv2dNativeBackpropInput: Any

def depthwise_conv2d_native_backprop_input_eager_fallback(input_sizes, filter, out_backprop, strides, padding, explicit_paddings, data_format, dilations, name, ctx): ...
def dilation2d(input, filter, strides, rates, padding, name: Any | None = ...): ...

Dilation2D: Any

def dilation2d_eager_fallback(input, filter, strides, rates, padding, name, ctx): ...
def dilation2d_backprop_filter(input, filter, out_backprop, strides, rates, padding, name: Any | None = ...): ...

Dilation2DBackpropFilter: Any

def dilation2d_backprop_filter_eager_fallback(input, filter, out_backprop, strides, rates, padding, name, ctx): ...
def dilation2d_backprop_input(input, filter, out_backprop, strides, rates, padding, name: Any | None = ...): ...

Dilation2DBackpropInput: Any

def dilation2d_backprop_input_eager_fallback(input, filter, out_backprop, strides, rates, padding, name, ctx): ...
def elu(features, name: Any | None = ...): ...

Elu: Any

def elu_eager_fallback(features, name, ctx): ...
def elu_grad(gradients, outputs, name: Any | None = ...): ...

EluGrad: Any

def elu_grad_eager_fallback(gradients, outputs, name, ctx): ...

class _FractionalAvgPoolOutput(NamedTuple):
    output: Any
    row_pooling_sequence: Any
    col_pooling_sequence: Any

def fractional_avg_pool(value, pooling_ratio, pseudo_random: bool = ..., overlapping: bool = ..., deterministic: bool = ..., seed: int = ..., seed2: int = ..., name: Any | None = ...): ...

FractionalAvgPool: Any

def fractional_avg_pool_eager_fallback(value, pooling_ratio, pseudo_random, overlapping, deterministic, seed, seed2, name, ctx): ...
def fractional_avg_pool_grad(orig_input_tensor_shape, out_backprop, row_pooling_sequence, col_pooling_sequence, overlapping: bool = ..., name: Any | None = ...): ...

FractionalAvgPoolGrad: Any

def fractional_avg_pool_grad_eager_fallback(orig_input_tensor_shape, out_backprop, row_pooling_sequence, col_pooling_sequence, overlapping, name, ctx): ...

class _FractionalMaxPoolOutput(NamedTuple):
    output: Any
    row_pooling_sequence: Any
    col_pooling_sequence: Any

def fractional_max_pool(value, pooling_ratio, pseudo_random: bool = ..., overlapping: bool = ..., deterministic: bool = ..., seed: int = ..., seed2: int = ..., name: Any | None = ...): ...

FractionalMaxPool: Any

def fractional_max_pool_eager_fallback(value, pooling_ratio, pseudo_random, overlapping, deterministic, seed, seed2, name, ctx): ...
def fractional_max_pool_grad(orig_input, orig_output, out_backprop, row_pooling_sequence, col_pooling_sequence, overlapping: bool = ..., name: Any | None = ...): ...

FractionalMaxPoolGrad: Any

def fractional_max_pool_grad_eager_fallback(orig_input, orig_output, out_backprop, row_pooling_sequence, col_pooling_sequence, overlapping, name, ctx): ...

class _FusedBatchNormOutput(NamedTuple):
    y: Any
    batch_mean: Any
    batch_variance: Any
    reserve_space_1: Any
    reserve_space_2: Any
FusedBatchNorm: Any

class _FusedBatchNormGradOutput(NamedTuple):
    x_backprop: Any
    scale_backprop: Any
    offset_backprop: Any
    reserve_space_3: Any
    reserve_space_4: Any

def fused_batch_norm_grad(y_backprop, x, scale, reserve_space_1, reserve_space_2, epsilon: float = ..., data_format: str = ..., is_training: bool = ..., name: Any | None = ...): ...

FusedBatchNormGrad: Any

def fused_batch_norm_grad_eager_fallback(y_backprop, x, scale, reserve_space_1, reserve_space_2, epsilon, data_format, is_training, name, ctx): ...

class _FusedBatchNormGradV2Output(NamedTuple):
    x_backprop: Any
    scale_backprop: Any
    offset_backprop: Any
    reserve_space_3: Any
    reserve_space_4: Any

def fused_batch_norm_grad_v2(y_backprop, x, scale, reserve_space_1, reserve_space_2, epsilon: float = ..., data_format: str = ..., is_training: bool = ..., name: Any | None = ...): ...

FusedBatchNormGradV2: Any

def fused_batch_norm_grad_v2_eager_fallback(y_backprop, x, scale, reserve_space_1, reserve_space_2, epsilon, data_format, is_training, name, ctx): ...

class _FusedBatchNormGradV3Output(NamedTuple):
    x_backprop: Any
    scale_backprop: Any
    offset_backprop: Any
    reserve_space_4: Any
    reserve_space_5: Any

def fused_batch_norm_grad_v3(y_backprop, x, scale, reserve_space_1, reserve_space_2, reserve_space_3, epsilon: float = ..., data_format: str = ..., is_training: bool = ..., name: Any | None = ...): ...

FusedBatchNormGradV3: Any

def fused_batch_norm_grad_v3_eager_fallback(y_backprop, x, scale, reserve_space_1, reserve_space_2, reserve_space_3, epsilon, data_format, is_training, name, ctx): ...

class _FusedBatchNormV2Output(NamedTuple):
    y: Any
    batch_mean: Any
    batch_variance: Any
    reserve_space_1: Any
    reserve_space_2: Any

def fused_batch_norm_v2(x, scale, offset, mean, variance, epsilon: float = ..., exponential_avg_factor: int = ..., data_format: str = ..., is_training: bool = ..., name: Any | None = ...): ...

FusedBatchNormV2: Any

def fused_batch_norm_v2_eager_fallback(x, scale, offset, mean, variance, epsilon, exponential_avg_factor, data_format, is_training, name, ctx): ...

class _FusedBatchNormV3Output(NamedTuple):
    y: Any
    batch_mean: Any
    batch_variance: Any
    reserve_space_1: Any
    reserve_space_2: Any
    reserve_space_3: Any

def fused_batch_norm_v3(x, scale, offset, mean, variance, epsilon: float = ..., exponential_avg_factor: int = ..., data_format: str = ..., is_training: bool = ..., name: Any | None = ...): ...

FusedBatchNormV3: Any

def fused_batch_norm_v3_eager_fallback(x, scale, offset, mean, variance, epsilon, exponential_avg_factor, data_format, is_training, name, ctx): ...
def fused_pad_conv2d(input, paddings, filter, mode, strides, padding, name: Any | None = ...): ...

FusedPadConv2D: Any

def fused_pad_conv2d_eager_fallback(input, paddings, filter, mode, strides, padding, name, ctx): ...
def fused_resize_and_pad_conv2d(input, size, paddings, filter, mode, strides, padding, resize_align_corners: bool = ..., name: Any | None = ...): ...

FusedResizeAndPadConv2D: Any

def fused_resize_and_pad_conv2d_eager_fallback(input, size, paddings, filter, mode, strides, padding, resize_align_corners, name, ctx): ...
def in_top_k(predictions, targets, k, name: Any | None = ...): ...

InTopK: Any

def in_top_k_eager_fallback(predictions, targets, k, name, ctx): ...
def in_top_kv2(predictions, targets, k, name: Any | None = ...): ...

InTopKV2: Any

def in_top_kv2_eager_fallback(predictions, targets, k, name, ctx): ...

class _IsotonicRegressionOutput(NamedTuple):
    output: Any
    segments: Any

def isotonic_regression(input, output_dtype=..., name: Any | None = ...): ...

IsotonicRegression: Any

def isotonic_regression_eager_fallback(input, output_dtype, name, ctx): ...
def l2_loss(t, name: Any | None = ...): ...

L2Loss: Any

def l2_loss_eager_fallback(t, name, ctx): ...
def lrn(input, depth_radius: int = ..., bias: int = ..., alpha: int = ..., beta: float = ..., name: Any | None = ...): ...

LRN: Any

def lrn_eager_fallback(input, depth_radius, bias, alpha, beta, name, ctx): ...
def lrn_grad(input_grads, input_image, output_image, depth_radius: int = ..., bias: int = ..., alpha: int = ..., beta: float = ..., name: Any | None = ...): ...

LRNGrad: Any

def lrn_grad_eager_fallback(input_grads, input_image, output_image, depth_radius, bias, alpha, beta, name, ctx): ...
def leaky_relu(features, alpha: float = ..., name: Any | None = ...): ...

LeakyRelu: Any

def leaky_relu_eager_fallback(features, alpha, name, ctx): ...
def leaky_relu_grad(gradients, features, alpha: float = ..., name: Any | None = ...): ...

LeakyReluGrad: Any

def leaky_relu_grad_eager_fallback(gradients, features, alpha, name, ctx): ...
def log_softmax(logits, name: Any | None = ...): ...

LogSoftmax: Any

def log_softmax_eager_fallback(logits, name, ctx): ...
def max_pool(input, ksize, strides, padding, explicit_paddings=..., data_format: str = ..., name: Any | None = ...): ...

MaxPool: Any

def max_pool_eager_fallback(input, ksize, strides, padding, explicit_paddings, data_format, name, ctx): ...
def max_pool3d(input, ksize, strides, padding, data_format: str = ..., name: Any | None = ...): ...

MaxPool3D: Any

def max_pool3d_eager_fallback(input, ksize, strides, padding, data_format, name, ctx): ...
def max_pool3d_grad(orig_input, orig_output, grad, ksize, strides, padding, data_format: str = ..., name: Any | None = ...): ...

MaxPool3DGrad: Any

def max_pool3d_grad_eager_fallback(orig_input, orig_output, grad, ksize, strides, padding, data_format, name, ctx): ...
def max_pool3d_grad_grad(orig_input, orig_output, grad, ksize, strides, padding, data_format: str = ..., name: Any | None = ...): ...

MaxPool3DGradGrad: Any

def max_pool3d_grad_grad_eager_fallback(orig_input, orig_output, grad, ksize, strides, padding, data_format, name, ctx): ...
def max_pool_grad(orig_input, orig_output, grad, ksize, strides, padding, explicit_paddings=..., data_format: str = ..., name: Any | None = ...): ...

MaxPoolGrad: Any

def max_pool_grad_eager_fallback(orig_input, orig_output, grad, ksize, strides, padding, explicit_paddings, data_format, name, ctx): ...
def max_pool_grad_grad(orig_input, orig_output, grad, ksize, strides, padding, data_format: str = ..., name: Any | None = ...): ...

MaxPoolGradGrad: Any

def max_pool_grad_grad_eager_fallback(orig_input, orig_output, grad, ksize, strides, padding, data_format, name, ctx): ...
def max_pool_grad_grad_v2(orig_input, orig_output, grad, ksize, strides, padding, data_format: str = ..., name: Any | None = ...): ...

MaxPoolGradGradV2: Any

def max_pool_grad_grad_v2_eager_fallback(orig_input, orig_output, grad, ksize, strides, padding, data_format, name, ctx): ...
def max_pool_grad_grad_with_argmax(input, grad, argmax, ksize, strides, padding, include_batch_in_index: bool = ..., name: Any | None = ...): ...

MaxPoolGradGradWithArgmax: Any

def max_pool_grad_grad_with_argmax_eager_fallback(input, grad, argmax, ksize, strides, padding, include_batch_in_index, name, ctx): ...
def max_pool_grad_v2(orig_input, orig_output, grad, ksize, strides, padding, data_format: str = ..., name: Any | None = ...): ...

MaxPoolGradV2: Any

def max_pool_grad_v2_eager_fallback(orig_input, orig_output, grad, ksize, strides, padding, data_format, name, ctx): ...
def max_pool_grad_with_argmax(input, grad, argmax, ksize, strides, padding, include_batch_in_index: bool = ..., name: Any | None = ...): ...

MaxPoolGradWithArgmax: Any

def max_pool_grad_with_argmax_eager_fallback(input, grad, argmax, ksize, strides, padding, include_batch_in_index, name, ctx): ...
def max_pool_v2(input, ksize, strides, padding, data_format: str = ..., name: Any | None = ...): ...

MaxPoolV2: Any

def max_pool_v2_eager_fallback(input, ksize, strides, padding, data_format, name, ctx): ...

class _MaxPoolWithArgmaxOutput(NamedTuple):
    output: Any
    argmax: Any

def max_pool_with_argmax(input, ksize, strides, padding, Targmax=..., include_batch_in_index: bool = ..., name: Any | None = ...): ...

MaxPoolWithArgmax: Any

def max_pool_with_argmax_eager_fallback(input, ksize, strides, padding, Targmax, include_batch_in_index, name, ctx): ...
def nth_element(input, n, reverse: bool = ..., name: Any | None = ...): ...

NthElement: Any

def nth_element_eager_fallback(input, n, reverse, name, ctx): ...

class _QuantizedAvgPoolOutput(NamedTuple):
    output: Any
    min_output: Any
    max_output: Any

def quantized_avg_pool(input, min_input, max_input, ksize, strides, padding, name: Any | None = ...): ...

QuantizedAvgPool: Any

def quantized_avg_pool_eager_fallback(input, min_input, max_input, ksize, strides, padding, name, ctx): ...

class _QuantizedBatchNormWithGlobalNormalizationOutput(NamedTuple):
    result: Any
    result_min: Any
    result_max: Any

def quantized_batch_norm_with_global_normalization(t, t_min, t_max, m, m_min, m_max, v, v_min, v_max, beta, beta_min, beta_max, gamma, gamma_min, gamma_max, out_type, variance_epsilon, scale_after_normalization, name: Any | None = ...): ...

QuantizedBatchNormWithGlobalNormalization: Any

def quantized_batch_norm_with_global_normalization_eager_fallback(t, t_min, t_max, m, m_min, m_max, v, v_min, v_max, beta, beta_min, beta_max, gamma, gamma_min, gamma_max, out_type, variance_epsilon, scale_after_normalization, name, ctx): ...

class _QuantizedBiasAddOutput(NamedTuple):
    output: Any
    min_out: Any
    max_out: Any

def quantized_bias_add(input, bias, min_input, max_input, min_bias, max_bias, out_type, name: Any | None = ...): ...

QuantizedBiasAdd: Any

def quantized_bias_add_eager_fallback(input, bias, min_input, max_input, min_bias, max_bias, out_type, name, ctx): ...

class _QuantizedConv2DOutput(NamedTuple):
    output: Any
    min_output: Any
    max_output: Any

def quantized_conv2d(input, filter, min_input, max_input, min_filter, max_filter, strides, padding, out_type=..., dilations=..., name: Any | None = ...): ...

QuantizedConv2D: Any

def quantized_conv2d_eager_fallback(input, filter, min_input, max_input, min_filter, max_filter, strides, padding, out_type, dilations, name, ctx): ...

class _QuantizedConv2DAndReluOutput(NamedTuple):
    output: Any
    min_output: Any
    max_output: Any

def quantized_conv2d_and_relu(input, filter, min_input, max_input, min_filter, max_filter, strides, padding, out_type=..., dilations=..., padding_list=..., name: Any | None = ...): ...

QuantizedConv2DAndRelu: Any

def quantized_conv2d_and_relu_eager_fallback(input, filter, min_input, max_input, min_filter, max_filter, strides, padding, out_type, dilations, padding_list, name, ctx): ...

class _QuantizedConv2DAndReluAndRequantizeOutput(NamedTuple):
    output: Any
    min_output: Any
    max_output: Any

def quantized_conv2d_and_relu_and_requantize(input, filter, min_input, max_input, min_filter, max_filter, min_freezed_output, max_freezed_output, strides, padding, out_type=..., dilations=..., padding_list=..., name: Any | None = ...): ...

QuantizedConv2DAndReluAndRequantize: Any

def quantized_conv2d_and_relu_and_requantize_eager_fallback(input, filter, min_input, max_input, min_filter, max_filter, min_freezed_output, max_freezed_output, strides, padding, out_type, dilations, padding_list, name, ctx): ...

class _QuantizedConv2DAndRequantizeOutput(NamedTuple):
    output: Any
    min_output: Any
    max_output: Any

def quantized_conv2d_and_requantize(input, filter, min_input, max_input, min_filter, max_filter, min_freezed_output, max_freezed_output, strides, padding, out_type=..., dilations=..., padding_list=..., name: Any | None = ...): ...

QuantizedConv2DAndRequantize: Any

def quantized_conv2d_and_requantize_eager_fallback(input, filter, min_input, max_input, min_filter, max_filter, min_freezed_output, max_freezed_output, strides, padding, out_type, dilations, padding_list, name, ctx): ...

class _QuantizedConv2DPerChannelOutput(NamedTuple):
    output: Any
    min_output: Any
    max_output: Any

def quantized_conv2d_per_channel(input, filter, min_input, max_input, min_filter, max_filter, strides, padding, out_type=..., dilations=..., name: Any | None = ...): ...

QuantizedConv2DPerChannel: Any

def quantized_conv2d_per_channel_eager_fallback(input, filter, min_input, max_input, min_filter, max_filter, strides, padding, out_type, dilations, name, ctx): ...

class _QuantizedConv2DWithBiasOutput(NamedTuple):
    output: Any
    min_output: Any
    max_output: Any

def quantized_conv2d_with_bias(input, filter, bias, min_input, max_input, min_filter, max_filter, strides, padding, out_type=..., dilations=..., padding_list=..., name: Any | None = ...): ...

QuantizedConv2DWithBias: Any

def quantized_conv2d_with_bias_eager_fallback(input, filter, bias, min_input, max_input, min_filter, max_filter, strides, padding, out_type, dilations, padding_list, name, ctx): ...

class _QuantizedConv2DWithBiasAndReluOutput(NamedTuple):
    output: Any
    min_output: Any
    max_output: Any

def quantized_conv2d_with_bias_and_relu(input, filter, bias, min_input, max_input, min_filter, max_filter, strides, padding, out_type=..., dilations=..., padding_list=..., name: Any | None = ...): ...

QuantizedConv2DWithBiasAndRelu: Any

def quantized_conv2d_with_bias_and_relu_eager_fallback(input, filter, bias, min_input, max_input, min_filter, max_filter, strides, padding, out_type, dilations, padding_list, name, ctx): ...

class _QuantizedConv2DWithBiasAndReluAndRequantizeOutput(NamedTuple):
    output: Any
    min_output: Any
    max_output: Any

def quantized_conv2d_with_bias_and_relu_and_requantize(input, filter, bias, min_input, max_input, min_filter, max_filter, min_freezed_output, max_freezed_output, strides, padding, out_type=..., dilations=..., padding_list=..., name: Any | None = ...): ...

QuantizedConv2DWithBiasAndReluAndRequantize: Any

def quantized_conv2d_with_bias_and_relu_and_requantize_eager_fallback(input, filter, bias, min_input, max_input, min_filter, max_filter, min_freezed_output, max_freezed_output, strides, padding, out_type, dilations, padding_list, name, ctx): ...

class _QuantizedConv2DWithBiasAndRequantizeOutput(NamedTuple):
    output: Any
    min_output: Any
    max_output: Any

def quantized_conv2d_with_bias_and_requantize(input, filter, bias, min_input, max_input, min_filter, max_filter, min_freezed_output, max_freezed_output, strides, padding, out_type=..., dilations=..., padding_list=..., name: Any | None = ...): ...

QuantizedConv2DWithBiasAndRequantize: Any

def quantized_conv2d_with_bias_and_requantize_eager_fallback(input, filter, bias, min_input, max_input, min_filter, max_filter, min_freezed_output, max_freezed_output, strides, padding, out_type, dilations, padding_list, name, ctx): ...

class _QuantizedConv2DWithBiasSignedSumAndReluAndRequantizeOutput(NamedTuple):
    output: Any
    min_output: Any
    max_output: Any

def quantized_conv2d_with_bias_signed_sum_and_relu_and_requantize(input, filter, bias, min_input, max_input, min_filter, max_filter, min_freezed_output, max_freezed_output, summand, min_summand, max_summand, strides, padding, out_type=..., dilations=..., padding_list=..., name: Any | None = ...): ...

QuantizedConv2DWithBiasSignedSumAndReluAndRequantize: Any

def quantized_conv2d_with_bias_signed_sum_and_relu_and_requantize_eager_fallback(input, filter, bias, min_input, max_input, min_filter, max_filter, min_freezed_output, max_freezed_output, summand, min_summand, max_summand, strides, padding, out_type, dilations, padding_list, name, ctx): ...

class _QuantizedConv2DWithBiasSumAndReluOutput(NamedTuple):
    output: Any
    min_output: Any
    max_output: Any

def quantized_conv2d_with_bias_sum_and_relu(input, filter, bias, min_input, max_input, min_filter, max_filter, summand, strides, padding, out_type=..., dilations=..., padding_list=..., name: Any | None = ...): ...

QuantizedConv2DWithBiasSumAndRelu: Any

def quantized_conv2d_with_bias_sum_and_relu_eager_fallback(input, filter, bias, min_input, max_input, min_filter, max_filter, summand, strides, padding, out_type, dilations, padding_list, name, ctx): ...

class _QuantizedConv2DWithBiasSumAndReluAndRequantizeOutput(NamedTuple):
    output: Any
    min_output: Any
    max_output: Any

def quantized_conv2d_with_bias_sum_and_relu_and_requantize(input, filter, bias, min_input, max_input, min_filter, max_filter, min_freezed_output, max_freezed_output, summand, min_summand, max_summand, strides, padding, out_type=..., dilations=..., padding_list=..., name: Any | None = ...): ...

QuantizedConv2DWithBiasSumAndReluAndRequantize: Any

def quantized_conv2d_with_bias_sum_and_relu_and_requantize_eager_fallback(input, filter, bias, min_input, max_input, min_filter, max_filter, min_freezed_output, max_freezed_output, summand, min_summand, max_summand, strides, padding, out_type, dilations, padding_list, name, ctx): ...

class _QuantizedDepthwiseConv2DOutput(NamedTuple):
    output: Any
    min_output: Any
    max_output: Any

def quantized_depthwise_conv2d(input, filter, min_input, max_input, min_filter, max_filter, strides, padding, out_type=..., dilations=..., name: Any | None = ...): ...

QuantizedDepthwiseConv2D: Any

def quantized_depthwise_conv2d_eager_fallback(input, filter, min_input, max_input, min_filter, max_filter, strides, padding, out_type, dilations, name, ctx): ...

class _QuantizedDepthwiseConv2DWithBiasOutput(NamedTuple):
    output: Any
    min_output: Any
    max_output: Any

def quantized_depthwise_conv2d_with_bias(input, filter, bias, min_input, max_input, min_filter, max_filter, strides, padding, out_type=..., dilations=..., name: Any | None = ...): ...

QuantizedDepthwiseConv2DWithBias: Any

def quantized_depthwise_conv2d_with_bias_eager_fallback(input, filter, bias, min_input, max_input, min_filter, max_filter, strides, padding, out_type, dilations, name, ctx): ...

class _QuantizedDepthwiseConv2DWithBiasAndReluOutput(NamedTuple):
    output: Any
    min_output: Any
    max_output: Any

def quantized_depthwise_conv2d_with_bias_and_relu(input, filter, bias, min_input, max_input, min_filter, max_filter, strides, padding, out_type=..., dilations=..., padding_list=..., name: Any | None = ...): ...

QuantizedDepthwiseConv2DWithBiasAndRelu: Any

def quantized_depthwise_conv2d_with_bias_and_relu_eager_fallback(input, filter, bias, min_input, max_input, min_filter, max_filter, strides, padding, out_type, dilations, padding_list, name, ctx): ...

class _QuantizedDepthwiseConv2DWithBiasAndReluAndRequantizeOutput(NamedTuple):
    output: Any
    min_output: Any
    max_output: Any

def quantized_depthwise_conv2d_with_bias_and_relu_and_requantize(input, filter, bias, min_input, max_input, min_filter, max_filter, min_freezed_output, max_freezed_output, strides, padding, out_type=..., dilations=..., padding_list=..., name: Any | None = ...): ...

QuantizedDepthwiseConv2DWithBiasAndReluAndRequantize: Any

def quantized_depthwise_conv2d_with_bias_and_relu_and_requantize_eager_fallback(input, filter, bias, min_input, max_input, min_filter, max_filter, min_freezed_output, max_freezed_output, strides, padding, out_type, dilations, padding_list, name, ctx): ...

class _QuantizedMatMulWithBiasOutput(NamedTuple):
    out: Any
    min_out: Any
    max_out: Any

def quantized_mat_mul_with_bias(a, b, bias, min_a, max_a, min_b, max_b, Toutput=..., transpose_a: bool = ..., transpose_b: bool = ..., input_quant_mode: str = ..., name: Any | None = ...): ...

QuantizedMatMulWithBias: Any

def quantized_mat_mul_with_bias_eager_fallback(a, b, bias, min_a, max_a, min_b, max_b, Toutput, transpose_a, transpose_b, input_quant_mode, name, ctx): ...
def quantized_mat_mul_with_bias_and_dequantize(a, b, bias, min_a, max_a, min_b, max_b, min_freezed_output, max_freezed_output, Toutput, transpose_a: bool = ..., transpose_b: bool = ..., input_quant_mode: str = ..., name: Any | None = ...): ...

QuantizedMatMulWithBiasAndDequantize: Any

def quantized_mat_mul_with_bias_and_dequantize_eager_fallback(a, b, bias, min_a, max_a, min_b, max_b, min_freezed_output, max_freezed_output, Toutput, transpose_a, transpose_b, input_quant_mode, name, ctx): ...

class _QuantizedMatMulWithBiasAndReluOutput(NamedTuple):
    out: Any
    min_out: Any
    max_out: Any

def quantized_mat_mul_with_bias_and_relu(a, b, bias, min_a, max_a, min_b, max_b, Toutput=..., transpose_a: bool = ..., transpose_b: bool = ..., input_quant_mode: str = ..., name: Any | None = ...): ...

QuantizedMatMulWithBiasAndRelu: Any

def quantized_mat_mul_with_bias_and_relu_eager_fallback(a, b, bias, min_a, max_a, min_b, max_b, Toutput, transpose_a, transpose_b, input_quant_mode, name, ctx): ...

class _QuantizedMatMulWithBiasAndReluAndRequantizeOutput(NamedTuple):
    out: Any
    min_out: Any
    max_out: Any

def quantized_mat_mul_with_bias_and_relu_and_requantize(a, b, bias, min_a, max_a, min_b, max_b, min_freezed_output, max_freezed_output, Toutput=..., transpose_a: bool = ..., transpose_b: bool = ..., input_quant_mode: str = ..., name: Any | None = ...): ...

QuantizedMatMulWithBiasAndReluAndRequantize: Any

def quantized_mat_mul_with_bias_and_relu_and_requantize_eager_fallback(a, b, bias, min_a, max_a, min_b, max_b, min_freezed_output, max_freezed_output, Toutput, transpose_a, transpose_b, input_quant_mode, name, ctx): ...

class _QuantizedMatMulWithBiasAndRequantizeOutput(NamedTuple):
    out: Any
    min_out: Any
    max_out: Any

def quantized_mat_mul_with_bias_and_requantize(a, b, bias, min_a, max_a, min_b, max_b, min_freezed_output, max_freezed_output, Toutput=..., transpose_a: bool = ..., transpose_b: bool = ..., input_quant_mode: str = ..., name: Any | None = ...): ...

QuantizedMatMulWithBiasAndRequantize: Any

def quantized_mat_mul_with_bias_and_requantize_eager_fallback(a, b, bias, min_a, max_a, min_b, max_b, min_freezed_output, max_freezed_output, Toutput, transpose_a, transpose_b, input_quant_mode, name, ctx): ...

class _QuantizedMaxPoolOutput(NamedTuple):
    output: Any
    min_output: Any
    max_output: Any

def quantized_max_pool(input, min_input, max_input, ksize, strides, padding, name: Any | None = ...): ...

QuantizedMaxPool: Any

def quantized_max_pool_eager_fallback(input, min_input, max_input, ksize, strides, padding, name, ctx): ...

class _QuantizedReluOutput(NamedTuple):
    activations: Any
    min_activations: Any
    max_activations: Any

def quantized_relu(features, min_features, max_features, out_type=..., name: Any | None = ...): ...

QuantizedRelu: Any

def quantized_relu_eager_fallback(features, min_features, max_features, out_type, name, ctx): ...

class _QuantizedRelu6Output(NamedTuple):
    activations: Any
    min_activations: Any
    max_activations: Any

def quantized_relu6(features, min_features, max_features, out_type=..., name: Any | None = ...): ...

QuantizedRelu6: Any

def quantized_relu6_eager_fallback(features, min_features, max_features, out_type, name, ctx): ...

class _QuantizedReluXOutput(NamedTuple):
    activations: Any
    min_activations: Any
    max_activations: Any

def quantized_relu_x(features, max_value, min_features, max_features, out_type=..., name: Any | None = ...): ...

QuantizedReluX: Any

def quantized_relu_x_eager_fallback(features, max_value, min_features, max_features, out_type, name, ctx): ...
def relu(features, name: Any | None = ...): ...

Relu: Any

def relu_eager_fallback(features, name, ctx): ...
def relu6(features, name: Any | None = ...): ...

Relu6: Any

def relu6_eager_fallback(features, name, ctx): ...
def relu6_grad(gradients, features, name: Any | None = ...): ...

Relu6Grad: Any

def relu6_grad_eager_fallback(gradients, features, name, ctx): ...
def relu_grad(gradients, features, name: Any | None = ...): ...

ReluGrad: Any

def relu_grad_eager_fallback(gradients, features, name, ctx): ...
def selu(features, name: Any | None = ...): ...

Selu: Any

def selu_eager_fallback(features, name, ctx): ...
def selu_grad(gradients, outputs, name: Any | None = ...): ...

SeluGrad: Any

def selu_grad_eager_fallback(gradients, outputs, name, ctx): ...
def softmax(logits, name: Any | None = ...): ...

Softmax: Any

def softmax_eager_fallback(logits, name, ctx): ...

class _SoftmaxCrossEntropyWithLogitsOutput(NamedTuple):
    loss: Any
    backprop: Any

def softmax_cross_entropy_with_logits(features, labels, name: Any | None = ...): ...

SoftmaxCrossEntropyWithLogits: Any

def softmax_cross_entropy_with_logits_eager_fallback(features, labels, name, ctx): ...
def softplus(features, name: Any | None = ...): ...

Softplus: Any

def softplus_eager_fallback(features, name, ctx): ...
def softplus_grad(gradients, features, name: Any | None = ...): ...

SoftplusGrad: Any

def softplus_grad_eager_fallback(gradients, features, name, ctx): ...
def softsign(features, name: Any | None = ...): ...

Softsign: Any

def softsign_eager_fallback(features, name, ctx): ...
def softsign_grad(gradients, features, name: Any | None = ...): ...

SoftsignGrad: Any

def softsign_grad_eager_fallback(gradients, features, name, ctx): ...

class _SparseSoftmaxCrossEntropyWithLogitsOutput(NamedTuple):
    loss: Any
    backprop: Any

def sparse_softmax_cross_entropy_with_logits(features, labels, name: Any | None = ...): ...

SparseSoftmaxCrossEntropyWithLogits: Any

def sparse_softmax_cross_entropy_with_logits_eager_fallback(features, labels, name, ctx): ...

class _TopKOutput(NamedTuple):
    values: Any
    indices: Any

def top_k(input, k, sorted: bool = ..., name: Any | None = ...): ...

TopK: Any

def top_k_eager_fallback(input, k, sorted, name, ctx): ...

class _TopKV2Output(NamedTuple):
    values: Any
    indices: Any

def top_kv2(input, k, sorted: bool = ..., name: Any | None = ...): ...

TopKV2: Any

def top_kv2_eager_fallback(input, k, sorted, name, ctx): ...
