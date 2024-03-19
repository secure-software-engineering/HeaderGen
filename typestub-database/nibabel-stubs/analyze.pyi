from _typeshed import Incomplete

from .arrayproxy import ArrayProxy as ArrayProxy
from .arraywriters import ArrayWriter as ArrayWriter
from .arraywriters import WriterError as WriterError
from .arraywriters import get_slope_inter as get_slope_inter
from .arraywriters import make_array_writer as make_array_writer
from .batteryrunners import Report as Report
from .fileholders import copy_file_map as copy_file_map
from .spatialimages import HeaderDataError as HeaderDataError
from .spatialimages import HeaderTypeError as HeaderTypeError
from .spatialimages import SpatialHeader as SpatialHeader
from .spatialimages import SpatialImage as SpatialImage
from .volumeutils import apply_read_scaling as apply_read_scaling
from .volumeutils import array_from_file as array_from_file
from .volumeutils import make_dt_codes as make_dt_codes
from .volumeutils import native_code as native_code
from .volumeutils import seek_tell as seek_tell
from .volumeutils import shape_zoom_affine as shape_zoom_affine
from .volumeutils import swapped_code as swapped_code
from .wrapstruct import LabeledWrapStruct as LabeledWrapStruct

header_key_dtd: Incomplete
image_dimension_dtd: Incomplete
data_history_dtd: list[tuple[str, str] | tuple[str, str, tuple[int, ...]]]
header_dtype: Incomplete
data_type_codes: Incomplete

class AnalyzeHeader(LabeledWrapStruct, SpatialHeader):
    template_dtype = header_dtype
    default_x_flip: bool
    has_data_slope: bool
    has_data_intercept: bool
    sizeof_hdr: int
    def __init__(
        self,
        binaryblock: Incomplete | None = None,
        endianness: Incomplete | None = None,
        check: bool = True,
    ) -> None: ...
    @classmethod
    def guessed_endian(klass, hdr): ...
    @classmethod
    def default_structarr(klass, endianness: Incomplete | None = None): ...
    @classmethod
    def from_header(klass, header: Incomplete | None = None, check: bool = True): ...
    def raw_data_from_fileobj(self, fileobj): ...
    def data_from_fileobj(self, fileobj): ...
    def data_to_fileobj(self, data, fileobj, rescale: bool = True) -> None: ...
    def get_data_dtype(self): ...
    def set_data_dtype(self, datatype) -> None: ...
    def get_data_shape(self): ...
    def set_data_shape(self, shape) -> None: ...
    def get_base_affine(self): ...
    get_best_affine = get_base_affine
    def get_zooms(self): ...
    def set_zooms(self, zooms) -> None: ...
    def as_analyze_map(self): ...
    def set_data_offset(self, offset) -> None: ...
    def get_data_offset(self): ...
    def get_slope_inter(self): ...
    def set_slope_inter(self, slope, inter: Incomplete | None = None) -> None: ...
    @classmethod
    def may_contain_header(klass, binaryblock): ...

class AnalyzeImage(SpatialImage):
    header_class: type[AnalyzeHeader]
    header: AnalyzeHeader
    files_types: tuple[tuple[str, str], ...]
    valid_exts: tuple[str, ...]
    makeable: bool
    rw: bool
    ImageArrayProxy = ArrayProxy
    def __init__(
        self,
        dataobj,
        affine,
        header: Incomplete | None = None,
        extra: Incomplete | None = None,
        file_map: Incomplete | None = None,
        dtype: Incomplete | None = None,
    ) -> None: ...
    def get_data_dtype(self): ...
    def set_data_dtype(self, dtype) -> None: ...
    @classmethod
    def from_file_map(
        klass, file_map, *, mmap: bool = True, keep_file_open: Incomplete | None = None
    ): ...
    file_map: Incomplete
    def to_file_map(
        self, file_map: Incomplete | None = None, dtype: Incomplete | None = None
    ) -> None: ...

load: Incomplete
save: Incomplete
