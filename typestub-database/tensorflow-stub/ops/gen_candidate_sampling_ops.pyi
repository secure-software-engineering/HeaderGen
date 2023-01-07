from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

class _AllCandidateSamplerOutput(NamedTuple):
    sampled_candidates: Any
    true_expected_count: Any
    sampled_expected_count: Any

def all_candidate_sampler(true_classes, num_true, num_sampled, unique, seed: int = ..., seed2: int = ..., name: Any | None = ...): ...

AllCandidateSampler: Any

def all_candidate_sampler_eager_fallback(true_classes, num_true, num_sampled, unique, seed, seed2, name, ctx): ...

class _ComputeAccidentalHitsOutput(NamedTuple):
    indices: Any
    ids: Any
    weights: Any

def compute_accidental_hits(true_classes, sampled_candidates, num_true, seed: int = ..., seed2: int = ..., name: Any | None = ...): ...

ComputeAccidentalHits: Any

def compute_accidental_hits_eager_fallback(true_classes, sampled_candidates, num_true, seed, seed2, name, ctx): ...

class _FixedUnigramCandidateSamplerOutput(NamedTuple):
    sampled_candidates: Any
    true_expected_count: Any
    sampled_expected_count: Any

def fixed_unigram_candidate_sampler(true_classes, num_true, num_sampled, unique, range_max, vocab_file: str = ..., distortion: int = ..., num_reserved_ids: int = ..., num_shards: int = ..., shard: int = ..., unigrams=..., seed: int = ..., seed2: int = ..., name: Any | None = ...): ...

FixedUnigramCandidateSampler: Any

def fixed_unigram_candidate_sampler_eager_fallback(true_classes, num_true, num_sampled, unique, range_max, vocab_file, distortion, num_reserved_ids, num_shards, shard, unigrams, seed, seed2, name, ctx): ...

class _LearnedUnigramCandidateSamplerOutput(NamedTuple):
    sampled_candidates: Any
    true_expected_count: Any
    sampled_expected_count: Any

def learned_unigram_candidate_sampler(true_classes, num_true, num_sampled, unique, range_max, seed: int = ..., seed2: int = ..., name: Any | None = ...): ...

LearnedUnigramCandidateSampler: Any

def learned_unigram_candidate_sampler_eager_fallback(true_classes, num_true, num_sampled, unique, range_max, seed, seed2, name, ctx): ...

class _LogUniformCandidateSamplerOutput(NamedTuple):
    sampled_candidates: Any
    true_expected_count: Any
    sampled_expected_count: Any

def log_uniform_candidate_sampler(true_classes, num_true, num_sampled, unique, range_max, seed: int = ..., seed2: int = ..., name: Any | None = ...): ...

LogUniformCandidateSampler: Any

def log_uniform_candidate_sampler_eager_fallback(true_classes, num_true, num_sampled, unique, range_max, seed, seed2, name, ctx): ...

class _ThreadUnsafeUnigramCandidateSamplerOutput(NamedTuple):
    sampled_candidates: Any
    true_expected_count: Any
    sampled_expected_count: Any

def thread_unsafe_unigram_candidate_sampler(true_classes, num_true, num_sampled, unique, range_max, seed: int = ..., seed2: int = ..., name: Any | None = ...): ...

ThreadUnsafeUnigramCandidateSampler: Any

def thread_unsafe_unigram_candidate_sampler_eager_fallback(true_classes, num_true, num_sampled, unique, range_max, seed, seed2, name, ctx): ...

class _UniformCandidateSamplerOutput(NamedTuple):
    sampled_candidates: Any
    true_expected_count: Any
    sampled_expected_count: Any

def uniform_candidate_sampler(true_classes, num_true, num_sampled, unique, range_max, seed: int = ..., seed2: int = ..., name: Any | None = ...): ...

UniformCandidateSampler: Any

def uniform_candidate_sampler_eager_fallback(true_classes, num_true, num_sampled, unique, range_max, seed, seed2, name, ctx): ...
