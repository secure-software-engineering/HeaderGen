from typing import Union, Any, Hashable

class OutputKey:
    label: Hashable
    position: int

plotting_methods: Any
common_apply_allowlist: Any
series_apply_allowlist: frozenset[str]
dataframe_apply_allowlist: frozenset[str]
cythonized_kernels: Any
reduction_kernels: Any

def maybe_normalize_deprecated_kernels(kernel): ...

transformation_kernels: Any
groupby_other_methods: Any
transform_kernel_allowlist: Any
