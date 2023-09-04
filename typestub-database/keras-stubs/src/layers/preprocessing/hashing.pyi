from typing import Any

from keras import backend as backend
from keras.src.engine import base_layer as base_layer
from keras.src.engine import base_preprocessing_layer as base_preprocessing_layer
from keras.utils import layer_utils as layer_utils

INT: Any
MULTI_HOT: Any
ONE_HOT: Any
COUNT: Any

class Hashing(base_layer.Layer):
    num_bins: Any
    mask_value: Any
    strong_hash: Any
    output_mode: Any
    sparse: Any
    salt: Any
    def __init__(
        self,
        num_bins,
        mask_value: Any | None = ...,
        salt: Any | None = ...,
        output_mode: str = ...,
        sparse: bool = ...,
        **kwargs
    ) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def compute_output_signature(self, input_spec): ...
    def get_config(self): ...
