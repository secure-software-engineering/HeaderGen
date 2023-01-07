from typing import Any

class SaveSpec:
    slice_spec: Any
    name: Any
    dtype: Any
    device: Any
    def __init__(self, tensor, slice_spec, name, dtype: Any | None = ..., device: Any | None = ...) -> None: ...
    @property
    def tensor(self): ...

class SaveableObject:
    op: Any
    specs: Any
    name: Any
    def __init__(self, op, specs, name) -> None: ...
    @property
    def optional_restore(self): ...
    @property
    def device(self): ...
    def restore(self, restored_tensors, restored_shapes) -> None: ...
