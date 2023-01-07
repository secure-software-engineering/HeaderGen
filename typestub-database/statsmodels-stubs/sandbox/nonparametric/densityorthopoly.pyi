from typing import Any

sqr2: Any

class FPoly:
    order: Any
    domain: Any
    intdomain: Any
    def __init__(self, order) -> None: ...
    def __call__(self, x): ...

class F2Poly:
    order: Any
    domain: Any
    intdomain: Any
    offsetfactor: int
    def __init__(self, order) -> None: ...
    def __call__(self, x): ...

class ChebyTPoly:
    order: Any
    poly: Any
    domain: Any
    intdomain: Any
    offsetfactor: float
    def __init__(self, order) -> None: ...
    def __call__(self, x): ...

logpi2: Any

class HPoly:
    order: Any
    poly: Any
    domain: Any
    offsetfactor: float
    def __init__(self, order) -> None: ...
    def __call__(self, x): ...

def polyvander(x, polybase, order: int = ...): ...
def inner_cont(polys, lower, upper, weight: Any | None = ...): ...
def is_orthonormal_cont(polys, lower, upper, rtol: int = ..., atol: float = ...): ...

class DensityOrthoPoly:
    polybase: Any
    polys: Any
    def __init__(self, polybase: Any | None = ..., order: int = ...) -> None: ...
    offsetfac: Any
    offset: Any
    shrink: Any
    shift: Any
    x: Any
    coeffs: Any
    def fit(self, x, polybase: Any | None = ..., order: int = ..., limits: Any | None = ...): ...
    def evaluate(self, xeval, order: Any | None = ...): ...
    def __call__(self, xeval): ...

def density_orthopoly(x, polybase, order: int = ..., xeval: Any | None = ...): ...
