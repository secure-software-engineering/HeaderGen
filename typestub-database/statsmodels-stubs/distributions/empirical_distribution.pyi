from typing import Any

class StepFunction:
    side: Any
    x: Any
    y: Any
    n: Any
    def __init__(self, x, y, ival: float = ..., sorted: bool = ..., side: str = ...) -> None: ...
    def __call__(self, time): ...

class ECDF(StepFunction):
    def __init__(self, x, side: str = ...) -> None: ...

def monotone_fn_inverter(fn, x, vectorized: bool = ..., **keywords): ...
