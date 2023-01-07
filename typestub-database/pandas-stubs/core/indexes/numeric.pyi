import numpy as np
from pandas._libs import lib as lib
from pandas._typing import Dtype as Dtype, DtypeObj as DtypeObj, npt as npt
from pandas.core.dtypes.cast import astype_nansafe as astype_nansafe
from pandas.core.dtypes.common import is_dtype_equal as is_dtype_equal, is_extension_array_dtype as is_extension_array_dtype, is_float as is_float, is_float_dtype as is_float_dtype, is_integer_dtype as is_integer_dtype, is_numeric_dtype as is_numeric_dtype, is_scalar as is_scalar, is_signed_integer_dtype as is_signed_integer_dtype, is_unsigned_integer_dtype as is_unsigned_integer_dtype, needs_i8_conversion as needs_i8_conversion, pandas_dtype as pandas_dtype
from pandas.core.dtypes.generic import ABCSeries as ABCSeries
from pandas.core.indexes.base import Index as Index, maybe_extract_name as maybe_extract_name
from pandas.util._decorators import cache_readonly as cache_readonly, doc as doc
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Union, Any

class NumericIndex(Index):
    def inferred_type(self) -> str: ...
    def __new__(cls, data: Any | None = ..., dtype: Union[Dtype, None] = ..., copy: bool = ..., name: Any | None = ...): ...
    def __contains__(self, key) -> bool: ...
    def astype(self, dtype, copy: bool = ...): ...

class IntegerIndex(NumericIndex):
    @property
    def asi8(self) -> npt.NDArray[np.int64]: ...

class Int64Index(IntegerIndex):
    __doc__: Any

class UInt64Index(IntegerIndex):
    __doc__: Any

class Float64Index(NumericIndex):
    __doc__: Any
