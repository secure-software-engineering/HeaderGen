from keras import initializers as initializers
from keras.engine import base_layer as base_layer, input_spec as input_spec
from typing import Any

class RandomFourierFeatures(base_layer.Layer):
    output_dim: Any
    kernel_initializer: Any
    scale: Any
    def __init__(self, output_dim, kernel_initializer: str = ..., scale: Any | None = ..., trainable: bool = ..., name: Any | None = ..., **kwargs) -> None: ...
    input_spec: Any
    unscaled_kernel: Any
    bias: Any
    kernel_scale: Any
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...
