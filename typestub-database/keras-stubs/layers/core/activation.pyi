from keras import activations as activations
from keras.engine.base_layer import Layer as Layer
from typing import Any

class Activation(Layer):
    supports_masking: bool
    activation: Any
    def __init__(self, activation, **kwargs) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...
