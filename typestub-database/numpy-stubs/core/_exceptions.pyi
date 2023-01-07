from numpy.core.overrides import set_module as set_module
from typing import Any

class UFuncTypeError(TypeError):
    ufunc: Any
    def __init__(self, ufunc) -> None: ...

class _UFuncBinaryResolutionError(UFuncTypeError):
    dtypes: Any
    def __init__(self, ufunc, dtypes) -> None: ...

class _UFuncNoLoopError(UFuncTypeError):
    dtypes: Any
    def __init__(self, ufunc, dtypes) -> None: ...

class _UFuncCastingError(UFuncTypeError):
    casting: Any
    from_: Any
    to: Any
    def __init__(self, ufunc, casting, from_, to) -> None: ...

class _UFuncInputCastingError(_UFuncCastingError):
    in_i: Any
    def __init__(self, ufunc, casting, from_, to, i) -> None: ...

class _UFuncOutputCastingError(_UFuncCastingError):
    out_i: Any
    def __init__(self, ufunc, casting, from_, to, i) -> None: ...

class TooHardError(RuntimeError): ...

class AxisError(ValueError, IndexError):
    def __init__(self, axis, ndim: Any | None = ..., msg_prefix: Any | None = ...) -> None: ...

class _ArrayMemoryError(MemoryError):
    shape: Any
    dtype: Any
    def __init__(self, shape, dtype) -> None: ...
