from typing import Any

from keras.src.engine import base_layer as base_layer
from keras.src.engine import input_layer as input_layer
from keras.src.engine import input_spec as input_spec
from keras.src.layers import advanced_activations as advanced_activations
from keras.src.layers import convolutional as convolutional
from keras.src.layers import convolutional_recurrent as convolutional_recurrent
from keras.src.layers import core as core
from keras.src.layers import cudnn_recurrent as cudnn_recurrent
from keras.src.layers import dense_attention as dense_attention
from keras.src.layers import einsum_dense as einsum_dense
from keras.src.layers import embeddings as embeddings
from keras.src.layers import local as local
from keras.src.layers import merge as merge
from keras.src.layers import multi_head_attention as multi_head_attention
from keras.src.layers import noise as noise
from keras.src.layers import pooling as pooling
from keras.src.layers import recurrent as recurrent
from keras.src.layers import recurrent_v2 as recurrent_v2
from keras.src.layers import rnn_cell_wrapper_v2 as rnn_cell_wrapper_v2
from keras.src.layers import wrappers as wrappers
from keras.src.layers.normalization import batch_normalization as batch_normalization
from keras.src.layers.normalization import (
    batch_normalization_v1 as batch_normalization_v1,
)
from keras.src.layers.normalization import layer_normalization as layer_normalization
from keras.src.layers.preprocessing import category_encoding as category_encoding
from keras.src.layers.preprocessing import discretization as discretization
from keras.src.layers.preprocessing import hashed_crossing as hashed_crossing
from keras.src.layers.preprocessing import hashing as hashing
from keras.src.layers.preprocessing import image_preprocessing as image_preprocessing
from keras.src.layers.preprocessing import integer_lookup as integer_lookup
from keras.src.layers.preprocessing import string_lookup as string_lookup
from keras.src.layers.preprocessing import text_vectorization as text_vectorization
from keras.utils import generic_utils as generic_utils

ALL_MODULES: Any
ALL_V2_MODULES: Any
LOCAL: Any

def populate_deserializable_objects(): ...
def serialize(layer): ...
def deserialize(config, custom_objects: Any | None = ...): ...
def get_builtin_layer(class_name): ...
