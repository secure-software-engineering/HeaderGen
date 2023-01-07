# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% _uuid="8f2839f25d086af736a60e9eeb907d3b93b6e0e5" _cell_guid="b1076dfc-b9ad-4769-8c92-a6c4dae69d19"
import os
import numpy as np
import pandas as pd

# %% _cell_guid="79c7e3d0-c299-4dcb-8224-4455121ee9b0" _uuid="d629ff2d2480ee46fbb7e2d37f6b5fab8052498a"
train_df = pd.read_csv('../input/train.csv')
test_df = pd.read_csv('../input/test.csv')

# %%
features = train_df.columns
features[2:]

# %%
from tqdm import tqdm_notebook as tqdm


# %%
# Code from: https://stackoverflow.com/questions/45028260/gaussian-to-uniform-distribution-conversion-has-errors-at-the-edges-of-uniform-d
def gaussian_estimation(vector):
    mu = np.mean(vector)
    sig = np.std(vector)
    return mu, sig

# Adjusts the data so it forms a gaussian with mean of 0 and std of 1
def gaussian_normalization(vector, char = None):
    if char is None:
        mu , sig = gaussian_estimation(vector)
    else:
        mu = char[0]
        sig = char[1]
    normalized = (vector-mu)/sig
    return normalized

# Taken from https://en.wikipedia.org/wiki/Normal_distribution#Cumulative_distribution_function
def CDF(x, max_i = 100):
    sum = x
    value = x
    for i in np.arange(max_i)+1:
        value = value*x*x/(2.0*i+1)
        sum = sum + value
    return 0.5 + (sum/np.sqrt(2*np.pi))*np.exp(-1*(x*x)/2)

def gaussian_to_uniform(vector, if_normal = False):
    if (if_normal == False):
        vector = gaussian_normalization(vector)
    uni = np.apply_along_axis(CDF, 0, vector)
    return uni



# %%
#for f in tqdm(features[2:]):
#     train_df.loc[:, f] = gaussian_to_uniform(train_df.loc[:, f].values)
#    
#     test_df.loc[:, f] = gaussian_to_uniform(test_df.loc[:, f].values)

# %%
from keras.utils import Sequence  
from keras.callbacks import Callback
import random

class DataGenerator(Sequence):
    def __init__(self, x, y, batch_size=256):
        self.x = x
        self.y = y
        self.batch_size = batch_size
        
        self.pos_x = x[y==1]
        self.neg_x = x[y==0]
        
        self.pos_idx = list(range(len(self.pos_x)))
        self.neg_idx = list(range(len(self.neg_x)))
        
    def __len__(self):
        return int(len(self.y)/self.batch_size)
    
    def __getitem__(self, indx):
        poss_b, neg_b, anch_b = [], [], []
        
        for _ in range(self.batch_size):
            if random.uniform(0, 1) > 0.5:
                p_i = random.choice(self.pos_idx)
                n_i = random.choice(self.neg_idx)
                a_i = random.choice(self.pos_idx)
                    
                p_x = self.pos_x[p_i]
                n_x = self.neg_x[n_i]
                a_x = self.pos_x[a_i]
            else:
                p_i = random.choice(self.neg_idx)
                n_i = random.choice(self.pos_idx)
                a_i = random.choice(self.neg_idx)
                
                p_x = self.neg_x[p_i]
                n_x = self.pos_x[n_i]
                a_x = self.neg_x[a_i]
            # augmentation
            if random.uniform(0, 1) > 0.5:
                ids = [0, 1]
                np.random.shuffle(ids)
                _x = np.array([p_x, a_x])
                _x1 = np.array([p_x, a_x])
                for c in range(_x.shape[1]):
                    np.random.shuffle(ids)
                    _x1[:,c] = _x[ids][:,c]
                p_x, a_x = _x1[0], _x[1]    
            
            poss_b.append(p_x)
            neg_b.append(n_x)
            anch_b.append(a_x)
        return [np.array(poss_b), np.array(neg_b), np.array(anch_b)], np.zeros((self.batch_size, 2))


