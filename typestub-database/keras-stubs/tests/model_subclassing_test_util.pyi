import keras
from keras import testing_utils as testing_utils
from typing import Any

class SimpleConvTestModel(keras.Model):
    num_classes: Any
    conv1: Any
    flatten: Any
    dense1: Any
    def __init__(self, num_classes: int = ...) -> None: ...
    def call(self, x): ...

def get_multi_io_subclass_model(use_bn: bool = ..., use_dp: bool = ..., num_classes=...): ...

class NestedTestModel1(keras.Model):
    num_classes: Any
    dense1: Any
    dense2: Any
    bn: Any
    test_net: Any
    def __init__(self, num_classes: int = ...) -> None: ...
    def call(self, inputs): ...

class NestedTestModel2(keras.Model):
    num_classes: Any
    dense1: Any
    dense2: Any
    bn: Any
    test_net: Any
    def __init__(self, num_classes: int = ...) -> None: ...
    @staticmethod
    def get_functional_graph_model(input_dim, num_classes): ...
    def call(self, inputs): ...

def get_nested_model_3(input_dim, num_classes): ...

class CustomCallModel(keras.Model):
    dense1: Any
    dense2: Any
    def __init__(self) -> None: ...
    def call(self, first, second, fiddle_with_output: str = ..., training: bool = ...): ...

class TrainingNoDefaultModel(keras.Model):
    dense1: Any
    def __init__(self) -> None: ...
    def call(self, x, training): ...

class TrainingMaskingModel(keras.Model):
    dense1: Any
    def __init__(self) -> None: ...
    def call(self, x, training: bool = ..., mask: Any | None = ...): ...
