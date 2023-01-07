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

# You can write up to 5GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

# %% _uuid="d629ff2d2480ee46fbb7e2d37f6b5fab8052498a" _cell_guid="79c7e3d0-c299-4dcb-8224-4455121ee9b0"
import numpy as np
import pandas as pd 

# %%
sales_data = pd.read_csv('../input/competitive-data-science-predict-future-sales/sales_train.csv')
item_cat = pd.read_csv('../input/competitive-data-science-predict-future-sales/item_categories.csv')
items = pd.read_csv('../input/competitive-data-science-predict-future-sales/items.csv')
shops = pd.read_csv('../input/competitive-data-science-predict-future-sales/shops.csv')
sample_submission = pd.read_csv('../input/competitive-data-science-predict-future-sales/sample_submission.csv')
test_data = pd.read_csv('../input/competitive-data-science-predict-future-sales/test.csv')


# %%
def basic_eda(df):

    print("----------TOP 5 RECORDS--------")
    print(df.head(5))
    print("----------INFO-----------------")
    print(df.info())
    print("----------Describe-------------")
    print(df.describe())
    print("----------Columns--------------")
    print(df.columns)
    print("----------Data Types-----------")
    print(df.dtypes)
    print("-------Missing Values----------")
    print(df.isnull().sum())
    print("-------NULL values-------------")
    print(df.isna().sum())
    print("-----Shape Of Data-------------")
    print(df.shape)


# %%
sales_data['date'] = pd.to_datetime(sales_data['date'],format = '%d.%m.%Y')

# %%
dataset = sales_data.pivot_table(index = ['shop_id','item_id'],values = ['item_cnt_day'],columns = ['date_block_num'],fill_value = 0,aggfunc='sum')

# %%
dataset

# %%
dataset.reset_index(inplace = True)

# %%
dataset

# %%
# predict
dataset = pd.merge(test_data,dataset,on = ['item_id','shop_id'],how = 'left')

# %%
dataset

# %%
# lets fill all NaN values with 0
dataset.fillna(0,inplace = True)

# %%
dataset.drop(['shop_id','item_id','ID'],inplace = True, axis = 1)
dataset.head()

# %%
# X we will keep all columns execpt the last one 
X_train = np.expand_dims(dataset.values[:,:-1],axis = 2)
# the last column is our label
y_train = dataset.values[:,-1:]

# for test we keep all the columns execpt the first one
X_test = np.expand_dims(dataset.values[:,1:],axis = 2)

# lets have a look on the shape 
print(X_train.shape,y_train.shape,X_test.shape)


# %%
from keras.models import Sequential
from keras.layers import LSTM,Dense,Dropout

# %%
# our defining our model 
my_model = Sequential()
my_model.add(LSTM(units = 64,input_shape = (33,1)))

my_model.add(Dropout(0.4))
my_model.add(Dense(1))

my_model.compile(loss = 'mse',optimizer = 'adam', metrics = ['mean_squared_error'])
my_model.summary()

# %%

# %%
# my_model.fit(X_train,y_train,batch_size = 4096,epochs = 10)

# %%
# our defining our model 
my_model2 = Sequential()
my_model2.add(LSTM(units = 32,input_shape = (33,1), return_sequences=True))
my_model2.add(LSTM(units = 64, return_sequences=True))
my_model2.add(LSTM(units = 128, return_sequences=True))
my_model2.add(Dropout(0.4))

my_model2.add(LSTM(units = 128, return_sequences=True))
my_model2.add(LSTM(units = 64, return_sequences=True))
my_model2.add(LSTM(units = 32))
my_model2.add(Dropout(0.4))

my_model2.add(Dense(1))

my_model2.compile(loss = 'mse',optimizer = 'adam', metrics = ['mean_squared_error'])
my_model2.summary()

# %%
my_model2.fit(X_train,y_train,batch_size = 4096,epochs = 10)

# %%
# creating submission file 
submission_pfs = my_model2.predict(X_test)
# we will keep every value between 0 and 20
submission_pfs = submission_pfs.clip(0,20)
# creating dataframe with required columns 
submission = pd.DataFrame({'ID':test_data['ID'],'item_cnt_month':submission_pfs.ravel()})
# creating csv file from dataframe
submission.to_csv('sub_pfs2.csv',index = False)

# %%

# regressor = Sequential()

# regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (33, 1)))
# regressor.add(Dropout(0.2))

# regressor.add(LSTM(units = 50, return_sequences = True))
# regressor.add(Dropout(0.2))

# regressor.add(LSTM(units = 50, return_sequences = True))
# regressor.add(Dropout(0.2))

# regressor.add(LSTM(units = 50))
# regressor.add(Dropout(0.2))

# regressor.add(Dense(units = 1))

# regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

# regressor.fit(X_train, y_train, epochs = 10, batch_size = 4096)


# %%
# submission_pfss = regressor.predict(X_test)
# # we will keep every value between 0 and 20
# submission_pfss = submission_pfss.clip(0,20)
# # creating dataframe with required columns 
# submission12 = pd.DataFrame({'ID':test_data['ID'],'item_cnt_month':submission_pfss.ravel()})
# # creating csv file from dataframe
# submission12.to_csv('sub_pfs12.csv',index = False)
