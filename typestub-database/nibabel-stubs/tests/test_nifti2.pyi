from _typeshed import Incomplete

from .. import nifti2 as nifti2
from ..nifti1 import Nifti1Extension as Nifti1Extension
from ..nifti1 import Nifti1Extensions as Nifti1Extensions
from ..nifti1 import Nifti1Header as Nifti1Header
from ..nifti1 import Nifti1PairHeader as Nifti1PairHeader
from ..nifti2 import Nifti2Header as Nifti2Header
from ..nifti2 import Nifti2Image as Nifti2Image
from ..nifti2 import Nifti2Pair as Nifti2Pair
from ..nifti2 import Nifti2PairHeader as Nifti2PairHeader
from ..testing import data_path as data_path
from . import test_nifti1 as tn1

header_file: Incomplete
image_file: Incomplete

class _Nifti2Mixin:
    example_file = header_file
    sizeof_hdr: Incomplete
    quat_dtype: Incomplete
    def test_freesurfer_large_vector_hack(self) -> None: ...
    def test_freesurfer_ico7_hack(self) -> None: ...
    def test_eol_check(self) -> None: ...

class TestNifti2PairHeader(_Nifti2Mixin, tn1.TestNifti1PairHeader):
    header_class = Nifti2PairHeader
    example_file = header_file

class TestNifti2SingleHeader(_Nifti2Mixin, tn1.TestNifti1SingleHeader):
    header_class = Nifti2Header
    example_file = header_file

class TestNifti2Image(tn1.TestNifti1Image):
    image_class = Nifti2Image

class TestNifti2Pair(tn1.TestNifti1Pair):
    image_class = Nifti2Pair

class TestNifti2General(tn1.TestNifti1General):
    single_class = Nifti2Image
    pair_class = Nifti2Pair
    module = nifti2
    example_file = image_file

def test_nifti12_conversion() -> None: ...
