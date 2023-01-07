from tensorflow.python import tf2 as tf2
from tensorflow.python.framework import ops as ops, tensor_util as tensor_util
from tensorflow.python.keras.engine import base_layer as base_layer, functional as functional, input_layer as input_layer, training_utils as training_utils
from tensorflow.python.keras.saving.saved_model import model_serialization as model_serialization
from tensorflow.python.keras.utils import generic_utils as generic_utils, layer_utils as layer_utils, tf_inspect as tf_inspect, tf_utils as tf_utils
from tensorflow.python.module import module as module
from tensorflow.python.ops.numpy_ops import np_arrays as np_arrays
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

SINGLE_LAYER_OUTPUT_ERROR_MSG: str

class Sequential(functional.Functional):
    supports_masking: bool
    def __init__(self, layers: Any | None = ..., name: Any | None = ...) -> None: ...
    @property
    def layers(self): ...
    built: bool
    outputs: Any
    inputs: Any
    def add(self, layer) -> None: ...
    def pop(self) -> None: ...
    def build(self, input_shape: Any | None = ...) -> None: ...
    def call(self, inputs, training: Any | None = ..., mask: Any | None = ...): ...
    def compute_output_shape(self, input_shape): ...
    def compute_mask(self, inputs, mask): ...
    def predict_proba(self, x, batch_size: int = ..., verbose: int = ...): ...
    def predict_classes(self, x, batch_size: int = ..., verbose: int = ...): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Any | None = ...): ...
    @property
    def input_spec(self): ...
    @input_spec.setter
    def input_spec(self, value) -> None: ...

def relax_input_shape(shape_1, shape_2): ...
def clear_previously_created_nodes(layer, created_nodes) -> None: ...
def track_nodes_created_by_last_call(layer, created_nodes) -> None: ...
