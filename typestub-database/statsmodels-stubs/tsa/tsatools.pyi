from statsmodels.compat.python import Literal
from typing import Any

def add_trend(x, trend: str = ..., prepend: bool = ..., has_constant: str = ...): ...
def lagmat(x, maxlag: int, trim: Any = ..., original: Any = ..., use_pandas: bool = ...): ...
def lagmat2ds(x, maxlag0, maxlagex: Any | None = ..., dropex: int = ..., trim: str = ..., use_pandas: bool = ...): ...
def vec(mat): ...
def vech(mat): ...
def unvec(v): ...
def unvech(v): ...
def duplication_matrix(n): ...
def elimination_matrix(n): ...
def commutation_matrix(p, q): ...
def freq_to_period(freq): ...
def rename_trend(trend: str): ...
