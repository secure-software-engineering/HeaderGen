from typing import Any

def aitchison_aitken(h, Xi, x, num_levels: Any | None = ...): ...
def wang_ryzin(h, Xi, x): ...
def gaussian(h, Xi, x): ...
def tricube(h, Xi, x): ...
def gaussian_convolution(h, Xi, x): ...
def wang_ryzin_convolution(h, Xi, Xj): ...
def aitchison_aitken_convolution(h, Xi, Xj): ...
def gaussian_cdf(h, Xi, x): ...
def aitchison_aitken_cdf(h, Xi, x_u): ...
def wang_ryzin_cdf(h, Xi, x_u): ...
def d_gaussian(h, Xi, x): ...
def aitchison_aitken_reg(h, Xi, x): ...
def wang_ryzin_reg(h, Xi, x): ...
