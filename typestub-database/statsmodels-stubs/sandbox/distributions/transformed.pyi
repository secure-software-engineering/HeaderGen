from scipy.stats import distributions
from typing import Any

def get_u_argskwargs(**kwargs): ...

class Transf_gen(distributions.rv_continuous):
    func: Any
    funcinv: Any
    numargs: Any
    decr: Any
    kls: Any
    def __init__(self, kls, func, funcinv, *args, **kwargs) -> None: ...

def inverse(x): ...

mux: Any
stdx: Any

def inversew(x): ...
def inversew_inv(x): ...
def identit(x): ...

invdnormalg: Any
lognormalg: Any
loggammaexpg: Any

class ExpTransf_gen(distributions.rv_continuous):
    numargs: Any
    kls: Any
    def __init__(self, kls, *args, **kwargs) -> None: ...

class LogTransf_gen(distributions.rv_continuous):
    numargs: Any
    kls: Any
    def __init__(self, kls, *args, **kwargs) -> None: ...

def examples_transf() -> None: ...

class TransfTwo_gen(distributions.rv_continuous):
    func: Any
    funcinvplus: Any
    funcinvminus: Any
    derivplus: Any
    derivminus: Any
    numargs: Any
    shape: Any
    kls: Any
    def __init__(self, kls, func, funcinvplus, funcinvminus, derivplus, derivminus, *args, **kwargs) -> None: ...

class SquareFunc:
    def inverseplus(self, x): ...
    def inverseminus(self, x): ...
    def derivplus(self, x): ...
    def derivminus(self, x): ...
    def squarefunc(self, x): ...

sqfunc: Any
squarenormalg: Any
squaretg: Any

def inverseplus(x): ...
def inverseminus(x): ...
def derivplus(x): ...
def derivminus(x): ...
def negsquarefunc(x): ...

negsquarenormalg: Any

def absfunc(x): ...

absnormalg: Any
