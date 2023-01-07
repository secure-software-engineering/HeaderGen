from keras.engine import base_layer as base_layer, input_layer as input_layer, input_spec as input_spec
from keras.layers import advanced_activations as advanced_activations, convolutional as convolutional, convolutional_recurrent as convolutional_recurrent, core as core, cudnn_recurrent as cudnn_recurrent, dense_attention as dense_attention, einsum_dense as einsum_dense, embeddings as embeddings, local as local, merge as merge, multi_head_attention as multi_head_attention, noise as noise, pooling as pooling, recurrent as recurrent, recurrent_v2 as recurrent_v2, rnn_cell_wrapper_v2 as rnn_cell_wrapper_v2, wrappers as wrappers
from keras.layers.normalization import batch_normalization as batch_normalization, batch_normalization_v1 as batch_normalization_v1, layer_normalization as layer_normalization
from keras.layers.preprocessing import category_encoding as category_encoding, discretization as discretization, hashed_crossing as hashed_crossing, hashing as hashing, image_preprocessing as image_preprocessing, integer_lookup as integer_lookup, string_lookup as string_lookup, text_vectorization as text_vectorization
from keras.utils import generic_utils as generic_utils
from typing import Any

ALL_MODULES: Any
ALL_V2_MODULES: Any
LOCAL: Any

def populate_deserializable_objects(): ...
def serialize(layer): ...
def deserialize(config, custom_objects: Any | None = ...): ...
def get_builtin_layer(class_name): ...
