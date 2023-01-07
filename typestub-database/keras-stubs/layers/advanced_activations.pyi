from keras import backend as backend, constraints as constraints, initializers as initializers, regularizers as regularizers
from keras.engine.base_layer import Layer as Layer
from keras.engine.input_spec import InputSpec as InputSpec
from keras.utils import tf_utils as tf_utils
from typing import Any

def get_globals(): ...

class LeakyReLU(Layer):
    supports_masking: bool
    alpha: Any
    def __init__(self, alpha: float = ..., **kwargs) -> None: ...
    def call(self, inputs): ...
    def get_config(self): ...
    def compute_output_shape(self, input_shape): ...

class PReLU(Layer):
    supports_masking: bool
    alpha_initializer: Any
    alpha_regularizer: Any
    alpha_constraint: Any
    shared_axes: Any
    def __init__(self, alpha_initializer: str = ..., alpha_regularizer: Any | None = ..., alpha_constraint: Any | None = ..., shared_axes: Any | None = ..., **kwargs) -> None: ...
    alpha: Any
    input_spec: Any
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
    def get_config(self): ...
    def compute_output_shape(self, input_shape): ...

class ELU(Layer):
    supports_masking: bool
    alpha: Any
    def __init__(self, alpha: float = ..., **kwargs) -> None: ...
    def call(self, inputs): ...
    def get_config(self): ...
    def compute_output_shape(self, input_shape): ...

class ThresholdedReLU(Layer):
    supports_masking: bool
    theta: Any
    def __init__(self, theta: float = ..., **kwargs) -> None: ...
    def call(self, inputs): ...
    def get_config(self): ...
    def compute_output_shape(self, input_shape): ...

class Softmax(Layer):
    supports_masking: bool
    axis: Any
    def __init__(self, axis: int = ..., **kwargs) -> None: ...
    def call(self, inputs, mask: Any | None = ...): ...
    def get_config(self): ...
    def compute_output_shape(self, input_shape): ...

class ReLU(Layer):
    supports_masking: bool
    max_value: Any
    negative_slope: Any
    threshold: Any
    def __init__(self, max_value: Any | None = ..., negative_slope: float = ..., threshold: float = ..., **kwargs) -> None: ...
    def call(self, inputs): ...
    def get_config(self): ...
    def compute_output_shape(self, input_shape): ...
