from _typeshed import Incomplete

MEGABYTE: Incomplete

def is_array_sequence(obj): ...
def is_ndarray_of_int_or_bool(obj): ...

class _BuildCache:
    offsets: Incomplete
    lengths: Incomplete
    next_offset: Incomplete
    bytes_per_buf: Incomplete
    dtype: Incomplete
    common_shape: Incomplete
    rows_per_buf: Incomplete
    def __init__(self, arr_seq, common_shape, dtype) -> None: ...
    def update_seq(self, arr_seq) -> None: ...

class ArraySequence:
    def __init__(
        self, iterable: Incomplete | None = None, buffer_size: int = 4
    ) -> None: ...
    @property
    def is_sliced_view(self): ...
    @property
    def is_array_sequence(self): ...
    @property
    def common_shape(self): ...
    @property
    def total_nb_rows(self): ...
    def get_data(self): ...
    def append(self, element, cache_build: bool = False) -> None: ...
    def finalize_append(self) -> None: ...
    def shrink_data(self) -> None: ...
    def extend(self, elements) -> None: ...
    def copy(self): ...
    def __getitem__(self, idx): ...
    def __setitem__(self, idx, elements) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def save(self, filename) -> None: ...
    @classmethod
    def load(cls, filename): ...

def create_arraysequences_from_generator(
    gen, n, buffer_sizes: Incomplete | None = None
): ...
def concatenate(seqs, axis): ...