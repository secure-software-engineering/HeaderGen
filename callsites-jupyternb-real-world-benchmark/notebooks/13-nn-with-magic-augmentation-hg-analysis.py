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

# %%
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.metrics import roc_auc_score, log_loss
import pandas as pd
import numpy as np
import time
import random
from tqdm import tqdm
import warnings
warnings.filterwarnings('ignore')

import torch
from torch import nn
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader

MODEL_PATH = ''


train_df = pd.read_csv('../input/santander-customer-transaction-prediction/train.csv',index_col='ID_code')
test_df = pd.read_csv('../input/santander-customer-transaction-prediction/test.csv',index_col='ID_code')

synthetic_indices = np.load('../input/synthetissantandersamples/synthetic_samples_indexes.npy')
mask=np.full(len(test_df),True,dtype=bool)
mask[synthetic_indices]=False
test_df_nonsynthetic = test_df.iloc[mask].reset_index(drop=True).copy()


y = train_df.pop('target')
target = y

tr_te = pd.concat([train_df,test_df])

num_cols = [c for c in train_df.columns]

for f in tqdm(num_cols):
    tr_te[f+'_counts'] = tr_te[f].map(pd.concat([train_df[f], test_df_nonsynthetic[f]], axis=0).value_counts().to_dict(), na_action='ignore')
    tr_te[f+'_counts'] = tr_te[f+'_counts'].fillna(1)


count_cols = [f+'_counts' for f in num_cols]


from scipy.special import erfinv
from scipy.stats import rankdata

def rankgauss(x):
    r = (rankdata(x) - 1) / len(x)  # to [0,1]
    r = 2 * r - 1  # to [-1,1]
    r = np.clip(r, -0.99, 0.99)
    r2 = erfinv(r)
    return r2




print('scaling num_cols')
for col in num_cols + count_cols:
    print('scaling {}'.format(col))
    col_mean = tr_te[col].mean()
    col_std = tr_te[col].std()
    tr_te[col].fillna(col_mean, inplace=True)
    tr_te[col] = rankgauss(tr_te[col].values)


train_df = tr_te[0:train_df.shape[0]]
test_df = tr_te[train_df.shape[0]:]





X = np.stack([train_df[num_cols].values,train_df[count_cols].values],axis = -1)
X_test = np.stack([test_df[num_cols].values,test_df[count_cols].values],axis = -1)
#X = train_df[num_cols].values

def augment_counts(x, y, t_pos, t_neg):
    xs,xn = [],[]
    for i in range(t_pos):
        mask = y>0
        x1 = x[mask].copy()
        ids = np.arange(x1.shape[0])
        for c in range(200):
            np.random.shuffle(ids)
            x1[:,c] = x1[ids][:,c]
            #x1[:,c+200] = x1[ids][:,c+200]
        xs.append(x1)

    for i in range(t_neg):
        mask = y==0
        x1 = x[mask].copy()
        ids = np.arange(x1.shape[0])
        for c in range(200):
            np.random.shuffle(ids)
            x1[:,c] = x1[ids][:,c]
            #x1[:,c+200] = x1[ids][:,c+200]
        xn.append(x1)

    xs = np.vstack(xs)
    xn = np.vstack(xn)
    ys = np.ones(xs.shape[0])
    yn = np.zeros(xn.shape[0])
    x = np.vstack([x,xs,xn])
    y = np.concatenate([y,ys,yn])
    return x,y

from keras import layers as L
import keras.backend as K
from keras.models import Model
from keras.optimizers import Adam
from keras.losses import binary_crossentropy
from keras.callbacks import ModelCheckpoint
def build_model():
    inp = L.Input((200,2))
    x = L.Dense(64)(inp)
    x = L.PReLU()(x)
    x = L.BatchNormalization()(x)
    x = L.Dropout(0.2)(x)
    x = L.Dense(8)(x)
    x = L.PReLU()(x)
    x = L.Flatten()(x)
    out = L.Dense(1,activation='sigmoid')(x)

    m = Model(inp,out)
    print(m.summary())
    return m

num_folds = 5
folds = StratifiedKFold(n_splits=num_folds, shuffle=True, random_state=42)
splits = list(folds.split(train_df.values, target.values))

oof_preds = np.zeros(y.shape)
test_preds = np.zeros(X_test.shape[0])

from keras.callbacks import ReduceLROnPlateau

for fold_ in [0, 1, 2, 3, 4]:
    trn_idx, val_idx = splits[fold_]

    X_train, y_train = X[trn_idx], y[trn_idx]
    X_valid, y_valid = X[val_idx], y[val_idx]
    
    X_train, y_train = augment_counts(X_train, y_train, 2, 1)

    m = build_model()
    ckpt = ModelCheckpoint(MODEL_PATH + 'nn{}.hdf5'.format(fold_), save_best_only=True, verbose=True)
    pl = ReduceLROnPlateau(factor=0.5,patience=5)
    m.compile(optimizer=Adam(), loss=binary_crossentropy)
    m.fit(X_train, y_train, validation_data=(X_valid, y_valid), epochs=20, verbose=1, callbacks=[ckpt,pl], batch_size = 256)
    m.load_weights(MODEL_PATH + 'nn{}.hdf5'.format(fold_))
    oof_preds[val_idx] = m.predict(X_valid)[:, 0]
    test_preds += m.predict(X_test)[:,0]
test_preds/= 5



np.save(MODEL_PATH + 'oof_NN13b_aug.npy',oof_preds)
np.save(MODEL_PATH + 'sub_NN13b_aug.npy',test_preds)

# %%
submission = pd.read_csv('../input/santander-customer-transaction-prediction/sample_submission.csv')
submission['target'] = test_preds
submission.to_csv(MODEL_PATH + 'submission.csv',index=False)

# %%
