from typing import Any

class TryCLogit:
    endog: Any
    exog_bychoices: Any
    ncommon: Any
    nchoices: Any
    beta_indices: Any
    def __init__(self, endog, exog_bychoices, ncommon) -> None: ...
    def xbetas(self, params): ...
    def loglike(self, params): ...
    def fit(self, start_params: Any | None = ...): ...

class TryNCLogit:
    endog: Any
    exog_bychoices: Any
    ncommon: Any
    nchoices: Any
    beta_indices: Any
    def __init__(self, endog, exog_bychoices, ncommon) -> None: ...
    def xbetas(self, params): ...
    def loglike_leafbranch(self, params, tau): ...
    def loglike_branch(self, params, tau) -> None: ...

testxb: int

class RU2NMNL:
    endog: Any
    datadict: Any
    tree: Any
    paramsind: Any
    branchsum: str
    probs: Any
    def __init__(self, endog, exog, tree, paramsind) -> None: ...
    def calc_prob(self, tree, keys: Any | None = ...): ...

dta: Any
endog: Any
nobs: Any
nchoices: Any
datafloat: Any
exog: Any
varnames: Any
modes: Any
exog_choice_names: Any
exog_choice: Any
exog_individual: Any
choice_index: Any
hinca: Any
dta2: Any
xi: Any
dta1: Any
xivar: Any
ncommon: int
betaind: Any
zi: Any
z: Any
betaindices: Any
beta: Any
betai: Any
xifloat: Any
clogit: Any
debug: int
res: Any
tab2324: Any
res2: Any
res3: Any
res3corr: Any
tree0: Any
datadict: Any
paramsind: Any
modru: Any
