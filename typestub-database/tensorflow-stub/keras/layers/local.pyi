from tensorflow.python.keras import activations as activations, backend as backend, constraints as constraints, initializers as initializers, regularizers as regularizers
from tensorflow.python.keras.engine.base_layer import Layer as Layer
from tensorflow.python.keras.engine.input_spec import InputSpec as InputSpec
from tensorflow.python.keras.utils import conv_utils as conv_utils, tf_utils as tf_utils
from tensorflow.python.ops import array_ops as array_ops, gen_sparse_ops as gen_sparse_ops, math_ops as math_ops
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

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
    def __init__(self, filters, kernel_size, strides: int = ..., padding: str = ..., data_format: Any | None = ..., activation: Any | None = ..., use_bias: bool = ..., kernel_initializer: str = ..., bias_initializer: str = ..., kernel_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., kernel_constraint: Any | None = ..., bias_constraint: Any | None = ..., implementation: int = ..., **kwargs) -> None: ...
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
    def __init__(self, filters, kernel_size, strides=..., padding: str = ..., data_format: Any | None = ..., activation: Any | None = ..., use_bias: bool = ..., kernel_initializer: str = ..., bias_initializer: str = ..., kernel_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., kernel_constraint: Any | None = ..., bias_constraint: Any | None = ..., implementation: int = ..., **kwargs) -> None: ...
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

def get_locallyconnected_mask(input_shape, kernel_shape, strides, padding, data_format): ...
def local_conv_matmul(inputs, kernel, kernel_mask, output_shape): ...
def local_conv_sparse_matmul(inputs, kernel, kernel_idxs, kernel_shape, output_shape): ...
def make_2d(tensor, split_dim): ...
