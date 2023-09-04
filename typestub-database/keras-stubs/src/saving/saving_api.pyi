from typing import Any

from keras.src.engine.training import Model as Model
from keras.src.saving import hdf5_format as hdf5_format
from keras.src.saving import saving_utils as saving_utils
from keras.src.saving.saved_model import load_context as load_context
from keras.utils import generic_utils as generic_utils
from keras.utils import traceback_utils as traceback_utils
from keras.utils.io_utils import path_to_string as path_to_string

def save_model(
    model,
    filepath,
    overwrite: bool = ...,
    include_optimizer: bool = ...,
    save_format: Any | None = ...,
    signatures: Any | None = ...,
    options: Any | None = ...,
    save_traces: bool = ...,
) -> None: ...
def load_model(
    filepath,
    custom_objects: Any | None = ...,
    compile: bool = ...,
    options: Any | None = ...,
) -> Model: ...
