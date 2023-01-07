from tensorflow.python.framework import ops as ops
from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.feature_column import base_feature_layer as kfc
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

class SequenceFeatures(kfc._BaseFeaturesLayer):
    def __init__(self, feature_columns, trainable: bool = ..., name: Any | None = ..., **kwargs) -> None: ...
    def call(self, features, training: Any | None = ...): ...
