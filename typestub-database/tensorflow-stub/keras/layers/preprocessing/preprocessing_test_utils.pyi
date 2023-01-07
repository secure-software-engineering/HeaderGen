from tensorflow.python.platform import test as test
from typing import Any

class PreprocessingLayerTest(test.TestCase):
    def assertAllCloseOrEqual(self, a, b, msg: Any | None = ...) -> None: ...
    def assert_extracted_output_equal(self, combiner, acc1, acc2, msg: Any | None = ...) -> None: ...
    compare_accumulators: Any
    def validate_accumulator_computation(self, combiner, data, expected) -> None: ...
    def validate_accumulator_extract(self, combiner, data, expected) -> None: ...
    def validate_accumulator_extract_and_restore(self, combiner, data, expected) -> None: ...
    def validate_accumulator_serialize_and_deserialize(self, combiner, data, expected) -> None: ...
    def validate_accumulator_uniqueness(self, combiner, data) -> None: ...
