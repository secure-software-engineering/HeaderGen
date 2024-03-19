from _typeshed import Incomplete
from numpy.testing import assert_array_equal as assert_array_equal

from ..ecat import load as load
from .nibabel_data import get_nibabel_data as get_nibabel_data
from .nibabel_data import needs_nibabel_data as needs_nibabel_data

ECAT_TEST_PATH: Incomplete

class TestNegatives:
    opener: Incomplete
    example_params: Incomplete
    def test_load(self) -> None: ...

class TestMultiframe(TestNegatives):
    example_params: Incomplete
