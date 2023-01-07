from keras import activations as activations, backend as backend
from keras.utils import data_utils as data_utils
from typing import Any

CLASS_INDEX: Any
CLASS_INDEX_PATH: str
PREPROCESS_INPUT_DOC: str
PREPROCESS_INPUT_MODE_DOC: str
PREPROCESS_INPUT_DEFAULT_ERROR_DOC: str
PREPROCESS_INPUT_ERROR_DOC: str
PREPROCESS_INPUT_RET_DOC_TF: str
PREPROCESS_INPUT_RET_DOC_TORCH: str
PREPROCESS_INPUT_RET_DOC_CAFFE: str

def preprocess_input(x, data_format: Any | None = ..., mode: str = ...): ...
def decode_predictions(preds, top: int = ...): ...
def obtain_input_shape(input_shape, default_size, min_size, data_format, require_flatten, weights: Any | None = ...): ...
def correct_pad(inputs, kernel_size): ...
def validate_activation(classifier_activation, weights) -> None: ...
