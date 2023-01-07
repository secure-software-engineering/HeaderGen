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
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

# %%
import matplotlib.pyplot as plt 
# %matplotlib inline 
import seaborn as sns

# %%
df_Train=pd.read_csv('/kaggle/input/titanic/train.csv')
df_Test=pd.read_csv('/kaggle/input/titanic/test.csv')

# %%
df_Train.head()

# %%
df_Test.head()

# %%
df_Train.isnull().sum()

# %%
df_Test.isnull().sum()


# %%
def bar_chart(feature):
    survived = df_Train[df_Train['Survived']==1][feature].value_counts()
    dead = df_Train[df_Train['Survived']==0][feature].value_counts()
    df = pd.DataFrame([survived,dead])
    df.index = ['Survived','Dead']
    df.plot(kind='bar',stacked=True, figsize=(10,5))


# %%
bar_chart('Sex')

# %%
bar_chart('Pclass')

# %%
bar_chart('Embarked')

# %%
#Deleting unneccesary columns
df_Train.drop('Name', axis=1, inplace=True)
df_Test.drop('Name', axis=1, inplace=True)

# %%
df_Train.head()

# %%
df_Test.head()

# %%
df_Train.Sex[df_Train.Sex == 'male'] = 1
df_Train.Sex[df_Train.Sex == 'female'] = 2

df_Test.Sex[df_Test.Sex == 'male'] = 1
df_Test.Sex[df_Test.Sex == 'female'] = 2

# %%
df_Train.Embarked[df_Train.Embarked == 'Q'] = 1
df_Train.Embarked[df_Train.Embarked == 'S'] = 2
df_Train.Embarked[df_Train.Embarked == 'C'] = 3

df_Test.Embarked[df_Test.Embarked == 'Q'] = 1
df_Test.Embarked[df_Test.Embarked == 'S'] = 2
df_Test.Embarked[df_Test.Embarked == 'C'] = 3

# %%
df_Train['Age']=df_Train['Age'].fillna(df_Train['Age'].mode()[0])
df_Test['Age']=df_Test['Age'].fillna(df_Test['Age'].mode()[0])

df_Train['Embarked']=df_Train['Embarked'].fillna(df_Train['Embarked'].mode()[0])
df_Test['Fare']=df_Test['Fare'].fillna(df_Test['Fare'].mode()[0])

# %%
sns.heatmap(df_Train.isnull(),yticklabels=False,cbar=False)

# %%
sns.heatmap(df_Test.isnull(),yticklabels=False,cbar=False)

# %%
df_Train.drop(['Cabin'],axis=1,inplace=True)
df_Test.drop(['Cabin'],axis=1,inplace=True)

df_Train.drop(['Ticket'],axis=1,inplace=True)
df_Test.drop(['Ticket'],axis=1,inplace=True)

# %%
df_Train.head()

# %%
df_Test.head()

# %%
df_Train.Fare[df_Train.Fare <= 17] = 1
df_Train.Fare[(df_Train.Fare > 17) & (df_Train.Fare <= 30)] = 2
df_Train.Fare[(df_Train.Fare > 30) & (df_Train.Fare <= 100)] = 3
df_Train.Fare[df_Train.Fare > 100] = 4

df_Test.Fare[df_Test.Fare <= 17] = 1
df_Test.Fare[(df_Test.Fare > 17) & (df_Test.Fare <= 30)] = 2
df_Test.Fare[(df_Test.Fare > 30) & (df_Test.Fare <= 100)] = 3
df_Test.Fare[df_Test.Fare > 100] = 4

# %%
df_Train.Age[df_Train.Age <= 16] = 0
df_Train.Age[(df_Train.Age > 16) & (df_Train.Age <= 26)] = 1
df_Train.Age[(df_Train.Age > 26) & (df_Train.Age <= 36)] = 2
df_Train.Age[(df_Train.Age > 36) & (df_Train.Age <= 62)] = 3
df_Train.Age[df_Train.Age > 62] = 4

df_Test.Age[df_Test.Age <= 16] = 0
df_Test.Age[(df_Test.Age > 16) & (df_Test.Age <= 26)] = 1
df_Test.Age[(df_Test.Age > 26) & (df_Test.Age <= 36)] = 2
df_Test.Age[(df_Test.Age > 36) & (df_Test.Age <= 62)] = 3
df_Test.Age[df_Test.Age > 62] = 4

# %%
df_Train.head()

# %%
df_Test.head()

# %%
X=df_Train[['PassengerId','Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']]
y=df_Train[['Survived']]

# %%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# %%
df_Train.isnull().sum()

# %%
df_Test.dtypes

# %%
df_Test['Sex'] = df_Test['Sex'].astype(int) 
df_Test['Embarked'] = df_Test['Embarked'].astype(int)
df_Test.dtypes

# %%
df_Test.isnull().sum()

# %%
df_Test

# %%
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
df_Test1 = sc.fit_transform(df_Test)
df_Test1

# %%
X.shape

# %%
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# %%
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LeakyReLU,PReLU,ELU
from keras.layers import Dropout

# %%
classifier = Sequential()
classifier.add(Dense(units = 20, kernel_initializer = 'he_uniform',activation='relu',input_dim = 8))
classifier.add(Dense(units = 10, kernel_initializer = 'he_uniform',activation='relu'))
classifier.add(Dense(units = 15, kernel_initializer = 'he_uniform',activation='relu'))
classifier.add(Dense(units = 1, kernel_initializer = 'glorot_uniform', activation = 'sigmoid'))

classifier.compile(optimizer = 'Adamax', loss = 'binary_crossentropy', metrics = ['accuracy'])

# %%
model=classifier.fit(X_train, y_train, validation_split=0.350, batch_size = 5, epochs = 100)

# %%
y_pred = classifier.predict(df_Test1)
y_pred = (y_pred > 0.5) #returns values in True / False in a list of lists format

# Converting True and False values to int
y_pred_int = y_pred.astype(int)

# Coverting list of list to 1 flat list
y_pred_list = [item for sublist in y_pred_int for item in sublist]

# Converting the flat list to np array
y_pred1 = np.asarray(y_pred_list , dtype = int)

# %%
y_pred1

# %%
output = pd.DataFrame({'PassengerId': df_Test.PassengerId, 'Survived': y_pred1})
output.to_csv('my_submission15.csv', index=False)

# %%
