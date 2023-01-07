from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

def stateless_random_get_alg(name: Any | None = ...): ...

StatelessRandomGetAlg: Any

def stateless_random_get_alg_eager_fallback(name, ctx): ...

class _StatelessRandomGetKeyCounterOutput(NamedTuple):
    key: Any
    counter: Any

def stateless_random_get_key_counter(seed, name: Any | None = ...): ...

StatelessRandomGetKeyCounter: Any

def stateless_random_get_key_counter_eager_fallback(seed, name, ctx): ...

class _StatelessRandomGetKeyCounterAlgOutput(NamedTuple):
    key: Any
    counter: Any
    alg: Any

def stateless_random_get_key_counter_alg(seed, name: Any | None = ...): ...

StatelessRandomGetKeyCounterAlg: Any

def stateless_random_get_key_counter_alg_eager_fallback(seed, name, ctx): ...
def stateless_random_normal_v2(shape, key, counter, alg, dtype=..., name: Any | None = ...): ...

StatelessRandomNormalV2: Any

def stateless_random_normal_v2_eager_fallback(shape, key, counter, alg, dtype, name, ctx): ...
def stateless_random_uniform_full_int_v2(shape, key, counter, alg, dtype=..., name: Any | None = ...): ...

StatelessRandomUniformFullIntV2: Any

def stateless_random_uniform_full_int_v2_eager_fallback(shape, key, counter, alg, dtype, name, ctx): ...
def stateless_random_uniform_int_v2(shape, key, counter, alg, minval, maxval, name: Any | None = ...): ...

StatelessRandomUniformIntV2: Any

def stateless_random_uniform_int_v2_eager_fallback(shape, key, counter, alg, minval, maxval, name, ctx): ...
def stateless_random_uniform_v2(shape, key, counter, alg, dtype=..., name: Any | None = ...): ...

StatelessRandomUniformV2: Any

def stateless_random_uniform_v2_eager_fallback(shape, key, counter, alg, dtype, name, ctx): ...
def stateless_truncated_normal_v2(shape, key, counter, alg, dtype=..., name: Any | None = ...): ...

StatelessTruncatedNormalV2: Any

def stateless_truncated_normal_v2_eager_fallback(shape, key, counter, alg, dtype, name, ctx): ...
