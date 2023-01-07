from tensorflow.python.keras import constraints as constraints, initializers as initializers, regularizers as regularizers
from tensorflow.python.keras.engine.base_layer import Layer as Layer
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops, nn as nn
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

class LayerNormalization(Layer):
    axis: Any
    epsilon: Any
    center: Any
    scale: Any
    beta_initializer: Any
    gamma_initializer: Any
    beta_regularizer: Any
    gamma_regularizer: Any
    beta_constraint: Any
    gamma_constraint: Any
    supports_masking: bool
    def __init__(self, axis: int = ..., epsilon: float = ..., center: bool = ..., scale: bool = ..., beta_initializer: str = ..., gamma_initializer: str = ..., beta_regularizer: Any | None = ..., gamma_regularizer: Any | None = ..., beta_constraint: Any | None = ..., gamma_constraint: Any | None = ..., **kwargs) -> None: ...
    gamma: Any
    beta: Any
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...
