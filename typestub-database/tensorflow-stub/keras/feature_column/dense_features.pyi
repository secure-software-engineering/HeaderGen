from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.feature_column import base_feature_layer as kfc
from tensorflow.python.keras.saving.saved_model import json_utils as json_utils
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

class DenseFeatures(kfc._BaseFeaturesLayer):
    def __init__(self, feature_columns, trainable: bool = ..., name: Any | None = ..., partitioner: Any | None = ..., **kwargs) -> None: ...
    def call(self, features, cols_to_output_tensors: Any | None = ..., training: Any | None = ...): ...
