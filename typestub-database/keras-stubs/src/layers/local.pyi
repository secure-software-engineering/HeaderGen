from typing import Any

from keras import activations as activations
from keras import backend as backend
from keras import constraints as constraints
from keras import initializers as initializers
from keras import regularizers as regularizers
from keras.src.engine.base_layer import Layer as Layer
from keras.src.engine.input_spec import InputSpec as InputSpec
from keras.utils import conv_utils as conv_utils
from keras.utils import tf_utils as tf_utils

class LocallyConnected1D(Layer):
    filters: Any
    kernel_size: Any
    strides: Any
    padding: Any
    data_format: Any
    activation: Any
    use_bias: Any
    kernel_initializer: Any
    bias_initializer: Any
    kernel_regularizer: Any
    bias_regularizer: Any
    activity_regularizer: Any
    kernel_constraint: Any
    bias_constraint: Any
    implementation: Any
    input_spec: Any
    def __init__(
        self,
        filters,
        kernel_size,
        strides: int = ...,
        padding: str = ...,
        data_format: Any | None = ...,
        activation: Any | None = ...,
        use_bias: bool = ...,
        kernel_initializer: str = ...,
        bias_initializer: str = ...,
        kernel_regularizer: Any | None = ...,
        bias_regularizer: Any | None = ...,
        activity_regularizer: Any | None = ...,
        kernel_constraint: Any | None = ...,
        bias_constraint: Any | None = ...,
        implementation: int = ...,
        **kwargs
    ) -> None: ...
    output_length: Any
    kernel_shape: Any
    kernel: Any
    kernel_mask: Any
    kernel_idxs: Any
    bias: Any
    built: bool
    def build(self, input_shape) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...

class LocallyConnected2D(Layer):
    filters: Any
    kernel_size: Any
    strides: Any
    padding: Any
    data_format: Any
    activation: Any
    use_bias: Any
    kernel_initializer: Any
    bias_initializer: Any
    kernel_regularizer: Any
    bias_regularizer: Any
    activity_regularizer: Any
    kernel_constraint: Any
    bias_constraint: Any
    implementation: Any
    input_spec: Any
    def __init__(
        self,
        filters,
        kernel_size,
        strides=...,
        padding: str = ...,
        data_format: Any | None = ...,
        activation: Any | None = ...,
        use_bias: bool = ...,
        kernel_initializer: str = ...,
        bias_initializer: str = ...,
        kernel_regularizer: Any | None = ...,
        bias_regularizer: Any | None = ...,
        activity_regularizer: Any | None = ...,
        kernel_constraint: Any | None = ...,
        bias_constraint: Any | None = ...,
        implementation: int = ...,
        **kwargs
    ) -> None: ...
    output_row: Any
    output_col: Any
    kernel_shape: Any
    kernel: Any
    kernel_mask: Any
    kernel_idxs: Any
    bias: Any
    built: bool
    def build(self, input_shape) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...

def get_locallyconnected_mask(
    input_shape, kernel_shape, strides, padding, data_format
): ...
def local_conv_matmul(inputs, kernel, kernel_mask, output_shape): ...
def local_conv_sparse_matmul(
    inputs, kernel, kernel_idxs, kernel_shape, output_shape
): ...
def make_2d(tensor, split_dim): ...
