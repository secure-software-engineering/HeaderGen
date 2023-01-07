from keras import backend as backend
from keras.engine.training import Model as Model
from keras.layers.core.lambda_layer import Lambda as Lambda
from keras.layers.merge import concatenate as concatenate

def multi_gpu_model(model, gpus, cpu_merge: bool = ..., cpu_relocation: bool = ...): ...
