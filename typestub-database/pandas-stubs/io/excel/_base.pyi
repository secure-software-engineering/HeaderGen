import abc
from typing import Any, Callable, Hashable, Iterable, Literal, Sequence, Union, overload

from pandas._config import config as config
from pandas._libs.parsers import STR_NA_VALUES as STR_NA_VALUES
from pandas._typing import DtypeArg as DtypeArg
from pandas._typing import FilePath as FilePath
from pandas._typing import IntStrT as IntStrT
from pandas._typing import ReadBuffer as ReadBuffer
from pandas._typing import StorageOptions as StorageOptions
from pandas._typing import WriteExcelBuffer as WriteExcelBuffer
from pandas.compat._optional import get_version as get_version
from pandas.compat._optional import (
    import_optional_dependency as import_optional_dependency,
)
from pandas.core.dtypes.common import is_bool as is_bool
from pandas.core.dtypes.common import is_float as is_float
from pandas.core.dtypes.common import is_integer as is_integer
from pandas.core.dtypes.common import is_list_like as is_list_like
from pandas.core.frame import DataFrame as DataFrame
from pandas.errors import EmptyDataError as EmptyDataError
from pandas.io.common import IOHandles as IOHandles
from pandas.io.common import get_handle as get_handle
from pandas.io.common import stringify_path as stringify_path
from pandas.io.common import validate_header_arg as validate_header_arg
from pandas.io.excel._odfreader import ODFReader as ODFReader
from pandas.io.excel._openpyxl import OpenpyxlReader as OpenpyxlReader
from pandas.io.excel._pyxlsb import PyxlsbReader as PyxlsbReader
from pandas.io.excel._util import fill_mi_header as fill_mi_header
from pandas.io.excel._util import get_default_engine as get_default_engine
from pandas.io.excel._util import get_writer as get_writer
from pandas.io.excel._util import maybe_convert_usecols as maybe_convert_usecols
from pandas.io.excel._util import pop_header_name as pop_header_name
from pandas.io.excel._xlrd import XlrdReader as XlrdReader
from pandas.io.parsers import TextParser as TextParser
from pandas.util._decorators import Appender as Appender
from pandas.util._decorators import (
    deprecate_nonkeyword_arguments as deprecate_nonkeyword_arguments,
)
from pandas.util._decorators import doc as doc
from pandas.util._exceptions import find_stack_level as find_stack_level
from pandas.util.version import Version as Version

@overload
def read_excel(
    io,
    sheet_name: Union[str, int],
    header: Union[int, Sequence[int], None] = ...,
    names=...,
    index_col: Union[int, Sequence[int], None] = ...,
    usecols=...,
    squeeze: Union[bool, None] = ...,
    dtype: Union[DtypeArg, None] = ...,
    engine: Union[Literal[xlrd, openpyxl, odf, pyxlsb], None] = ...,
    converters=...,
    true_values: Union[Iterable[Hashable], None] = ...,
    false_values: Union[Iterable[Hashable], None] = ...,
    skiprows: Union[Sequence[int], int, Callable[[int], object], None] = ...,
    nrows: Union[int, None] = ...,
    na_values=...,
    keep_default_na: bool = ...,
    na_filter: bool = ...,
    verbose: bool = ...,
    parse_dates=...,
    date_parser=...,
    thousands: Union[str, None] = ...,
    decimal: str = ...,
    comment: Union[str, None] = ...,
    skipfooter: int = ...,
    convert_float: Union[bool, None] = ...,
    mangle_dupe_cols: bool = ...,
    storage_options: StorageOptions = ...,
) -> DataFrame: ...

class BaseExcelReader(metaclass=abc.ABCMeta):
    handles: Any
    book: Any
    def __init__(
        self, filepath_or_buffer, storage_options: StorageOptions = ...
    ) -> None: ...
    @abc.abstractmethod
    def load_workbook(self, filepath_or_buffer): ...
    def close(self) -> None: ...
    @property
    @abc.abstractmethod
    def sheet_names(self) -> list[str]: ...
    @abc.abstractmethod
    def get_sheet_by_name(self, name: str): ...
    @abc.abstractmethod
    def get_sheet_by_index(self, index: int): ...
    @abc.abstractmethod
    def get_sheet_data(self, sheet, convert_float: bool): ...
    def raise_if_bad_sheet_by_index(self, index: int) -> None: ...
    def raise_if_bad_sheet_by_name(self, name: str) -> None: ...
    def parse(
        self,
        sheet_name: Union[str, int, list[int], list[str], None] = ...,
        header: Union[int, Sequence[int], None] = ...,
        names: Any | None = ...,
        index_col: Union[int, Sequence[int], None] = ...,
        usecols: Any | None = ...,
        squeeze: Union[bool, None] = ...,
        dtype: Union[DtypeArg, None] = ...,
        true_values: Union[Iterable[Hashable], None] = ...,
        false_values: Union[Iterable[Hashable], None] = ...,
        skiprows: Union[Sequence[int], int, Callable[[int], object], None] = ...,
        nrows: Union[int, None] = ...,
        na_values: Any | None = ...,
        verbose: bool = ...,
        parse_dates: bool = ...,
        date_parser: Any | None = ...,
        thousands: Union[str, None] = ...,
        decimal: str = ...,
        comment: Union[str, None] = ...,
        skipfooter: int = ...,
        convert_float: Union[bool, None] = ...,
        mangle_dupe_cols: bool = ...,
        **kwds
    ): ...

