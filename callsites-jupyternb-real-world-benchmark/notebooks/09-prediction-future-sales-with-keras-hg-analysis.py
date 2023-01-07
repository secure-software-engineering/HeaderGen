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
train = pd.read_csv('/kaggle/input/competitive-data-science-predict-future-sales/sales_train.csv')
train.head(2)

# %%
item = pd.read_csv('/kaggle/input/competitive-data-science-predict-future-sales/items.csv')
item.head(2)

# %%
cat = pd.read_csv('/kaggle/input/competitive-data-science-predict-future-sales/item_categories.csv')
cat.head(2)

# %%
shop = pd.read_csv('/kaggle/input/competitive-data-science-predict-future-sales/shops.csv')
shop.head(2)

# %%
test = pd.read_csv('/kaggle/input/competitive-data-science-predict-future-sales/test.csv')
test.head(2)

# %%
train.head()

# %%
test.shape

# %%
submission = pd.read_csv('/kaggle/input/competitive-data-science-predict-future-sales/sample_submission.csv')
submission.head(2)

# %%
submission.shape

# %%
train.shape

# %%
train = train[train.item_id.isin (test.item_id)]
train = train[train.shop_id.isin (test.shop_id)]

# %%
train.info()

# %%
train.head()

# %%
train.drop(['date'],axis=1,inplace=True)

# %%
test.head()

# %%
train['date_block_num']

# %%
test['date_block_num'] = 34
test = test[['date_block_num','shop_id','item_id']]
test.head(2)

# %%
item_price = dict(train.groupby('item_id')['item_price'].last().reset_index().values)

# %%
test['item_price'] = test.item_id.map(item_price)
test.head()

# %%
test.isnull().sum()

# %%
train.shape, test.shape

# %%
train = train[train.item_id.isin (test.item_id)]
train = train[train.shop_id.isin (test.shop_id)]

# %%
train.shape, test.shape

# %%
test.isnull().sum()

# %%
train['shop*item'] = train.shop_id *train.item_id
test['shop*item'] = test.shop_id *test.item_id

# %%
item.head()
item.drop('item_name',axis=1,inplace = True)

# %%
item_cat = dict(item.values)
train['item_cat'] = train.item_id.map(item_cat)
test['item_cat'] = test.item_id.map(item_cat)


# %%
train.head(2)

# %%
train.info()

# %%
import seaborn as sns
import matplotlib.pyplot as plt

# %%
df = pd.concat([train,test])

# %%
sns.histplot(df['item_price']);

# %%

df = pd.concat([train,test])
#Normalize
df.item_price = np.log1p(df.item_price)
#fil l the missing
df.item_price = df.item_price.fillna(df.item_price.mean())

#rremove the outlier
df.item_cnt_day = df.item_cnt_day.apply(lambda x : 10 if x>10 else x)

# %%
train = df[df.item_cnt_day.notnull()]
test = df[df.item_cnt_day.isnull()]

# %%
train.shape

# %%
test.isnull().sum()

# %%
test.drop('item_cnt_day',axis = 1,inplace  = True)

# %%
test.shape

# %%
x_train = train.drop('item_cnt_day',axis = 1).values
y_train = train.item_cnt_day.values

# %%
x_test = test

# %%
from sklearn.preprocessing import MinMaxScaler
SC = MinMaxScaler()
#SC = StandardScaler()
x_train = SC.fit_transform(x_train)
x_test = SC.transform(x_test)

# %%
import keras 
from keras.models import Sequential 
from keras.layers import Dense

# %%

# Initialising the NN
model = Sequential()

# layers
model.add(Dense(9, kernel_initializer = 'uniform', activation = 'relu', input_dim = 6))
model.add(Dense(9, kernel_initializer = 'uniform', activation = 'relu'))
model.add(Dense(5, kernel_initializer = 'uniform', activation = 'relu'))
model.add(Dense(1, kernel_initializer = 'uniform', activation = 'linear'))

# summary
model.summary()

# %%
model.compile(optimizer = 'adam', loss = 'mean_absolute_error', metrics = ['mse','mae'])


# %%
history = model.fit(x_train, y_train, epochs=32, validation_split=0.2)


# %%
from sklearn.metrics import mean_squared_error
pred_train= model.predict(x_train)
print(np.sqrt(mean_squared_error(y_train,pred_train)))

# %%
y_pred = model.predict(x_test).flatten()

# %%
output = pd.DataFrame({'ID': submission['ID'], 'item_cnt_month': y_pred})
output.to_csv('submission1.csv', index=False)

# %%
pred=pd.DataFrame(y_pred)
datasets=pd.concat([submission['ID'],pred],axis=1)
datasets.columns=['ID','item_cnt_day']
datasets.to_csv('new_submission.csv',index=False)

# %%
