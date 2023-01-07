from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.saved_model import signature_constants as signature_constants, signature_def_utils as signature_def_utils, tag_constants as tag_constants
from tensorflow.python.saved_model.model_utils import mode_keys as mode_keys
from tensorflow.python.util import compat as compat
from typing import Any

EXPORT_TAG_MAP: Any
SIGNATURE_KEY_MAP: Any
SINGLE_FEATURE_DEFAULT_NAME: str
SINGLE_RECEIVER_DEFAULT_NAME: str
SINGLE_LABEL_DEFAULT_NAME: str

def build_all_signature_defs(receiver_tensors, export_outputs, receiver_tensors_alternatives: Any | None = ..., serving_only: bool = ...): ...

MAX_DIRECTORY_CREATION_ATTEMPTS: int

def get_timestamped_export_dir(export_dir_base): ...
def get_temp_export_dir(timestamped_export_dir): ...
def export_outputs_for_mode(mode, serving_export_outputs: Any | None = ..., predictions: Any | None = ..., loss: Any | None = ..., metrics: Any | None = ...): ...
def get_export_outputs(export_outputs, predictions): ...
