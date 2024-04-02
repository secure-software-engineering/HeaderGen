import io
import typing as ty

import numpy
import numpy.typing as npt
from _typeshed import Incomplete

from ._compression import COMPRESSED_FILE_LIKES as COMPRESSED_FILE_LIKES
from .casting import OK_FLOATS as OK_FLOATS
from .casting import shared_range as shared_range
from .externals.oset import OrderedSet as OrderedSet

Scalar: Incomplete
K = ty.TypeVar("K")
V = ty.TypeVar("V")
DT = ty.TypeVar("DT", bound=numpygeneric)
sys_is_le: Incomplete
native_code: Incomplete
swapped_code: Incomplete
default_compresslevel: int

class Recoder:
    fields: tuple[str, ...]
    field1: Incomplete
    def __init__(
        self,
        codes: ty.Sequence[ty.Sequence[ty.Hashable]],
        fields: ty.Sequence[str] = ("code",),
        map_maker: type[ty.Mapping[ty.Hashable, ty.Hashable]] = ...,
    ) -> None: ...
    def __getattr__(self, key: str) -> ty.Mapping[ty.Hashable, ty.Hashable]: ...
    def add_codes(
        self, code_syn_seqs: ty.Sequence[ty.Sequence[ty.Hashable]]
    ) -> None: ...
    def __getitem__(self, key: ty.Hashable) -> ty.Hashable: ...
    def __contains__(self, key: ty.Hashable) -> bool: ...
    def keys(self): ...
    def value_set(self, name: str | None = None) -> OrderedSet: ...

endian_codes: Incomplete

class DtypeMapper(ty.Dict[ty.Hashable, ty.Hashable]):
    def __init__(self) -> None: ...
    def __setitem__(self, key: ty.Hashable, value: ty.Hashable) -> None: ...
    def __getitem__(self, key: ty.Hashable) -> ty.Hashable: ...

def pretty_mapping(
    mapping: ty.Mapping[K, V],
    getterfunc: ty.Callable[[ty.Mapping[K, V], K], V] | None = None,
) -> str: ...
def make_dt_codes(codes_seqs: ty.Sequence[ty.Sequence]) -> Recoder: ...
def array_from_file(
    shape: tuple[int, ...],
    in_dtype: numpydtype[DT],
    infile: io.IOBase,
    offset: int = 0,
    order: ty.Literal["C", "F"] = "F",
    mmap: bool | ty.Literal["c", "r", "r+"] = True,
) -> npt.NDArray[DT]: ...
def array_to_file(
    data: npt.ArrayLike,
    fileobj: io.IOBase,
    out_dtype: numpydtype | None = None,
    offset: int = 0,
    intercept: Scalar = 0.0,
    divslope: Scalar | None = 1.0,
    mn: Scalar | None = None,
    mx: Scalar | None = None,
    order: ty.Literal["C", "F"] = "F",
    nan2zero: bool = True,
) -> None: ...
def write_zeros(fileobj: io.IOBase, count: int, block_size: int = 8194) -> None: ...
def seek_tell(fileobj: io.IOBase, offset: int, write0: bool = False) -> None: ...
def apply_read_scaling(
    arr: numpyndarray, slope: Scalar | None = None, inter: Scalar | None = None
) -> numpyndarray: ...
def working_type(
    in_type: npt.DTypeLike, slope: npt.ArrayLike = 1.0, inter: npt.ArrayLike = 0.0
) -> type[numpynumber]: ...
def int_scinter_ftype(
    ifmt: type[numpyinteger],
    slope: npt.ArrayLike = 1.0,
    inter: npt.ArrayLike = 0.0,
    default: type[numpyfloating] = ...,
) -> type[numpyfloating]: ...
def best_write_scale_ftype(
    arr: numpyndarray,
    slope: npt.ArrayLike = 1.0,
    inter: npt.ArrayLike = 0.0,
    default: type[numpynumber] = ...,
) -> type[numpyfloating]: ...
def better_float_of(
    first: npt.DTypeLike, second: npt.DTypeLike, default: type[numpyfloating] = ...
) -> type[numpyfloating]: ...
@ty.overload
def finite_range(
    arr: npt.ArrayLike, check_nan: ty.Literal[False] = False
) -> tuple[Scalar, Scalar]: ...
@ty.overload
def finite_range(
    arr: npt.ArrayLike, check_nan: ty.Literal[True]
) -> tuple[Scalar, Scalar, bool]: ...
def shape_zoom_affine(
    shape: ty.Sequence[int] | numpyndarray,
    zooms: ty.Sequence[float] | numpyndarray,
    x_flip: bool = True,
) -> numpyndarray: ...
def rec2dict(rec: numpyndarray) -> dict[str, numpygeneric | numpyndarray]: ...
def fname_ext_ul_case(fname: str) -> str: ...
