from _typeshed import Incomplete

from .arrayproxy import ArrayProxy as ArrayProxy
from .fileslice import strided_scalar as strided_scalar
from .spatialimages import HeaderDataError as HeaderDataError
from .spatialimages import ImageDataError as ImageDataError
from .spatialimages import SpatialHeader as SpatialHeader
from .spatialimages import SpatialImage as SpatialImage
from .volumeutils import Recoder as Recoder

filepath: Incomplete
datadir: Incomplete
space_codes: Incomplete

class AFNIImageError(ImageDataError): ...
class AFNIHeaderError(HeaderDataError): ...

DATA_OFFSET: int
TYPE_RE: Incomplete
NAME_RE: Incomplete

def parse_AFNI_header(fobj): ...

class AFNIArrayProxy(ArrayProxy):
    def __init__(
        self,
        file_like,
        header,
        *,
        mmap: bool = True,
        keep_file_open: Incomplete | None = None
    ) -> None: ...
    @property
    def scaling(self): ...

class AFNIHeader(SpatialHeader):
    info: Incomplete
    def __init__(self, info) -> None: ...
    @classmethod
    def from_header(klass, header: Incomplete | None = None): ...
    @classmethod
    def from_fileobj(klass, fileobj): ...
    def copy(self): ...
    def get_space(self): ...
    def get_affine(self): ...
    def get_data_scaling(self): ...
    def get_slope_inter(self): ...
    def get_data_offset(self): ...
    def get_volume_labels(self): ...

class AFNIImage(SpatialImage):
    header_class = AFNIHeader
    header: AFNIHeader
    valid_exts: Incomplete
    files_types: Incomplete
    makeable: bool
    rw: bool
    ImageArrayProxy = AFNIArrayProxy
    @classmethod
    def from_file_map(
        klass, file_map, *, mmap: bool = True, keep_file_open: Incomplete | None = None
    ): ...
    @classmethod
    def filespec_to_file_map(klass, filespec): ...

load: Incomplete
