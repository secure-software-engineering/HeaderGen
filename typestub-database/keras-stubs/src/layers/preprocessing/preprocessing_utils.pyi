from typing import Any

from keras.utils import tf_utils as tf_utils

INT: str
ONE_HOT: str
MULTI_HOT: str
COUNT: str
TF_IDF: str

def ensure_tensor(inputs, dtype: Any | None = ...): ...
def listify_tensors(x): ...
def sparse_bincount(
    inputs, depth, binary_output, dtype, count_weights: Any | None = ...
): ...
def dense_bincount(
    inputs, depth, binary_output, dtype, count_weights: Any | None = ...
): ...
def expand_dims(inputs, axis): ...
def encode_categorical_inputs(
    inputs,
    output_mode,
    depth,
    dtype: str = ...,
    sparse: bool = ...,
    count_weights: Any | None = ...,
    idf_weights: Any | None = ...,
): ...
def compute_shape_for_encode_categorical(shape, output_mode, depth): ...
