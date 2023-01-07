from statsmodels.compat.python import lzip as lzip
from statsmodels.stats.base import AllPairsResults as AllPairsResults, HolderTuple as HolderTuple
from statsmodels.tools.sm_exceptions import HypothesisTestWarning as HypothesisTestWarning
from statsmodels.tools.testing import Holder as Holder
from typing import Any

def proportion_confint(count, nobs, alpha: float = ..., method: str = ...): ...
def multinomial_proportions_confint(counts, alpha: float = ..., method: str = ...): ...
def samplesize_confint_proportion(proportion, half_length, alpha: float = ..., method: str = ...): ...
def proportion_effectsize(prop1, prop2, method: str = ...): ...
def std_prop(prop, nobs): ...
def binom_tost(count, nobs, low, upp): ...
def binom_tost_reject_interval(low, upp, nobs, alpha: float = ...): ...
def binom_test_reject_interval(value, nobs, alpha: float = ..., alternative: str = ...): ...
def binom_test(count, nobs, prop: float = ..., alternative: str = ...): ...
def power_binom_tost(low, upp, nobs, p_alt: Any | None = ..., alpha: float = ...): ...
def power_ztost_prop(low, upp, nobs, p_alt, alpha: float = ..., dist: str = ..., variance_prop: Any | None = ..., discrete: bool = ..., continuity: int = ..., critval_continuity: int = ...): ...
def proportions_ztest(count, nobs, value: Any | None = ..., alternative: str = ..., prop_var: bool = ...): ...
def proportions_ztost(count, nobs, low, upp, prop_var: str = ...): ...
def proportions_chisquare(count, nobs, value: Any | None = ...): ...
def proportions_chisquare_allpairs(count, nobs, multitest_method: str = ...): ...
def proportions_chisquare_pairscontrol(count, nobs, value: Any | None = ..., multitest_method: str = ..., alternative: str = ...): ...
def confint_proportions_2indep(count1, nobs1, count2, nobs2, method: Any | None = ..., compare: str = ..., alpha: float = ..., correction: bool = ...): ...
def score_test_proportions_2indep(count1, nobs1, count2, nobs2, value: Any | None = ..., compare: str = ..., alternative: str = ..., correction: bool = ..., return_results: bool = ...): ...
def test_proportions_2indep(count1, nobs1, count2, nobs2, value: Any | None = ..., method: Any | None = ..., compare: str = ..., alternative: str = ..., correction: bool = ..., return_results: bool = ...): ...
def tost_proportions_2indep(count1, nobs1, count2, nobs2, low, upp, method: Any | None = ..., compare: str = ..., correction: bool = ...): ...
def power_proportions_2indep(diff, prop2, nobs1, ratio: int = ..., alpha: float = ..., value: int = ..., alternative: str = ..., return_results: bool = ...): ...
def samplesize_proportions_2indep_onetail(diff, prop2, power, ratio: int = ..., alpha: float = ..., value: int = ..., alternative: str = ...): ...
