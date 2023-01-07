from statsmodels.compat.python import lmap as lmap, lzip as lzip
from typing import Any

def logsumexp(a, axis: Any | None = ...): ...
def discretize(X, method: str = ..., nbins: Any | None = ...): ...
def logbasechange(a, b): ...
def natstobits(X): ...
def bitstonats(X): ...
def shannonentropy(px, logbase: int = ...): ...
def shannoninfo(px, logbase: int = ...): ...
def condentropy(px, py, pxpy: Any | None = ..., logbase: int = ...): ...
def mutualinfo(px, py, pxpy, logbase: int = ...): ...
def corrent(px, py, pxpy, logbase: int = ...): ...
def covent(px, py, pxpy, logbase: int = ...): ...
def renyientropy(px, alpha: int = ..., logbase: int = ..., measure: str = ...): ...
def gencrossentropy(px, py, pxpy, alpha: int = ..., logbase: int = ..., measure: str = ...) -> None: ...
