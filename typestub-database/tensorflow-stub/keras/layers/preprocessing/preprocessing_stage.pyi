from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import ops as ops
from tensorflow.python.keras.engine import base_preprocessing_layer as base_preprocessing_layer, functional as functional, sequential as sequential
from tensorflow.python.keras.utils import tf_utils as tf_utils
from tensorflow.python.util import nest as nest

class PreprocessingStage(sequential.Sequential, base_preprocessing_layer.PreprocessingLayer):
    def adapt(self, data, reset_state: bool = ...): ...

class FunctionalPreprocessingStage(functional.Functional, base_preprocessing_layer.PreprocessingLayer):
    def fit(self, *args, **kwargs) -> None: ...
    def adapt(self, data, reset_state: bool = ...): ...
