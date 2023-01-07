from ..base import BaseEstimator, BiclusterMixin
from abc import ABCMeta, abstractmethod
from typing import Any

class BaseSpectral(BiclusterMixin, BaseEstimator, metaclass=ABCMeta):
    n_clusters: Any
    svd_method: Any
    n_svd_vecs: Any
    mini_batch: Any
    init: Any
    n_init: Any
    random_state: Any
    @abstractmethod
    def __init__(self, n_clusters: int = ..., svd_method: str = ..., n_svd_vecs: Any | None = ..., mini_batch: bool = ..., init: str = ..., n_init: int = ..., random_state: Any | None = ...): ...
    def fit(self, X, y: Any | None = ...): ...

class SpectralCoclustering(BaseSpectral):
    def __init__(self, n_clusters: int = ..., *, svd_method: str = ..., n_svd_vecs: Any | None = ..., mini_batch: bool = ..., init: str = ..., n_init: int = ..., random_state: Any | None = ...) -> None: ...

class SpectralBiclustering(BaseSpectral):
    method: Any
    n_components: Any
    n_best: Any
    def __init__(self, n_clusters: int = ..., *, method: str = ..., n_components: int = ..., n_best: int = ..., svd_method: str = ..., n_svd_vecs: Any | None = ..., mini_batch: bool = ..., init: str = ..., n_init: int = ..., random_state: Any | None = ...) -> None: ...
