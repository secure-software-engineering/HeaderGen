import typing as ty

import numpy
import numpy.typing as npt

from .arrayproxy import ArrayLike as ArrayLike
from .deprecated import deprecate_with_version as deprecate_with_version
from .filebasedimages import FileBasedHeader as FileBasedHeader
from .filebasedimages import FileBasedImage as FileBasedImage
from .fileholders import FileMap as FileMap
from .filename_parser import FileSpec as FileSpec

ArrayImgT = ty.TypeVar("ArrayImgT", bound="DataobjImage")

class DataobjImage(FileBasedImage):
    def __init__(
        self,
        dataobj: ArrayLike,
        header: FileBasedHeader | ty.Mapping | None = None,
        extra: ty.Mapping | None = None,
        file_map: FileMap | None = None,
    ) -> None: ...
    @property
    def dataobj(self) -> ArrayLike: ...
    def get_data(self, caching: str = "fill") -> numpy.ndarray: ...
    def get_fdata(
        self,
        caching: ty.Literal["fill", "unchanged"] = "fill",
        dtype: npt.DTypeLike = ...,
    ) -> numpy.ndarray[ty.Any, numpy.dtype[numpy.floating]]: ...
    @property
    def in_memory(self) -> bool: ...
    def uncache(self) -> None: ...
    @property
    def shape(self) -> tuple[int, ...]: ...
    @property
    def ndim(self) -> int: ...
    @classmethod
    def from_file_map(
        klass: type[ArrayImgT],
        file_map: FileMap,
        *,
        mmap: bool | ty.Literal["c", "r"] = True,
        keep_file_open: bool | None = None
    ) -> ArrayImgT: ...
    @classmethod
    def from_filename(
        klass: type[ArrayImgT],
        filename: FileSpec,
        *,
        mmap: bool | ty.Literal["c", "r"] = True,
        keep_file_open: bool | None = None
    ) -> ArrayImgT: ...
    load = from_filename
