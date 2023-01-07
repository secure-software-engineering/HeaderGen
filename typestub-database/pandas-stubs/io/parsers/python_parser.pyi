from collections import abc
from pandas._typing import ArrayLike as ArrayLike, ReadCsvBuffer as ReadCsvBuffer, Scalar as Scalar
from pandas.core.dtypes.common import is_integer as is_integer
from pandas.core.dtypes.inference import is_dict_like as is_dict_like
from pandas.errors import EmptyDataError as EmptyDataError, ParserError as ParserError
from pandas.io.parsers.base_parser import ParserBase as ParserBase, parser_defaults as parser_defaults
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Union, Any, IO, Literal

class PythonParser(ParserBase):
    data: Any
    buf: Any
    pos: int
    line_pos: int
    skiprows: Any
    skipfunc: Any
    skipfooter: Any
    delimiter: Any
    quotechar: Any
    escapechar: Any
    doublequote: Any
    skipinitialspace: Any
    lineterminator: Any
    quoting: Any
    skip_blank_lines: Any
    names_passed: Any
    has_index_names: bool
    verbose: Any
    converters: Any
    thousands: Any
    decimal: Any
    comment: Any
    columns: Any
    orig_names: Any
    index_names: Any
    num: Any
    def __init__(self, f: Union[ReadCsvBuffer[str], list], **kwds): ...
    def read(self, rows: Union[int, None] = ...): ...
    def get_chunk(self, size: Any | None = ...): ...

class FixedWidthReader(abc.Iterator):
    f: Any
    buffer: Any
    delimiter: Any
    comment: Any
    colspecs: Any
    def __init__(self, f: IO[str], colspecs: Union[list[tuple[int, int]], Literal[infer]], delimiter: Union[str, None], comment: Union[str, None], skiprows: Union[set[int], None] = ..., infer_nrows: int = ...) -> None: ...
    def get_rows(self, infer_nrows: int, skiprows: Union[set[int], None] = ...) -> list[str]: ...
    def detect_colspecs(self, infer_nrows: int = ..., skiprows: Union[set[int], None] = ...) -> list[tuple[int, int]]: ...
    def __next__(self) -> list[str]: ...

class FixedWidthFieldParser(PythonParser):
    colspecs: Any
    infer_nrows: Any
    def __init__(self, f: ReadCsvBuffer[str], **kwds) -> None: ...

def count_empty_vals(vals) -> int: ...
