from _typeshed import Incomplete

from ..affines import from_matvec as from_matvec
from ..affines import voxel_sizes as voxel_sizes
from ..arrayproxy import ArrayProxy as ArrayProxy
from ..arrayproxy import reshape_dataobj as reshape_dataobj
from ..batteryrunners import BatteryRunner as BatteryRunner
from ..batteryrunners import Report as Report
from ..filebasedimages import SerializableImage as SerializableImage
from ..fileholders import FileHolder as FileHolder
from ..openers import ImageOpener as ImageOpener
from ..spatialimages import HeaderDataError as HeaderDataError
from ..spatialimages import SpatialHeader as SpatialHeader
from ..spatialimages import SpatialImage as SpatialImage
from ..volumeutils import Recoder as Recoder
from ..volumeutils import array_from_file as array_from_file
from ..volumeutils import array_to_file as array_to_file
from ..volumeutils import endian_codes as endian_codes
from ..wrapstruct import LabeledWrapStruct as LabeledWrapStruct

DATA_OFFSET: int
header_dtd: Incomplete
footer_dtd: Incomplete
header_dtype: Incomplete
footer_dtype: Incomplete
hf_dtype: Incomplete
data_type_codes: Incomplete

class MGHError(Exception): ...

class MGHHeader(LabeledWrapStruct, SpatialHeader):
    template_dtype = hf_dtype
    def __init__(
        self, binaryblock: Incomplete | None = None, check: bool = True
    ) -> None: ...
    @staticmethod
    def chk_version(hdr, fix: bool = False): ...
    @classmethod
    def from_header(klass, header: Incomplete | None = None, check: bool = True): ...
    @classmethod
    def from_fileobj(klass, fileobj, check: bool = True): ...
    def get_affine(self): ...
    get_best_affine = get_affine
    def get_vox2ras(self): ...
    def get_vox2ras_tkr(self): ...
    def get_ras2vox(self): ...
    def get_data_dtype(self): ...
    def set_data_dtype(self, datatype) -> None: ...
    def get_zooms(self): ...
    def set_zooms(self, zooms) -> None: ...
    def get_data_shape(self): ...
    def set_data_shape(self, shape) -> None: ...
    def get_data_bytespervox(self): ...
    def get_data_size(self): ...
    def get_data_offset(self): ...
    def get_footer_offset(self): ...
    def data_from_fileobj(self, fileobj): ...
    def get_slope_inter(self): ...
    @classmethod
    def guessed_endian(klass, mapping): ...
    @classmethod
    def default_structarr(klass, endianness: Incomplete | None = None): ...
    def writehdr_to(self, fileobj) -> None: ...
    def writeftr_to(self, fileobj) -> None: ...
    def copy(self): ...
    def as_byteswapped(self, endianness: Incomplete | None = None): ...
    @classmethod
    def diagnose_binaryblock(
        klass, binaryblock, endianness: Incomplete | None = None
    ): ...

class MGHImage(SpatialImage, SerializableImage):
    header_class = MGHHeader
    header: MGHHeader
    valid_exts: Incomplete
    files_types: Incomplete
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
    ) -> None: ...
    @classmethod
    def filespec_to_file_map(klass, filespec): ...
    @classmethod
    def from_file_map(
        klass, file_map, *, mmap: bool = True, keep_file_open: Incomplete | None = None
    ): ...
    file_map: Incomplete
    def to_file_map(self, file_map: Incomplete | None = None) -> None: ...

load: Incomplete
save: Incomplete
