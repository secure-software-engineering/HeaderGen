# import pandas as pd

# train_df = pd.read_csv('../input/train.csv')
# train_df.head()

# df = pd.DataFrame(raw_data, columns=[
#                   'first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
# df.head()

# from sklearn.preprocessing import StandardScaler
# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test = sc.transform(X_test)

import pandas as pd
df = pd.read_csv('../input/competitive-data-science-predict-future-sales/sales_train.csv')
items = pd.read_csv('../input/competitive-data-science-predict-future-sales/items.csv')


# %%
df

# %%
df['date_block_num']

# %%
print(df[0:20])

# %%
Y = df[['target']]

# %%
all_features = df + df

# %%
category = []
for i in df['item_id']:
    category.append(items['item_category_id'][i])

# %%
df['item_category_id'] = category

# %%
target = df['item_cnt_day']

# %%
df.columns = ['item_cnt_month','ID']

# %%
data = df[df['item_cnt_day']<=50]

# %%
data = data[data['item_cnt_day']>-3]

# %%
X=data[['PassengerId','Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']]

# %%
data.Sex[data.Sex == 'male'] = 1
data.Fare[data.Fare <= 17] = 1

# %%
data['shop*item'] = data.shop_id *data.item_id

# %%
class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('accuracy') > 0.82):
            self.model.stop_training = True
callbacks = myCallback();

# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%