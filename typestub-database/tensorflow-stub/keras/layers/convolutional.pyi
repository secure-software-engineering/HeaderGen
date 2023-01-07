from tensorflow.python.eager import context as context
from tensorflow.python.framework import tensor_shape as tensor_shape
from tensorflow.python.keras import activations as activations, backend as backend, constraints as constraints, initializers as initializers, regularizers as regularizers
from tensorflow.python.keras.engine.base_layer import Layer as Layer
from tensorflow.python.keras.engine.input_spec import InputSpec as InputSpec
from tensorflow.python.keras.layers.pooling import AveragePooling1D as AveragePooling1D, AveragePooling2D as AveragePooling2D, AveragePooling3D as AveragePooling3D, MaxPooling1D as MaxPooling1D, MaxPooling2D as MaxPooling2D, MaxPooling3D as MaxPooling3D
from tensorflow.python.keras.utils import conv_utils as conv_utils, tf_utils as tf_utils
from tensorflow.python.ops import array_ops as array_ops, nn as nn, nn_ops as nn_ops
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

class Conv(Layer):
    rank: Any
    filters: Any
    groups: Any
    kernel_size: Any
    strides: Any
    padding: Any
    data_format: Any
    dilation_rate: Any
    activation: Any
    use_bias: Any
    kernel_initializer: Any
    bias_initializer: Any
    kernel_regularizer: Any
    bias_regularizer: Any
    kernel_constraint: Any
    bias_constraint: Any
    input_spec: Any
    def __init__(self, rank, filters, kernel_size, strides: int = ..., padding: str = ..., data_format: Any | None = ..., dilation_rate: int = ..., groups: int = ..., activation: Any | None = ..., use_bias: bool = ..., kernel_initializer: str = ..., bias_initializer: str = ..., kernel_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., kernel_constraint: Any | None = ..., bias_constraint: Any | None = ..., trainable: bool = ..., name: Any | None = ..., conv_op: Any | None = ..., **kwargs) -> None: ...
    kernel: Any
    bias: Any
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class Conv1D(Conv):
    def __init__(self, filters, kernel_size, strides: int = ..., padding: str = ..., data_format: str = ..., dilation_rate: int = ..., groups: int = ..., activation: Any | None = ..., use_bias: bool = ..., kernel_initializer: str = ..., bias_initializer: str = ..., kernel_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., kernel_constraint: Any | None = ..., bias_constraint: Any | None = ..., **kwargs) -> None: ...

class Conv2D(Conv):
    def __init__(self, filters, kernel_size, strides=..., padding: str = ..., data_format: Any | None = ..., dilation_rate=..., groups: int = ..., activation: Any | None = ..., use_bias: bool = ..., kernel_initializer: str = ..., bias_initializer: str = ..., kernel_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., kernel_constraint: Any | None = ..., bias_constraint: Any | None = ..., **kwargs) -> None: ...

class Conv3D(Conv):
    def __init__(self, filters, kernel_size, strides=..., padding: str = ..., data_format: Any | None = ..., dilation_rate=..., groups: int = ..., activation: Any | None = ..., use_bias: bool = ..., kernel_initializer: str = ..., bias_initializer: str = ..., kernel_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., kernel_constraint: Any | None = ..., bias_constraint: Any | None = ..., **kwargs) -> None: ...

class Conv1DTranspose(Conv1D):
    output_padding: Any
    def __init__(self, filters, kernel_size, strides: int = ..., padding: str = ..., output_padding: Any | None = ..., data_format: Any | None = ..., dilation_rate: int = ..., activation: Any | None = ..., use_bias: bool = ..., kernel_initializer: str = ..., bias_initializer: str = ..., kernel_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., kernel_constraint: Any | None = ..., bias_constraint: Any | None = ..., **kwargs) -> None: ...
    input_spec: Any
    kernel: Any
    bias: Any
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class Conv2DTranspose(Conv2D):
    output_padding: Any
    def __init__(self, filters, kernel_size, strides=..., padding: str = ..., output_padding: Any | None = ..., data_format: Any | None = ..., dilation_rate=..., activation: Any | None = ..., use_bias: bool = ..., kernel_initializer: str = ..., bias_initializer: str = ..., kernel_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., kernel_constraint: Any | None = ..., bias_constraint: Any | None = ..., **kwargs) -> None: ...
    input_spec: Any
    kernel: Any
    bias: Any
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class Conv3DTranspose(Conv3D):
    output_padding: Any
    def __init__(self, filters, kernel_size, strides=..., padding: str = ..., output_padding: Any | None = ..., data_format: Any | None = ..., dilation_rate=..., activation: Any | None = ..., use_bias: bool = ..., kernel_initializer: str = ..., bias_initializer: str = ..., kernel_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., kernel_constraint: Any | None = ..., bias_constraint: Any | None = ..., **kwargs) -> None: ...
    input_spec: Any
    kernel: Any
    bias: Any
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class SeparableConv(Conv):
    depth_multiplier: Any
    depthwise_initializer: Any
    pointwise_initializer: Any
    depthwise_regularizer: Any
    pointwise_regularizer: Any
    depthwise_constraint: Any
    pointwise_constraint: Any
    def __init__(self, rank, filters, kernel_size, strides: int = ..., padding: str = ..., data_format: Any | None = ..., dilation_rate: int = ..., depth_multiplier: int = ..., activation: Any | None = ..., use_bias: bool = ..., depthwise_initializer: str = ..., pointwise_initializer: str = ..., bias_initializer: str = ..., depthwise_regularizer: Any | None = ..., pointwise_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., depthwise_constraint: Any | None = ..., pointwise_constraint: Any | None = ..., bias_constraint: Any | None = ..., trainable: bool = ..., name: Any | None = ..., **kwargs) -> None: ...
    input_spec: Any
    depthwise_kernel: Any
    pointwise_kernel: Any
    bias: Any
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs) -> None: ...
    def get_config(self): ...

