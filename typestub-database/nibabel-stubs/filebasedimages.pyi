import io
import typing as ty
from urllib import request

from _typeshed import Incomplete

from ._compression import COMPRESSION_ERRORS as COMPRESSION_ERRORS
from .fileholders import FileHolder as FileHolder
from .fileholders import FileMap as FileMap
from .filename_parser import ExtensionSpec as ExtensionSpec
from .filename_parser import FileSpec as FileSpec
from .filename_parser import TypesFilenamesError as TypesFilenamesError
from .filename_parser import splitext_addext as splitext_addext
from .filename_parser import types_filenames as types_filenames
from .openers import ImageOpener as ImageOpener

FileSniff: Incomplete
ImgT = ty.TypeVar("ImgT", bound="FileBasedImage")
HdrT = ty.TypeVar("HdrT", bound="FileBasedHeader")
StreamImgT = ty.TypeVar("StreamImgT", bound="SerializableImage")

class ImageFileError(Exception): ...

class FileBasedHeader:
    @classmethod
    def from_header(
        klass: type[HdrT], header: FileBasedHeader | ty.Mapping | None = None
    ) -> HdrT: ...
    @classmethod
    def from_fileobj(klass: type[HdrT], fileobj: io.IOBase) -> HdrT: ...
    def write_to(self, fileobj: io.IOBase) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def copy(self) -> HdrT: ...

class FileBasedImage:
    header_class: type[FileBasedHeader]
    files_types: tuple[ExtensionSpec, ...]
    valid_exts: tuple[str, ...]
    makeable: bool
    rw: bool
    extra: Incomplete
    file_map: Incomplete
    def __init__(
        self,
        header: FileBasedHeader | ty.Mapping | None = None,
        extra: ty.Mapping | None = None,
        file_map: FileMap | None = None,
    ) -> None: ...
    @property
    def header(self) -> FileBasedHeader: ...
    def __getitem__(self, key) -> None: ...
    def get_filename(self) -> str | None: ...
    def set_filename(self, filename: str) -> None: ...
    @classmethod
    def from_filename(klass: type[ImgT], filename: FileSpec) -> ImgT: ...
    @classmethod
    def from_file_map(klass: type[ImgT], file_map: FileMap) -> ImgT: ...
    @classmethod
    def filespec_to_file_map(klass, filespec: FileSpec) -> FileMap: ...
    def to_filename(self, filename: FileSpec, **kwargs) -> None: ...
    def to_file_map(self, file_map: FileMap | None = None, **kwargs) -> None: ...
    @classmethod
    def make_file_map(
        klass, mapping: ty.Mapping[str, str | io.IOBase] | None = None
    ) -> FileMap: ...
    load = from_filename
    @classmethod
    def instance_to_filename(
        klass, img: FileBasedImage, filename: FileSpec
    ) -> None: ...
    @classmethod
    def from_image(klass: type[ImgT], img: FileBasedImage) -> ImgT: ...
    @classmethod
    def path_maybe_image(
        klass, filename: FileSpec, sniff: FileSniff | None = None, sniff_max: int = 1024
    ) -> tuple[bool, FileSniff | None]: ...

class SerializableImage(FileBasedImage):
    @classmethod
    def from_stream(klass: type[StreamImgT], io_obj: io.IOBase) -> StreamImgT: ...
    def to_stream(self, io_obj: io.IOBase, **kwargs) -> None: ...
    @classmethod
    def from_bytes(klass: type[StreamImgT], bytestring: bytes) -> StreamImgT: ...
    def to_bytes(self, **kwargs) -> bytes: ...
    @classmethod
    def from_url(
        klass: type[StreamImgT], url: str | request.Request, timeout: float = 5
    ) -> StreamImgT: ...
