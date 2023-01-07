from .try_ols_anova import data2dummy as data2dummy
from statsmodels.compat.python import lmap as lmap
from statsmodels.regression.linear_model import OLS as OLS
from statsmodels.tools.tools import add_constant as add_constant
from typing import Any

filenameli: Any

def getnist(filename): ...
def anova_oneway(y, x, seq: int = ...): ...
def anova_ols(y, x): ...
