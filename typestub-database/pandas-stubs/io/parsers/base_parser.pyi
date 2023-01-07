from enum import Enum
from pandas import DataFrame as DataFrame
from pandas._libs.parsers import STR_NA_VALUES as STR_NA_VALUES
from pandas._libs.tslibs import parsing as parsing
from pandas._typing import ArrayLike as ArrayLike, DtypeArg as DtypeArg
from pandas.core import algorithms as algorithms
from pandas.core.arrays import Categorical as Categorical
from pandas.core.dtypes.cast import astype_nansafe as astype_nansafe
from pandas.core.dtypes.common import ensure_object as ensure_object, is_bool_dtype as is_bool_dtype, is_categorical_dtype as is_categorical_dtype, is_dict_like as is_dict_like, is_dtype_equal as is_dtype_equal, is_extension_array_dtype as is_extension_array_dtype, is_integer as is_integer, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_object_dtype as is_object_dtype, is_scalar as is_scalar, is_string_dtype as is_string_dtype, pandas_dtype as pandas_dtype
from pandas.core.dtypes.dtypes import CategoricalDtype as CategoricalDtype
from pandas.core.dtypes.missing import isna as isna
from pandas.core.indexes.api import Index as Index, MultiIndex as MultiIndex, ensure_index_from_sequences as ensure_index_from_sequences
from pandas.core.series import Series as Series
from pandas.errors import ParserError as ParserError, ParserWarning as ParserWarning
from pandas.io.date_converters import generic_parser as generic_parser
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Union, Any

class ParserBase:
    class BadLineHandleMethod(Enum):
        ERROR: int
        WARN: int
        SKIP: int
    names: Any
    orig_names: Any
    prefix: Any
    index_col: Any
    unnamed_cols: Any
    index_names: Any
    col_names: Any
    parse_dates: Any
    date_parser: Any
    dayfirst: Any
    keep_date_col: Any
    na_values: Any
    na_fvalues: Any
    na_filter: Any
    keep_default_na: Any
    dtype: Any
    true_values: Any
    false_values: Any
    mangle_dupe_cols: Any
    infer_datetime_format: Any
    cache_dates: Any
    header: Any
    on_bad_lines: Any
    def __init__(self, kwds) -> None: ...
    def close(self) -> None: ...

parser_defaults: Any

def is_index_col(col) -> bool: ...
