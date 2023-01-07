from . import DecisionTreeClassifier as DecisionTreeClassifier
from ..base import is_classifier as is_classifier
from ..utils.validation import check_is_fitted as check_is_fitted
from ._reingold_tilford import Tree as Tree, buchheim as buchheim
from typing import Any

class Sentinel: ...

SENTINEL: Any

def plot_tree(decision_tree, *, max_depth: Any | None = ..., feature_names: Any | None = ..., class_names: Any | None = ..., label: str = ..., filled: bool = ..., impurity: bool = ..., node_ids: bool = ..., proportion: bool = ..., rounded: bool = ..., precision: int = ..., ax: Any | None = ..., fontsize: Any | None = ...): ...

class _BaseTreeExporter:
    max_depth: Any
    feature_names: Any
    class_names: Any
    label: Any
    filled: Any
    impurity: Any
    node_ids: Any
    proportion: Any
    rounded: Any
    precision: Any
    fontsize: Any
    def __init__(self, max_depth: Any | None = ..., feature_names: Any | None = ..., class_names: Any | None = ..., label: str = ..., filled: bool = ..., impurity: bool = ..., node_ids: bool = ..., proportion: bool = ..., rounded: bool = ..., precision: int = ..., fontsize: Any | None = ...) -> None: ...
    def get_color(self, value): ...
    def get_fill_color(self, tree, node_id): ...
    def node_to_str(self, tree, node_id, criterion): ...

class _DOTTreeExporter(_BaseTreeExporter):
    leaves_parallel: Any
    out_file: Any
    special_characters: Any
    fontname: Any
    rotate: Any
    characters: Any
    ranks: Any
    colors: Any
    def __init__(self, out_file=..., max_depth: Any | None = ..., feature_names: Any | None = ..., class_names: Any | None = ..., label: str = ..., filled: bool = ..., leaves_parallel: bool = ..., impurity: bool = ..., node_ids: bool = ..., proportion: bool = ..., rotate: bool = ..., rounded: bool = ..., special_characters: bool = ..., precision: int = ..., fontname: str = ...) -> None: ...
    def export(self, decision_tree) -> None: ...
    def tail(self) -> None: ...
    def head(self) -> None: ...
    def recurse(self, tree, node_id, criterion, parent: Any | None = ..., depth: int = ...) -> None: ...

class _MPLTreeExporter(_BaseTreeExporter):
    fontsize: Any
    ranks: Any
    colors: Any
    characters: Any
    bbox_args: Any
    arrow_args: Any
    def __init__(self, max_depth: Any | None = ..., feature_names: Any | None = ..., class_names: Any | None = ..., label: str = ..., filled: bool = ..., impurity: bool = ..., node_ids: bool = ..., proportion: bool = ..., rounded: bool = ..., precision: int = ..., fontsize: Any | None = ...) -> None: ...
    def export(self, decision_tree, ax: Any | None = ...): ...
    def recurse(self, node, tree, ax, max_x, max_y, depth: int = ...) -> None: ...

def export_graphviz(decision_tree, out_file: Any | None = ..., *, max_depth: Any | None = ..., feature_names: Any | None = ..., class_names: Any | None = ..., label: str = ..., filled: bool = ..., leaves_parallel: bool = ..., impurity: bool = ..., node_ids: bool = ..., proportion: bool = ..., rotate: bool = ..., rounded: bool = ..., special_characters: bool = ..., precision: int = ..., fontname: str = ...): ...
def export_text(decision_tree, *, feature_names: Any | None = ..., max_depth: int = ..., spacing: int = ..., decimals: int = ..., show_weights: bool = ...): ...
