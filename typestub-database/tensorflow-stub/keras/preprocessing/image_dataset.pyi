from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.keras.layers.preprocessing import image_preprocessing as image_preprocessing
from tensorflow.python.keras.preprocessing import dataset_utils as dataset_utils
from tensorflow.python.ops import image_ops as image_ops, io_ops as io_ops
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

ALLOWLIST_FORMATS: Any

def image_dataset_from_directory(directory, labels: str = ..., label_mode: str = ..., class_names: Any | None = ..., color_mode: str = ..., batch_size: int = ..., image_size=..., shuffle: bool = ..., seed: Any | None = ..., validation_split: Any | None = ..., subset: Any | None = ..., interpolation: str = ..., follow_links: bool = ..., crop_to_aspect_ratio: bool = ..., **kwargs): ...
def paths_and_labels_to_dataset(image_paths, image_size, num_channels, labels, label_mode, num_classes, interpolation, crop_to_aspect_ratio: bool = ...): ...
def load_image(path, image_size, num_channels, interpolation, crop_to_aspect_ratio: bool = ...): ...
