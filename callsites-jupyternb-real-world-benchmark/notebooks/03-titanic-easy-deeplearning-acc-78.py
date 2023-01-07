# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% _uuid="8f2839f25d086af736a60e9eeb907d3b93b6e0e5" _cell_guid="b1076dfc-b9ad-4769-8c92-a6c4dae69d19"
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
train = pd.read_csv('/kaggle/input/titanic/train.csv')
train['Sec_Name'] = train['Name'].astype(str).str.split().str[1]
#print(train)
Y_train = np.array(train['Survived'])
X_train = train[['Pclass', 'Sex', 'Age', 'Embarked', 'Sec_Name']]
X_train = X_train.replace('male', 0)
X_train = X_train.replace('female', 1)
X_train['Embarked'] = X_train['Embarked'].replace('S',1)
X_train['Embarked'] = X_train['Embarked'].replace('C',2)
X_train['Embarked'] = X_train['Embarked'].replace('Q',3)
X_train = X_train.replace(np.nan, X_train['Age'].mean())
X_train['Sec_Name'] = X_train['Sec_Name'].replace('Mr.',1)
X_train['Sec_Name'] = X_train['Sec_Name'].replace('Mrs.',2)
X_train['Sec_Name'] = X_train['Sec_Name'].replace('Miss.',3)
X_train['Sec_Name'] = X_train['Sec_Name'].replace('Master.',4)
X_train['Sec_Name'] = pd.to_numeric(X_train['Sec_Name'], errors = 'coerce')
X_train['Sec_Name'] = X_train['Sec_Name'].replace(np.nan,0)
X_train = np.array(X_train)
print(X_train)


# %%
class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('accuracy') > 0.82):
            self.model.stop_training = True
callbacks = myCallback();

# %% _uuid="d629ff2d2480ee46fbb7e2d37f6b5fab8052498a" _cell_guid="79c7e3d0-c299-4dcb-8224-4455121ee9b0"
model = tf.keras.Sequential([keras.layers.Dense(5, input_dim = 5, activation = tf.nn.relu), tf.keras.layers.Dense(4, activation = tf.nn.relu), tf.keras.layers.Dense(3, activation = tf.nn.relu), tf.keras.layers.Dense(2, activation = tf.nn.relu), tf.keras.layers.Dense(1, activation = tf.nn.sigmoid)])
model.compile(optimizer="Adam", loss = 'binary_crossentropy', metrics = ['accuracy'])
model.fit(X_train, Y_train, validation_split=0.15,epochs = 100,batch_size=5, callbacks = [callbacks])

# %%
test = pd.read_csv('/kaggle/input/titanic/test.csv')
test['Sec_Name'] = test['Name'].astype(str).str.split().str[1]
X_test = test[['Pclass', 'Sex', 'Age', 'Embarked', 'Sec_Name']]
X_test = X_test.replace('male', 0)
X_test = X_test.replace('female', 1)
X_test = X_test.replace(np.nan, X_test['Age'].mean())
X_test['Embarked'] = X_test['Embarked'].replace('S',1)
X_test['Embarked'] = X_test['Embarked'].replace('C',2)
X_test['Embarked'] = X_test['Embarked'].replace('Q',3)
X_test['Sec_Name'] = X_test['Sec_Name'].replace('Mr.',1)
X_test['Sec_Name'] = X_test['Sec_Name'].replace('Mrs.',2)
X_test['Sec_Name'] = X_test['Sec_Name'].replace('Miss.',3)
X_test['Sec_Name'] = X_test['Sec_Name'].replace('Master.',4)
X_test['Sec_Name'] = pd.to_numeric(X_test['Sec_Name'], errors = 'coerce')
X_test['Sec_Name'] = X_test['Sec_Name'].replace(np.nan,0)
X_test = np.array(X_test)
p = model.predict(X_test)
p = np.where(p >= 0.5, 1, 0)
#model.evaluate(x_test, y_test)
#np.savetxt("test_ans4.csv", p, delimiter=",")
df_sub = pd.DataFrame()
df_sub['PassengerId'] = test['PassengerId']
df_sub['Survived'] = p.astype(np.int)

df_sub.to_csv('submission4.csv', index=False)

# %%
