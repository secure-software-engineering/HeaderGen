from typing import Any

from keras.src.engine.base_layer import Layer as Layer
from keras.src.engine.input_spec import InputSpec as InputSpec
from keras.utils import conv_utils as conv_utils

class Flatten(Layer):
    data_format: Any
    input_spec: Any
    def __init__(self, data_format: Any | None = ..., **kwargs) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...
