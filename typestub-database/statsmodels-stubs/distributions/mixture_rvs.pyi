from typing import Any

def mixture_rvs(prob, size, dist, kwargs: Any | None = ...): ...

class MixtureDistribution:
    def rvs(self, prob, size, dist, kwargs: Any | None = ...): ...
    def pdf(self, x, prob, dist, kwargs: Any | None = ...): ...
    def cdf(self, x, prob, dist, kwargs: Any | None = ...): ...

def mv_mixture_rvs(prob, size, dist, nvars, **kwargs): ...
