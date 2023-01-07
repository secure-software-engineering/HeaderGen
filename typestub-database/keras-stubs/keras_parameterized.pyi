import tensorflow.compat.v2 as tf
from absl.testing import parameterized
from keras import testing_utils as testing_utils
from typing import Any

class TestCase(tf.test.TestCase, parameterized.TestCase):
    def tearDown(self) -> None: ...

def run_with_all_saved_model_formats(test_or_class: Any | None = ..., exclude_formats: Any | None = ...): ...
def run_with_all_weight_formats(test_or_class: Any | None = ..., exclude_formats: Any | None = ...): ...
def run_with_all_model_types(test_or_class: Any | None = ..., exclude_models: Any | None = ...): ...
def run_all_keras_modes(test_or_class: Any | None = ..., config: Any | None = ..., always_skip_v1: bool = ..., always_skip_eager: bool = ..., **kwargs): ...
