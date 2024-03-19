from _typeshed import Incomplete

from .affines import apply_affine as apply_affine
from .affines import dot_reduce as dot_reduce
from .affines import from_matvec as from_matvec
from .eulerangles import euler2mat as euler2mat
from .fileslice import fileslice as fileslice
from .fileslice import strided_scalar as strided_scalar
from .nifti1 import unit_codes as unit_codes
from .openers import ImageOpener as ImageOpener
from .spatialimages import SpatialHeader as SpatialHeader
from .spatialimages import SpatialImage as SpatialImage
from .volumeutils import Recoder as Recoder
from .volumeutils import array_from_file as array_from_file

PSL_TO_RAS: Incomplete
ACQ_TO_PSL: Incomplete
DEG2RAD: Incomplete
image_def_dtds: Incomplete
supported_versions: Incomplete
image_def_dtype: Incomplete
slice_orientation_codes: Incomplete

class PARRECError(Exception): ...

GEN_RE: Incomplete

def vol_numbers(slice_nos): ...
def vol_is_full(slice_nos, slice_max, slice_min: int = 1): ...
def one_line(long_str): ...
def parse_PAR_header(fobj): ...
def exts2pars(exts_source): ...

class PARRECArrayProxy:
    file_like: Incomplete
    def __init__(
        self, file_like, header, *, mmap: bool = True, scaling: str = "dv"
    ) -> None: ...
    @property
    def shape(self): ...
    @property
    def ndim(self): ...
    @property
    def dtype(self): ...
    @property
    def is_proxy(self): ...
    def get_unscaled(self): ...
    def __array__(self, dtype: Incomplete | None = None): ...
    def __getitem__(self, slicer): ...

class PARRECHeader(SpatialHeader):
    general_info: Incomplete
    image_defs: Incomplete
    permit_truncated: Incomplete
    strict_sort: Incomplete
    def __init__(
        self,
        info,
        image_defs,
        permit_truncated: bool = False,
        strict_sort: bool = False,
    ) -> None: ...
    @classmethod
    def from_header(klass, header: Incomplete | None = None): ...
    @classmethod
    def from_fileobj(
        klass, fileobj, permit_truncated: bool = False, strict_sort: bool = False
    ): ...
    def copy(self): ...
    def as_analyze_map(self): ...
    def get_water_fat_shift(self): ...
    def get_echo_train_length(self): ...
    def get_q_vectors(self): ...
    def get_bvals_bvecs(self): ...
    def get_def(self, name): ...
    def get_data_offset(self): ...
    def set_data_offset(self, offset) -> None: ...
    def get_affine(self, origin: str = "scanner"): ...
    def get_data_scaling(self, method: str = "dv"): ...
    def get_slice_orientation(self): ...
    def get_rec_shape(self): ...
    def get_sorted_slice_indices(self): ...
    def get_volume_labels(self): ...

class PARRECImage(SpatialImage):
    header_class = PARRECHeader
    header: PARRECHeader
    valid_exts: Incomplete
    files_types: Incomplete
    makeable: bool
    rw: bool
    ImageArrayProxy = PARRECArrayProxy
    @classmethod
    def from_file_map(
        klass,
        file_map,
        *,
        mmap: bool = True,
        permit_truncated: bool = False,
        scaling: str = "dv",
        strict_sort: bool = False
    ): ...
    @classmethod
    def from_filename(
        klass,
        filename,
        *,
        mmap: bool = True,
        permit_truncated: bool = False,
        scaling: str = "dv",
        strict_sort: bool = False
    ): ...
    load = from_filename

load: Incomplete
