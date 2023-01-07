from statsmodels.compat.python import lrange as lrange
from typing import Any

def randintw(w, size: int = ...): ...
def getbranches(tree): ...
def getnodes(tree): ...

testxb: int

class RU2NMNL:
    endog: Any
    datadict: Any
    tree: Any
    paramsind: Any
    branchsum: str
    probs: Any
    probstxt: Any
    branchleaves: Any
    branchvalues: Any
    branchsums: Any
    bprobs: Any
    nbranches: Any
    paramsnames: Any
    nparams: Any
    paramsidx: Any
    parinddict: Any
    recursionparams: Any
    def __init__(self, endog, exog, tree, paramsind) -> None: ...
    def get_probs(self, params): ...
    def calc_prob(self, tree, parent: Any | None = ...): ...
