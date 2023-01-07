from tensorflow.python.feature_column import feature_column_v2 as fc
from tensorflow.python.framework import ops as ops
from tensorflow.python.keras.feature_column import dense_features as dense_features
from tensorflow.python.keras.utils import tf_contextlib as tf_contextlib
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

class DenseFeatures(dense_features.DenseFeatures):
    def __init__(self, feature_columns, trainable: bool = ..., name: Any | None = ..., **kwargs) -> None: ...
    def build(self, _) -> None: ...

class _StateManagerImplV2(fc._StateManagerImpl):
    def create_variable(self, feature_column, name, shape, dtype: Any | None = ..., trainable: bool = ..., use_resource: bool = ..., initializer: Any | None = ...): ...

def no_manual_dependency_tracking_scope(obj) -> None: ...
