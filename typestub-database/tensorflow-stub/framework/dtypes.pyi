from tensorflow.core.framework import types_pb2 as types_pb2
from tensorflow.python import pywrap_tensorflow as pywrap_tensorflow
from tensorflow.python.framework import _dtypes
from tensorflow.python.types import doc_typealias as doc_typealias
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class DType(_dtypes.DType):
    def base_dtype(self): ...
    def real_dtype(self): ...
    def as_numpy_dtype(self): ...
    def min(self): ...
    def max(self): ...
    def limits(self, clip_negative: bool = ...): ...
    def is_compatible_with(self, other): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    __hash__: Any
    def __reduce__(self): ...

dtype_range: Any
resource: Any
variant: Any
uint8: Any
uint16: Any
uint32: Any
uint64: Any
int8: Any
int16: Any
int32: Any
int64: Any
float16: Any
half = float16
float32: Any
float64: Any
double = float64
complex64: Any
complex128: Any
string: Any
bool: Any
qint8: Any
qint16: Any
qint32: Any
quint8: Any
quint16: Any
bfloat16: Any
resource_ref: Any
variant_ref: Any
float16_ref: Any
half_ref = float16_ref
float32_ref: Any
float64_ref: Any
double_ref = float64_ref
int32_ref: Any
uint32_ref: Any
uint8_ref: Any
uint16_ref: Any
int16_ref: Any
int8_ref: Any
string_ref: Any
complex64_ref: Any
complex128_ref: Any
int64_ref: Any
uint64_ref: Any
bool_ref: Any
qint8_ref: Any
quint8_ref: Any
qint16_ref: Any
quint16_ref: Any
qint32_ref: Any
bfloat16_ref: Any
np_resource: Any
TF_VALUE_DTYPES: Any
QUANTIZED_DTYPES: Any

def as_dtype(type_value): ...
