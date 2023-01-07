from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def composite_tensor_variant_from_components(components, metadata, name: Any | None = ...): ...

CompositeTensorVariantFromComponents: Any

def composite_tensor_variant_from_components_eager_fallback(components, metadata, name, ctx): ...
def composite_tensor_variant_to_components(encoded, metadata, Tcomponents, name: Any | None = ...): ...

CompositeTensorVariantToComponents: Any

def composite_tensor_variant_to_components_eager_fallback(encoded, metadata, Tcomponents, name, ctx): ...
