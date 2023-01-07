from keras import activations as activations, backend as backend, constraints as constraints, initializers as initializers, regularizers as regularizers
from keras.engine.base_layer import Layer as Layer
from keras.engine.input_spec import InputSpec as InputSpec
from typing import Any

class Dense(Layer):
    units: Any
    activation: Any
    use_bias: Any
    kernel_initializer: Any
    bias_initializer: Any
    kernel_regularizer: Any
    bias_regularizer: Any
    kernel_constraint: Any
    bias_constraint: Any
    input_spec: Any
    supports_masking: bool
    def __init__(self, units, activation: Any | None = ..., use_bias: bool = ..., kernel_initializer: str = ..., bias_initializer: str = ..., kernel_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., kernel_constraint: Any | None = ..., bias_constraint: Any | None = ..., **kwargs) -> None: ...
    kernel: Any
    bias: Any
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...
