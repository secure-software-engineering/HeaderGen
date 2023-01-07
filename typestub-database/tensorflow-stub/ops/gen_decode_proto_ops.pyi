from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

class _DecodeProtoV2Output(NamedTuple):
    sizes: Any
    values: Any

def decode_proto_v2(bytes, message_type, field_names, output_types, descriptor_source: str = ..., message_format: str = ..., sanitize: bool = ..., name: Any | None = ...): ...

DecodeProtoV2: Any

def decode_proto_v2_eager_fallback(bytes, message_type, field_names, output_types, descriptor_source, message_format, sanitize, name, ctx): ...
