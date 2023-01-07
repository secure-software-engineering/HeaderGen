import abc
from pandas.core.computation.align import align_terms as align_terms, reconstruct_object as reconstruct_object
from pandas.core.computation.expr import Expr as Expr
from pandas.core.computation.ops import MATHOPS as MATHOPS, REDUCTIONS as REDUCTIONS
from typing import Union, Any

class NumExprClobberingError(NameError): ...

class AbstractEngine(metaclass=abc.ABCMeta):
    has_neg_frac: bool
    expr: Any
    aligned_axes: Any
    result_type: Any
    def __init__(self, expr) -> None: ...
    def convert(self) -> str: ...
    def evaluate(self) -> object: ...

class NumExprEngine(AbstractEngine):
    has_neg_frac: bool

class PythonEngine(AbstractEngine):
    has_neg_frac: bool
    def evaluate(self): ...

ENGINES: dict[str, type[AbstractEngine]]
