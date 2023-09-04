from typing import Any

import tensorflow.compat.v2 as tf
from keras import testing_utils as testing_utils

KERAS_MODEL_TYPES: Any

def keras_mode_combinations(mode: Any | None = ..., run_eagerly: Any | None = ...): ...
def keras_model_type_combinations(): ...

class KerasModeCombination(tf.__internal__.test.combinations.TestCombination):
    def context_managers(self, kwargs): ...
    def parameter_modifiers(self): ...

class KerasModelTypeCombination(tf.__internal__.test.combinations.TestCombination):
    def context_managers(self, kwargs): ...
    def parameter_modifiers(self): ...

generate: Any
combine: Any
times: Any
NamedObject: Any
