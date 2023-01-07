from . import tools as tools
from .initialization import Initialization as Initialization
from .tools import find_best_blas_type as find_best_blas_type, validate_matrix_shape as validate_matrix_shape, validate_vector_shape as validate_vector_shape
from typing import Any

class OptionWrapper:
    mask_attribute: Any
    mask_value: Any
    def __init__(self, mask_attribute, mask_value) -> None: ...
    def __get__(self, obj, objtype): ...
    def __set__(self, obj, value) -> None: ...

class MatrixWrapper:
    name: Any
    attribute: Any
    def __init__(self, name, attribute) -> None: ...
    def __get__(self, obj, objtype): ...
    def __set__(self, obj, value) -> None: ...

class Representation:
    endog: Any
    design: Any
    obs_intercept: Any
    obs_cov: Any
    transition: Any
    state_intercept: Any
    selection: Any
    state_cov: Any
    shapes: Any
    k_endog: Any
    nobs: Any
    k_states: Any
    k_posdef: Any
    initial_variance: Any
    prefix_statespace_map: Any
    initialization: Any
    def __init__(self, k_endog, k_states, k_posdef: Any | None = ..., initial_variance: float = ..., nobs: int = ..., dtype=..., design: Any | None = ..., obs_intercept: Any | None = ..., obs_cov: Any | None = ..., transition: Any | None = ..., state_intercept: Any | None = ..., selection: Any | None = ..., state_cov: Any | None = ..., statespace_classes: Any | None = ..., **kwargs) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def clone(self, endog, **kwargs): ...
    def extend(self, endog, start: Any | None = ..., end: Any | None = ..., **kwargs): ...
    def diff_endog(self, new_endog, tolerance: float = ...): ...
    @property
    def prefix(self): ...
    @property
    def dtype(self): ...
    @property
    def time_invariant(self): ...
    @property
    def obs(self): ...
    def bind(self, endog) -> None: ...
    def initialize(self, initialization, approximate_diffuse_variance: Any | None = ..., constant: Any | None = ..., stationary_cov: Any | None = ...) -> None: ...
    def initialize_known(self, constant, stationary_cov) -> None: ...
    def initialize_approximate_diffuse(self, variance: Any | None = ...) -> None: ...
    def initialize_stationary(self) -> None: ...
    def initialize_diffuse(self) -> None: ...

class FrozenRepresentation:
    def __init__(self, model) -> None: ...
    model: Any
    prefix: Any
    dtype: Any
    nobs: Any
    k_endog: Any
    k_states: Any
    k_posdef: Any
    time_invariant: Any
    endog: Any
    design: Any
    obs_intercept: Any
    obs_cov: Any
    transition: Any
    state_intercept: Any
    selection: Any
    state_cov: Any
    missing: Any
    nmissing: Any
    shapes: Any
    initialization: Any
    initial_state: Any
    initial_state_cov: Any
    initial_diffuse_state_cov: Any
    def update_representation(self, model) -> None: ...
