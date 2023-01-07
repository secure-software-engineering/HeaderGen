from statsmodels.base.model import GenericLikelihoodModel as GenericLikelihoodModel
from statsmodels.datasets import sunspots as sunspots
from statsmodels.tsa.arima_process import ArmaProcess as ArmaProcess, arma_acovf as arma_acovf, arma_generate_sample as arma_generate_sample

def mvn_loglike_sum(x, sigma): ...
def mvn_loglike(x, sigma): ...
def mvn_loglike_chol(x, sigma): ...
def mvn_nloglike_obs(x, sigma): ...
def invertibleroots(ma): ...
def getpoly(self, params): ...

class MLEGLS(GenericLikelihoodModel):
    def loglike(self, params): ...
    def fit_invertible(self, *args, **kwds): ...
