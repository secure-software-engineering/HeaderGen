from _typeshed import Incomplete

from .. import Nifti1Image as Nifti1Image
from ..optpkg import optional_package as optional_package
from .nibabel_data import get_nibabel_data as get_nibabel_data
from .nibabel_data import needs_nibabel_data as needs_nibabel_data

h5py: Incomplete
have_h5py: Incomplete
setup_module: Incomplete
MINC2_PATH: Incomplete

class TestEPIFrame:
    opener: Incomplete
    x_cos: Incomplete
    y_cos: Incomplete
    z_cos: Incomplete
    zooms: Incomplete
    starts: Incomplete
    example_params: Incomplete
    def test_load(self) -> None: ...

class TestB0(TestEPIFrame):
    x_cos: Incomplete
    y_cos: Incomplete
    z_cos: Incomplete
    zooms: Incomplete
    starts: Incomplete
    example_params: Incomplete

class TestFA(TestEPIFrame):
    example_params: Incomplete
    new_params: Incomplete

class TestGado(TestEPIFrame):
    x_cos: Incomplete
    y_cos: Incomplete
    z_cos: Incomplete
    zooms: Incomplete
    starts: Incomplete
    example_params: Incomplete

class TestT1(TestEPIFrame):
    x_cos: Incomplete
    y_cos: Incomplete
    z_cos: Incomplete
    zooms: Incomplete
    starts: Incomplete
    example_params: Incomplete

class TestPD(TestEPIFrame):
    example_params: Incomplete
    new_params: Incomplete

class TestMask(TestEPIFrame):
    example_params: Incomplete
    new_params: Incomplete
