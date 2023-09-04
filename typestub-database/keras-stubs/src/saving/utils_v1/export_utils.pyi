from typing import Any

from keras.src.saving.utils_v1 import mode_keys as mode_keys
from keras.src.saving.utils_v1 import unexported_constants as unexported_constants

EXPORT_TAG_MAP: Any
SIGNATURE_KEY_MAP: Any
SINGLE_FEATURE_DEFAULT_NAME: str
SINGLE_RECEIVER_DEFAULT_NAME: str
SINGLE_LABEL_DEFAULT_NAME: str

def build_all_signature_defs(
    receiver_tensors,
    export_outputs,
    receiver_tensors_alternatives: Any | None = ...,
    serving_only: bool = ...,
): ...

MAX_DIRECTORY_CREATION_ATTEMPTS: int

def get_timestamped_export_dir(export_dir_base): ...
def get_temp_export_dir(timestamped_export_dir): ...
def export_outputs_for_mode(
    mode,
    serving_export_outputs: Any | None = ...,
    predictions: Any | None = ...,
    loss: Any | None = ...,
    metrics: Any | None = ...,
): ...
def get_export_outputs(export_outputs, predictions): ...
