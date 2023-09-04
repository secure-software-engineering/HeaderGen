from keras.src.engine import base_preprocessing_layer as base_preprocessing_layer
from keras.src.engine import functional as functional
from keras.src.engine import sequential as sequential
from keras.utils import tf_utils as tf_utils

class PreprocessingStage(
    sequential.Sequential, base_preprocessing_layer.PreprocessingLayer
):
    def adapt(self, data, reset_state: bool = ...): ...

class FunctionalPreprocessingStage(
    functional.Functional, base_preprocessing_layer.PreprocessingLayer
):
    def fit(self, *args, **kwargs) -> None: ...
    def adapt(self, data, reset_state: bool = ...): ...
