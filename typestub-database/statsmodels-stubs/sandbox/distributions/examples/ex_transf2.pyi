from statsmodels.sandbox.distributions.extras import ExpTransf_gen as ExpTransf_gen, LogTransf_gen as LogTransf_gen, absnormalg as absnormalg, negsquarenormalg as negsquarenormalg, squarenormalg as squarenormalg, squaretg as squaretg
from typing import Any

l: Any
s: Any
ppfq: Any
xx: Any
nxx: Any

def test_loggamma() -> None: ...
def test_loglaplace() -> None: ...

class CheckDistEquivalence:
    def test_cdf(self) -> None: ...
    def test_pdf(self) -> None: ...
    def test_ppf(self) -> None: ...
    def test_rvs(self) -> None: ...
    def test_stats(self) -> None: ...

class TestLoggamma_1(CheckDistEquivalence):
    dist: Any
    trargs: Any
    trkwds: Any
    statsdist: Any
    stargs: Any
    stkwds: Any
    def __init__(self) -> None: ...

class TestSquaredNormChi2_1(CheckDistEquivalence):
    dist: Any
    trargs: Any
    trkwds: Any
    statsdist: Any
    stargs: Any
    stkwds: Any
    def __init__(self) -> None: ...

class TestSquaredNormChi2_2(CheckDistEquivalence):
    dist: Any
    trargs: Any
    trkwds: Any
    statsdist: Any
    stargs: Any
    stkwds: Any
    def __init__(self) -> None: ...

class TestAbsNormHalfNorm(CheckDistEquivalence):
    dist: Any
    trargs: Any
    trkwds: Any
    statsdist: Any
    stargs: Any
    stkwds: Any
    def __init__(self) -> None: ...

class TestSquaredTF(CheckDistEquivalence):
    dist: Any
    trargs: Any
    trkwds: Any
    statsdist: Any
    stargs: Any
    stkwds: Any
    def __init__(self) -> None: ...

def test_squared_normal_chi2() -> None: ...
