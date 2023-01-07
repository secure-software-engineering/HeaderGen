from pandas._libs.lib import is_bool as is_bool, is_integer as is_integer
from pandas.errors import UnsupportedFunctionCall as UnsupportedFunctionCall
from pandas.util._validators import validate_args as validate_args, validate_args_and_kwargs as validate_args_and_kwargs, validate_kwargs as validate_kwargs
from typing import Union, Any

class CompatValidator:
    fname: Any
    method: Any
    defaults: Any
    max_fname_arg_count: Any
    def __init__(self, defaults, fname: Any | None = ..., method: Union[str, None] = ..., max_fname_arg_count: Any | None = ...) -> None: ...
    def __call__(self, args, kwargs, fname: Any | None = ..., max_fname_arg_count: Any | None = ..., method: Union[str, None] = ...) -> None: ...

ARGMINMAX_DEFAULTS: Any
validate_argmin: Any
validate_argmax: Any

def process_skipna(skipna, args): ...
def validate_argmin_with_skipna(skipna, args, kwargs): ...
def validate_argmax_with_skipna(skipna, args, kwargs): ...

ARGSORT_DEFAULTS: dict[str, Union[int, str, None]]
validate_argsort: Any
ARGSORT_DEFAULTS_KIND: dict[str, Union[int, None]]
validate_argsort_kind: Any

def validate_argsort_with_ascending(ascending, args, kwargs): ...

CLIP_DEFAULTS: dict[str, Any]
validate_clip: Any

def validate_clip_with_axis(axis, args, kwargs): ...

CUM_FUNC_DEFAULTS: dict[str, Any]
validate_cum_func: Any
validate_cumsum: Any

def validate_cum_func_with_skipna(skipna, args, kwargs, name): ...

ALLANY_DEFAULTS: dict[str, Union[bool, None]]
validate_all: Any
validate_any: Any
LOGICAL_FUNC_DEFAULTS: Any
validate_logical_func: Any
MINMAX_DEFAULTS: Any
validate_min: Any
validate_max: Any
RESHAPE_DEFAULTS: dict[str, str]
validate_reshape: Any
REPEAT_DEFAULTS: dict[str, Any]
validate_repeat: Any
ROUND_DEFAULTS: dict[str, Any]
validate_round: Any
SORT_DEFAULTS: dict[str, Union[int, str, None]]
validate_sort: Any
STAT_FUNC_DEFAULTS: dict[str, Union[Any, None]]
SUM_DEFAULTS: Any
PROD_DEFAULTS: Any
MEDIAN_DEFAULTS: Any
validate_stat_func: Any
validate_sum: Any
validate_prod: Any
validate_mean: Any
validate_median: Any
STAT_DDOF_FUNC_DEFAULTS: dict[str, Union[bool, None]]
validate_stat_ddof_func: Any
TAKE_DEFAULTS: dict[str, Union[str, None]]
validate_take: Any

def validate_take_with_convert(convert, args, kwargs): ...

TRANSPOSE_DEFAULTS: Any
validate_transpose: Any

def validate_window_func(name, args, kwargs) -> None: ...
def validate_rolling_func(name, args, kwargs) -> None: ...
def validate_expanding_func(name, args, kwargs) -> None: ...
def validate_groupby_func(name, args, kwargs, allowed: Any | None = ...) -> None: ...

RESAMPLER_NUMPY_OPS: Any

def validate_resampler_func(method: str, args, kwargs) -> None: ...
def validate_minmax_axis(axis: Union[int, None], ndim: int = ...) -> None: ...
