from tensorflow.python import tf2 as tf2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import ops as ops, test_combinations as test_combinations
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class EagerGraphCombination(test_combinations.TestCombination):
    def context_managers(self, kwargs): ...
    def parameter_modifiers(self): ...

class TFVersionCombination(test_combinations.TestCombination):
    def should_execute_combination(self, kwargs): ...
    def parameter_modifiers(self): ...

generate: Any
combine: Any
times: Any
NamedObject: Any
