from tensorflow.python import tf2 as tf2
from tensorflow.python.keras.saving import hdf5_format as hdf5_format, saving_utils as saving_utils
from tensorflow.python.keras.saving.saved_model import load_context as load_context
from tensorflow.python.keras.utils import generic_utils as generic_utils
from tensorflow.python.keras.utils.io_utils import path_to_string as path_to_string
from tensorflow.python.util import keras_deps as keras_deps
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

def save_model(model, filepath, overwrite: bool = ..., include_optimizer: bool = ..., save_format: Any | None = ..., signatures: Any | None = ..., options: Any | None = ..., save_traces: bool = ...) -> None: ...
def load_model(filepath, custom_objects: Any | None = ..., compile: bool = ..., options: Any | None = ...): ...
