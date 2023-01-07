# %%
from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import std

# seed the random number generator
seed(1)
# generate two sets of univariate observations
data1 = 5 * randn(100) + 50
data2 = 5 * randn(100) + 51
# summarize
print('data1: mean=%.3f stdv=%.3f' % (mean(data1), std(data1)))
print('data2: mean=%.3f stdv=%.3f' % (mean(data2), std(data2)))

import pandas as pd

response_file  = "/tmp/evaluation/user_study/individual_responses/questions_results.csv"
outpath = "/results"

data = pd.read_csv(response_file, 
            header=0)

listdata_1 = []
listdata_2 = []
skiprow = []
for index, row in data.iterrows():
    for i in range(1, 11):
        if i in skiprow:
            continue
        if row['study_id'] == 2.0:
            if i in range(1, 6):
                listdata_1.append({
                    'type': "Annotated",
                    'f1score': row[f"Fs_{i}"]
                })
            else:
                listdata_2.append({
                    'type': "Undocumented",
                    'f1score': row[f"Fs_{i}"]
                })

        elif row['study_id'] == 1.0:
            if i in range(1, 6):
                listdata_1.append({
                    'type': "Undocumented",
                    'f1score': row[f"Fs_{i}"]
                })
            else:
                listdata_2.append({
                    'type': "Annotated",
                    'f1score': row[f"Fs_{i}"]
                })


processed_data_nb1 = pd.DataFrame(listdata_1)
processed_data_nb2 = pd.DataFrame(listdata_2)
processed_data_all = pd.DataFrame(listdata_1+listdata_2)

annotated = list(processed_data_all["f1score"].where(processed_data_all["type"] == "Annotated").dropna())
undocumented = list(processed_data_all["f1score"].where(processed_data_all["type"] == "Undocumented").dropna())

# %%
from scipy.stats import wilcoxon
# compare samples
stat, p = wilcoxon(annotated, undocumented)
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
    print('Same distribution (fail to reject H0)')
else:
    print('Different distribution (reject H0)')

# %%
response_file_timings = "/tmp/evaluation/user_study/individual_responses/timings/timings.csv"

df_time = pd.read_csv(response_file_timings, 
            header=0)

df_time = df_time.drop(["ID", "Study_id"], axis=1)

stat, p = wilcoxon(df_time["Annotated"], df_time["Undocumented"])
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
    print('Same distribution (fail to reject H0)')
else:
    print('Different distribution (reject H0)')

# %%
from scipy import stats
stats.ttest_rel(df_time["Undocumented"], df_time["Annotated"])

