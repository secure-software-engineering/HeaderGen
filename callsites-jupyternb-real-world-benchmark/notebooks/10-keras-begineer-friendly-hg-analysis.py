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
df = pd.read_csv('../input/competitive-data-science-predict-future-sales/sales_train.csv')
sample = pd.read_csv('../input/competitive-data-science-predict-future-sales/sample_submission.csv')

# %%
df.head()

# %%
sample.head()

# %%
items = pd.read_csv('../input/competitive-data-science-predict-future-sales/items.csv')
items_category = pd.read_csv('../input/competitive-data-science-predict-future-sales/item_categories.csv')
shops = pd.read_csv('../input/competitive-data-science-predict-future-sales/shops.csv')

# %%
items.head()

# %%
items.shape

# %%
items_category.shape

# %%
items.head(5)

# %%
items = items.drop(columns = ['item_name','item_name'])

# %%
items_category.head()

# %%
shops.head()

# %%
shops.shape

# %%
category = []
for i in df['item_id']:
    category.append(items['item_category_id'][i])

# %%
print(category[0:20])

# %%
items.iloc[22154,:]

# %%
df['item_category_id'] = category

# %%
df.head()

# %%
data = df[df['item_cnt_day']<=50]

# %%
data = data[data['item_cnt_day']>-3]

# %%
data.shape

# %%
df.shape

# %%
len(data['item_cnt_day'].unique())

# %%
data_train = data.drop(columns = ['item_cnt_day','item_id','date'])

# %%
target = data['item_cnt_day']

# %%
print(target.value_counts())

# %%
# temp = data.value_counts()
# import matplotlib.pyplot as plt
# plt.plot(temp[:])

# %%
data.shape

# %%
data.head()

# %%
data.drop(columns = ['date','item_id'],inplace = True)

# %%
date_block = []
for i in data['date_block_num']:
    date_block.append(i%12)
        

# %%
data['date_block_engineered'] = date_block

# %%
data['date_block_engineered'].unique()

# %%
data.drop(columns = ['date_block_num'],inplace = True)

# %%
data.head()

# %%
import tensorflow.keras as keras

# %%
labels = data['item_cnt_day']

# %%
len(labels.unique())

# %%
# labels = pd.get_dummies(labels)

# %%
labels.head()

# %%
labels.shape

# %%
data.head()

# %%
data = data.drop(columns = ['item_cnt_day'])

# %%
data.shape

# %%
labels.shape

# %%
label = labels.transpose()

# %%
keras.backend.clear_session()
model = keras.models.Sequential([
    keras.layers.Dense(3,input_dim = 2,activation = 'relu'),
    keras.layers.Dense(1,activation = 'relu')
])
early = keras.callbacks.EarlyStopping(patience = 5)
model_check = keras.callbacks.ModelCheckpoint('model.h5',save_best_only = True)
model.compile(loss = 'mse',optimizer = 'adam',metrics = ['accuracy'])


# %%
data.head()

# %%
data_x = data.drop(columns = ['date_block_engineered','item_price'])

# %%
data_x.head()

# %%
model.fit(data_x,labels,epochs = 500,validation_split = 0.2,callbacks = [early,model_check],batch_size = 64)

# %%
test = pd.read_csv('../input/competitive-data-science-predict-future-sales/test.csv')

# %%
item_category = []
for i in test['item_id']:
    item_category.append(items['item_category_id'][i])

# %%
test['item_category_id'] = item_category

# %%
test.head()

# %%
# df_sorted = df.sort_values(['item_id'])

# %%
# df_sorted.head()

# %%
test = test.drop(columns = ['ID','item_id'])

# %%
predictions = model.predict(test)

# %%
predictions = pd.DataFrame(predictions)

# %%
predictions.head()

# %%
pred = []
for i in predictions[0]:
    pred.append(round(i))

# %%
predictions['item_cnt_day'] = pred

# %%
predictions.head()

# %%
test = pd.read_csv('../input/competitive-data-science-predict-future-sales/test.csv')

# %%
predictions['ID'] = test['ID']

# %%
predictions.head()

# %%
predictions = predictions.drop(columns = [0])

# %%
predictions.head()

# %%
predictions.to_csv('Submit_1.csv',index = False)

# %%
predictions.columns = ['item_cnt_month','ID']

# %%
predictions.to_csv('Submit_2.csv',index = False)

# %%
