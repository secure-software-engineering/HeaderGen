import gzip
import io
import typing as ty
from types import TracebackType

from _typeshed import Incomplete
from _typeshed import WriteableBuffer as WriteableBuffer

from ._compression import HAVE_INDEXED_GZIP as HAVE_INDEXED_GZIP
from ._compression import IndexedGzipFile as IndexedGzipFile
from ._compression import pyzstd as pyzstd

ModeRT: Incomplete
ModeRB: Incomplete
ModeWT: Incomplete
ModeWB: Incomplete
ModeR: Incomplete
ModeW: Incomplete
Mode: Incomplete
OpenerDef: Incomplete

class Fileish(ty.Protocol):
    def read(self, size: int = -1) -> bytes: ...
    def write(self, b: bytes) -> int | None: ...

class DeterministicGzipFile(gzip.GzipFile):
    def __init__(
        self,
        filename: str | None = None,
        mode: Mode | None = None,
        compresslevel: int = 9,
        fileobj: io.FileIO | None = None,
        mtime: int = 0,
    ) -> None: ...

class Opener:
    gz_def: Incomplete
    bz2_def: Incomplete
    zstd_def: Incomplete
    compress_ext_map: dict[str | None, OpenerDef]
    default_compresslevel: int
    default_zst_compresslevel: int
    default_level_or_option: Incomplete
    compress_ext_icase: bool
    fobj: io.IOBase
    me_opened: bool
    def __init__(self, fileish: str | io.IOBase, *args, **kwargs) -> None: ...
    @property
    def closed(self) -> bool: ...
    @property
    def name(self) -> str | None: ...
    @property
    def mode(self) -> str: ...
    def fileno(self) -> int: ...
    def read(self, size: int = -1) -> bytes: ...
    def readinto(self, buffer: WriteableBuffer) -> int | None: ...
    def write(self, b: bytes) -> int | None: ...
    def seek(self, pos: int, whence: int = 0) -> int: ...
    def tell(self) -> int: ...
    def close(self) -> None: ...
    def __iter__(self) -> ty.Iterator[bytes]: ...
    def close_if_mine(self) -> None: ...
    def __enter__(self) -> Opener: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...

class ImageOpener(Opener):
    compress_ext_map: Incomplete
