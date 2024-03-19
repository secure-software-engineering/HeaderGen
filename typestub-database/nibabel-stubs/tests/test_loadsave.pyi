from _typeshed import Incomplete

from .. import Nifti1Image as Nifti1Image
from .. import Nifti1Pair as Nifti1Pair
from .. import Nifti2Image as Nifti2Image
from .. import Nifti2Pair as Nifti2Pair
from .. import Spm2AnalyzeImage as Spm2AnalyzeImage
from .. import Spm99AnalyzeImage as Spm99AnalyzeImage
from ..filebasedimages import ImageFileError as ImageFileError
from ..loadsave import load as load
from ..loadsave import read_img_data as read_img_data
from ..openers import Opener as Opener
from ..optpkg import optional_package as optional_package
from ..testing import deprecated_to as deprecated_to
from ..testing import expires as expires
from ..tmpdirs import InTemporaryDirectory as InTemporaryDirectory

_: Incomplete
have_scipy: Incomplete
have_pyzstd: Incomplete
data_path: Incomplete

def test_read_img_data() -> None: ...
def test_file_not_found() -> None: ...
def test_load_empty_image() -> None: ...
def test_load_bad_compressed_extension(tmp_path, extension) -> None: ...
def test_load_good_extension_with_bad_data(tmp_path, extension) -> None: ...
def test_signature_matches_extension(tmp_path) -> None: ...
def test_read_img_data_nifti() -> None: ...
