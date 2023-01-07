# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% _uuid="8f2839f25d086af736a60e9eeb907d3b93b6e0e5" _cell_guid="b1076dfc-b9ad-4769-8c92-a6c4dae69d19"
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns

from keras.regularizers import l1
from keras import backend as K

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from scipy.stats import skew
from scipy.stats.stats import pearsonr

import matplotlib.pyplot as plt
# %matplotlib inline

import csv
import re

from keras.models import Sequential
from keras.layers import Dense, Activation, BatchNormalization, Dropout
from keras.callbacks import ModelCheckpoint
from keras.optimizers import Adam

# ignore Deprecation Warning
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

import os

train_orj = pd.read_csv("../input/train.csv", header=0)
test_orj = pd.read_csv("../input/test.csv", header=0)
train_orj.head()
# Any results you write to the current directory are saved as output.

# %% _cell_guid="79c7e3d0-c299-4dcb-8224-4455121ee9b0" _uuid="d629ff2d2480ee46fbb7e2d37f6b5fab8052498a"
train_orj.info()


# %% _uuid="facfa03728a1b6f9022048d24900fb877419c784"
def preprocess(data):
    
    #Kabin
    data.Cabin.fillna('9', inplace=True)
    #data['Cabin'].replace('0', 9, inplace=True)
    data.loc[data.Cabin.str[0] == 'A', 'Cabin'] = 1
    data.loc[data.Cabin.str[0] == 'B', 'Cabin'] = 2
    data.loc[data.Cabin.str[0] == 'C', 'Cabin'] = 3
    data.loc[data.Cabin.str[0] == 'D', 'Cabin'] = 4
    data.loc[data.Cabin.str[0] == 'E', 'Cabin'] = 5
    data.loc[data.Cabin.str[0] == 'F', 'Cabin'] = 6
    data.loc[data.Cabin.str[0] == 'G', 'Cabin'] = 7
    data.loc[data.Cabin.str[0] == 'T', 'Cabin'] = 8
    data = data.drop(["Cabin"],axis=1)

    # Cinsiyeti tam sayıya çevirelim
    data['Sex'].replace('female', 1, inplace=True)
    data['Sex'].replace('male', 2, inplace=True)
    
    # Gemiye biniş limanlarını tam sayıya çevirelim
    data['Embarked'].replace('S', 1, inplace=True)
    data['Embarked'].replace('C', 2, inplace=True)
    data['Embarked'].replace('Q', 3, inplace=True)
    
    # Olmayan (NA) yaş değerlerini medyan ile dolduralım
    data['Age'].fillna(data['Age'].median(), inplace=True)
    #data['Age'] = [0 if each >= 60 else 1 if each >= 35 else 2 if each >= 18 else 3 if each >= 12 else 4 if each >= 5 else 5 for each in data['Age']]
   
    data['Fare'].fillna(data['Fare'].median(), inplace=True)
    data['Embarked'].fillna(data['Embarked'].median(), inplace=True)
    
    data = data.drop(["Ticket"],axis=1)
    data = data.drop(["Fare"],axis=1)
    data['SibSp'].replace(0, 9, inplace=True)
    data['Parch'].replace(0, 9, inplace=True)
    return data

def group_titles(data):
    #data['Names'] = data['Name'].map(lambda x: len(re.split(' ', x)))
    data['Title'] = data['Name'].map(lambda x: re.search(', (.+?) ', x).group(1))
    data['Title'].replace('Master.', 1, inplace=True)
    data['Title'].replace('Mr.', 2, inplace=True)
    data['Title'].replace(['Ms.','Mlle.', 'Miss.'], 3, inplace=True)
    data['Title'].replace(['Mme.', 'Mrs.'], 4, inplace=True)
    data['Title'].replace(['Dona.', 'Lady.', 'the Countess.', 'Capt.', 'Col.', 'Don.', 'Dr.', 'Major.', 'Rev.', 'Sir.', 'Jonkheer.', 'the'], 5, inplace=True)
    return data


