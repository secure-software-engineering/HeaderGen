from sklearn.metrics.cluster import adjusted_mutual_info_score as adjusted_mutual_info_score, adjusted_rand_score as adjusted_rand_score, completeness_score as completeness_score, contingency_matrix as contingency_matrix, entropy as entropy, expected_mutual_information as expected_mutual_information, fowlkes_mallows_score as fowlkes_mallows_score, homogeneity_completeness_v_measure as homogeneity_completeness_v_measure, homogeneity_score as homogeneity_score, mutual_info_score as mutual_info_score, normalized_mutual_info_score as normalized_mutual_info_score, pair_confusion_matrix as pair_confusion_matrix, rand_score as rand_score, v_measure_score as v_measure_score
from sklearn.metrics.cluster._supervised import check_clusterings as check_clusterings
from sklearn.utils import assert_all_finite as assert_all_finite
from sklearn.utils._testing import assert_almost_equal as assert_almost_equal, ignore_warnings as ignore_warnings
from typing import Any

score_funcs: Any

def test_error_messages_on_wrong_input() -> None: ...
def test_generalized_average() -> None: ...
def test_perfect_matches() -> None: ...
def test_homogeneous_but_not_complete_labeling() -> None: ...
def test_complete_but_not_homogeneous_labeling() -> None: ...
def test_not_complete_and_not_homogeneous_labeling() -> None: ...
def test_beta_parameter() -> None: ...
def test_non_consecutive_labels() -> None: ...
def uniform_labelings_scores(score_func, n_samples, k_range, n_runs: int = ..., seed: int = ...): ...
def test_adjustment_for_chance() -> None: ...
def test_adjusted_mutual_info_score() -> None: ...
def test_expected_mutual_info_overflow() -> None: ...
def test_int_overflow_mutual_info_fowlkes_mallows_score() -> None: ...
def test_entropy() -> None: ...
def test_contingency_matrix() -> None: ...
def test_contingency_matrix_sparse() -> None: ...
def test_exactly_zero_info_score() -> None: ...
def test_v_measure_and_mutual_information(seed: int = ...) -> None: ...
def test_fowlkes_mallows_score() -> None: ...
def test_fowlkes_mallows_score_properties() -> None: ...
def test_mutual_info_score_positive_constant_label(labels_true, labels_pred) -> None: ...
def test_check_clustering_error() -> None: ...
def test_pair_confusion_matrix_fully_dispersed() -> None: ...
def test_pair_confusion_matrix_single_cluster() -> None: ...
def test_pair_confusion_matrix() -> None: ...
def test_rand_score_edge_cases(clustering1, clustering2) -> None: ...
def test_rand_score() -> None: ...
def test_adjusted_rand_score_overflow() -> None: ...
