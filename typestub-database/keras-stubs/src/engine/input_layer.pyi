from typing import Any

from keras import backend as backend
from keras.distribute import distributed_training_utils as distributed_training_utils
from keras.src.engine import base_layer as base_layer
from keras.src.engine import keras_tensor as keras_tensor
from keras.src.saving.saved_model import layer_serialization as layer_serialization
from keras.utils import tf_utils as tf_utils
from keras.utils import traceback_utils as traceback_utils

class InputLayer(base_layer.Layer):
    built: bool
    sparse: Any
    ragged: Any
    batch_size: Any
    supports_masking: bool
    is_placeholder: bool
    def __init__(
        self,
        input_shape: Any | None = ...,
        batch_size: Any | None = ...,
        dtype: Any | None = ...,
        input_tensor: Any | None = ...,
        sparse: Any | None = ...,
        name: Any | None = ...,
        ragged: Any | None = ...,
        type_spec: Any | None = ...,
        **kwargs
    ) -> None: ...
    def get_config(self): ...

def Input(
    shape: Any | None = ...,
    batch_size: Any | None = ...,
    name: Any | None = ...,
    dtype: Any | None = ...,
    sparse: Any | None = ...,
    tensor: Any | None = ...,
    ragged: Any | None = ...,
    type_spec: Any | None = ...,
    **kwargs
): ...
