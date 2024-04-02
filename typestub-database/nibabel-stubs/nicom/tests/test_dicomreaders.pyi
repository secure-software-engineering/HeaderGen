from _typeshed import Incomplete
from nibabel.optpkg import optional_package as optional_package

from .test_dicomwrappers import DATA as DATA
from .test_dicomwrappers import EXPECTED_AFFINE as EXPECTED_AFFINE
from .test_dicomwrappers import EXPECTED_PARAMS as EXPECTED_PARAMS
from .test_dicomwrappers import IO_DATA_PATH as IO_DATA_PATH

pydicom: Incomplete
_: Incomplete
setup_module: Incomplete

def test_read_dwi() -> None: ...
def test_read_dwis() -> None: ...
def test_passing_kwds() -> None: ...
def test_slices_to_series() -> None: ...
