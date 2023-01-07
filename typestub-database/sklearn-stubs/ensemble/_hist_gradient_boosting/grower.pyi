from ._bitset import set_raw_bitset_from_binned_bitset as set_raw_bitset_from_binned_bitset
from .common import MonotonicConstraint as MonotonicConstraint, PREDICTOR_RECORD_DTYPE as PREDICTOR_RECORD_DTYPE, X_BITSET_INNER_DTYPE as X_BITSET_INNER_DTYPE, Y_DTYPE as Y_DTYPE
from .histogram import HistogramBuilder as HistogramBuilder
from .predictor import TreePredictor as TreePredictor
from .splitting import Splitter as Splitter
from .utils import sum_parallel as sum_parallel
from typing import Any

EPS: Any

class TreeNode:
    split_info: Any
    left_child: Any
    right_child: Any
    histograms: Any
    partition_start: int
    partition_stop: int
    depth: Any
    sample_indices: Any
    n_samples: Any
    sum_gradients: Any
    sum_hessians: Any
    value: Any
    is_leaf: bool
    def __init__(self, depth, sample_indices, sum_gradients, sum_hessians, value: Any | None = ...) -> None: ...
    children_lower_bound: Any
    children_upper_bound: Any
    def set_children_bounds(self, lower, upper) -> None: ...
    def __lt__(self, other_node): ...

class TreeGrower:
    with_monotonic_cst: bool
    histogram_builder: Any
    splitter: Any
    n_bins_non_missing: Any
    missing_values_bin_idx: Any
    max_leaf_nodes: Any
    has_missing_values: Any
    monotonic_cst: Any
    is_categorical: Any
    l2_regularization: Any
    n_features: Any
    max_depth: Any
    min_samples_leaf: Any
    X_binned: Any
    min_gain_to_split: Any
    shrinkage: Any
    n_threads: Any
    splittable_nodes: Any
    finalized_leaves: Any
    total_find_split_time: float
    total_compute_hist_time: float
    total_apply_split_time: float
    n_categorical_splits: int
    n_nodes: int
    def __init__(self, X_binned, gradients, hessians, max_leaf_nodes: Any | None = ..., max_depth: Any | None = ..., min_samples_leaf: int = ..., min_gain_to_split: float = ..., n_bins: int = ..., n_bins_non_missing: Any | None = ..., has_missing_values: bool = ..., is_categorical: Any | None = ..., monotonic_cst: Any | None = ..., l2_regularization: float = ..., min_hessian_to_split: float = ..., shrinkage: float = ..., n_threads: Any | None = ...) -> None: ...
    def grow(self) -> None: ...
    def split_next(self): ...
    def make_predictor(self, binning_thresholds): ...
