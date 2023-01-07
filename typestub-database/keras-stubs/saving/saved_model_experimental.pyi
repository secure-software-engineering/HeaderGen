from keras import backend as backend, optimizer_v1 as optimizer_v1
from keras.optimizer_v2 import optimizer_v2 as optimizer_v2
from keras.saving import model_config as model_config, saving_utils as saving_utils
from keras.utils import mode_keys as mode_keys
from keras.utils.generic_utils import LazyLoader as LazyLoader
from typing import Any

metrics_lib: Any
models_lib: Any
sequential: Any
SAVED_MODEL_FILENAME_JSON: str

def export_saved_model(model, saved_model_path, custom_objects: Any | None = ..., as_text: bool = ..., input_signature: Any | None = ..., serving_only: bool = ...) -> None: ...
def create_placeholder(spec): ...
def load_from_saved_model(saved_model_path, custom_objects: Any | None = ...): ...
