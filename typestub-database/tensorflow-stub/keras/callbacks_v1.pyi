from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, errors as errors
from tensorflow.python.keras import callbacks as callbacks
from tensorflow.python.ops import array_ops as array_ops, state_ops as state_ops, summary_ops_v2 as summary_ops_v2, variables as variables
from tensorflow.python.training import saver as saver
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

class TensorBoard(callbacks.TensorBoard):
    log_dir: Any
    histogram_freq: Any
    merged: Any
    write_graph: Any
    write_grads: Any
    write_images: Any
    batch_size: Any
    embeddings_freq: Any
    embeddings_layer_names: Any
    embeddings_metadata: Any
    embeddings_data: Any
    update_freq: int
    def __init__(self, log_dir: str = ..., histogram_freq: int = ..., batch_size: int = ..., write_graph: bool = ..., write_grads: bool = ..., write_images: bool = ..., embeddings_freq: int = ..., embeddings_layer_names: Any | None = ..., embeddings_metadata: Any | None = ..., embeddings_data: Any | None = ..., update_freq: str = ..., profile_batch: int = ...) -> None: ...
    model: Any
    assign_embeddings: Any
    batch_id: Any
    step: Any
    saver: Any
    def set_model(self, model) -> None: ...
    def on_train_batch_begin(self, batch, logs: Any | None = ...) -> None: ...
    def on_train_batch_end(self, batch, logs: Any | None = ...): ...
    def on_test_begin(self, logs: Any | None = ...) -> None: ...
    def on_test_end(self, logs: Any | None = ...) -> None: ...
    def on_batch_end(self, batch, logs: Any | None = ...) -> None: ...
    def on_train_begin(self, logs: Any | None = ...) -> None: ...
    def on_epoch_begin(self, epoch, logs: Any | None = ...) -> None: ...
    def on_epoch_end(self, epoch, logs: Any | None = ...) -> None: ...
    def on_train_end(self, logs: Any | None = ...) -> None: ...
