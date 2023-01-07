from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

class _CTCBeamSearchDecoderOutput(NamedTuple):
    decoded_indices: Any
    decoded_values: Any
    decoded_shape: Any
    log_probability: Any

def ctc_beam_search_decoder(inputs, sequence_length, beam_width, top_paths, merge_repeated: bool = ..., name: Any | None = ...): ...

CTCBeamSearchDecoder: Any

def ctc_beam_search_decoder_eager_fallback(inputs, sequence_length, beam_width, top_paths, merge_repeated, name, ctx): ...

class _CTCGreedyDecoderOutput(NamedTuple):
    decoded_indices: Any
    decoded_values: Any
    decoded_shape: Any
    log_probability: Any

def ctc_greedy_decoder(inputs, sequence_length, merge_repeated: bool = ..., blank_index: int = ..., name: Any | None = ...): ...

CTCGreedyDecoder: Any

def ctc_greedy_decoder_eager_fallback(inputs, sequence_length, merge_repeated, blank_index, name, ctx): ...

class _CTCLossOutput(NamedTuple):
    loss: Any
    gradient: Any

def ctc_loss(inputs, labels_indices, labels_values, sequence_length, preprocess_collapse_repeated: bool = ..., ctc_merge_repeated: bool = ..., ignore_longer_outputs_than_inputs: bool = ..., name: Any | None = ...): ...

CTCLoss: Any

def ctc_loss_eager_fallback(inputs, labels_indices, labels_values, sequence_length, preprocess_collapse_repeated, ctc_merge_repeated, ignore_longer_outputs_than_inputs, name, ctx): ...

class _CTCLossV2Output(NamedTuple):
    loss: Any
    gradient: Any

def ctc_loss_v2(inputs, labels_indices, labels_values, sequence_length, preprocess_collapse_repeated: bool = ..., ctc_merge_repeated: bool = ..., ignore_longer_outputs_than_inputs: bool = ..., name: Any | None = ...): ...

CTCLossV2: Any

def ctc_loss_v2_eager_fallback(inputs, labels_indices, labels_values, sequence_length, preprocess_collapse_repeated, ctc_merge_repeated, ignore_longer_outputs_than_inputs, name, ctx): ...
