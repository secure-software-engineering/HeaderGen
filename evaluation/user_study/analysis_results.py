# %%
import csv
import json

import pandas

response_file = "/app/HeaderGen/evaluation/user_study/Responses.csv"
out_path = "/app/HeaderGen/evaluation/user_study/individual_responses"


def measure_precision(actual, expected, start, end):
    num_all = 0
    num_caught = 0
    print("Precision...")
    for node in range(start, end + 1):
        node = str(node)
        # for node in actual:
        num_all += len(actual[node])
        for item in actual[node]:
            if expected.get(node, None) == None:
                continue
            if item in expected[node]:
                num_caught += 1
            else:
                print(node, ": ", item)

    if num_all == 0:
        num_all = 1

    return float(num_caught) / float(num_all)


def measure_recall(actual, expected, start, end):
    num_all = 0
    num_caught = 0
    print("Recall...")
    for node in range(start, end + 1):
        node = str(node)
        num_all += len(expected[node])
        for item in expected[node]:
            if actual.get(node, None) == None:
                continue
            if item in actual[node]:
                num_caught += 1
            else:
                print(node, ": ", item)
    if num_all == 0:
        num_all = 1
    return float(num_caught) / float(num_all)


def measure_precision_questions(actual, expected, start, end):
    num_all = 0
    num_caught = 0
    print("Precision...")
    question_based = {}
    for node in range(start, end + 1):
        node = str(node)
        num_all += len(actual[node])
        q_all = len(actual[node])
        q_caught = 0
        for item in actual[node]:
            if expected.get(node, None) == None:
                continue
            if item in expected[node]:
                num_caught += 1
                q_caught += 1
            else:
                print(node, ": ", item)

        question_based[f"PQ{node}"] = float(q_caught) / float(q_all)

    if num_all == 0:
        num_all = 1

    return question_based


def measure_recall_questions(actual, expected, start, end):
    num_all = 0
    num_caught = 0
    print("Recall...")
    question_based = {}

    for node in range(start, end + 1):
        node = str(node)
        num_all += len(expected[node])
        q_all = len(expected[node])
        q_caught = 0
        for item in expected[node]:
            if actual.get(node, None) == None:
                continue
            if item in actual[node]:
                num_caught += 1
                q_caught += 1
            else:
                print(node, ": ", item)

        question_based[f"RQ{node}"] = float(q_caught) / float(q_all)

    if num_all == 0:
        num_all = 1

    return question_based


def write_results(data, results_path):
    header = [
        "Project",
        "Precision_1",
        "Recall_1",
        "Precision_2",
        "Recall_2",
        "Studyid",
    ]
    prec_sum_1 = 0
    rec_sum_1 = 0
    prec_sum_2 = 0
    rec_sum_2 = 0
    cnt = 0
    with open(results_path, "w+") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(header)
        for project, dt in data.items():
            writer.writerow(
                [
                    project,
                    dt["precision_1"],
                    dt["recall_1"],
                    dt["precision_2"],
                    dt["recall_2"],
                    dt["study_id"],
                ]
            )
            try:
                float(dt["precision_1"])
                float(dt["recall_1"])
                float(dt["precision_2"])
                float(dt["recall_2"])
                prec_sum_1 += dt["precision_1"]
                rec_sum_1 += dt["recall_1"]
                prec_sum_2 += dt["precision_2"]
                rec_sum_2 += dt["recall_2"]
                cnt += 1
            except Exception as e:
                continue
        writer.writerow(
            [
                "Average",
                round(prec_sum_1 / cnt, 1),
                round(rec_sum_1 / cnt, 1),
                round(prec_sum_2 / cnt, 1),
                round(rec_sum_2 / cnt, 1),
            ]
        )
        print(
            "P:",
            round(prec_sum_1 / cnt, 1),
            "P:",
            round(prec_sum_2 / cnt, 1),
            "R:",
            round(rec_sum_1 / cnt, 1),
            "R:",
            round(rec_sum_2 / cnt, 1),
        )


df = pandas.read_csv(response_file, index_col="ID", header=0)


data = {}
for index, row in df.iterrows():
    response_dict = {"name": row["Name"], "study_id": row["Study_id"]}
    for i in range(1, 11):
        response_dict[str(i)] = [x.strip() for x in row[f"Q{i}"].split(",")]

    with open(f"{out_path}/response_{index}.json", "w") as f:
        f.write(json.dumps(dict(sorted(response_dict.items())), indent=4))


with open(f"{out_path}/response_expected.json", "r") as f:
    expected = json.loads(f.read())

questions_data = {}
for i in range(2, 10):
    with open(f"{out_path}/response_{i}.json", "r") as f:
        actual = json.loads(f.read())

    print(f"{i}\n")

    # if actual['study_id'] == 1:
    precision_1 = measure_precision(actual, expected, 1, 5)
    recall_1 = measure_recall(actual, expected, 1, 5)
    precision_2 = measure_precision(actual, expected, 6, 10)
    recall_2 = measure_recall(actual, expected, 6, 10)

    precision_questions = measure_precision_questions(actual, expected, 1, 10)
    recall_questions = measure_recall_questions(actual, expected, 1, 10)

    # f1_scores = {k:v for k, v in zip(range(1, 11), 1*2)}

    questions_data[i] = {k: v for k, v in precision_questions.items()}

    questions_data[i] = (
        questions_data[i]
        | {k: v for k, v in recall_questions.items()}
        | {"study_id": actual["study_id"]}
    )

    data[i] = {
        "precision_1": round(precision_1 * 100, 1),
        "recall_1": round(recall_1 * 100, 1),
        "precision_2": round(precision_2 * 100, 1),
        "recall_2": round(recall_2 * 100, 1),
        "study_id": actual["study_id"],
    }

write_results(data, f"{out_path}/results.csv")

df = pandas.DataFrame.from_dict(questions_data).T

for i in range(1, 11):
    df[f"Fs_{i}"] = (2 * df[f"PQ{i}"] * df[f"RQ{i}"]) / (df[f"PQ{i}"] + df[f"RQ{i}"])

# (['PQ1'] * (pandas.DataFrame.from_dict(questions_data).T)['RQ1']

with open(f"{out_path}/questions_results.csv", "w+") as f:
    f.write(df.to_csv())
