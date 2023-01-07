import tensorflow.compat.v2 as tf
from absl.testing import parameterized
from keras.engine import sequential as sequential
from keras.layers.preprocessing import string_lookup as string_lookup
from keras.optimizer_v2 import gradient_descent as gradient_descent
from keras.utils import dataset_creator as dataset_creator

class DatasetCreatorModelFitTestBase(tf.test.TestCase, parameterized.TestCase): ...
