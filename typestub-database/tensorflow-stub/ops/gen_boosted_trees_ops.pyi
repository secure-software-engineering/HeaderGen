from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

def boosted_trees_aggregate_stats(node_ids, gradients, hessians, feature, max_splits, num_buckets, name: Any | None = ...): ...

BoostedTreesAggregateStats: Any

def boosted_trees_aggregate_stats_eager_fallback(node_ids, gradients, hessians, feature, max_splits, num_buckets, name, ctx): ...
def boosted_trees_bucketize(float_values, bucket_boundaries, name: Any | None = ...): ...

BoostedTreesBucketize: Any

def boosted_trees_bucketize_eager_fallback(float_values, bucket_boundaries, name, ctx): ...

class _BoostedTreesCalculateBestFeatureSplitOutput(NamedTuple):
    node_ids: Any
    gains: Any
    feature_dimensions: Any
    thresholds: Any
    left_node_contribs: Any
    right_node_contribs: Any
    split_with_default_directions: Any

def boosted_trees_calculate_best_feature_split(node_id_range, stats_summary, l1, l2, tree_complexity, min_node_weight, logits_dimension, split_type: str = ..., name: Any | None = ...): ...

BoostedTreesCalculateBestFeatureSplit: Any

def boosted_trees_calculate_best_feature_split_eager_fallback(node_id_range, stats_summary, l1, l2, tree_complexity, min_node_weight, logits_dimension, split_type, name, ctx): ...

class _BoostedTreesCalculateBestFeatureSplitV2Output(NamedTuple):
    node_ids: Any
    gains: Any
    feature_ids: Any
    feature_dimensions: Any
    thresholds: Any
    left_node_contribs: Any
    right_node_contribs: Any
    split_with_default_directions: Any

def boosted_trees_calculate_best_feature_split_v2(node_id_range, stats_summaries_list, split_types, candidate_feature_ids, l1, l2, tree_complexity, min_node_weight, logits_dimension, name: Any | None = ...): ...

BoostedTreesCalculateBestFeatureSplitV2: Any

def boosted_trees_calculate_best_feature_split_v2_eager_fallback(node_id_range, stats_summaries_list, split_types, candidate_feature_ids, l1, l2, tree_complexity, min_node_weight, logits_dimension, name, ctx): ...

class _BoostedTreesCalculateBestGainsPerFeatureOutput(NamedTuple):
    node_ids_list: Any
    gains_list: Any
    thresholds_list: Any
    left_node_contribs_list: Any
    right_node_contribs_list: Any

def boosted_trees_calculate_best_gains_per_feature(node_id_range, stats_summary_list, l1, l2, tree_complexity, min_node_weight, max_splits, name: Any | None = ...): ...

BoostedTreesCalculateBestGainsPerFeature: Any

def boosted_trees_calculate_best_gains_per_feature_eager_fallback(node_id_range, stats_summary_list, l1, l2, tree_complexity, min_node_weight, max_splits, name, ctx): ...
def boosted_trees_center_bias(tree_ensemble_handle, mean_gradients, mean_hessians, l1, l2, name: Any | None = ...): ...

BoostedTreesCenterBias: Any

def boosted_trees_center_bias_eager_fallback(tree_ensemble_handle, mean_gradients, mean_hessians, l1, l2, name, ctx): ...
def boosted_trees_create_ensemble(tree_ensemble_handle, stamp_token, tree_ensemble_serialized, name: Any | None = ...): ...

BoostedTreesCreateEnsemble: Any

def boosted_trees_create_ensemble_eager_fallback(tree_ensemble_handle, stamp_token, tree_ensemble_serialized, name, ctx): ...
def boosted_trees_create_quantile_stream_resource(quantile_stream_resource_handle, epsilon, num_streams, max_elements: int = ..., name: Any | None = ...): ...

BoostedTreesCreateQuantileStreamResource: Any

def boosted_trees_create_quantile_stream_resource_eager_fallback(quantile_stream_resource_handle, epsilon, num_streams, max_elements, name, ctx): ...
def boosted_trees_deserialize_ensemble(tree_ensemble_handle, stamp_token, tree_ensemble_serialized, name: Any | None = ...): ...

BoostedTreesDeserializeEnsemble: Any

