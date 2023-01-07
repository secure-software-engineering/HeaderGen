from pandas import Index as Index, MultiIndex as MultiIndex
from pandas._typing import ArrayLike as ArrayLike, DtypeArg as DtypeArg, DtypeObj as DtypeObj, ReadCsvBuffer as ReadCsvBuffer
from pandas.core.dtypes.common import is_categorical_dtype as is_categorical_dtype, pandas_dtype as pandas_dtype
from pandas.core.dtypes.concat import union_categoricals as union_categoricals
from pandas.core.dtypes.dtypes import ExtensionDtype as ExtensionDtype
from pandas.core.indexes.api import ensure_index_from_sequences as ensure_index_from_sequences
from pandas.errors import DtypeWarning as DtypeWarning
from pandas.io.parsers.base_parser import ParserBase as ParserBase, is_index_col as is_index_col
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Union, Any, Hashable, Mapping, Sequence

class CParserWrapper(ParserBase):
    low_memory: bool
    kwds: Any
    unnamed_cols: Any
    names: Any
    orig_names: Any
    index_names: Any
    def __init__(self, src: ReadCsvBuffer[str], **kwds) -> None: ...
    def close(self) -> None: ...
    def read(self, nrows: Union[int, None] = ...) -> tuple[Union[Index, MultiIndex, None], Union[Sequence[Hashable], MultiIndex], Mapping[Hashable, ArrayLike]]: ...

def ensure_dtype_objs(dtype: Union[DtypeArg, dict[Hashable, DtypeArg], None]) -> Union[DtypeObj, dict[Hashable, DtypeObj], None]: ...