class SeparableConv1D(SeparableConv):
    def __init__(self, filters, kernel_size, strides: int = ..., padding: str = ..., data_format: Any | None = ..., dilation_rate: int = ..., depth_multiplier: int = ..., activation: Any | None = ..., use_bias: bool = ..., depthwise_initializer: str = ..., pointwise_initializer: str = ..., bias_initializer: str = ..., depthwise_regularizer: Any | None = ..., pointwise_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., depthwise_constraint: Any | None = ..., pointwise_constraint: Any | None = ..., bias_constraint: Any | None = ..., **kwargs) -> None: ...
    def call(self, inputs): ...

class SeparableConv2D(SeparableConv):
    def __init__(self, filters, kernel_size, strides=..., padding: str = ..., data_format: Any | None = ..., dilation_rate=..., depth_multiplier: int = ..., activation: Any | None = ..., use_bias: bool = ..., depthwise_initializer: str = ..., pointwise_initializer: str = ..., bias_initializer: str = ..., depthwise_regularizer: Any | None = ..., pointwise_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., depthwise_constraint: Any | None = ..., pointwise_constraint: Any | None = ..., bias_constraint: Any | None = ..., **kwargs) -> None: ...
    def call(self, inputs): ...

class DepthwiseConv2D(Conv2D):
    depth_multiplier: Any
    depthwise_initializer: Any
    depthwise_regularizer: Any
    depthwise_constraint: Any
    bias_initializer: Any
    def __init__(self, kernel_size, strides=..., padding: str = ..., depth_multiplier: int = ..., data_format: Any | None = ..., dilation_rate=..., activation: Any | None = ..., use_bias: bool = ..., depthwise_initializer: str = ..., bias_initializer: str = ..., depthwise_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., depthwise_constraint: Any | None = ..., bias_constraint: Any | None = ..., **kwargs) -> None: ...
    depthwise_kernel: Any
    bias: Any
    input_spec: Any
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class UpSampling1D(Layer):
    size: Any
    input_spec: Any
    def __init__(self, size: int = ..., **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...

class UpSampling2D(Layer):
    data_format: Any
    size: Any
    interpolation: Any
    input_spec: Any
    def __init__(self, size=..., data_format: Any | None = ..., interpolation: str = ..., **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...

class UpSampling3D(Layer):
    data_format: Any
    size: Any
    input_spec: Any
    def __init__(self, size=..., data_format: Any | None = ..., **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...

class ZeroPadding1D(Layer):
    padding: Any
    input_spec: Any
    def __init__(self, padding: int = ..., **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...

class ZeroPadding2D(Layer):
    data_format: Any
    padding: Any
    input_spec: Any
    def __init__(self, padding=..., data_format: Any | None = ..., **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...

class ZeroPadding3D(Layer):
    data_format: Any
    padding: Any
    input_spec: Any
    def __init__(self, padding=..., data_format: Any | None = ..., **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...

class Cropping1D(Layer):
    cropping: Any
    input_spec: Any
    def __init__(self, cropping=..., **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...

class Cropping2D(Layer):
    data_format: Any
    cropping: Any
    input_spec: Any
    def __init__(self, cropping=..., data_format: Any | None = ..., **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...

class Cropping3D(Layer):
    data_format: Any
    cropping: Any
    input_spec: Any
    def __init__(self, cropping=..., data_format: Any | None = ..., **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...
Convolution1D = Conv1D
Convolution2D = Conv2D
Convolution3D = Conv3D
SeparableConvolution1D = SeparableConv1D
SeparableConvolution2D = SeparableConv2D
Convolution2DTranspose = Conv2DTranspose
Convolution3DTranspose = Conv3DTranspose
Deconvolution2D = Conv2DTranspose
Deconv2D = Conv2DTranspose
Deconvolution3D = Conv3DTranspose
Deconv3D = Conv3DTranspose
