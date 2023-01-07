from keras import backend as backend
from keras.engine import base_layer as base_layer, base_preprocessing_layer as base_preprocessing_layer
from keras.utils import layer_utils as layer_utils
from typing import Any

INT: Any
ONE_HOT: Any
MULTI_HOT: Any
COUNT: Any

class CategoryEncoding(base_layer.Layer):
    num_tokens: Any
    output_mode: Any
    sparse: Any
    def __init__(self, num_tokens: Any | None = ..., output_mode: str = ..., sparse: bool = ..., **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def compute_output_signature(self, input_spec): ...
    def get_config(self): ...
    def call(self, inputs, count_weights: Any | None = ...): ...