# %% _uuid="d05c1efea8ba5e4e3008d395df3a3abed3ad572a"
train = train_orj.copy().drop(["PassengerId"],axis=1)
train=preprocess(train)
train=group_titles(train)
train = train.drop(["Name"],axis=1)
train.head()

# %% _uuid="8a29acfbda9afd7569858a496b42b841f73f2510"
train.info()

# %% _uuid="499a867e84b4afc5b6e7f94d238ef3193d5bdc24"
plt.figure(figsize=(10,5))
sns.countplot(train.Age, palette="icefire")
#train.Age.value_counts()

# %% _uuid="299a4f206b1dba1e38edd31e9f67d87cd2a1bd5b"
x = train.iloc[:,1:train.shape[1]].values #bağımsız değişkenler
y = train.Survived.values

from sklearn.model_selection import train_test_split
X_train, X_val, Y_train, Y_val = train_test_split(x, y, test_size = 0.1, random_state=2)
print("x_train shape",X_train.shape)
print("x_test shape",X_val.shape)
print("y_train shape",Y_train.shape)
print("y_test shape",Y_val.shape)


#Y_train=np.array(Y_train).astype(int)
#X_train=np.array(X_train).astype(float)
#Y_val = np.array(Y_val).astype(int)
#X_val = np.array(X_val).astype(float)

# %% _uuid="8981e7fcb315c6aece7948257d5d804ed9a42995"
plt.figure(figsize=(10,5))
sns.countplot(Y_train, palette="icefire")
plt.title("Number of Survived classes")

# %% _uuid="760749aad03ad34562ba669eab9f2c8c961ef50e"
#model 1
'''
num_epochs = 200
batch_size = 32

model = Sequential()
model.add(Dense(64, input_dim=input_length-1, activation='softplus'))
model.add(Dense(32, activation='softplus'))
model.add(Dense(16, activation='softplus'))  
model.add(Dense(8, activation='softplus')) 
model.add(Dense(1, activation='softplus'))

lr = .001
adam0 = Adam(lr = lr)

# Modeli derleyip ve daha iyi bir sonuç elde edildiğinde ağırlıkları kaydedelim
model.compile(loss='binary_crossentropy', optimizer=adam0, metrics=['accuracy'])
filepath = 'weights.best.hdf5'
checkpoint = ModelCheckpoint(filepath, monitor='acc', verbose=1, save_best_only=True, mode='max')
callbacks_list = [checkpoint]

history_model = model.fit(X_train, Y_train, callbacks=callbacks_list, epochs=num_epochs, batch_size=batch_size, verbose=0)

'''

# %% _uuid="e943c35d044c8e76eb83baad9b7b420f383a1333"
# model 2
model = Sequential()

# layers
model.add(Dense(units = 128, kernel_initializer = 'uniform', activation = 'relu', input_dim = X_train.shape[1]))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(units = 64, kernel_initializer = 'uniform', activation = 'relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(units = 32, kernel_initializer = 'uniform', activation = 'relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(units = 16, kernel_initializer = 'uniform', activation = 'relu'))
model.add(Dropout(0.3))
model.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
optimizer = Adam(lr=0.001, beta_1=0.9, beta_2=0.999)
model.compile(optimizer = optimizer, loss = 'binary_crossentropy', metrics = ['accuracy'])

# Train the ANN
history = model.fit(X_train, Y_train, batch_size = 32, epochs = 300, validation_data = (X_val,Y_val))

scores = model.evaluate(X_train, Y_train, verbose=0)
print("%s: %.3f%%" % (model.metrics_names[1], scores[1]*100))

# %% _uuid="487c5432ed4a6ef8f5e2583e1a93423716e6350f"
# Plot the loss and accuracy curves for training and validation 
plt.plot(history.history['val_loss'], color='b', label="validation loss")
plt.xlabel("Number of Epochs")
plt.ylabel("Loss")
plt.legend()
plt.show()

