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
import numpy as np
import pandas as pd
import keras

import keras
from keras.models import Model
from keras.layers import Input,Dense
from keras import Sequential

train = pd.read_csv("../input/titanic/train.csv")
test = pd.read_csv("../input/titanic/test.csv")

train.Pclass = train.Pclass.values.astype('str')
test.Pclass = test.Pclass.values.astype('str')

train.SibSp = train.SibSp.values.astype('str')
test.SibSp = test.SibSp.values.astype('str')

train.Parch = train.Parch.values.astype('str')
test.Parch = test.Parch.values.astype('str')

use_col =  ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp','Parch','Fare', 'Embarked']

train["Age"] = train.Age.fillna(30.).values
test["Age"] = test.Age.fillna(30.).values

test.Fare[152]=np.mean(test.Fare)

train = train[use_col]
test_x = test[use_col[1:]]

train = train.dropna()

train_y = train[use_col[0]].values
train_x = train[use_col[1:]].copy()

# %%
import numpy as np
import pandas as pd

def pandas_type(inp):
    if str(type(inp)) != "<class 'pandas.core.frame.DataFrame'>":
        print("Use pandas DataFrame")
        return False
    else:
        if np.any(inp.isnull()==True)==True:
            print("Your data is a mess")
            return False
        else:
            pass
    
def pandas_enc_str(inp,m_co_var=True):
    out = pd.DataFrame()
    zw = inp.astype
    try:
        zzw = zw.unique()
    except:
        zw = pd.Series(inp)
        zzw = zw.unique()

    if m_co_var == True:
        for i in zzw[1:]:
            try:
                bin_ = eval('zw=='+str(i)).replace({True : 1 , False : 0})
            except:
                bin_ = eval('zw=="'+str(i)+'"').replace({True : 1 , False : 0})
            out[i]=bin_
        return out
    else:
        for i in zzw:
            try:
                bin_ = eval('zw=='+str(i)).replace({True : 1 , False : 0})
            except:
                bin_ = eval('zw=="'+str(i)+'"').replace({True : 1 , False : 0})
            out[i]=bin_
        return out
    
def get_split_len(inp):
    nn1 = str(np.float32(np.mean(inp))-min(inp)).split(".")[0]
    nn2 = str(np.float32(min(inp))).split(".")[1]
    if nn1 != "0":
        return -len(nn1)+3
    else:
        return len(nn2)

def categorize_cat(inp,bins):
    nn = get_split_len(inp)
    leng = (max(inp)-min(inp))/bins
    cats = []
    for i in range(bins):
        cats.append(min(inp)+leng*(i+1))
    return np.around(cats,nn)

def categorize_(inp,bins):
    out = inp.values
    bins_ = categorize_cat(inp,bins)
    zw = np.ones(len(out))*bins_[0]
    for i in range(len(bins_[:-1])):
        for j in range(len(zw)):
            if out[j] > bins_[i]:
                zw[j]=bins_[i+1]
    return zw

def cat_str(inp):
    zw = pd.Series(inp)
    zzw = np.sort(zw.unique())
    cat_dic={}
    for i in range(1,len(zzw)-1):
        cat_dic.update({zzw[i] : str(zzw[i])+"-"+str(zzw[i+1])})
    cat_dic.update({zzw[-1] : "> "+str(zzw[-1])})
    cat_dic.update({zzw[0] : " <"+str(zzw[0])})
    return pd.Series(zw),cat_dic

def pandas_enc(inp,col,bins=5,m_co_var=True):
    out1 = inp[inp.columns[inp.columns!=col]]
    zw = inp[col]
    if pandas_type(inp)!=False:
        pass
    else:
        return None
    if zw.dtype==float:
        zw = categorize_(zw,bins)
        zw,cat_dic = cat_str(zw)
        out2 = pandas_enc_str(zw,m_co_var)
        out2 = out2[np.sort(out2.columns)]
        out2 = out2.rename(columns=cat_dic)
    elif zw.dtype==int:
        print("Specify: str or float")
    elif zw.dtype=="O":
        zw=str(col)+"_"+zw
        out2 = pandas_enc_str(zw,m_co_var)
    else:
        print("Strange dtype")
    return pd.concat([out1,out2], axis=1)

def pandas_multi_enc(inp,col,bins=5,m_co_var=True):
    out = inp
    for i in col:
        out = pandas_enc(out,str(i))
    return out


# %%
zw = train_x.append(test_x)
zzw = pandas_multi_enc(zw,['Pclass', 'Sex', 'SibSp', 'Parch', 'Embarked'])

train_x = zzw.iloc[:len(train_x)].values
test_x = zzw.iloc[len(train_x):].values

# %%
model=Sequential()
model.add(Dense(512,input_dim=zzw.shape[1],activation='linear'))
model.add(Dense(2048,activation='sigmoid'))
model.add(Dense(512,activation='sigmoid'))
model.add(Dense(16,activation='linear'))
model.add(Dense(1,activation='linear'))


sgd=keras.optimizers.SGD(lr=.0001)
model.compile(optimizer=sgd,loss='mse')

res_model = model.fit(train_x,train_y, batch_size=32, epochs=100)

# %%
zw = model.predict(test_x)

result_csv=pd.DataFrame()

result_csv["PassengerId"]=test.PassengerId
result_csv["Survived"]=np.rint(zw).astype(int)

# %%
result_csv.to_csv("my_titanic_res.csv",index=False)
