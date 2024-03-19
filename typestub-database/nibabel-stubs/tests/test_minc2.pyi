from _typeshed import Incomplete

from .. import minc2 as minc2
from ..minc2 import Minc2File as Minc2File
from ..minc2 import Minc2Image as Minc2Image
from ..optpkg import optional_package as optional_package
from ..testing import data_path as data_path
from . import test_minc1 as tm2

h5py: Incomplete
have_h5py: Incomplete
setup_module: Incomplete
EXAMPLE_IMAGES: Incomplete

class TestMinc2File(tm2._TestMincFile):
    module = minc2
    file_class = Minc2File
    opener: Incomplete
    test_files = EXAMPLE_IMAGES

class TestMinc2Image(tm2.TestMinc1Image):
    image_class = Minc2Image
    eg_images: Incomplete
    module = minc2

def test_bad_diminfo() -> None: ...
