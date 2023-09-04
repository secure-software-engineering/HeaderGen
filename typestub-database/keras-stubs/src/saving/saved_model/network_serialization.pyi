from keras.src.saving.saved_model import constants as constants
from keras.src.saving.saved_model import model_serialization as model_serialization

class NetworkSavedModelSaver(model_serialization.ModelSavedModelSaver):
    @property
    def object_identifier(self): ...
