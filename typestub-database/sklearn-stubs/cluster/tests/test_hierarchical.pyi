from sklearn.cluster import AgglomerativeClustering as AgglomerativeClustering, FeatureAgglomeration as FeatureAgglomeration, ward_tree as ward_tree
from sklearn.cluster._agglomerative import linkage_tree as linkage_tree
from sklearn.cluster._hierarchical_fast import average_merge as average_merge, max_merge as max_merge, mst_linkage_core as mst_linkage_core
from sklearn.datasets import make_circles as make_circles, make_moons as make_moons
from sklearn.feature_extraction.image import grid_to_graph as grid_to_graph
from sklearn.metrics import DistanceMetric as DistanceMetric
from sklearn.metrics.cluster import adjusted_rand_score as adjusted_rand_score, normalized_mutual_info_score as normalized_mutual_info_score
from sklearn.metrics.pairwise import PAIRED_DISTANCES as PAIRED_DISTANCES, cosine_distances as cosine_distances, manhattan_distances as manhattan_distances, pairwise_distances as pairwise_distances
from sklearn.metrics.tests.test_dist_metrics import METRICS_DEFAULT_PARAMS as METRICS_DEFAULT_PARAMS
from sklearn.neighbors import kneighbors_graph as kneighbors_graph
from sklearn.utils._fast_dict import IntFloatDict as IntFloatDict
from sklearn.utils._testing import assert_almost_equal as assert_almost_equal, assert_array_almost_equal as assert_array_almost_equal, assert_array_equal as assert_array_equal, create_memmap_backed_data as create_memmap_backed_data, ignore_warnings as ignore_warnings

def test_linkage_misc() -> None: ...
def test_structured_linkage_tree() -> None: ...
def test_unstructured_linkage_tree() -> None: ...
def test_height_linkage_tree() -> None: ...
def test_agglomerative_clustering_wrong_arg_memory() -> None: ...
def test_zero_cosine_linkage_tree() -> None: ...
def test_agglomerative_clustering_distances(n_clusters, compute_distances, distance_threshold, linkage) -> None: ...
def test_agglomerative_clustering() -> None: ...
def test_agglomerative_clustering_memory_mapped() -> None: ...
def test_ward_agglomeration() -> None: ...
def test_single_linkage_clustering() -> None: ...
def assess_same_labelling(cut1, cut2) -> None: ...
def test_sparse_scikit_vs_scipy() -> None: ...
def test_vector_scikit_single_vs_scipy_single(seed) -> None: ...
def test_mst_linkage_core_memory_mapped(metric_param_grid) -> None: ...
def test_identical_points() -> None: ...
def test_connectivity_propagation() -> None: ...
def test_ward_tree_children_order() -> None: ...
def test_ward_linkage_tree_return_distance() -> None: ...
def test_connectivity_fixing_non_lil() -> None: ...
def test_int_float_dict() -> None: ...
def test_connectivity_callable() -> None: ...
def test_connectivity_ignores_diagonal() -> None: ...
def test_compute_full_tree() -> None: ...
def test_n_components() -> None: ...
def test_agg_n_clusters() -> None: ...
def test_affinity_passed_to_fix_connectivity(): ...
def test_agglomerative_clustering_with_distance_threshold(linkage) -> None: ...
def test_small_distance_threshold() -> None: ...
def test_cluster_distances_with_distance_threshold() -> None: ...
def test_agglomerative_clustering_with_distance_threshold_edge_case(linkage, threshold, y_true) -> None: ...
def test_dist_threshold_invalid_parameters() -> None: ...
def test_invalid_shape_precomputed_dist_matrix() -> None: ...
def test_precomputed_connectivity_affinity_with_2_connected_components() -> None: ...
