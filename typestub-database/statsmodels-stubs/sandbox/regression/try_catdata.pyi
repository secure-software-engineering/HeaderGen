from statsmodels.compat.python import lrange as lrange
from typing import Any

def labelmeanfilter(y, x): ...
def labelmeanfilter_nd(y, x): ...
def labelmeanfilter_str(ys, x): ...
def groupstatsbin(factors, values): ...
def convertlabels(ys, indices: Any | None = ...): ...
def groupsstats_1d(y, x, labelsunique): ...
def cat2dummy(y, nonseq: int = ...): ...
def groupsstats_dummy(y, x, nonseq: int = ...): ...
