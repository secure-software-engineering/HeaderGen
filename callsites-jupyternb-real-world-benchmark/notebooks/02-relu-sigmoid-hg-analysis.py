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
import pandas as pd
import numpy as np
import h5py
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.optimizers import Adam
from keras.optimizers import SGD
import matplotlib.pyplot as plt
from keras.models import load_model

# %%
train_df = pd.read_csv("../input/titanic/train.csv")
test_df = pd.read_csv("../input/titanic/test.csv")

# %%
train_df['Age'].fillna((train_df['Age'].mean()),inplace=True)

test_df['Age'].fillna((test_df['Age'].mean()),inplace=True)

train_df['Sex'] = train_df['Sex'].replace('male',value = 1)
train_df['Sex'] = train_df['Sex'].replace('female',value = 0)

test_df['Sex'] = test_df['Sex'].replace('male',value = 1)
test_df['Sex'] = test_df['Sex'].replace('female',value = 0)

# %%
train_df.describe()

# %%
n_train = 700
X_train_class = train_df["Pclass"].values.reshape(-1,1)
X_train_sex = train_df["Sex"].values.reshape(-1,1)
X_train_age = train_df["Age"].values.reshape(-1,1)
X_train_sib = train_df["SibSp"].values.reshape(-1,1)
X_train_par = train_df["Parch"].values.reshape(-1,1)


y = train_df["Survived"].values.T

# %%
X_train = np.hstack((X_train_sex[:n_train,:],X_train_class[:n_train,:],X_train_sib[:n_train,:],X_train_age[:n_train,:],X_train_par[:n_train,:]))
X_test = np.hstack((X_train_sex[n_train:,:],X_train_class[n_train:,:],X_train_sib[n_train:,:],X_train_age[n_train:,:],X_train_par[n_train:,:]))
X_train, X_test = tf.convert_to_tensor(X_train.astype(np.float64)),tf.convert_to_tensor(X_test.astype(np.float64))
y_train, y_test = y[:n_train], y[n_train:]

# %%
model = Sequential()
model.add(Dense(300,input_dim=5,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(150,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(100,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(50,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(25,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.01,beta_1=0.99,beta_2=0.999), metrics=['accuracy'])

# %%
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs = 300, verbose = 0)

# %%
_, train_acc = model.evaluate(X_train, y_train, verbose=2)
_, test_acc = model.evaluate(X_test, y_test, verbose=2)
print('Train: %.3f, Test: %.3f' % (train_acc, test_acc))

plt.plot(history.history['accuracy'], label='train')
plt.plot(history.history['val_accuracy'], label='test')
plt.legend()
plt.show()

# %%
model.save('model_' + str(1) + '.h5')

# %%
model = load_model("./model_1.h5")
model.summary()

# %%
X_test_class = test_df["Pclass"].values.reshape(-1,1)
X_test_sex = test_df["Sex"].values.reshape(-1,1)
X_test_age = test_df["Age"].values.reshape(-1,1)
X_test_sib = test_df["SibSp"].values.reshape(-1,1)
X_test_par = test_df["Parch"].values.reshape(-1,1)

x_test = np.hstack((X_test_sex,X_test_class,X_test_sib,X_test_age,X_test_par)).astype(np.float64)

# %%
y_pred =[]
prediction = model.predict(x_test).ravel().tolist()
y_pred += prediction

# %%
for i in range(0,len(y_pred)):
    if y_pred[i] > 0.8:
        y_pred[i] = 1
    else:
        y_pred[i] = 0

# %%
submission = pd.read_csv('../input/titanic/gender_submission.csv')
submission['Survived'] = y_pred
submission.to_csv('submission.csv',index=False)

# %%