class ExcelWriter(metaclass=abc.ABCMeta):
    def __new__(
        cls,
        path: Union[FilePath, WriteExcelBuffer, ExcelWriter],
        engine: Union[str, None] = ...,
        date_format: Union[str, None] = ...,
        datetime_format: Union[str, None] = ...,
        mode: str = ...,
        storage_options: StorageOptions = ...,
        if_sheet_exists: Union[Literal[error, new, replace, overlay], None] = ...,
        engine_kwargs: Union[dict, None] = ...,
        **kwargs
    ): ...
    path: Any
    @property
    @abc.abstractmethod
    def supported_extensions(self) -> Union[tuple[str, ...], list[str]]: ...
    @property
    @abc.abstractmethod
    def engine(self) -> str: ...
    @abc.abstractmethod
    def write_cells(
        self,
        cells,
        sheet_name: Union[str, None] = ...,
        startrow: int = ...,
        startcol: int = ...,
        freeze_panes: Union[tuple[int, int], None] = ...,
    ) -> None: ...
    @abc.abstractmethod
    def save(self) -> None: ...
    handles: Any
    sheets: Any
    cur_sheet: Any
    date_format: str
    datetime_format: str
    mode: Any
    if_sheet_exists: Any
    def __init__(
        self,
        path: Union[FilePath, WriteExcelBuffer, ExcelWriter],
        engine: Union[str, None] = ...,
        date_format: Union[str, None] = ...,
        datetime_format: Union[str, None] = ...,
        mode: str = ...,
        storage_options: StorageOptions = ...,
        if_sheet_exists: Union[str, None] = ...,
        engine_kwargs: Union[dict, None] = ...,
        **kwargs
    ) -> None: ...
    def __fspath__(self): ...
    @classmethod
    def check_extension(cls, ext: str) -> Literal[True]: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...
    def close(self) -> None: ...

XLS_SIGNATURES: Any
ZIP_SIGNATURE: bytes
PEEK_SIZE: Any

def inspect_excel_format(
    content_or_path: Union[FilePath, ReadBuffer[bytes]],
    storage_options: StorageOptions = ...,
) -> Union[str, None]: ...

class ExcelFile:
    io: Any
    engine: Any
    storage_options: Any
    def __init__(
        self,
        path_or_buffer,
        engine: Union[str, None] = ...,
        storage_options: StorageOptions = ...,
    ) -> None: ...
    def __fspath__(self): ...
    def parse(
        self,
        sheet_name: Union[str, int, list[int], list[str], None] = ...,
        header: Union[int, Sequence[int], None] = ...,
        names: Any | None = ...,
        index_col: Union[int, Sequence[int], None] = ...,
        usecols: Any | None = ...,
        squeeze: Union[bool, None] = ...,
        converters: Any | None = ...,
        true_values: Union[Iterable[Hashable], None] = ...,
        false_values: Union[Iterable[Hashable], None] = ...,
        skiprows: Union[Sequence[int], int, Callable[[int], object], None] = ...,
        nrows: Union[int, None] = ...,
        na_values: Any | None = ...,
        parse_dates: bool = ...,
        date_parser: Any | None = ...,
        thousands: Union[str, None] = ...,
        comment: Union[str, None] = ...,
        skipfooter: int = ...,
        convert_float: Union[bool, None] = ...,
        mangle_dupe_cols: bool = ...,
        **kwds
    ) -> Union[DataFrame, dict[str, DataFrame], dict[int, DataFrame]]: ...
    @property
    def book(self): ...
    @property
    def sheet_names(self): ...
    def close(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...
    def __del__(self) -> None: ...