# %% _uuid="f6be620cee72b5b9f411c0daa3ab4dadbe58f223"
# confusion matrix
import seaborn as sns
from sklearn.metrics import confusion_matrix
# Predict the values from the validation dataset
y_pred = model.predict(X_val)
y_final = (y_pred > 0.5).astype(int).reshape(X_val.shape[0])
# compute the confusion matrix
confusion_mtx = confusion_matrix(Y_val, y_final) 
# plot the confusion matrix
f,ax = plt.subplots(figsize=(8, 8))
sns.heatmap(confusion_mtx, annot=True, linewidths=0.01,cmap="Greens",linecolor="gray", fmt= '.1f',ax=ax)
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix")
plt.show()

# %% _uuid="eced493bb8226d199354caefee1bb69e15e8bc28"
# model 3
'''
from keras.layers import Input
import keras
from keras.models import Model

def DenseNet(X_train):
    ip = Input(shape=(X_train.shape[1],))
    x_list = [ip]
    
    x = Dense(128, use_bias=False)(ip)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = Dropout(0.5)(x)

    x_list.append(x)
    x = keras.layers.concatenate(x_list)    
    x = Dense(128, use_bias=False)(x)    
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = Dropout(0.5)(x)

    x_list.append(x)
    x = keras.layers.concatenate(x_list)    
    x = Dense(64, use_bias=False)(x)    
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = Dropout(0.5)(x)

    x_list.append(x)
    x = keras.layers.concatenate(x_list)    
    x = Dense(64, use_bias=False)(x)    
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = Dropout(0.5)(x)

    x_list.append(x)
    x = keras.layers.concatenate(x_list)    
    x = Dense(32, use_bias=False)(x)    
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = Dropout(0.5)(x)

    x_list.append(x)
    x = keras.layers.concatenate(x_list)    
    x = Dense(32, use_bias=False)(x)    
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = Dropout(0.5)(x)

    x_list.append(x)
    x = keras.layers.concatenate(x_list)    
    x = Dense(16, use_bias=False)(x)    
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = Dropout(0.5)(x)
    
    x_list.append(x)
    x = keras.layers.concatenate(x_list)    
    x = Dense(16, use_bias=False)(ip)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = Dropout(0.5)(x)    
    
    op = Dense(1, activation='sigmoid')(x)

    model = Model(inputs=ip, outputs=op)
    adam = Adam(lr=0.05,)
    model.compile(loss='binary_crossentropy', optimizer=adam, metrics=['accuracy'])
    return model

model = DenseNet(X_train)
history_model=model.fit(X_train, Y_train, epochs=32, batch_size=200, verbose=0,
          validation_split=0.1)
scores = model.evaluate(X_train, Y_train, verbose=0)
print("%s: %.3f%%" % (model.metrics_names[1], scores[1]*100))
'''

# %% _uuid="417caaedebc5cd53925d6b69a0639a2db2c91364"
test = test_orj.copy()
test=preprocess(test)
test=group_titles(test)
test = test.drop(["Name"],axis=1)
test.head()
#print(test.Title.value_counts())
test.info()

# %% _uuid="959d59cae62b742c04c82b04530de86acc96ea67"
sns.countplot(test.Age, palette="icefire")
#train.Age.value_counts()

# %% _uuid="816ff32b1086e438cd245d46c927bd81346eadfc"
test_ids = test.iloc[:,0].values #test_orj['PassengerId'].copy()
testdata = test.iloc[:,1:test.shape[1]].values #bağımsız değişkenler
X_test =testdata # np.array(testdata).astype(float)

#print(len(X_test))
#print(X_test[0])

y_pred = model.predict(X_test)
y_final = (y_pred > 0.5).astype(int).reshape(X_test.shape[0])
#print(len(y_final))
output = pd.DataFrame({'PassengerId': test_orj['PassengerId'], 'Survived': y_final})
output.to_csv('prediction-ann_0150.csv', index=False)

plt.figure(figsize=(10,5))
sns.countplot(y_final, palette="icefire")
plt.title("(Test data) Number of Survived classes")
