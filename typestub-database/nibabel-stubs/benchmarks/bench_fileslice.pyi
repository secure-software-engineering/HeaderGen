from _typeshed import Incomplete

from ..fileslice import fileslice as fileslice
from ..openers import ImageOpener as ImageOpener
from ..optpkg import optional_package as optional_package
from ..rstutils import rst_table as rst_table
from ..tmpdirs import InTemporaryDirectory as InTemporaryDirectory

SHAPE: Incomplete
ROW_NAMES: Incomplete
COL_NAMES: Incomplete
HAVE_ZSTD: Incomplete

def run_slices(file_like, repeat: int = 3, offset: int = 0, order: str = "F"): ...
def bench_fileslice(
    bytes: bool = True,
    file_: bool = True,
    gz: bool = True,
    bz2: bool = False,
    zst: bool = True,
) -> None: ...
