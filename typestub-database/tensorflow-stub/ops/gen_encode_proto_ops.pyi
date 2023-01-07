from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def encode_proto(sizes, values, field_names, message_type, descriptor_source: str = ..., name: Any | None = ...): ...

EncodeProto: Any

def encode_proto_eager_fallback(sizes, values, field_names, message_type, descriptor_source, name, ctx): ...
