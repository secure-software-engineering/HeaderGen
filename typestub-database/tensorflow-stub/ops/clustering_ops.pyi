from tensorflow.python.ops.gen_clustering_ops import *
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, gen_clustering_ops as gen_clustering_ops, math_ops as math_ops, nn_impl as nn_impl, random_ops as random_ops, state_ops as state_ops, variable_scope as variable_scope
from tensorflow.python.ops.embedding_ops import embedding_lookup as embedding_lookup

SQUARED_EUCLIDEAN_DISTANCE: str
COSINE_DISTANCE: str
RANDOM_INIT: str
KMEANS_PLUS_PLUS_INIT: str
KMC2_INIT: str
CLUSTERS_VAR_NAME: str

class KMeans:
    def __init__(self, inputs, num_clusters, initial_clusters=..., distance_metric=..., use_mini_batch: bool = ..., mini_batch_steps_per_iteration: int = ..., random_seed: int = ..., kmeans_plus_plus_num_retries: int = ..., kmc2_chain_length: int = ...) -> None: ...
    def training_graph(self): ...

class _InitializeClustersOpFactory:
    def __init__(self, inputs, num_clusters, initial_clusters, distance_metric, random_seed, kmeans_plus_plus_num_retries, kmc2_chain_length, cluster_centers, cluster_centers_updated, cluster_centers_initialized) -> None: ...
    def op(self): ...
