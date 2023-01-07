from typing import Any

class MachArLike:
    title: Any
    epsilon: Any
    epsneg: Any
    xmax: Any
    xmin: Any
    ibeta: Any
    precision: Any
    resolution: Any
    def __init__(self, ftype, eps, epsneg, huge, tiny, ibeta, **kwargs): ...

class finfo:
    def __new__(cls, dtype): ...

class iinfo:
    dtype: Any
    kind: Any
    bits: Any
    key: Any
    def __init__(self, int_type) -> None: ...
    @property
    def min(self): ...
    @property
    def max(self): ...
