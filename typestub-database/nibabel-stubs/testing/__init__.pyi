import typing as ty
import warnings

from _typeshed import Incomplete
from importlib_resources import as_file as as_file
from importlib_resources.abc import Traversable

from .helpers import assert_data_similar as assert_data_similar
from .helpers import bytesio_filemap as bytesio_filemap
from .helpers import bytesio_round_trip as bytesio_round_trip
from .np_features import memmap_after_ufunc as memmap_after_ufunc

def get_test_data(
    subdir: ty.Literal["gifti", "nicom", "externals"] | None = None,
    fname: str | None = None,
) -> Traversable: ...

data_path: Incomplete

def assert_dt_equal(a, b) -> None: ...
def assert_allclose_safely(
    a, b, match_nans: bool = True, rtol: float = 1e-05, atol: float = 1e-08
) -> None: ...
def assert_arrays_equal(arrays1, arrays2) -> None: ...
def assert_re_in(regex, c, flags: int = 0) -> None: ...
def get_fresh_mod(mod_name=...): ...

class clear_and_catch_warnings(warnings.catch_warnings):
    class_modules: Incomplete
    modules: Incomplete
    def __init__(self, record: bool = True, modules=()) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *exc_info) -> None: ...

class error_warnings(clear_and_catch_warnings):
    filter: str
    def __enter__(self): ...

class suppress_warnings(error_warnings):
    filter: str

EXTRA_SET: Incomplete

def runif_extra_has(test_str): ...
def assert_arr_dict_equal(dict1, dict2) -> None: ...
def expires(version): ...
def deprecated_to(version): ...