# %%
class CyclicLR(Callback):
    """This callback implements a cyclical learning rate policy (CLR).
    The method cycles the learning rate between two boundaries with
    some constant frequency, as detailed in this paper (https://arxiv.org/abs/1506.01186).
    The amplitude of the cycle can be scaled on a per-iteration or 
    per-cycle basis.
    This class has three built-in policies, as put forth in the paper.
    "triangular":
        A basic triangular cycle w/ no amplitude scaling.
    "triangular2":
        A basic triangular cycle that scales initial amplitude by half each cycle.
    "exp_range":
        A cycle that scales initial amplitude by gamma**(cycle iterations) at each 
        cycle iteration.
    For more detail, please see paper.
    
    # Example
        ```python
            clr = CyclicLR(base_lr=0.001, max_lr=0.006,
                                step_size=2000., mode='triangular')
            model.fit(X_train, Y_train, callbacks=[clr])
        ```
    
    Class also supports custom scaling functions:
        ```python
            clr_fn = lambda x: 0.5*(1+np.sin(x*np.pi/2.))
            clr = CyclicLR(base_lr=0.001, max_lr=0.006,
                                step_size=2000., scale_fn=clr_fn,
                                scale_mode='cycle')
            model.fit(X_train, Y_train, callbacks=[clr])
        ```    
    # Arguments
        base_lr: initial learning rate which is the
            lower boundary in the cycle.
        max_lr: upper boundary in the cycle. Functionally,
            it defines the cycle amplitude (max_lr - base_lr).
            The lr at any cycle is the sum of base_lr
            and some scaling of the amplitude; therefore 
            max_lr may not actually be reached depending on
            scaling function.
        step_size: number of training iterations per
            half cycle. Authors suggest setting step_size
            2-8 x training iterations in epoch.
        mode: one of {triangular, triangular2, exp_range}.
            Default 'triangular'.
            Values correspond to policies detailed above.
            If scale_fn is not None, this argument is ignored.
        gamma: constant in 'exp_range' scaling function:
            gamma**(cycle iterations)
        scale_fn: Custom scaling policy defined by a single
            argument lambda function, where 
            0 <= scale_fn(x) <= 1 for all x >= 0.
            mode paramater is ignored 
        scale_mode: {'cycle', 'iterations'}.
            Defines whether scale_fn is evaluated on 
            cycle number or cycle iterations (training
            iterations since start of cycle). Default is 'cycle'.
    """

    def __init__(self, base_lr=0.001, max_lr=0.006, step_size=2000., mode='triangular',
                 gamma=1., scale_fn=None, scale_mode='cycle', decay=0.1):
        super(CyclicLR, self).__init__()

        self.base_lr = base_lr
        self.max_lr = max_lr
        self.step_size = step_size
        self.mode = mode
        self.gamma = gamma
        if scale_fn == None:
            if self.mode == 'triangular':
                self.scale_fn = lambda x: 1.
                self.scale_mode = 'cycle'
            elif self.mode == 'triangular2':
                self.scale_fn = lambda x: 1/(2.**(x-1))
                self.scale_mode = 'cycle'
            elif self.mode == 'exp_range':
                self.scale_fn = lambda x: gamma**(x)
                self.scale_mode = 'iterations'
        else:
            self.scale_fn = scale_fn
            self.scale_mode = scale_mode
        self.clr_iterations = 0.
        self.trn_iterations = 0.
        self.history = {}
        self.decay = decay

        self._reset()

    def _reset(self, new_base_lr=None, new_max_lr=None,
               new_step_size=None):
        """Resets cycle iterations.
        Optional boundary/step size adjustment.
        """
        if new_base_lr != None:
            self.base_lr = new_base_lr
        if new_max_lr != None:
            self.max_lr = new_max_lr
        if new_step_size != None:
            self.step_size = new_step_size
        self.clr_iterations = 0.
        
    def clr(self):
        cycle = np.floor(1+self.clr_iterations/(2*self.step_size))
        x = np.abs(self.clr_iterations/self.step_size - 2*cycle + 1)
        if self.scale_mode == 'cycle':
            return self.base_lr + (self.max_lr-self.base_lr)*np.maximum(0, (1-x))*self.scale_fn(cycle)
        else:
            return self.base_lr + (self.max_lr-self.base_lr)*np.maximum(0, (1-x))*self.scale_fn(self.clr_iterations)
        
    def on_train_begin(self, logs={}):
        logs = logs or {}

        if self.clr_iterations == 0:
            K.set_value(self.model.optimizer.lr, self.base_lr)
        else:
            K.set_value(self.model.optimizer.lr, self.clr())        
            
    def on_batch_end(self, epoch, logs=None):
        
        logs = logs or {}
        self.trn_iterations += 1
        self.clr_iterations += 1

        self.history.setdefault('lr', []).append(K.get_value(self.model.optimizer.lr))
        self.history.setdefault('iterations', []).append(self.trn_iterations)

        for k, v in logs.items():
            self.history.setdefault(k, []).append(v)
        
        K.set_value(self.model.optimizer.lr, self.clr())
        
        
    def on_epoch_end(self, epoch, logs=None):
        self.base_lr = self.base_lr*np.exp(-epoch*self.decay)
        self.max_lr = self.max_lr*np.exp(-epoch*self.decay)



