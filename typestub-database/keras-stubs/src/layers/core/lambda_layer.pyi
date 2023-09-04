from typing import Any

from keras.src.engine.base_layer import Layer as Layer
from keras.utils import generic_utils as generic_utils
from keras.utils import tf_inspect as tf_inspect
from keras.utils import tf_utils as tf_utils

class Lambda(Layer):
    arguments: Any
    function: Any
    supports_masking: bool
    mask: Any
    def __init__(
        self,
        function,
        output_shape: Any | None = ...,
        mask: Any | None = ...,
        arguments: Any | None = ...,
        **kwargs
    ) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs, mask: Any | None = ..., training: Any | None = ...): ...
    def compute_mask(self, inputs, mask: Any | None = ...): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Any | None = ...): ...
