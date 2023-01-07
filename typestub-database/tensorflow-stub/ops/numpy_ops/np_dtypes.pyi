from tensorflow.python.framework import dtypes as dtypes
from tensorflow.python.ops.numpy_ops import np_export as np_export
from typing import Any

bool_: Any
complex_: Any
complex128: Any
complex64: Any
float_: Any
float16: Any
float32: Any
float64: Any
inexact: Any
int_: Any
int16: Any
int32: Any
int64: Any
int8: Any
object_: Any
string_: Any
uint16: Any
uint32: Any
uint64: Any
uint8: Any
unicode_: Any
iinfo: Any
issubdtype: Any

def is_prefer_float32(): ...
def set_prefer_float32(b) -> None: ...
def is_allow_float64(): ...
def set_allow_float64(b) -> None: ...
def canonicalize_dtype(dtype): ...
def default_float_type(): ...
