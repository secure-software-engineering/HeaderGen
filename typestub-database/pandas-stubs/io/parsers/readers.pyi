from collections import abc
from pandas._libs.parsers import STR_NA_VALUES as STR_NA_VALUES
from pandas._typing import ArrayLike as ArrayLike, CSVEngine as CSVEngine, CompressionOptions as CompressionOptions, DtypeArg as DtypeArg, FilePath as FilePath, ReadCsvBuffer as ReadCsvBuffer, StorageOptions as StorageOptions
from pandas.core.dtypes.common import is_file_like as is_file_like, is_float as is_float, is_integer as is_integer, is_list_like as is_list_like
from pandas.core.frame import DataFrame as DataFrame
from pandas.core.indexes.api import RangeIndex as RangeIndex
from pandas.errors import AbstractMethodError as AbstractMethodError, ParserWarning as ParserWarning
from pandas.io.common import IOHandles as IOHandles, get_handle as get_handle, validate_header_arg as validate_header_arg
from pandas.io.parsers.arrow_parser_wrapper import ArrowParserWrapper as ArrowParserWrapper
from pandas.io.parsers.base_parser import ParserBase as ParserBase, is_index_col as is_index_col, parser_defaults as parser_defaults
from pandas.io.parsers.c_parser_wrapper import CParserWrapper as CParserWrapper
from pandas.io.parsers.python_parser import FixedWidthFieldParser as FixedWidthFieldParser, PythonParser as PythonParser
from pandas.util._decorators import Appender as Appender, deprecate_nonkeyword_arguments as deprecate_nonkeyword_arguments
from pandas.util._exceptions import find_stack_level as find_stack_level
from pandas.util._validators import validate_bool_kwarg as validate_bool_kwarg
from typing import Union, Any, NamedTuple

class _DeprecationConfig(NamedTuple):
    default_value: Any
    msg: Union[str, None]

def validate_integer(name, val, min_val: int = ...): ...
def read_csv(filepath_or_buffer: Union[FilePath, ReadCsvBuffer[bytes], ReadCsvBuffer[str]], sep=..., delimiter: Any | None = ..., header: str = ..., names=..., index_col: Any | None = ..., usecols: Any | None = ..., squeeze: Any | None = ..., prefix=..., mangle_dupe_cols: bool = ..., dtype: Union[DtypeArg, None] = ..., engine: Union[CSVEngine, None] = ..., converters: Any | None = ..., true_values: Any | None = ..., false_values: Any | None = ..., skipinitialspace: bool = ..., skiprows: Any | None = ..., skipfooter: int = ..., nrows: Any | None = ..., na_values: Any | None = ..., keep_default_na: bool = ..., na_filter: bool = ..., verbose: bool = ..., skip_blank_lines: bool = ..., parse_dates: Any | None = ..., infer_datetime_format: bool = ..., keep_date_col: bool = ..., date_parser: Any | None = ..., dayfirst: bool = ..., cache_dates: bool = ..., iterator: bool = ..., chunksize: Any | None = ..., compression: CompressionOptions = ..., thousands: Any | None = ..., decimal: str = ..., lineterminator: Any | None = ..., quotechar: str = ..., quoting=..., doublequote: bool = ..., escapechar: Any | None = ..., comment: Any | None = ..., encoding: Any | None = ..., encoding_errors: Union[str, None] = ..., dialect: Any | None = ..., error_bad_lines: Any | None = ..., warn_bad_lines: Any | None = ..., on_bad_lines: Any | None = ..., delim_whitespace: bool = ..., low_memory=..., memory_map: bool = ..., float_precision: Any | None = ..., storage_options: StorageOptions = ...) -> DataFrame: ...
def read_table(filepath_or_buffer: Union[FilePath, ReadCsvBuffer[bytes], ReadCsvBuffer[str]], sep=..., delimiter: Any | None = ..., header: str = ..., names=..., index_col: Any | None = ..., usecols: Any | None = ..., squeeze: Any | None = ..., prefix=..., mangle_dupe_cols: bool = ..., dtype: Union[DtypeArg, None] = ..., engine: Union[CSVEngine, None] = ..., converters: Any | None = ..., true_values: Any | None = ..., false_values: Any | None = ..., skipinitialspace: bool = ..., skiprows: Any | None = ..., skipfooter: int = ..., nrows: Any | None = ..., na_values: Any | None = ..., keep_default_na: bool = ..., na_filter: bool = ..., verbose: bool = ..., skip_blank_lines: bool = ..., parse_dates: bool = ..., infer_datetime_format: bool = ..., keep_date_col: bool = ..., date_parser: Any | None = ..., dayfirst: bool = ..., cache_dates: bool = ..., iterator: bool = ..., chunksize: Any | None = ..., compression: CompressionOptions = ..., thousands: Any | None = ..., decimal: str = ..., lineterminator: Any | None = ..., quotechar: str = ..., quoting=..., doublequote: bool = ..., escapechar: Any | None = ..., comment: Any | None = ..., encoding: Any | None = ..., encoding_errors: Union[str, None] = ..., dialect: Any | None = ..., error_bad_lines: Any | None = ..., warn_bad_lines: Any | None = ..., on_bad_lines: Any | None = ..., delim_whitespace: bool = ..., low_memory=..., memory_map: bool = ..., float_precision: Any | None = ..., storage_options: StorageOptions = ...): ...
def read_fwf(filepath_or_buffer: Union[FilePath, ReadCsvBuffer[bytes], ReadCsvBuffer[str]], colspecs: Union[list[tuple[int, int]], str, None] = ..., widths: Union[list[int], None] = ..., infer_nrows: int = ..., **kwds) -> Union[DataFrame, TextFileReader]: ...

class TextFileReader(abc.Iterator):
    engine: Any
    orig_options: Any
    chunksize: Any
    nrows: Any
    squeeze: Any
    handles: Any
    def __init__(self, f: Union[FilePath, ReadCsvBuffer[bytes], ReadCsvBuffer[str], list], engine: Union[CSVEngine, None] = ..., **kwds) -> None: ...
    def close(self) -> None: ...
    def __next__(self): ...
    def read(self, nrows: Any | None = ...): ...
    def get_chunk(self, size: Any | None = ...): ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...

def TextParser(*args, **kwds): ...

MANDATORY_DIALECT_ATTRS: Any
