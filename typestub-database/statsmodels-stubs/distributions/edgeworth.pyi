from scipy.stats import rv_continuous

def cumulant_from_moments(momt, n): ...

class ExpandedNormal(rv_continuous):
    def __init__(self, cum, name: str = ..., **kwds): ...
