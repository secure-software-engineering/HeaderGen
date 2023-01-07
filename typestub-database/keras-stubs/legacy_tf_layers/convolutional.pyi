from keras import layers as keras_layers
from keras.legacy_tf_layers import base as base
from typing import Any

class Conv1D(keras_layers.Conv1D, base.Layer):
    def __init__(self, filters, kernel_size, strides: int = ..., padding: str = ..., data_format: str = ..., dilation_rate: int = ..., activation: Any | None = ..., use_bias: bool = ..., kernel_initializer: Any | None = ..., bias_initializer=..., kernel_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., kernel_constraint: Any | None = ..., bias_constraint: Any | None = ..., trainable: bool = ..., name: Any | None = ..., **kwargs) -> None: ...

def conv1d(inputs, filters, kernel_size, strides: int = ..., padding: str = ..., data_format: str = ..., dilation_rate: int = ..., activation: Any | None = ..., use_bias: bool = ..., kernel_initializer: Any | None = ..., bias_initializer=..., kernel_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., kernel_constraint: Any | None = ..., bias_constraint: Any | None = ..., trainable: bool = ..., name: Any | None = ..., reuse: Any | None = ...): ...

class Conv2D(keras_layers.Conv2D, base.Layer):
    def __init__(self, filters, kernel_size, strides=..., padding: str = ..., data_format: str = ..., dilation_rate=..., activation: Any | None = ..., use_bias: bool = ..., kernel_initializer: Any | None = ..., bias_initializer=..., kernel_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., kernel_constraint: Any | None = ..., bias_constraint: Any | None = ..., trainable: bool = ..., name: Any | None = ..., **kwargs) -> None: ...

def conv2d(inputs, filters, kernel_size, strides=..., padding: str = ..., data_format: str = ..., dilation_rate=..., activation: Any | None = ..., use_bias: bool = ..., kernel_initializer: Any | None = ..., bias_initializer=..., kernel_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., kernel_constraint: Any | None = ..., bias_constraint: Any | None = ..., trainable: bool = ..., name: Any | None = ..., reuse: Any | None = ...): ...

class Conv3D(keras_layers.Conv3D, base.Layer):
    def __init__(self, filters, kernel_size, strides=..., padding: str = ..., data_format: str = ..., dilation_rate=..., activation: Any | None = ..., use_bias: bool = ..., kernel_initializer: Any | None = ..., bias_initializer=..., kernel_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., kernel_constraint: Any | None = ..., bias_constraint: Any | None = ..., trainable: bool = ..., name: Any | None = ..., **kwargs) -> None: ...

def conv3d(inputs, filters, kernel_size, strides=..., padding: str = ..., data_format: str = ..., dilation_rate=..., activation: Any | None = ..., use_bias: bool = ..., kernel_initializer: Any | None = ..., bias_initializer=..., kernel_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., kernel_constraint: Any | None = ..., bias_constraint: Any | None = ..., trainable: bool = ..., name: Any | None = ..., reuse: Any | None = ...): ...

class SeparableConv1D(keras_layers.SeparableConv1D, base.Layer):
    def __init__(self, filters, kernel_size, strides: int = ..., padding: str = ..., data_format: str = ..., dilation_rate: int = ..., depth_multiplier: int = ..., activation: Any | None = ..., use_bias: bool = ..., depthwise_initializer: Any | None = ..., pointwise_initializer: Any | None = ..., bias_initializer=..., depthwise_regularizer: Any | None = ..., pointwise_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., depthwise_constraint: Any | None = ..., pointwise_constraint: Any | None = ..., bias_constraint: Any | None = ..., trainable: bool = ..., name: Any | None = ..., **kwargs) -> None: ...

class SeparableConv2D(keras_layers.SeparableConv2D, base.Layer):
    def __init__(self, filters, kernel_size, strides=..., padding: str = ..., data_format: str = ..., dilation_rate=..., depth_multiplier: int = ..., activation: Any | None = ..., use_bias: bool = ..., depthwise_initializer: Any | None = ..., pointwise_initializer: Any | None = ..., bias_initializer=..., depthwise_regularizer: Any | None = ..., pointwise_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., depthwise_constraint: Any | None = ..., pointwise_constraint: Any | None = ..., bias_constraint: Any | None = ..., trainable: bool = ..., name: Any | None = ..., **kwargs) -> None: ...

