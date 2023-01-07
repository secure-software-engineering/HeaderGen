from scipy import stats
from typing import Any

__date__: str

class MaxDist(stats.rv_continuous):
    dist: Any
    n: Any
    def __init__(self, dist, n) -> None: ...

maxdistr: Any
