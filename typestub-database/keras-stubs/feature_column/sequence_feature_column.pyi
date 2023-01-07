from keras import backend as backend
from keras.feature_column import base_feature_layer as kfc
from typing import Any

class SequenceFeatures(kfc._BaseFeaturesLayer):
    def __init__(self, feature_columns, trainable: bool = ..., name: Any | None = ..., **kwargs) -> None: ...
    def call(self, features, training: Any | None = ...): ...
