from .axisgrid import Grid
from typing import Any

class _HeatMapper:
    xticks: Any
    xticklabels: Any
    yticks: Any
    yticklabels: Any
    xlabel: Any
    ylabel: Any
    data: Any
    plot_data: Any
    annot: Any
    annot_data: Any
    fmt: Any
    annot_kws: Any
    cbar: Any
    cbar_kws: Any
    def __init__(self, data, vmin, vmax, cmap, center, robust, annot, fmt, annot_kws, cbar, cbar_kws, xticklabels: bool = ..., yticklabels: bool = ..., mask: Any | None = ...) -> None: ...
    def plot(self, ax, cax, kws) -> None: ...

def heatmap(data, *, vmin: Any | None = ..., vmax: Any | None = ..., cmap: Any | None = ..., center: Any | None = ..., robust: bool = ..., annot: Any | None = ..., fmt: str = ..., annot_kws: Any | None = ..., linewidths: int = ..., linecolor: str = ..., cbar: bool = ..., cbar_kws: Any | None = ..., cbar_ax: Any | None = ..., square: bool = ..., xticklabels: str = ..., yticklabels: str = ..., mask: Any | None = ..., ax: Any | None = ..., **kwargs): ...

class _DendrogramPlotter:
    axis: Any
    array: Any
    data: Any
    shape: Any
    metric: Any
    method: Any
    label: Any
    rotate: Any
    linkage: Any
    dendrogram: Any
    xticks: Any
    yticks: Any
    xticklabels: Any
    yticklabels: Any
    ylabel: Any
    xlabel: str
    dependent_coord: Any
    independent_coord: Any
    def __init__(self, data, linkage, metric, method, axis, label, rotate) -> None: ...
    @property
    def calculated_linkage(self): ...
    def calculate_dendrogram(self): ...
    @property
    def reordered_ind(self): ...
    def plot(self, ax, tree_kws): ...

class ClusterGrid(Grid):
    data: Any
    data2d: Any
    mask: Any
    gs: Any
    ax_row_dendrogram: Any
    ax_col_dendrogram: Any
    ax_row_colors: Any
    ax_col_colors: Any
    ax_heatmap: Any
    ax_cbar: Any
    cax: Any
    cbar_pos: Any
    dendrogram_row: Any
    dendrogram_col: Any
    def __init__(self, data, pivot_kws: Any | None = ..., z_score: Any | None = ..., standard_scale: Any | None = ..., figsize: Any | None = ..., row_colors: Any | None = ..., col_colors: Any | None = ..., mask: Any | None = ..., dendrogram_ratio: Any | None = ..., colors_ratio: Any | None = ..., cbar_pos: Any | None = ...) -> None: ...
    def format_data(self, data, pivot_kws, z_score: Any | None = ..., standard_scale: Any | None = ...): ...
    @staticmethod
    def z_score(data2d, axis: int = ...): ...
    @staticmethod
    def standard_scale(data2d, axis: int = ...): ...
    def dim_ratios(self, colors, dendrogram_ratio, colors_ratio): ...
    @staticmethod
    def color_list_to_matrix_and_cmap(colors, ind, axis: int = ...): ...
    def plot_dendrograms(self, row_cluster, col_cluster, metric, method, row_linkage, col_linkage, tree_kws) -> None: ...
    def plot_colors(self, xind, yind, **kws) -> None: ...
    def plot_matrix(self, colorbar_kws, xind, yind, **kws) -> None: ...
    def plot(self, metric, method, colorbar_kws, row_cluster, col_cluster, row_linkage, col_linkage, tree_kws, **kws): ...

def clustermap(data, *, pivot_kws: Any | None = ..., method: str = ..., metric: str = ..., z_score: Any | None = ..., standard_scale: Any | None = ..., figsize=..., cbar_kws: Any | None = ..., row_cluster: bool = ..., col_cluster: bool = ..., row_linkage: Any | None = ..., col_linkage: Any | None = ..., row_colors: Any | None = ..., col_colors: Any | None = ..., mask: Any | None = ..., dendrogram_ratio: float = ..., colors_ratio: float = ..., cbar_pos=..., tree_kws: Any | None = ..., **kwargs): ...
