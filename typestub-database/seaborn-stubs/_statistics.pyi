from typing import Any

class KDE:
    bw_method: Any
    bw_adjust: Any
    gridsize: Any
    cut: Any
    clip: Any
    cumulative: Any
    support: Any
    def __init__(self, *, bw_method: Any | None = ..., bw_adjust: int = ..., gridsize: int = ..., cut: int = ..., clip: Any | None = ..., cumulative: bool = ...) -> None: ...
    def define_support(self, x1, x2: Any | None = ..., weights: Any | None = ..., cache: bool = ...): ...
    def __call__(self, x1, x2: Any | None = ..., weights: Any | None = ...): ...

class Histogram:
    stat: Any
    bins: Any
    binwidth: Any
    binrange: Any
    discrete: Any
    cumulative: Any
    bin_kws: Any
    def __init__(self, stat: str = ..., bins: str = ..., binwidth: Any | None = ..., binrange: Any | None = ..., discrete: bool = ..., cumulative: bool = ...) -> None: ...
    def define_bin_params(self, x1, x2: Any | None = ..., weights: Any | None = ..., cache: bool = ...): ...
    def __call__(self, x1, x2: Any | None = ..., weights: Any | None = ...): ...

class ECDF:
    stat: Any
    complementary: Any
    def __init__(self, stat: str = ..., complementary: bool = ...) -> None: ...
    def __call__(self, x1, x2: Any | None = ..., weights: Any | None = ...): ...
