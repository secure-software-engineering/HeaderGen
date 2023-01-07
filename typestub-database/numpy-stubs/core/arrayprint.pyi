from contextlib import _GeneratorContextManager
from numpy import bool_ as bool_, bytes_ as bytes_, clongdouble as clongdouble, complexfloating as complexfloating, datetime64 as datetime64, floating as floating, generic as generic, integer as integer, longdouble as longdouble, ndarray as ndarray, str_ as str_, timedelta64 as timedelta64, void as void
from numpy.typing import ArrayLike as ArrayLike, _CharLike_co, _FloatLike_co
from types import TracebackType as TracebackType
from typing import Any, Callable, Optional
from typing_extensions import Literal, SupportsIndex, TypedDict

class _FormatDict(TypedDict):
    bool: Callable[[bool_], str]
    int: Callable[[integer[Any]], str]
    timedelta: Callable[[timedelta64], str]
    datetime: Callable[[datetime64], str]
    float: Callable[[floating[Any]], str]
    longfloat: Callable[[longdouble], str]
    complexfloat: Callable[[complexfloating[Any, Any]], str]
    longcomplexfloat: Callable[[clongdouble], str]
    void: Callable[[void], str]
    numpystr: Callable[[_CharLike_co], str]
    object: Callable[[object], str]
    all: Callable[[object], str]
    int_kind: Callable[[integer[Any]], str]
    float_kind: Callable[[floating[Any]], str]
    complex_kind: Callable[[complexfloating[Any, Any]], str]
    str_kind: Callable[[_CharLike_co], str]

class _FormatOptions(TypedDict):
    precision: int
    threshold: int
    edgeitems: int
    linewidth: int
    suppress: bool
    nanstr: str
    infstr: str
    formatter: Optional[_FormatDict]
    sign: Literal['-', '+', ' ']
    floatmode: _FloatMode
    legacy: Literal[False, '1.13']

def set_printoptions(precision: Optional[SupportsIndex] = ..., threshold: Optional[int] = ..., edgeitems: Optional[int] = ..., linewidth: Optional[int] = ..., suppress: Optional[bool] = ..., nanstr: Optional[str] = ..., infstr: Optional[str] = ..., formatter: Optional[_FormatDict] = ..., sign: Optional[Literal['-', '+', ' ']] = ..., floatmode: Optional[_FloatMode] = ..., *, legacy: Optional[Literal[False, '1.13']] = ...) -> None: ...
def get_printoptions() -> _FormatOptions: ...
def array2string(a: ndarray[Any, Any], max_line_width: Optional[int] = ..., precision: Optional[SupportsIndex] = ..., suppress_small: Optional[bool] = ..., separator: str = ..., prefix: str = ..., *, formatter: Optional[_FormatDict] = ..., threshold: Optional[int] = ..., edgeitems: Optional[int] = ..., sign: Optional[Literal['-', '+', ' ']] = ..., floatmode: Optional[_FloatMode] = ..., suffix: str = ..., legacy: Optional[Literal[False, '1.13']] = ...) -> str: ...
def format_float_scientific(x: _FloatLike_co, precision: Optional[int] = ..., unique: bool = ..., trim: Literal[k, '.', '0', '-'] = ..., sign: bool = ..., pad_left: Optional[int] = ..., exp_digits: Optional[int] = ..., min_digits: Optional[int] = ...) -> str: ...
def format_float_positional(x: _FloatLike_co, precision: Optional[int] = ..., unique: bool = ..., fractional: bool = ..., trim: Literal[k, '.', '0', '-'] = ..., sign: bool = ..., pad_left: Optional[int] = ..., pad_right: Optional[int] = ..., min_digits: Optional[int] = ...) -> str: ...
def array_repr(arr: ndarray[Any, Any], max_line_width: Optional[int] = ..., precision: Optional[SupportsIndex] = ..., suppress_small: Optional[bool] = ...) -> str: ...
def array_str(a: ndarray[Any, Any], max_line_width: Optional[int] = ..., precision: Optional[SupportsIndex] = ..., suppress_small: Optional[bool] = ...) -> str: ...
def set_string_function(f: Optional[Callable[[ndarray[Any, Any]], str]], repr: bool = ...) -> None: ...
def printoptions(precision: Optional[SupportsIndex] = ..., threshold: Optional[int] = ..., edgeitems: Optional[int] = ..., linewidth: Optional[int] = ..., suppress: Optional[bool] = ..., nanstr: Optional[str] = ..., infstr: Optional[str] = ..., formatter: Optional[_FormatDict] = ..., sign: Optional[Literal['-', '+', ' ']] = ..., floatmode: Optional[_FloatMode] = ..., *, legacy: Optional[Literal[False, '1.13']] = ...) -> _GeneratorContextManager[_FormatOptions]: ...
