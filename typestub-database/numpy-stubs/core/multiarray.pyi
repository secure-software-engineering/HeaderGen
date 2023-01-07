from ._multiarray_umath import *
from ._multiarray_umath import _ARRAY_API as _ARRAY_API, _fastCopyAndTranspose as _fastCopyAndTranspose, _flagdict as _flagdict, _insert as _insert, _monotonicity as _monotonicity, _reconstruct as _reconstruct, _vec_string as _vec_string
from typing import Any

def empty_like(prototype, dtype: Any | None = ..., order: Any | None = ..., subok: Any | None = ..., shape: Any | None = ...): ...
def concatenate(arrays, axis: Any | None = ..., out: Any | None = ..., *, dtype: Any | None = ..., casting: Any | None = ...): ...
def inner(a, b): ...
def where(condition, x: Any | None = ..., y: Any | None = ...): ...
def lexsort(keys, axis: Any | None = ...): ...
def can_cast(from_, to, casting: Any | None = ...): ...
def min_scalar_type(a): ...
def result_type(*arrays_and_dtypes): ...
def dot(a, b, out: Any | None = ...): ...
def vdot(a, b): ...
def bincount(x, weights: Any | None = ..., minlength: Any | None = ...): ...
def ravel_multi_index(multi_index, dims, mode: Any | None = ..., order: Any | None = ...): ...
def unravel_index(indices, shape: Any | None = ..., order: Any | None = ...): ...
def copyto(dst, src, casting: Any | None = ..., where: Any | None = ...): ...
def putmask(a, mask, values): ...
def packbits(a, axis: Any | None = ..., bitorder: str = ...): ...
def unpackbits(a, axis: Any | None = ..., count: Any | None = ..., bitorder: str = ...): ...
def shares_memory(a, b, max_work: Any | None = ...): ...
def may_share_memory(a, b, max_work: Any | None = ...): ...
def is_busday(dates, weekmask: Any | None = ..., holidays: Any | None = ..., busdaycal: Any | None = ..., out: Any | None = ...): ...
def busday_offset(dates, offsets, roll: Any | None = ..., weekmask: Any | None = ..., holidays: Any | None = ..., busdaycal: Any | None = ..., out: Any | None = ...): ...
def busday_count(begindates, enddates, weekmask: Any | None = ..., holidays: Any | None = ..., busdaycal: Any | None = ..., out: Any | None = ...): ...
def datetime_as_string(arr, unit: Any | None = ..., timezone: Any | None = ..., casting: Any | None = ...): ...

# Names in __all__ with no definition:
#   ALLOW_THREADS
#   BUFSIZE
#   CLIP
#   DATETIMEUNITS
#   ITEM_HASOBJECT
#   ITEM_IS_POINTER
#   LIST_PICKLE
#   MAXDIMS
#   MAY_SHARE_BOUNDS
#   MAY_SHARE_EXACT
#   NEEDS_INIT
#   NEEDS_PYAPI
#   RAISE
#   USE_GETITEM
#   USE_SETITEM
#   WRAP
#   add_docstring
#   arange
#   array
#   asanyarray
#   asarray
#   ascontiguousarray
#   asfortranarray
#   broadcast
#   busdaycalendar
#   c_einsum
#   compare_chararrays
#   correlate
#   correlate2
#   count_nonzero
#   datetime_data
#   digitize
#   dragon4_positional
#   dragon4_scientific
#   dtype
#   empty
#   error
#   flagsobj
#   flatiter
#   format_longfloat
#   frombuffer
#   fromfile
#   fromiter
#   fromstring
#   interp
#   interp_complex
#   matmul
#   ndarray
#   nditer
#   nested_iters
#   normalize_axis_index
#   promote_types
#   scalar
#   set_datetimeparse_function
#   set_legacy_print_mode
#   set_numeric_ops
#   set_string_function
#   set_typeDict
#   tracemalloc_domain
#   typeinfo
#   zeros
