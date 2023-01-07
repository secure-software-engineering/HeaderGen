from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

def decode_csv(records, record_defaults, field_delim: str = ..., use_quote_delim: bool = ..., na_value: str = ..., select_cols=..., name: Any | None = ...): ...

DecodeCSV: Any

def decode_csv_eager_fallback(records, record_defaults, field_delim, use_quote_delim, na_value, select_cols, name, ctx): ...
def decode_compressed(bytes, compression_type: str = ..., name: Any | None = ...): ...

DecodeCompressed: Any

def decode_compressed_eager_fallback(bytes, compression_type, name, ctx): ...
def decode_json_example(json_examples, name: Any | None = ...): ...

DecodeJSONExample: Any

def decode_json_example_eager_fallback(json_examples, name, ctx): ...
def decode_padded_raw(input_bytes, fixed_length, out_type, little_endian: bool = ..., name: Any | None = ...): ...

DecodePaddedRaw: Any

def decode_padded_raw_eager_fallback(input_bytes, fixed_length, out_type, little_endian, name, ctx): ...
def decode_raw(bytes, out_type, little_endian: bool = ..., name: Any | None = ...): ...

DecodeRaw: Any

def decode_raw_eager_fallback(bytes, out_type, little_endian, name, ctx): ...

class _ParseExampleOutput(NamedTuple):
    sparse_indices: Any
    sparse_values: Any
    sparse_shapes: Any
    dense_values: Any

def parse_example(serialized, names, sparse_keys, dense_keys, dense_defaults, sparse_types, dense_shapes, name: Any | None = ...): ...

ParseExample: Any

def parse_example_eager_fallback(serialized, names, sparse_keys, dense_keys, dense_defaults, sparse_types, dense_shapes, name, ctx): ...

class _ParseExampleV2Output(NamedTuple):
    sparse_indices: Any
    sparse_values: Any
    sparse_shapes: Any
    dense_values: Any
    ragged_values: Any
    ragged_row_splits: Any

def parse_example_v2(serialized, names, sparse_keys, dense_keys, ragged_keys, dense_defaults, num_sparse, sparse_types, ragged_value_types, ragged_split_types, dense_shapes, name: Any | None = ...): ...

ParseExampleV2: Any

def parse_example_v2_eager_fallback(serialized, names, sparse_keys, dense_keys, ragged_keys, dense_defaults, num_sparse, sparse_types, ragged_value_types, ragged_split_types, dense_shapes, name, ctx): ...

class _ParseSequenceExampleOutput(NamedTuple):
    context_sparse_indices: Any
    context_sparse_values: Any
    context_sparse_shapes: Any
    context_dense_values: Any
    feature_list_sparse_indices: Any
    feature_list_sparse_values: Any
    feature_list_sparse_shapes: Any
    feature_list_dense_values: Any
    feature_list_dense_lengths: Any

def parse_sequence_example(serialized, debug_name, context_dense_defaults, feature_list_dense_missing_assumed_empty, context_sparse_keys, context_dense_keys, feature_list_sparse_keys, feature_list_dense_keys, Ncontext_sparse: int = ..., Ncontext_dense: int = ..., Nfeature_list_sparse: int = ..., Nfeature_list_dense: int = ..., context_sparse_types=..., feature_list_dense_types=..., context_dense_shapes=..., feature_list_sparse_types=..., feature_list_dense_shapes=..., name: Any | None = ...): ...

ParseSequenceExample: Any

def parse_sequence_example_eager_fallback(serialized, debug_name, context_dense_defaults, feature_list_dense_missing_assumed_empty, context_sparse_keys, context_dense_keys, feature_list_sparse_keys, feature_list_dense_keys, Ncontext_sparse, Ncontext_dense, Nfeature_list_sparse, Nfeature_list_dense, context_sparse_types, feature_list_dense_types, context_dense_shapes, feature_list_sparse_types, feature_list_dense_shapes, name, ctx): ...

