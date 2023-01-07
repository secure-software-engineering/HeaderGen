from tensorflow.python.framework import ops as ops
from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.engine.training import Model as Model
from tensorflow.python.keras.layers.core import Lambda as Lambda
from tensorflow.python.keras.layers.merge import concatenate as concatenate
from tensorflow.python.ops import array_ops as array_ops

def multi_gpu_model(model, gpus, cpu_merge: bool = ..., cpu_relocation: bool = ...): ...
