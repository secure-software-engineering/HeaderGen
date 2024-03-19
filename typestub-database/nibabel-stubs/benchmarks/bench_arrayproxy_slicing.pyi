from _typeshed import Incomplete
from nibabel.openers import HAVE_INDEXED_GZIP as HAVE_INDEXED_GZIP
from nibabel.tmpdirs import InTemporaryDirectory as InTemporaryDirectory

from ..rstutils import rst_table as rst_table
from .butils import print_git_title as print_git_title

NITERS: int
SHAPE: Incomplete
SLICEOBJS: Incomplete
KEEP_OPENS: Incomplete
HAVE_IGZIP: Incomplete

def bench_arrayproxy_slicing(): ...
