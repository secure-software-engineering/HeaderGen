from _typeshed import Incomplete

from .. import AnalyzeImage as AnalyzeImage
from .. import MGHImage as MGHImage
from .. import Minc1Image as Minc1Image
from .. import Minc2Image as Minc2Image
from .. import Nifti1Header as Nifti1Header
from .. import Nifti1Image as Nifti1Image
from .. import Nifti1Pair as Nifti1Pair
from .. import Nifti2Image as Nifti2Image
from .. import Nifti2Pair as Nifti2Pair
from .. import Spm2AnalyzeImage as Spm2AnalyzeImage
from .. import Spm99AnalyzeImage as Spm99AnalyzeImage
from .. import all_image_classes as all_image_classes
from ..optpkg import optional_package as optional_package
from ..spatialimages import SpatialImage as SpatialImage
from ..testing import deprecated_to as deprecated_to
from ..testing import expires as expires
from ..tmpdirs import InTemporaryDirectory as InTemporaryDirectory
from ..volumeutils import native_code as native_code
from ..volumeutils import swapped_code as swapped_code

_: Incomplete
have_scipy: Incomplete
DATA_PATH: Incomplete
MGH_DATA_PATH: Incomplete

def round_trip(img): ...
def test_conversion_spatialimages(caplog) -> None: ...
def test_save_load_endian() -> None: ...
def test_save_load() -> None: ...
def test_two_to_one() -> None: ...
def test_negative_load_save() -> None: ...
def test_filename_save() -> None: ...
def test_guessed_image_type() -> None: ...
def test_fail_save() -> None: ...
