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
import tensorflow as tf
import pandas as pd
import os
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras import Sequential
from keras import layers
from keras import backend as K
from keras.layers.core import Dense
from keras import regularizers
from keras.layers import Dropout
from keras.constraints import max_norm

# %% _cell_guid="79c7e3d0-c299-4dcb-8224-4455121ee9b0" _uuid="d629ff2d2480ee46fbb7e2d37f6b5fab8052498a"
# Import data
train = pd.read_csv('../input/train.csv')
test = pd.read_csv('../input/test.csv')

# %% _uuid="ef491a4d42450d6c0a79924621c27beebc33a5fa"
train.shape

# %% _uuid="977e678a7a750cd0a10ee37e1174f16680fd6b29"
test.shape

# %% _uuid="cd9b334eabd747735355d44c9e93044b0c47bb1f"
#Check num of cases in label 
print(train.target.value_counts())
print(train.target.value_counts()[1]/train.target.value_counts()[0])

# %% _uuid="4aa3662a015dee0cc8ef691e818adc96adfdcfd6"
train_features = train.drop(['target', 'ID_code'], axis=1)
train_targets = train['target']
test_features = test.drop(['ID_code'], axis=1)

# %% _uuid="a22d536c925cf641d2830c09066d16b574e9aa7b"
X_train, X_test, y_train, y_test = train_test_split(train_features, train_targets, test_size = 0.25, random_state = 50)

# %% _uuid="e0e3037ae4eaef75b7f3df50764c7ba4d018e29c"
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
test_features = sc.transform(test_features)


# %% _uuid="8bf12627db197ae404d751061796d6fdde047cc2"
# Add RUC metric to monitor NN
def auc(y_true, y_pred):
    auc = tf.metrics.auc(y_true, y_pred)[1]
    K.get_session().run(tf.local_variables_initializer())
    return auc


# %% _uuid="80489233dcc33baa361ea1b713058bb3730dfe9e"
input_dim = X_train.shape[1]
input_dim

# %% _uuid="79bda7f30f3b3627c9dbacb49542b9dc2c2f0677"
# Try early stopping
#from keras.callbacks import EarlyStopping
#callback = EarlyStopping(monitor='loss', min_delta=0, patience=10, verbose=0, mode='auto', baseline=None, restore_best_weights=True)

# %% _uuid="083001c4e3e3a32522cbb2cf7df0e55906cdcd7b"
model = Sequential()
# Input layer
model.add(Dense(units = 200, activation = "relu", input_dim = input_dim, kernel_initializer = "normal", kernel_regularizer=regularizers.l2(0.005), 
                kernel_constraint = max_norm(5.)))
# Add dropout regularization
model.add(Dropout(rate=0.2))

# First hidden layer
model.add(Dense(units = 200, activation='relu', kernel_regularizer=regularizers.l2(0.005), kernel_constraint=max_norm(5)))
# Add dropout regularization
model.add(Dropout(rate=0.1))

# Second hidden layer
model.add(Dense(100, activation='relu', kernel_regularizer=regularizers.l2(0.005), kernel_constraint=max_norm(5)))
# Add dropout regularization
model.add(Dropout(rate=0.1))

# Third hidden layer
model.add(Dense(50, activation='tanh', kernel_regularizer=regularizers.l2(0.005), kernel_constraint=max_norm(5)))
# Add dropout regularization
model.add(Dropout(rate=0.1))

# Output layer
model.add(layers.Dense(units = 1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy', auc])
model.summary()

# %% _uuid="85799af4ef45d3809e9cbb1903b98522ebbe8fa0"
model.fit(X_train, y_train, batch_size = 16384, epochs = 125, validation_data = (X_test, y_test))#, callbacks = [callback])

# %% _uuid="b5d848c12f5f5b08f3a4a2b089aa53a8d20f46f7"
y_pred = model.predict_proba(X_test)
roc_auc_score(y_test, y_pred)

# %% _uuid="89b22d2fcee7187cf033ff95f3ab621ba4c7dba9"
id_code_test = test['ID_code']
# Make predicitions
pred = model.predict(test_features)
pred_ = pred[:,0]

# %% _uuid="b594f20d96642cef8cd64a347c1bb04124c09fd1"
pred_

# %% _kg_hide-output=false _uuid="c8d5f4fc81d2b5a0091269425383577bb2707592"
# To CSV
my_submission = pd.DataFrame({"ID_code" : id_code_test, "target" : pred_})

# %% _uuid="20483d977735cfd3ea4a90ad7f6b1396a76b07e2"
my_submission

# %% _uuid="33d7f6d84ad3acfb88de49899f4db775ae7857d8"
my_submission.to_csv('submission.csv', index = False, header = True)

# %% _uuid="5b9c899f9688e19de9049e1cd6f65a8055eaea6d"
