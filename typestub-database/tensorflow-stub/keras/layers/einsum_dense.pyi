from tensorflow.python.framework import tensor_shape as tensor_shape
from tensorflow.python.keras import activations as activations, constraints as constraints, initializers as initializers, regularizers as regularizers
from tensorflow.python.keras.engine.base_layer import Layer as Layer
from tensorflow.python.ops import special_math_ops as special_math_ops
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

class EinsumDense(Layer):
    equation: Any
    partial_output_shape: Any
    bias_axes: Any
    activation: Any
    kernel_initializer: Any
    bias_initializer: Any
    kernel_regularizer: Any
    bias_regularizer: Any
    kernel_constraint: Any
    bias_constraint: Any
    def __init__(self, equation, output_shape, activation: Any | None = ..., bias_axes: Any | None = ..., kernel_initializer: str = ..., bias_initializer: str = ..., kernel_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., kernel_constraint: Any | None = ..., bias_constraint: Any | None = ..., **kwargs) -> None: ...
    kernel: Any
    bias: Any
    def build(self, input_shape) -> None: ...
    def compute_output_shape(self, _): ...
    def get_config(self): ...
    def call(self, inputs): ...
