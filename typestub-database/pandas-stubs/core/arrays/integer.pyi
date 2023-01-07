import numpy as np
from pandas._libs import lib as lib
from pandas._typing import ArrayLike as ArrayLike, AstypeArg as AstypeArg, Dtype as Dtype, DtypeObj as DtypeObj, npt as npt
from pandas.core.arrays import ExtensionArray as ExtensionArray
from pandas.core.arrays.masked import BaseMaskedDtype as BaseMaskedDtype
from pandas.core.arrays.numeric import NumericArray as NumericArray, NumericDtype as NumericDtype
from pandas.core.dtypes.base import ExtensionDtype as ExtensionDtype, register_extension_dtype as register_extension_dtype
from pandas.core.dtypes.common import is_bool_dtype as is_bool_dtype, is_datetime64_dtype as is_datetime64_dtype, is_float_dtype as is_float_dtype, is_integer_dtype as is_integer_dtype, is_object_dtype as is_object_dtype, is_string_dtype as is_string_dtype, pandas_dtype as pandas_dtype
from pandas.core.tools.numeric import to_numeric as to_numeric
from pandas.util._decorators import cache_readonly as cache_readonly
from typing import Union, Any, overload

class _IntegerDtype(NumericDtype):
    def is_signed_integer(self) -> bool: ...
    def is_unsigned_integer(self) -> bool: ...
    @classmethod
    def construct_array_type(cls) -> type[IntegerArray]: ...

def safe_cast(values, dtype, copy: bool): ...
def coerce_to_array(values, dtype, mask: Any | None = ..., copy: bool = ...) -> tuple[np.ndarray, np.ndarray]: ...

class IntegerArray(NumericArray):
    def dtype(self) -> _IntegerDtype: ...
    def __init__(self, values: np.ndarray, mask: np.ndarray, copy: bool = ...) -> None: ...
    @overload
    def astype(self, dtype: npt.DTypeLike, copy: bool = ...) -> np.ndarray: ...
    @overload
    def astype(self, dtype: ExtensionDtype, copy: bool = ...) -> ExtensionArray: ...
    @overload
    def astype(self, dtype: AstypeArg, copy: bool = ...) -> ArrayLike: ...

class Int8Dtype(_IntegerDtype):
    type: Any
    name: str
    __doc__: Any

class Int16Dtype(_IntegerDtype):
    type: Any
    name: str
    __doc__: Any

class Int32Dtype(_IntegerDtype):
    type: Any
    name: str
    __doc__: Any

class Int64Dtype(_IntegerDtype):
    type: Any
    name: str
    __doc__: Any

class UInt8Dtype(_IntegerDtype):
    type: Any
    name: str
    __doc__: Any

class UInt16Dtype(_IntegerDtype):
    type: Any
    name: str
    __doc__: Any

class UInt32Dtype(_IntegerDtype):
    type: Any
    name: str
    __doc__: Any

class UInt64Dtype(_IntegerDtype):
    type: Any
    name: str
    __doc__: Any

INT_STR_TO_DTYPE: dict[str, _IntegerDtype]
