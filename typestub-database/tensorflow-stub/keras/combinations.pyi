from tensorflow.python import tf2 as tf2
from tensorflow.python.framework import combinations as combinations, test_combinations as test_combinations
from tensorflow.python.keras import testing_utils as testing_utils
from typing import Any

KERAS_MODEL_TYPES: Any

def keras_mode_combinations(mode: Any | None = ..., run_eagerly: Any | None = ...): ...
def keras_model_type_combinations(): ...

class KerasModeCombination(test_combinations.TestCombination):
    def context_managers(self, kwargs): ...
    def parameter_modifiers(self): ...

class KerasModelTypeCombination(test_combinations.TestCombination):
    def context_managers(self, kwargs): ...
    def parameter_modifiers(self): ...

generate: Any
combine: Any
times: Any
NamedObject: Any