def boosted_trees_deserialize_ensemble_eager_fallback(tree_ensemble_handle, stamp_token, tree_ensemble_serialized, name, ctx): ...
def boosted_trees_ensemble_resource_handle_op(container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

BoostedTreesEnsembleResourceHandleOp: Any

def boosted_trees_ensemble_resource_handle_op_eager_fallback(container, shared_name, name, ctx): ...
def boosted_trees_example_debug_outputs(tree_ensemble_handle, bucketized_features, logits_dimension, name: Any | None = ...): ...

BoostedTreesExampleDebugOutputs: Any

def boosted_trees_example_debug_outputs_eager_fallback(tree_ensemble_handle, bucketized_features, logits_dimension, name, ctx): ...
def boosted_trees_flush_quantile_summaries(quantile_stream_resource_handle, num_features, name: Any | None = ...): ...

BoostedTreesFlushQuantileSummaries: Any

def boosted_trees_flush_quantile_summaries_eager_fallback(quantile_stream_resource_handle, num_features, name, ctx): ...

class _BoostedTreesGetEnsembleStatesOutput(NamedTuple):
    stamp_token: Any
    num_trees: Any
    num_finalized_trees: Any
    num_attempted_layers: Any
    last_layer_nodes_range: Any

def boosted_trees_get_ensemble_states(tree_ensemble_handle, name: Any | None = ...): ...

BoostedTreesGetEnsembleStates: Any

def boosted_trees_get_ensemble_states_eager_fallback(tree_ensemble_handle, name, ctx): ...
def boosted_trees_make_quantile_summaries(float_values, example_weights, epsilon, name: Any | None = ...): ...

BoostedTreesMakeQuantileSummaries: Any

def boosted_trees_make_quantile_summaries_eager_fallback(float_values, example_weights, epsilon, name, ctx): ...
def boosted_trees_make_stats_summary(node_ids, gradients, hessians, bucketized_features_list, max_splits, num_buckets, name: Any | None = ...): ...

BoostedTreesMakeStatsSummary: Any

def boosted_trees_make_stats_summary_eager_fallback(node_ids, gradients, hessians, bucketized_features_list, max_splits, num_buckets, name, ctx): ...
def boosted_trees_predict(tree_ensemble_handle, bucketized_features, logits_dimension, name: Any | None = ...): ...

BoostedTreesPredict: Any

def boosted_trees_predict_eager_fallback(tree_ensemble_handle, bucketized_features, logits_dimension, name, ctx): ...
def boosted_trees_quantile_stream_resource_add_summaries(quantile_stream_resource_handle, summaries, name: Any | None = ...): ...

BoostedTreesQuantileStreamResourceAddSummaries: Any

def boosted_trees_quantile_stream_resource_add_summaries_eager_fallback(quantile_stream_resource_handle, summaries, name, ctx): ...
def boosted_trees_quantile_stream_resource_deserialize(quantile_stream_resource_handle, bucket_boundaries, name: Any | None = ...): ...

BoostedTreesQuantileStreamResourceDeserialize: Any

def boosted_trees_quantile_stream_resource_deserialize_eager_fallback(quantile_stream_resource_handle, bucket_boundaries, name, ctx): ...
def boosted_trees_quantile_stream_resource_flush(quantile_stream_resource_handle, num_buckets, generate_quantiles: bool = ..., name: Any | None = ...): ...

BoostedTreesQuantileStreamResourceFlush: Any

def boosted_trees_quantile_stream_resource_flush_eager_fallback(quantile_stream_resource_handle, num_buckets, generate_quantiles, name, ctx): ...
def boosted_trees_quantile_stream_resource_get_bucket_boundaries(quantile_stream_resource_handle, num_features, name: Any | None = ...): ...

BoostedTreesQuantileStreamResourceGetBucketBoundaries: Any

def boosted_trees_quantile_stream_resource_get_bucket_boundaries_eager_fallback(quantile_stream_resource_handle, num_features, name, ctx): ...
def boosted_trees_quantile_stream_resource_handle_op(container: str = ..., shared_name: str = ..., name: Any | None = ...): ...

BoostedTreesQuantileStreamResourceHandleOp: Any

def boosted_trees_quantile_stream_resource_handle_op_eager_fallback(container, shared_name, name, ctx): ...

class _BoostedTreesSerializeEnsembleOutput(NamedTuple):
    stamp_token: Any
    tree_ensemble_serialized: Any

def boosted_trees_serialize_ensemble(tree_ensemble_handle, name: Any | None = ...): ...

BoostedTreesSerializeEnsemble: Any

def boosted_trees_serialize_ensemble_eager_fallback(tree_ensemble_handle, name, ctx): ...

class _BoostedTreesSparseAggregateStatsOutput(NamedTuple):
    stats_summary_indices: Any
    stats_summary_values: Any
    stats_summary_shape: Any

def boosted_trees_sparse_aggregate_stats(node_ids, gradients, hessians, feature_indices, feature_values, feature_shape, max_splits, num_buckets, name: Any | None = ...): ...

BoostedTreesSparseAggregateStats: Any

def boosted_trees_sparse_aggregate_stats_eager_fallback(node_ids, gradients, hessians, feature_indices, feature_values, feature_shape, max_splits, num_buckets, name, ctx): ...

class _BoostedTreesSparseCalculateBestFeatureSplitOutput(NamedTuple):
    node_ids: Any
    gains: Any
    feature_dimensions: Any
    thresholds: Any
    left_node_contribs: Any
    right_node_contribs: Any
    split_with_default_directions: Any

def boosted_trees_sparse_calculate_best_feature_split(node_id_range, stats_summary_indices, stats_summary_values, stats_summary_shape, l1, l2, tree_complexity, min_node_weight, logits_dimension, split_type: str = ..., name: Any | None = ...): ...

BoostedTreesSparseCalculateBestFeatureSplit: Any

def boosted_trees_sparse_calculate_best_feature_split_eager_fallback(node_id_range, stats_summary_indices, stats_summary_values, stats_summary_shape, l1, l2, tree_complexity, min_node_weight, logits_dimension, split_type, name, ctx): ...

class _BoostedTreesTrainingPredictOutput(NamedTuple):
    partial_logits: Any
    tree_ids: Any
    node_ids: Any

def boosted_trees_training_predict(tree_ensemble_handle, cached_tree_ids, cached_node_ids, bucketized_features, logits_dimension, name: Any | None = ...): ...

BoostedTreesTrainingPredict: Any

def boosted_trees_training_predict_eager_fallback(tree_ensemble_handle, cached_tree_ids, cached_node_ids, bucketized_features, logits_dimension, name, ctx): ...
def boosted_trees_update_ensemble(tree_ensemble_handle, feature_ids, node_ids, gains, thresholds, left_node_contribs, right_node_contribs, max_depth, learning_rate, pruning_mode, name: Any | None = ...): ...

BoostedTreesUpdateEnsemble: Any

def boosted_trees_update_ensemble_eager_fallback(tree_ensemble_handle, feature_ids, node_ids, gains, thresholds, left_node_contribs, right_node_contribs, max_depth, learning_rate, pruning_mode, name, ctx): ...
def boosted_trees_update_ensemble_v2(tree_ensemble_handle, feature_ids, dimension_ids, node_ids, gains, thresholds, left_node_contribs, right_node_contribs, split_types, max_depth, learning_rate, pruning_mode, logits_dimension: int = ..., name: Any | None = ...): ...

BoostedTreesUpdateEnsembleV2: Any

def boosted_trees_update_ensemble_v2_eager_fallback(tree_ensemble_handle, feature_ids, dimension_ids, node_ids, gains, thresholds, left_node_contribs, right_node_contribs, split_types, max_depth, learning_rate, pruning_mode, logits_dimension, name, ctx): ...
def is_boosted_trees_ensemble_initialized(tree_ensemble_handle, name: Any | None = ...): ...

IsBoostedTreesEnsembleInitialized: Any

def is_boosted_trees_ensemble_initialized_eager_fallback(tree_ensemble_handle, name, ctx): ...
def is_boosted_trees_quantile_stream_resource_initialized(quantile_stream_resource_handle, name: Any | None = ...): ...

IsBoostedTreesQuantileStreamResourceInitialized: Any

def is_boosted_trees_quantile_stream_resource_initialized_eager_fallback(quantile_stream_resource_handle, name, ctx): ...
