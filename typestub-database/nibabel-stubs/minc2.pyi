from _typeshed import Incomplete

from .minc1 import Minc1File as Minc1File
from .minc1 import Minc1Image as Minc1Image
from .minc1 import MincError as MincError
from .minc1 import MincHeader as MincHeader

class Hdf5Bunch:
    def __init__(self, var) -> None: ...

class Minc2File(Minc1File):
    def __init__(self, mincfile) -> None: ...
    def get_data_dtype(self): ...
    def get_data_shape(self): ...
    def get_scaled_data(self, sliceobj=()): ...

class Minc2Header(MincHeader):
    @classmethod
    def may_contain_header(klass, binaryblock): ...

class Minc2Image(Minc1Image):
    header_class = Minc2Header
    header: Minc2Header
    @classmethod
    def from_file_map(
        klass, file_map, *, mmap: bool = True, keep_file_open: Incomplete | None = None
    ): ...

load: Incomplete
