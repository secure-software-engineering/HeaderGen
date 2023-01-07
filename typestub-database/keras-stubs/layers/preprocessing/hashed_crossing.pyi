from keras import backend as backend
from keras.engine import base_layer as base_layer, base_preprocessing_layer as base_preprocessing_layer
from keras.utils import layer_utils as layer_utils
from typing import Any

INT: Any
ONE_HOT: Any

class HashedCrossing(base_layer.Layer):
    num_bins: Any
    output_mode: Any
    sparse: Any
    def __init__(self, num_bins, output_mode: str = ..., sparse: bool = ..., **kwargs) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shapes): ...
    def compute_output_signature(self, input_specs): ...
    def get_config(self): ...
