from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

def kmc2_chain_initialization(distances, seed, name: Any | None = ...): ...

KMC2ChainInitialization: Any

def kmc2_chain_initialization_eager_fallback(distances, seed, name, ctx): ...
def kmeans_plus_plus_initialization(points, num_to_sample, seed, num_retries_per_sample, name: Any | None = ...): ...

KmeansPlusPlusInitialization: Any

def kmeans_plus_plus_initialization_eager_fallback(points, num_to_sample, seed, num_retries_per_sample, name, ctx): ...

class _NearestNeighborsOutput(NamedTuple):
    nearest_center_indices: Any
    nearest_center_distances: Any

def nearest_neighbors(points, centers, k, name: Any | None = ...): ...

NearestNeighbors: Any

def nearest_neighbors_eager_fallback(points, centers, k, name, ctx): ...
