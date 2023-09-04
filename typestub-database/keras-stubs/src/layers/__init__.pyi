from keras.src.engine.base_layer import Layer as Layer
from keras.src.engine.base_preprocessing_layer import (
    PreprocessingLayer as PreprocessingLayer,
)
from keras.src.engine.input_layer import Input as Input
from keras.src.engine.input_layer import InputLayer as InputLayer
from keras.src.engine.input_spec import InputSpec as InputSpec
from keras.src.layers import serialization as serialization
from keras.src.layers.advanced_activations import ELU as ELU
from keras.src.layers.advanced_activations import LeakyReLU as LeakyReLU
from keras.src.layers.advanced_activations import PReLU as PReLU
from keras.src.layers.advanced_activations import ReLU as ReLU
from keras.src.layers.advanced_activations import Softmax as Softmax
from keras.src.layers.advanced_activations import ThresholdedReLU as ThresholdedReLU
from keras.src.layers.convolutional import Conv1D as Conv1D
from keras.src.layers.convolutional import Conv1DTranspose as Conv1DTranspose
from keras.src.layers.convolutional import Conv2D as Conv2D
from keras.src.layers.convolutional import Conv2DTranspose as Conv2DTranspose
from keras.src.layers.convolutional import Conv3D as Conv3D
from keras.src.layers.convolutional import Conv3DTranspose as Conv3DTranspose
from keras.src.layers.convolutional import Convolution1D as Convolution1D
from keras.src.layers.convolutional import Convolution2D as Convolution2D
from keras.src.layers.convolutional import (
    Convolution2DTranspose as Convolution2DTranspose,
)
from keras.src.layers.convolutional import Convolution3D as Convolution3D
from keras.src.layers.convolutional import (
    Convolution3DTranspose as Convolution3DTranspose,
)
from keras.src.layers.convolutional import Cropping1D as Cropping1D
from keras.src.layers.convolutional import Cropping2D as Cropping2D
from keras.src.layers.convolutional import Cropping3D as Cropping3D
from keras.src.layers.convolutional import DepthwiseConv1D as DepthwiseConv1D
from keras.src.layers.convolutional import DepthwiseConv2D as DepthwiseConv2D
from keras.src.layers.convolutional import SeparableConv1D as SeparableConv1D
from keras.src.layers.convolutional import SeparableConv2D as SeparableConv2D
from keras.src.layers.convolutional import (
    SeparableConvolution1D as SeparableConvolution1D,
)
from keras.src.layers.convolutional import (
    SeparableConvolution2D as SeparableConvolution2D,
)
from keras.src.layers.convolutional import UpSampling1D as UpSampling1D
from keras.src.layers.convolutional import UpSampling2D as UpSampling2D
from keras.src.layers.convolutional import UpSampling3D as UpSampling3D
from keras.src.layers.convolutional import ZeroPadding1D as ZeroPadding1D
from keras.src.layers.convolutional import ZeroPadding2D as ZeroPadding2D
from keras.src.layers.convolutional import ZeroPadding3D as ZeroPadding3D
from keras.src.layers.convolutional_recurrent import ConvLSTM1D as ConvLSTM1D
from keras.src.layers.convolutional_recurrent import ConvLSTM2D as ConvLSTM2D
from keras.src.layers.convolutional_recurrent import ConvLSTM3D as ConvLSTM3D
from keras.src.layers.core.activation import Activation as Activation
from keras.src.layers.core.activity_regularization import (
    ActivityRegularization as ActivityRegularization,
)
from keras.src.layers.core.dense import Dense as Dense
from keras.src.layers.core.dropout import Dropout as Dropout
from keras.src.layers.core.flatten import Flatten as Flatten
from keras.src.layers.core.lambda_layer import Lambda as Lambda
from keras.src.layers.core.masking import Masking as Masking
from keras.src.layers.core.permute import Permute as Permute
from keras.src.layers.core.repeat_vector import RepeatVector as RepeatVector
from keras.src.layers.core.reshape import Reshape as Reshape
from keras.src.layers.core.spatial_dropout import SpatialDropout1D as SpatialDropout1D
from keras.src.layers.core.spatial_dropout import SpatialDropout2D as SpatialDropout2D
from keras.src.layers.core.spatial_dropout import SpatialDropout3D as SpatialDropout3D
from keras.src.layers.core.tf_op_layer import ClassMethod as ClassMethod
from keras.src.layers.core.tf_op_layer import InstanceMethod as InstanceMethod
from keras.src.layers.core.tf_op_layer import InstanceProperty as InstanceProperty
from keras.src.layers.core.tf_op_layer import SlicingOpLambda as SlicingOpLambda
from keras.src.layers.core.tf_op_layer import TFOpLambda as TFOpLambda
from keras.src.layers.cudnn_recurrent import CuDNNGRU as CuDNNGRU
from keras.src.layers.cudnn_recurrent import CuDNNLSTM as CuDNNLSTM
from keras.src.layers.dense_attention import AdditiveAttention as AdditiveAttention
from keras.src.layers.dense_attention import Attention as Attention
from keras.src.layers.einsum_dense import EinsumDense as EinsumDense
from keras.src.layers.embeddings import Embedding as Embedding
from keras.src.layers.kernelized import RandomFourierFeatures as RandomFourierFeatures
from keras.src.layers.local import LocallyConnected1D as LocallyConnected1D
from keras.src.layers.local import LocallyConnected2D as LocallyConnected2D
from keras.src.layers.merge import Add as Add
from keras.src.layers.merge import Average as Average
from keras.src.layers.merge import Concatenate as Concatenate
from keras.src.layers.merge import Dot as Dot
from keras.src.layers.merge import Maximum as Maximum
from keras.src.layers.merge import Minimum as Minimum
from keras.src.layers.merge import Multiply as Multiply
from keras.src.layers.merge import Subtract as Subtract
from keras.src.layers.merge import add as add
from keras.src.layers.merge import average as average
from keras.src.layers.merge import concatenate as concatenate
from keras.src.layers.merge import dot as dot
from keras.src.layers.merge import maximum as maximum
from keras.src.layers.merge import minimum as minimum
from keras.src.layers.merge import multiply as multiply
from keras.src.layers.merge import subtract as subtract
from keras.src.layers.multi_head_attention import (
    MultiHeadAttention as MultiHeadAttention,
)
from keras.src.layers.noise import AlphaDropout as AlphaDropout
from keras.src.layers.noise import GaussianDropout as GaussianDropout
from keras.src.layers.noise import GaussianNoise as GaussianNoise
from keras.src.layers.normalization.batch_normalization import (
    SyncBatchNormalization as SyncBatchNormalization,
)
from keras.src.layers.normalization.batch_normalization_v1 import (
    BatchNormalization as BatchNormalization,
)
from keras.src.layers.normalization.layer_normalization import (
    LayerNormalization as LayerNormalization,
)
from keras.src.layers.pooling import AveragePooling1D as AveragePooling1D
from keras.src.layers.pooling import AveragePooling2D as AveragePooling2D
from keras.src.layers.pooling import AveragePooling3D as AveragePooling3D
from keras.src.layers.pooling import AvgPool1D as AvgPool1D
from keras.src.layers.pooling import AvgPool2D as AvgPool2D
from keras.src.layers.pooling import AvgPool3D as AvgPool3D
from keras.src.layers.pooling import GlobalAveragePooling1D as GlobalAveragePooling1D
from keras.src.layers.pooling import GlobalAveragePooling2D as GlobalAveragePooling2D
from keras.src.layers.pooling import GlobalAveragePooling3D as GlobalAveragePooling3D
from keras.src.layers.pooling import GlobalAvgPool1D as GlobalAvgPool1D
from keras.src.layers.pooling import GlobalAvgPool2D as GlobalAvgPool2D
from keras.src.layers.pooling import GlobalAvgPool3D as GlobalAvgPool3D
from keras.src.layers.pooling import GlobalMaxPool1D as GlobalMaxPool1D
from keras.src.layers.pooling import GlobalMaxPool2D as GlobalMaxPool2D
from keras.src.layers.pooling import GlobalMaxPool3D as GlobalMaxPool3D
from keras.src.layers.pooling import GlobalMaxPooling1D as GlobalMaxPooling1D
from keras.src.layers.pooling import GlobalMaxPooling2D as GlobalMaxPooling2D
from keras.src.layers.pooling import GlobalMaxPooling3D as GlobalMaxPooling3D
from keras.src.layers.pooling import MaxPool1D as MaxPool1D
from keras.src.layers.pooling import MaxPool2D as MaxPool2D
from keras.src.layers.pooling import MaxPool3D as MaxPool3D
from keras.src.layers.pooling import MaxPooling1D as MaxPooling1D
from keras.src.layers.pooling import MaxPooling2D as MaxPooling2D
from keras.src.layers.pooling import MaxPooling3D as MaxPooling3D
from keras.src.layers.preprocessing.category_encoding import (
    CategoryEncoding as CategoryEncoding,
)
from keras.src.layers.preprocessing.discretization import (
    Discretization as Discretization,
)
from keras.src.layers.preprocessing.hashed_crossing import (
    HashedCrossing as HashedCrossing,
)
from keras.src.layers.preprocessing.hashing import Hashing as Hashing
from keras.src.layers.preprocessing.image_preprocessing import CenterCrop as CenterCrop
from keras.src.layers.preprocessing.image_preprocessing import (
    RandomContrast as RandomContrast,
)
from keras.src.layers.preprocessing.image_preprocessing import RandomCrop as RandomCrop
from keras.src.layers.preprocessing.image_preprocessing import RandomFlip as RandomFlip
from keras.src.layers.preprocessing.image_preprocessing import (
    RandomHeight as RandomHeight,
)
from keras.src.layers.preprocessing.image_preprocessing import (
    RandomRotation as RandomRotation,
)
from keras.src.layers.preprocessing.image_preprocessing import (
    RandomTranslation as RandomTranslation,
)
from keras.src.layers.preprocessing.image_preprocessing import (
    RandomWidth as RandomWidth,
)
from keras.src.layers.preprocessing.image_preprocessing import RandomZoom as RandomZoom
from keras.src.layers.preprocessing.image_preprocessing import Rescaling as Rescaling
from keras.src.layers.preprocessing.image_preprocessing import Resizing as Resizing
from keras.src.layers.preprocessing.integer_lookup import IntegerLookup as IntegerLookup
from keras.src.layers.preprocessing.normalization import Normalization as Normalization
from keras.src.layers.preprocessing.string_lookup import StringLookup as StringLookup
from keras.src.layers.preprocessing.text_vectorization import (
    TextVectorization as TextVectorization,
)
from keras.src.layers.recurrent import GRU as GRU
from keras.src.layers.recurrent import LSTM as LSTM
from keras.src.layers.recurrent import RNN as RNN
from keras.src.layers.recurrent import AbstractRNNCell as AbstractRNNCell
from keras.src.layers.recurrent import GRUCell as GRUCell
from keras.src.layers.recurrent import LSTMCell as LSTMCell
from keras.src.layers.recurrent import PeepholeLSTMCell as PeepholeLSTMCell
from keras.src.layers.recurrent import SimpleRNN as SimpleRNN
from keras.src.layers.recurrent import SimpleRNNCell as SimpleRNNCell
from keras.src.layers.recurrent import StackedRNNCells as StackedRNNCells
from keras.src.layers.rnn_cell_wrapper_v2 import DeviceWrapper as DeviceWrapper
from keras.src.layers.rnn_cell_wrapper_v2 import DropoutWrapper as DropoutWrapper
from keras.src.layers.rnn_cell_wrapper_v2 import ResidualWrapper as ResidualWrapper
from keras.src.layers.serialization import deserialize as deserialize
from keras.src.layers.serialization import get_builtin_layer as get_builtin_layer
from keras.src.layers.serialization import serialize as serialize
from keras.src.layers.wrappers import Bidirectional as Bidirectional
from keras.src.layers.wrappers import TimeDistributed as TimeDistributed
from keras.src.layers.wrappers import Wrapper as Wrapper
from tensorflow.python import tf2 as tf2

BatchNormalizationV2 = BatchNormalization
BatchNormalizationV1 = BatchNormalization
GRUV2 = GRU
GRUCellV2 = GRUCell
LSTMV2 = LSTM
LSTMCellV2 = LSTMCell
GRUV1 = GRU
GRUCellV1 = GRUCell
LSTMV1 = LSTM
LSTMCellV1 = LSTMCell

class VersionAwareLayers:
    def __getattr__(self, name): ...
