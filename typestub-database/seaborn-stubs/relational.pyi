from ._core import VectorPlotter
from typing import Any

class _RelationalPlotter(VectorPlotter):
    wide_structure: Any
    sort: bool
    legend_title: Any
    legend_data: Any
    legend_order: Any
    def add_legend_data(self, ax) -> None: ...

class _LinePlotter(_RelationalPlotter):
    estimator: Any
    ci: Any
    n_boot: Any
    seed: Any
    sort: Any
    err_style: Any
    err_kws: Any
    legend: Any
    def __init__(self, *, data: Any | None = ..., variables=..., estimator: Any | None = ..., ci: Any | None = ..., n_boot: Any | None = ..., seed: Any | None = ..., sort: bool = ..., err_style: Any | None = ..., err_kws: Any | None = ..., legend: Any | None = ...) -> None: ...
    def aggregate(self, vals, grouper, units: Any | None = ...): ...
    def plot(self, ax, kws) -> None: ...

class _ScatterPlotter(_RelationalPlotter):
    alpha: Any
    legend: Any
    def __init__(self, *, data: Any | None = ..., variables=..., x_bins: Any | None = ..., y_bins: Any | None = ..., estimator: Any | None = ..., ci: Any | None = ..., n_boot: Any | None = ..., alpha: Any | None = ..., x_jitter: Any | None = ..., y_jitter: Any | None = ..., legend: Any | None = ...) -> None: ...
    def plot(self, ax, kws) -> None: ...

def lineplot(*, x: Any | None = ..., y: Any | None = ..., hue: Any | None = ..., size: Any | None = ..., style: Any | None = ..., data: Any | None = ..., palette: Any | None = ..., hue_order: Any | None = ..., hue_norm: Any | None = ..., sizes: Any | None = ..., size_order: Any | None = ..., size_norm: Any | None = ..., dashes: bool = ..., markers: Any | None = ..., style_order: Any | None = ..., units: Any | None = ..., estimator: str = ..., ci: int = ..., n_boot: int = ..., seed: Any | None = ..., sort: bool = ..., err_style: str = ..., err_kws: Any | None = ..., legend: str = ..., ax: Any | None = ..., **kwargs): ...
def scatterplot(*, x: Any | None = ..., y: Any | None = ..., hue: Any | None = ..., style: Any | None = ..., size: Any | None = ..., data: Any | None = ..., palette: Any | None = ..., hue_order: Any | None = ..., hue_norm: Any | None = ..., sizes: Any | None = ..., size_order: Any | None = ..., size_norm: Any | None = ..., markers: bool = ..., style_order: Any | None = ..., x_bins: Any | None = ..., y_bins: Any | None = ..., units: Any | None = ..., estimator: Any | None = ..., ci: int = ..., n_boot: int = ..., alpha: Any | None = ..., x_jitter: Any | None = ..., y_jitter: Any | None = ..., legend: str = ..., ax: Any | None = ..., **kwargs): ...
def relplot(*, x: Any | None = ..., y: Any | None = ..., hue: Any | None = ..., size: Any | None = ..., style: Any | None = ..., data: Any | None = ..., row: Any | None = ..., col: Any | None = ..., col_wrap: Any | None = ..., row_order: Any | None = ..., col_order: Any | None = ..., palette: Any | None = ..., hue_order: Any | None = ..., hue_norm: Any | None = ..., sizes: Any | None = ..., size_order: Any | None = ..., size_norm: Any | None = ..., markers: Any | None = ..., dashes: Any | None = ..., style_order: Any | None = ..., legend: str = ..., kind: str = ..., height: int = ..., aspect: int = ..., facet_kws: Any | None = ..., units: Any | None = ..., **kwargs): ...
