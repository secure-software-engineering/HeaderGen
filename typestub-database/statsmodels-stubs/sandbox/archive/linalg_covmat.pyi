from .linalg_decomp_1 import SvdArray as SvdArray
from typing import Any

sqrt2pi: Any
logsqrt2pi: Any

class StandardNormal:
    def rvs(self, size): ...
    def pdf(self, x): ...
    def logpdf(self, x): ...

class AffineTransform:
    const: Any
    tmat: Any
    dist: Any
    nrv: Any
    tmatinv: Any
    absdet: Any
    logabsdet: Any
    def __init__(self, const, tmat, dist) -> None: ...
    def rvs(self, size): ...
    def transform(self, x): ...
    def invtransform(self, y): ...
    def pdf(self, x): ...
    def logpdf(self, x): ...

class MultivariateNormalChol:
    mean: Any
    sigma: Any
    sigmainv: Any
    cholsigma: Any
    cholsigmainv: Any
    def __init__(self, mean, sigma) -> None: ...
    def whiten(self, x): ...
    def logpdf_obs(self, x): ...
    def logpdf(self, x): ...
    def pdf(self, x): ...

class MultivariateNormal:
    mean: Any
    sigma: Any
    def __init__(self, mean, sigma) -> None: ...

def loglike_ar1(x, rho): ...
def ar2transform(x, arcoefs): ...
def mvn_loglike(x, sigma): ...
def mvn_nloglike_obs(x, sigma): ...

nobs: int
x: Any
autocov: Any
sigma: Any
cholsigma: Any
sigmainv: Any
cholsigmainv: Any
x_whitened: Any
logdetsigma: Any
sigma2: float
llike: Any
ll: Any
ls: Any
normtransf: Any
mch: Any
xw: Any
