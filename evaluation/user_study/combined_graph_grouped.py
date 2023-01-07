# %%
import pandas as pd
import matplotlib.pyplot as plt  # doesn't have color by hue
import seaborn as sns
import numpy as np  # for generating random data
import random  # for random gender selection
import statistics

user_study_folder = "/tmp/evaluation/user_study"

response_file = f"{user_study_folder}/individual_responses/questions_results.csv"
response_file_likert = f"{user_study_folder}/likert/Responses.csv"
response_file_timings = f"{user_study_folder}/timings/timings.csv"
outpath = "/results"

data = pd.read_csv(response_file, header=0)

question_map = {
    1: "T1",
    2: "T2",
    3: "T3",
    4: "T4",
    5: "T5",
    6: "T1",
    7: "T3",
    8: "T4",
    9: "T5",
    10: "T6",
}

listdata_1 = []
listdata_2 = []
skiprow = []
for index, row in data.iterrows():
    for i in range(1, 11):
        if i in skiprow:
            continue
        if row["study_id"] == 2.0:
            if i in range(1, 6):
                listdata_1.append(
                    {
                        "question": question_map[i],
                        "type": "Annotated",
                        "f1score": row[f"Fs_{i}"],
                    }
                )
            else:
                listdata_2.append(
                    {
                        "question": question_map[i],
                        "type": "Undocumented",
                        "f1score": row[f"Fs_{i}"],
                    }
                )

        elif row["study_id"] == 1.0:
            if i in range(1, 6):
                listdata_1.append(
                    {
                        "question": question_map[i],
                        "type": "Undocumented",
                        "f1score": row[f"Fs_{i}"],
                    }
                )
            else:
                listdata_2.append(
                    {
                        "question": question_map[i],
                        "type": "Annotated",
                        "f1score": row[f"Fs_{i}"],
                    }
                )


processed_data_nb1 = pd.DataFrame(listdata_1)
processed_data_nb2 = pd.DataFrame(listdata_2)
processed_data_all = pd.DataFrame(listdata_1 + listdata_2)

# %%
sns.set_style("ticks")
sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 1.5})
sns.color_palette("colorblind")

fig, axs = plt.subplots(
    1, 3, gridspec_kw={"width_ratios": [3.5, 1.25, 1.75]}, figsize=(20, 5), dpi=150
)

p = sns.boxplot(
    y="f1score",
    x="question",
    data=processed_data_all,
    width=0.5,
    hue="type",
    ax=axs[0],
    palette="muted",
    medianprops=dict(color="black", alpha=0.9),
    boxprops={"linewidth": 0.5},
)
# p = sns.swarmplot(y='f1score', x='question', data=processed_data_all, hue='type', ax=axs[0], palette="muted")

axs[0].set_xlabel("")
axs[0].set_ylabel("F1-score")

[
    axs[0].axvline(x, color="black", linestyle="--", linewidth="0.75")
    for x in np.arange(0.5, 5, 1)
]

axs[0].legend(loc="lower right")

# %%
# TIME GRAPH


df_time = pd.read_csv(response_file_timings, header=0)

df_time = df_time.drop(["ID", "Study_id"], axis=1)
p = sns.boxplot(
    data=df_time,
    ax=axs[1],
    palette="muted",
    width=0.225,
    dodge=1,
    medianprops=dict(color="black", alpha=0.9),
    boxprops={"linewidth": 0.5},
)


axs[1].set_ylabel("Time (s)")
axs[1].tick_params(labelsize=14)

[
    axs[1].axvline(x, color="black", linestyle="--", linewidth="0.75")
    for x in np.arange(0.5, 1, 1)
]


# LIKERT GRAPH


likert_df = pd.read_csv(response_file_likert, header=0)

p = sns.boxplot(
    data=likert_df,
    ax=axs[2],
    width=0.3,
    color="seagreen",
    dodge=1,
    medianprops=dict(color="black", alpha=0.9),
    boxprops={"linewidth": 0.5},
)
# p = sns.swarmplot(data=likert_df, ax=axs[1], size=5, color="0", dodge=1)

axs[2].set_ylabel("Likert Scale")

[
    axs[2].axvline(x, color="black", linestyle="--", linewidth="0.75")
    for x in np.arange(0.5, 3, 1)
]

axs[2].tick_params(labelsize=18)

plt.savefig(f"{outpath}/combined_graph.png", bbox_inches="tight")
plt.show()

# %%
# %%
for i in range(1, 7):
    print(f"\nQ{i}")

    a_mean = statistics.mean(
        processed_data_all["f1score"]
        .where(
            (processed_data_all["question"] == f"T{i}")
            & (processed_data_all["type"] == f"Annotated")
        )
        .dropna()
    )
    u_mean = statistics.mean(
        processed_data_all["f1score"]
        .where(
            (processed_data_all["question"] == f"T{i}")
            & (processed_data_all["type"] == f"Undocumented")
        )
        .dropna()
    )
    if a_mean > u_mean:
        print("Annotated Mean higher for Q", i)

    a_med = statistics.median(
        processed_data_all["f1score"]
        .where(
            (processed_data_all["question"] == f"T{i}")
            & (processed_data_all["type"] == f"Annotated")
        )
        .dropna()
    )
    u_med = statistics.median(
        processed_data_all["f1score"]
        .where(
            (processed_data_all["question"] == f"T{i}")
            & (processed_data_all["type"] == f"Undocumented")
        )
        .dropna()
    )
    if a_med > u_med:
        print("Annotated Median higher for Q", i)
    if a_med == u_med:
        print("Annotated Median equal for Q", i)

    a_var = statistics.stdev(
        processed_data_all["f1score"]
        .where(
            (processed_data_all["question"] == f"T{i}")
            & (processed_data_all["type"] == f"Annotated")
        )
        .dropna()
    )
    u_var = statistics.stdev(
        processed_data_all["f1score"]
        .where(
            (processed_data_all["question"] == f"T{i}")
            & (processed_data_all["type"] == f"Undocumented")
        )
        .dropna()
    )
    if u_var > a_var:
        print("Undocumented Variance higher for Q", i)


a_mean = statistics.mean(
    processed_data_all["f1score"]
    .where(processed_data_all["type"] == f"Annotated")
    .dropna()
)
u_mean = statistics.mean(
    processed_data_all["f1score"]
    .where(processed_data_all["type"] == f"Undocumented")
    .dropna()
)
if a_mean > u_mean:
    print("Annotated Mean higher")

a_med = statistics.median(
    processed_data_all["f1score"]
    .where(processed_data_all["type"] == f"Annotated")
    .dropna()
)
u_med = statistics.median(
    processed_data_all["f1score"]
    .where(processed_data_all["type"] == f"Undocumented")
    .dropna()
)
if a_med > u_med:
    print("Annotated Median higher")

a_var = statistics.variance(
    processed_data_all["f1score"]
    .where(processed_data_all["type"] == f"Annotated")
    .dropna()
)
u_var = statistics.variance(
    processed_data_all["f1score"]
    .where(processed_data_all["type"] == f"Undocumented")
    .dropna()
)
if u_var > a_var:
    print("Undocumented Variance higher")

# %%
