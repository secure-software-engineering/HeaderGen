import numpy as np
from pandas._libs import lib as lib
from pandas._typing import ArrayLike as ArrayLike, AstypeArg as AstypeArg, DtypeObj as DtypeObj, npt as npt
from pandas.core.arrays import ExtensionArray as ExtensionArray
from pandas.core.arrays.numeric import NumericArray as NumericArray, NumericDtype as NumericDtype
from pandas.core.dtypes.cast import astype_nansafe as astype_nansafe
from pandas.core.dtypes.common import is_bool_dtype as is_bool_dtype, is_datetime64_dtype as is_datetime64_dtype, is_float_dtype as is_float_dtype, is_integer_dtype as is_integer_dtype, is_object_dtype as is_object_dtype, pandas_dtype as pandas_dtype
from pandas.core.dtypes.dtypes import ExtensionDtype as ExtensionDtype, register_extension_dtype as register_extension_dtype
from pandas.core.tools.numeric import to_numeric as to_numeric
from pandas.util._decorators import cache_readonly as cache_readonly
from typing import Union, Any, overload

class FloatingDtype(NumericDtype):
    @classmethod
    def construct_array_type(cls) -> type[FloatingArray]: ...

def coerce_to_array(values, dtype: Any | None = ..., mask: Any | None = ..., copy: bool = ...) -> tuple[np.ndarray, np.ndarray]: ...

class FloatingArray(NumericArray):
    def dtype(self) -> FloatingDtype: ...
    def __init__(self, values: np.ndarray, mask: np.ndarray, copy: bool = ...) -> None: ...
    @overload
    def astype(self, dtype: npt.DTypeLike, copy: bool = ...) -> np.ndarray: ...
    @overload
    def astype(self, dtype: ExtensionDtype, copy: bool = ...) -> ExtensionArray: ...
    @overload
    def astype(self, dtype: AstypeArg, copy: bool = ...) -> ArrayLike: ...

class Float32Dtype(FloatingDtype):
    type: Any
    name: str
    __doc__: Any

class Float64Dtype(FloatingDtype):
    type: Any
    name: str
    __doc__: Any

FLOAT_STR_TO_DTYPE: Any
