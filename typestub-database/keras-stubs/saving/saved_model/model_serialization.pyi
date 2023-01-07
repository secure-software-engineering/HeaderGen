from keras.saving import saving_utils as saving_utils
from keras.saving.saved_model import constants as constants, layer_serialization as layer_serialization, save_impl as save_impl

class ModelSavedModelSaver(layer_serialization.LayerSavedModelSaver):
    @property
    def object_identifier(self): ...

class SequentialSavedModelSaver(ModelSavedModelSaver):
    @property
    def object_identifier(self): ...