class _ParseSequenceExampleV2Output(NamedTuple):
    context_sparse_indices: Any
    context_sparse_values: Any
    context_sparse_shapes: Any
    context_dense_values: Any
    context_ragged_values: Any
    context_ragged_row_splits: Any
    feature_list_sparse_indices: Any
    feature_list_sparse_values: Any
    feature_list_sparse_shapes: Any
    feature_list_dense_values: Any
    feature_list_dense_lengths: Any
    feature_list_ragged_values: Any
    feature_list_ragged_outer_splits: Any
    feature_list_ragged_inner_splits: Any

def parse_sequence_example_v2(serialized, debug_name, context_sparse_keys, context_dense_keys, context_ragged_keys, feature_list_sparse_keys, feature_list_dense_keys, feature_list_ragged_keys, feature_list_dense_missing_assumed_empty, context_dense_defaults, Ncontext_sparse: int = ..., context_sparse_types=..., context_ragged_value_types=..., context_ragged_split_types=..., context_dense_shapes=..., Nfeature_list_sparse: int = ..., Nfeature_list_dense: int = ..., feature_list_dense_types=..., feature_list_sparse_types=..., feature_list_ragged_value_types=..., feature_list_ragged_split_types=..., feature_list_dense_shapes=..., name: Any | None = ...): ...

ParseSequenceExampleV2: Any

def parse_sequence_example_v2_eager_fallback(serialized, debug_name, context_sparse_keys, context_dense_keys, context_ragged_keys, feature_list_sparse_keys, feature_list_dense_keys, feature_list_ragged_keys, feature_list_dense_missing_assumed_empty, context_dense_defaults, Ncontext_sparse, context_sparse_types, context_ragged_value_types, context_ragged_split_types, context_dense_shapes, Nfeature_list_sparse, Nfeature_list_dense, feature_list_dense_types, feature_list_sparse_types, feature_list_ragged_value_types, feature_list_ragged_split_types, feature_list_dense_shapes, name, ctx): ...

class _ParseSingleExampleOutput(NamedTuple):
    sparse_indices: Any
    sparse_values: Any
    sparse_shapes: Any
    dense_values: Any

def parse_single_example(serialized, dense_defaults, num_sparse, sparse_keys, dense_keys, sparse_types, dense_shapes, name: Any | None = ...): ...

ParseSingleExample: Any

def parse_single_example_eager_fallback(serialized, dense_defaults, num_sparse, sparse_keys, dense_keys, sparse_types, dense_shapes, name, ctx): ...

class _ParseSingleSequenceExampleOutput(NamedTuple):
    context_sparse_indices: Any
    context_sparse_values: Any
    context_sparse_shapes: Any
    context_dense_values: Any
    feature_list_sparse_indices: Any
    feature_list_sparse_values: Any
    feature_list_sparse_shapes: Any
    feature_list_dense_values: Any

def parse_single_sequence_example(serialized, feature_list_dense_missing_assumed_empty, context_sparse_keys, context_dense_keys, feature_list_sparse_keys, feature_list_dense_keys, context_dense_defaults, debug_name, context_sparse_types=..., feature_list_dense_types=..., context_dense_shapes=..., feature_list_sparse_types=..., feature_list_dense_shapes=..., name: Any | None = ...): ...

ParseSingleSequenceExample: Any

def parse_single_sequence_example_eager_fallback(serialized, feature_list_dense_missing_assumed_empty, context_sparse_keys, context_dense_keys, feature_list_sparse_keys, feature_list_dense_keys, context_dense_defaults, debug_name, context_sparse_types, feature_list_dense_types, context_dense_shapes, feature_list_sparse_types, feature_list_dense_shapes, name, ctx): ...
def parse_tensor(serialized, out_type, name: Any | None = ...): ...

ParseTensor: Any

def parse_tensor_eager_fallback(serialized, out_type, name, ctx): ...
def serialize_tensor(tensor, name: Any | None = ...): ...

SerializeTensor: Any

def serialize_tensor_eager_fallback(tensor, name, ctx): ...
def string_to_number(string_tensor, out_type=..., name: Any | None = ...): ...

StringToNumber: Any

def string_to_number_eager_fallback(string_tensor, out_type, name, ctx): ...
