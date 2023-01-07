from tensorflow.python.framework import tensor_shape as tensor_shape
from tensorflow.python.keras import activations as activations, initializers as initializers, regularizers as regularizers
from tensorflow.python.keras.engine import base_layer as base_layer, input_spec as input_spec, training as training
from tensorflow.python.keras.layers import core as core
from tensorflow.python.ops import nn as nn
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

class LinearModel(training.Model):
    units: Any
    activation: Any
    use_bias: Any
    kernel_initializer: Any
    bias_initializer: Any
    kernel_regularizer: Any
    bias_regularizer: Any
    def __init__(self, units: int = ..., activation: Any | None = ..., use_bias: bool = ..., kernel_initializer: str = ..., bias_initializer: str = ..., kernel_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., **kwargs) -> None: ...
    input_specs: Any
    dense_layers: Any
    bias: Any
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Any | None = ...): ...
