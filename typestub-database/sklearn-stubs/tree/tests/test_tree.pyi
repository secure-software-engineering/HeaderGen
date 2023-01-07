from sklearn import datasets as datasets, tree as tree
from sklearn.dummy import DummyRegressor as DummyRegressor
from sklearn.exceptions import NotFittedError as NotFittedError
from sklearn.metrics import accuracy_score as accuracy_score, mean_poisson_deviance as mean_poisson_deviance, mean_squared_error as mean_squared_error
from sklearn.model_selection import train_test_split as train_test_split
from sklearn.tree import DecisionTreeClassifier as DecisionTreeClassifier, DecisionTreeRegressor as DecisionTreeRegressor, ExtraTreeClassifier as ExtraTreeClassifier, ExtraTreeRegressor as ExtraTreeRegressor
from sklearn.tree._classes import CRITERIA_CLF as CRITERIA_CLF, CRITERIA_REG as CRITERIA_REG
from sklearn.tree._tree import NODE_DTYPE as NODE_DTYPE, TREE_LEAF as TREE_LEAF, TREE_UNDEFINED as TREE_UNDEFINED
from sklearn.utils import compute_sample_weight as compute_sample_weight
from sklearn.utils._testing import assert_almost_equal as assert_almost_equal, assert_array_almost_equal as assert_array_almost_equal, assert_array_equal as assert_array_equal, create_memmap_backed_data as create_memmap_backed_data, ignore_warnings as ignore_warnings, skip_if_32bit as skip_if_32bit
from sklearn.utils.estimator_checks import check_sample_weights_invariance as check_sample_weights_invariance
from sklearn.utils.validation import check_random_state as check_random_state
from typing import Any

CLF_CRITERIONS: Any
REG_CRITERIONS: Any
CLF_TREES: Any
REG_TREES: Any
ALL_TREES: dict
SPARSE_TREES: Any
X_small: Any
y_small: Any
y_small_reg: Any
X: Any
y: Any
T: Any
true_result: Any
iris: Any
rng: Any
perm: Any
diabetes: Any
digits: Any
random_state: Any
X_multilabel: Any
y_multilabel: Any
X_sparse_pos: Any
y_random: Any
X_sparse_mix: Any
DATASETS: Any

def assert_tree_equal(d, s, message) -> None: ...
def test_classification_toy() -> None: ...
def test_weighted_classification_toy() -> None: ...
def test_regression_toy(Tree, criterion) -> None: ...
def test_xor() -> None: ...
def test_iris() -> None: ...
def test_diabetes_overfit(name, Tree, criterion) -> None: ...
def test_diabetes_underfit(name, Tree, criterion, max_depth, metric, max_loss) -> None: ...
def test_probability() -> None: ...
def test_arrayrepr() -> None: ...
def test_pure_set() -> None: ...
def test_numerical_stability() -> None: ...
def test_importances() -> None: ...
def test_importances_raises() -> None: ...
def test_importances_gini_equal_squared_error() -> None: ...
def test_max_features() -> None: ...
def test_error() -> None: ...
def test_min_samples_split() -> None: ...
def test_min_samples_leaf() -> None: ...
def check_min_weight_fraction_leaf(name, datasets, sparse: bool = ...) -> None: ...
def test_min_weight_fraction_leaf_on_dense_input(name) -> None: ...
def test_min_weight_fraction_leaf_on_sparse_input(name) -> None: ...
def check_min_weight_fraction_leaf_with_min_samples_leaf(name, datasets, sparse: bool = ...) -> None: ...
def test_min_weight_fraction_leaf_with_min_samples_leaf_on_dense_input(name) -> None: ...
def test_min_weight_fraction_leaf_with_min_samples_leaf_on_sparse_input(name) -> None: ...
def test_min_impurity_decrease() -> None: ...
def test_multioutput() -> None: ...
def test_classes_shape() -> None: ...
def test_unbalanced_iris() -> None: ...
def test_memory_layout() -> None: ...
def test_sample_weight() -> None: ...
def test_sample_weight_invalid() -> None: ...
def check_class_weights(name) -> None: ...
def test_class_weights(name) -> None: ...
def check_class_weight_errors(name) -> None: ...
def test_class_weight_errors(name) -> None: ...
def test_max_leaf_nodes() -> None: ...
def test_max_leaf_nodes_max_depth() -> None: ...
def test_arrays_persist() -> None: ...
def test_only_constant_features() -> None: ...
def test_behaviour_constant_feature_after_splits() -> None: ...
def test_with_only_one_non_constant_features() -> None: ...
def test_big_input() -> None: ...
def test_realloc() -> None: ...
def test_huge_allocations() -> None: ...
def check_sparse_input(tree, dataset, max_depth: Any | None = ...) -> None: ...
def test_sparse_input(tree_type, dataset) -> None: ...
def test_sparse_input_reg_trees(tree_type, dataset) -> None: ...
def check_sparse_parameters(tree, dataset) -> None: ...
def check_sparse_criterion(tree, dataset) -> None: ...
def test_sparse(tree_type, dataset, check) -> None: ...
def check_explicit_sparse_zeros(tree, max_depth: int = ..., n_features: int = ...) -> None: ...
def test_explicit_sparse_zeros(tree_type) -> None: ...
def check_raise_error_on_1d_input(name) -> None: ...
def test_1d_input(name) -> None: ...
def check_min_weight_leaf_split_level(name) -> None: ...
def test_min_weight_leaf_split_level(name) -> None: ...
def check_public_apply(name) -> None: ...
def check_public_apply_sparse(name) -> None: ...
def test_public_apply_all_trees(name) -> None: ...
def test_public_apply_sparse_trees(name) -> None: ...
def test_decision_path_hardcoded() -> None: ...
def check_decision_path(name) -> None: ...
def test_decision_path(name) -> None: ...
def check_no_sparse_y_support(name) -> None: ...
def test_no_sparse_y_support(name) -> None: ...
def test_mae() -> None: ...
def test_criterion_copy(): ...
def test_empty_leaf_infinite_threshold() -> None: ...
def test_prune_tree_classifier_are_subtrees(criterion, dataset, tree_cls) -> None: ...
def test_prune_tree_regression_are_subtrees(criterion, dataset, tree_cls) -> None: ...
def test_prune_single_node_tree() -> None: ...
def assert_pruning_creates_subtree(estimator_cls, X, y, pruning_path) -> None: ...
def assert_is_subtree(tree, subtree) -> None: ...
def test_prune_tree_raises_negative_ccp_alpha() -> None: ...
def check_apply_path_readonly(name) -> None: ...
def test_apply_path_readonly_all_trees(name) -> None: ...
def test_balance_property(criterion, Tree) -> None: ...
def test_poisson_zero_nodes(seed) -> None: ...
def test_poisson_vs_mse() -> None: ...
def test_decision_tree_regressor_sample_weight_consistentcy(criterion) -> None: ...
def test_X_idx_sorted_deprecated(TreeEstimator) -> None: ...
def test_criterion_deprecated(Tree, old_criterion, new_criterion) -> None: ...
def test_n_features_deprecated(Tree) -> None: ...
def test_different_endianness_pickle(): ...
def test_different_endianness_joblib_pickle(): ...
def get_different_bitness_node_ndarray(node_ndarray): ...
def get_different_alignment_node_ndarray(node_ndarray): ...
def reduce_tree_with_different_bitness(tree): ...
def test_different_bitness_pickle(): ...
def test_different_bitness_joblib_pickle(): ...
def test_check_n_classes() -> None: ...
def test_check_value_ndarray() -> None: ...
def test_check_node_ndarray() -> None: ...
