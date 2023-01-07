from statsmodels.compat.python import lmap as lmap
from statsmodels.regression.linear_model import OLS as OLS
from typing import Any

dt_b: Any
dta: Any
mask: Any
vars: Any
datavarnames: Any
dta_use: Any
keeprows: Any
dta_used: Any
varsused: Any

def data2dummy(x, returnall: bool = ...): ...
def data2proddummy(x): ...
def data2groupcont(x1, x2): ...

sexdummy: Any
factors: Any
products: Any
X_b0: Any
y_b0: Any
res_b0: Any
anova_str0: str
anova_str: str

def anovadict(res): ...

X2: Any
res2: Any
X3: Any
res3: Any

def form2design(ss, data): ...

nobs: int
testdataint: Any
testdatacont: Any
dt2: Any
testdata: Any
xx: Any
n: Any
names: Any
X: Any
y: Any
rest1: Any

def dropname(ss, li): ...

m: Any
droprows: Any
dta_use_b1: Any
xx_b1: Any
names_b1: Any
X_b1: Any
y_b1: Any
rest_b1: Any
allexog: Any
xx_b1a: Any
names_b1a: Any
X_b1a: Any
y_b1a: Any
rest_b1a: Any
X_b1a_: Any
y_b1a_: Any
rest_b1a_: Any
