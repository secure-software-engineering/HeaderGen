from _typeshed import Incomplete

from .analyze import AnalyzeHeader as AnalyzeHeader
from .batteryrunners import Report as Report
from .filebasedimages import ImageFileError as ImageFileError
from .nifti1 import Nifti1Header as Nifti1Header
from .nifti1 import Nifti1Image as Nifti1Image
from .nifti1 import Nifti1Pair as Nifti1Pair
from .spatialimages import HeaderDataError as HeaderDataError

header_dtd: Incomplete
header_dtype: Incomplete

class Nifti2Header(Nifti1Header):
    template_dtype = header_dtype
    pair_vox_offset: int
    single_vox_offset: int
    pair_magic: bytes
    single_magic: bytes
    sizeof_hdr: int
    quaternion_threshold: Incomplete
    def get_data_shape(self): ...
    def set_data_shape(self, shape) -> None: ...
    @classmethod
    def default_structarr(klass, endianness: Incomplete | None = None): ...
    @classmethod
    def may_contain_header(klass, binaryblock): ...

class Nifti2PairHeader(Nifti2Header):
    is_single: bool

class Nifti2Pair(Nifti1Pair):
    header_class = Nifti2PairHeader

class Nifti2Image(Nifti1Image):
    header_class = Nifti2Header

def load(filename): ...
def save(img, filename) -> None: ...
