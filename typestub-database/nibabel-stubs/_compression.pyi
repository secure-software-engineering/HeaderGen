import gzip
import io

from .optpkg import optional_package as optional_package

HAVE_INDEXED_GZIP: bool
HAVE_ZSTD: bool
COMPRESSED_FILE_LIKES: tuple[type[io.IOBase], ...]
COMPRESSION_ERRORS: tuple[type[BaseException], ...]
IndexedGzipFile = gzip.GzipFile
