from keras.src.saving import saving_utils as saving_utils
from keras.src.saving.saved_model import constants as constants
from keras.src.saving.saved_model import layer_serialization as layer_serialization
from keras.src.saving.saved_model import save_impl as save_impl

class ModelSavedModelSaver(layer_serialization.LayerSavedModelSaver):
    @property
    def object_identifier(self): ...

class SequentialSavedModelSaver(ModelSavedModelSaver):
    @property
    def object_identifier(self): ...
