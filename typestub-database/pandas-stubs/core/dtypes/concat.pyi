from pandas._typing import ArrayLike as ArrayLike, DtypeObj as DtypeObj
from pandas.core.arrays.sparse import SparseArray as SparseArray
from pandas.core.dtypes.cast import astype_array as astype_array, find_common_type as find_common_type
from pandas.core.dtypes.common import is_categorical_dtype as is_categorical_dtype, is_dtype_equal as is_dtype_equal, is_sparse as is_sparse
from pandas.core.dtypes.dtypes import ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.generic import ABCCategoricalIndex as ABCCategoricalIndex, ABCExtensionArray as ABCExtensionArray, ABCSeries as ABCSeries
from pandas.util._exceptions import find_stack_level as find_stack_level

def cast_to_common_type(arr: ArrayLike, dtype: DtypeObj) -> ArrayLike: ...
def concat_compat(to_concat, axis: int = ..., ea_compat_axis: bool = ...): ...
def union_categoricals(to_union, sort_categories: bool = ..., ignore_order: bool = ...): ...
