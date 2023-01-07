import abc
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.layers import base as base
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, embedding_ops as embedding_ops, init_ops as init_ops, lookup_ops as lookup_ops, math_ops as math_ops, nn_ops as nn_ops, parsing_ops as parsing_ops, resource_variable_ops as resource_variable_ops, sparse_ops as sparse_ops, string_ops as string_ops, template as template, variable_scope as variable_scope, variables as variables
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.training import checkpoint_utils as checkpoint_utils
from tensorflow.python.util import nest as nest
from tensorflow.python.util.compat import collections_abc as collections_abc
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

def input_layer(features, feature_columns, weight_collections: Any | None = ..., trainable: bool = ..., cols_to_vars: Any | None = ..., cols_to_output_tensors: Any | None = ...): ...

class InputLayer:
    def __init__(self, feature_columns, weight_collections: Any | None = ..., trainable: bool = ..., cols_to_vars: Any | None = ..., name: str = ..., create_scope_now: bool = ...) -> None: ...
    def __call__(self, features): ...
    @property
    def name(self): ...
    @property
    def non_trainable_variables(self): ...
    @property
    def non_trainable_weights(self): ...
    @property
    def trainable_variables(self): ...
    @property
    def trainable_weights(self): ...
    @property
    def variables(self): ...
    @property
    def weights(self): ...

def linear_model(features, feature_columns, units: int = ..., sparse_combiner: str = ..., weight_collections: Any | None = ..., trainable: bool = ..., cols_to_vars: Any | None = ...): ...

class _FCLinearWrapper(base.Layer):
    def __init__(self, feature_column, units: int = ..., sparse_combiner: str = ..., weight_collections: Any | None = ..., trainable: bool = ..., name: Any | None = ..., **kwargs) -> None: ...
    built: bool
    def build(self, _) -> None: ...
    def call(self, builder): ...

class _BiasLayer(base.Layer):
    def __init__(self, units: int = ..., trainable: bool = ..., weight_collections: Any | None = ..., name: Any | None = ..., **kwargs) -> None: ...
    built: bool
    def build(self, _) -> None: ...
    def call(self, _): ...

class _LinearModel(base.Layer):
    def __init__(self, feature_columns, units: int = ..., sparse_combiner: str = ..., weight_collections: Any | None = ..., trainable: bool = ..., name: Any | None = ..., **kwargs): ...
    def cols_to_vars(self): ...
    def call(self, features): ...

def make_parse_example_spec(feature_columns): ...

class _EmbeddingColumnLayer(base.Layer):
    def __init__(self, embedding_shape, initializer, weight_collections: Any | None = ..., trainable: bool = ..., name: Any | None = ..., **kwargs) -> None: ...
    def set_weight_collections(self, weight_collections) -> None: ...
    built: bool
    def build(self, _) -> None: ...
    def call(self, _): ...

class _FeatureColumn(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def name(self): ...
    def __lt__(self, other): ...
    def __gt__(self, other): ...

class _DenseColumn(_FeatureColumn, metaclass=abc.ABCMeta): ...

class _CategoricalColumn(_FeatureColumn, metaclass=abc.ABCMeta):

    class IdWeightPair(NamedTuple):
        id_tensor: Any
        weight_tensor: Any

class _SequenceDenseColumn(_FeatureColumn, metaclass=abc.ABCMeta):

    class TensorSequenceLengthPair(NamedTuple):
        dense_tensor: Any
        sequence_length: Any

class _LazyBuilder:
    def __init__(self, features) -> None: ...
    def get(self, key): ...

class _NumericColumn(_DenseColumn):
    @property
    def name(self): ...

class _BucketizedColumn(_DenseColumn, _CategoricalColumn):
    @property
    def name(self): ...

class _EmbeddingColumn(_DenseColumn, _SequenceDenseColumn):
    def __new__(cls, categorical_column, dimension, combiner, layer_creator, ckpt_to_load_from, tensor_name_in_ckpt, max_norm, trainable, use_safe_embedding_lookup: bool = ...): ...
    @property
    def name(self): ...

class _SharedEmbeddingColumn(_DenseColumn, _SequenceDenseColumn):
    @property
    def name(self): ...

class _HashedCategoricalColumn(_CategoricalColumn):
    @property
    def name(self): ...

class _VocabularyFileCategoricalColumn(_CategoricalColumn):
    @property
    def name(self): ...

class _VocabularyListCategoricalColumn(_CategoricalColumn):
    @property
    def name(self): ...

class _IdentityCategoricalColumn(_CategoricalColumn):
    @property
    def name(self): ...

class _WeightedCategoricalColumn(_CategoricalColumn):
    @property
    def name(self): ...

class _CrossedColumn(_CategoricalColumn):
    @property
    def name(self): ...

class _IndicatorColumn(_DenseColumn, _SequenceDenseColumn):
    @property
    def name(self): ...

class _SequenceCategoricalColumn(_CategoricalColumn):
    @property
    def name(self): ...
