from tensorflow.python.distribute import distribution_strategy_context as distribution_strategy_context
from tensorflow.python.framework import ops as ops, tensor_shape as tensor_shape, tensor_spec as tensor_spec
from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.distribute import distributed_training_utils as distributed_training_utils
from tensorflow.python.keras.engine import base_layer as base_layer, keras_tensor as keras_tensor
from tensorflow.python.keras.saving.saved_model import layer_serialization as layer_serialization
from tensorflow.python.keras.utils import tf_utils as tf_utils
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

class InputLayer(base_layer.Layer):
    built: bool
    sparse: Any
    ragged: Any
    batch_size: Any
    supports_masking: bool
    is_placeholder: bool
    def __init__(self, input_shape: Any | None = ..., batch_size: Any | None = ..., dtype: Any | None = ..., input_tensor: Any | None = ..., sparse: Any | None = ..., name: Any | None = ..., ragged: Any | None = ..., type_spec: Any | None = ..., **kwargs) -> None: ...
    def get_config(self): ...

def Input(shape: Any | None = ..., batch_size: Any | None = ..., name: Any | None = ..., dtype: Any | None = ..., sparse: Any | None = ..., tensor: Any | None = ..., ragged: Any | None = ..., type_spec: Any | None = ..., **kwargs): ...