# %%
from keras import Model
from keras.layers import Dense, BatchNormalization, Activation, Dropout, Input, Add, AlphaDropout, GaussianNoise, GaussianDropout, Conv1D, GlobalMaxPool1D, Concatenate, LeakyReLU
from keras.optimizers import Nadam


# %%
OUTPUT_SIZE = 32

# %%
import keras.backend as K
beta=OUTPUT_SIZE
epsilon=1e-4
def triplet_loss_distance(y_true, y_pred):
    y_pred = K.sigmoid(y_pred)
    anchor = y_pred[..., :OUTPUT_SIZE]
    positive = y_pred[..., OUTPUT_SIZE:2*OUTPUT_SIZE]
    negative = y_pred[..., 2*OUTPUT_SIZE:]
    
    # distance between the anchor and the positive
    pos_dist = K.tf.reduce_sum(K.tf.square(K.tf.subtract(anchor,positive)),1)
    # distance between the anchor and the negative
    neg_dist = K.tf.reduce_sum(K.tf.square(K.tf.subtract(anchor,negative)),1)
    
    #Non Linear Values  
    
    # -ln(-x/N+1)
    pos_dist = -K.tf.log(-K.tf.divide((pos_dist),beta)+1+epsilon)
    neg_dist = -K.tf.log(-K.tf.divide((OUTPUT_SIZE-neg_dist),beta)+1+epsilon)
    
    return pos_dist + neg_dist


# %%
def get_model(shape=(200,)):
    inp = Input(shape)
    
    x = GaussianNoise(0.01)(inp)
    x = Dense(128, kernel_initializer='glorot_normal')(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    
    x = Dense(128, kernel_initializer='glorot_normal')(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    
    x = Dense(64, kernel_initializer='glorot_normal')(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    
    x = Dense(64, kernel_initializer='glorot_normal')(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    
    x = Dense(32)(x)
    
    model = Model(inp, x)
    return model


# %%
emb_model = get_model()
    

# %%
p_inp, n_inp, a_inp = Input((200,)), Input((200,)), Input((200,))

po, no, ao = emb_model(p_inp), emb_model(n_inp), emb_model(a_inp)
out = Concatenate()([ao, po, no])

model = Model(inputs=[p_inp, n_inp, a_inp], outputs=out)
model.compile(optimizer=Nadam(1e-3), loss=triplet_loss_distance)


# %%
x_train = train_df.iloc[:, 2:].values
y = train_df.loc[:, 'target'].values

# %%
model.fit_generator(DataGenerator(x_train, y, batch_size=1024), 
                    steps_per_epoch=1000,
                    epochs=15,
                    callbacks=[CyclicLR(base_lr=1*1e-3, max_lr=7*1e-3, step_size=500)])

# %%
x_emb = emb_model.predict(x_train, verbose=1)
x_emb_t = emb_model.predict(test_df.iloc[:, 1:].values, verbose=1)

np.savez('emb.npz', x=x_emb, xt=x_emb_t)

# %%
import matplotlib.pyplot as plt

# %%
from sklearn.decomposition import PCA

# %%
pca = PCA(n_components=2)
x_pca = pca.fit_transform(x_emb)

# %%
pca.explained_variance_ratio_

# %%
xep = x_pca[y==1]
xen = x_pca[y==0]

# %%
plt.figure(figsize=(10,10))

plt.scatter(xep[:, 0], xep[:, 1], alpha=0.9)
plt.scatter(xen[:, 0], xen[:, 1], alpha=0.3)

# %%

# %%
