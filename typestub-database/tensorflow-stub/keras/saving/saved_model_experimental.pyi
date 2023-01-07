from tensorflow.python.client import session as session
from tensorflow.python.framework import ops as ops
from tensorflow.python.keras import backend as backend, optimizer_v1 as optimizer_v1
from tensorflow.python.keras.optimizer_v2 import optimizer_v2 as optimizer_v2
from tensorflow.python.keras.saving import model_config as model_config, saving_utils as saving_utils
from tensorflow.python.keras.utils import mode_keys as mode_keys
from tensorflow.python.keras.utils.generic_utils import LazyLoader as LazyLoader
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.ops import variables as variables
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.saved_model import constants as constants
from tensorflow.python.training.tracking import graph_view as graph_view
from tensorflow.python.util import compat as compat, nest as nest
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

metrics_lib: Any
models_lib: Any
sequential: Any
SAVED_MODEL_FILENAME_JSON: str

def export_saved_model(model, saved_model_path, custom_objects: Any | None = ..., as_text: bool = ..., input_signature: Any | None = ..., serving_only: bool = ...) -> None: ...
def create_placeholder(spec): ...
def load_from_saved_model(saved_model_path, custom_objects: Any | None = ...): ...
