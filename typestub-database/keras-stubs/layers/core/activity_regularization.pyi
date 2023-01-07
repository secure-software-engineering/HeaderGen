from keras import regularizers as regularizers
from keras.engine.base_layer import Layer as Layer
from typing import Any

class ActivityRegularization(Layer):
    supports_masking: bool
    l1: Any
    l2: Any
    def __init__(self, l1: float = ..., l2: float = ..., **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...
