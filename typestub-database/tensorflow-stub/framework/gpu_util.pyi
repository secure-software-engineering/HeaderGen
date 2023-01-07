from typing import Any, NamedTuple

class GpuInfo(NamedTuple):
    name: Any
    compute_capability: Any

def compute_capability_from_device_desc(device_attrs): ...