def separable_conv1d(inputs, filters, kernel_size, strides: int = ..., padding: str = ..., data_format: str = ..., dilation_rate: int = ..., depth_multiplier: int = ..., activation: Any | None = ..., use_bias: bool = ..., depthwise_initializer: Any | None = ..., pointwise_initializer: Any | None = ..., bias_initializer=..., depthwise_regularizer: Any | None = ..., pointwise_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., depthwise_constraint: Any | None = ..., pointwise_constraint: Any | None = ..., bias_constraint: Any | None = ..., trainable: bool = ..., name: Any | None = ..., reuse: Any | None = ...): ...
def separable_conv2d(inputs, filters, kernel_size, strides=..., padding: str = ..., data_format: str = ..., dilation_rate=..., depth_multiplier: int = ..., activation: Any | None = ..., use_bias: bool = ..., depthwise_initializer: Any | None = ..., pointwise_initializer: Any | None = ..., bias_initializer=..., depthwise_regularizer: Any | None = ..., pointwise_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., depthwise_constraint: Any | None = ..., pointwise_constraint: Any | None = ..., bias_constraint: Any | None = ..., trainable: bool = ..., name: Any | None = ..., reuse: Any | None = ...): ...

class Conv2DTranspose(keras_layers.Conv2DTranspose, base.Layer):
    def __init__(self, filters, kernel_size, strides=..., padding: str = ..., data_format: str = ..., activation: Any | None = ..., use_bias: bool = ..., kernel_initializer: Any | None = ..., bias_initializer=..., kernel_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., kernel_constraint: Any | None = ..., bias_constraint: Any | None = ..., trainable: bool = ..., name: Any | None = ..., **kwargs) -> None: ...

def conv2d_transpose(inputs, filters, kernel_size, strides=..., padding: str = ..., data_format: str = ..., activation: Any | None = ..., use_bias: bool = ..., kernel_initializer: Any | None = ..., bias_initializer=..., kernel_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., kernel_constraint: Any | None = ..., bias_constraint: Any | None = ..., trainable: bool = ..., name: Any | None = ..., reuse: Any | None = ...): ...

class Conv3DTranspose(keras_layers.Conv3DTranspose, base.Layer):
    def __init__(self, filters, kernel_size, strides=..., padding: str = ..., data_format: str = ..., activation: Any | None = ..., use_bias: bool = ..., kernel_initializer: Any | None = ..., bias_initializer=..., kernel_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., kernel_constraint: Any | None = ..., bias_constraint: Any | None = ..., trainable: bool = ..., name: Any | None = ..., **kwargs) -> None: ...

def conv3d_transpose(inputs, filters, kernel_size, strides=..., padding: str = ..., data_format: str = ..., activation: Any | None = ..., use_bias: bool = ..., kernel_initializer: Any | None = ..., bias_initializer=..., kernel_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., kernel_constraint: Any | None = ..., bias_constraint: Any | None = ..., trainable: bool = ..., name: Any | None = ..., reuse: Any | None = ...): ...
Convolution1D = Conv1D
Convolution2D = Conv2D
Convolution3D = Conv3D
SeparableConvolution2D = SeparableConv2D
Convolution2DTranspose = Conv2DTranspose
Deconvolution2D = Conv2DTranspose
Deconv2D = Conv2DTranspose
Convolution3DTranspose = Conv3DTranspose
Deconvolution3D = Conv3DTranspose
Deconv3D = Conv3DTranspose
convolution1d = conv1d
convolution2d = conv2d
convolution3d = conv3d
separable_convolution2d = separable_conv2d
convolution2d_transpose = conv2d_transpose
deconvolution2d = conv2d_transpose
deconv2d = conv2d_transpose
convolution3d_transpose = conv3d_transpose
deconvolution3d = conv3d_transpose
deconv3d = conv3d_transpose
