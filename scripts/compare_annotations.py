import os
import sys
import json
import csv
from collections import Counter

HIGH_LEVEL_CLASSES = True
not_found_counter = []

short_forms = {
    "LL": "Library Loading",
    "DL": "Data Loading",
    "VIS": "Visualization",
    "OTH": "*Others",
    "DP": "Data Cleaning Preparation",
    "EDA": "Data Profiling and Exploratory Data Analysis",
    "DC": "Data Cleaning Filtering",
    "SPL": "Data Sub-sampling and Train-test Splitting",
    "FE": "Feature Engineering",
    "FT": "Feature Transformation",
    "FS": "Feature Selection",
    "MB": "Model Building and Training",
    "MT": "Model Training",
    "MPT": "Model Parameter Tuning",
    "MV": "Model Validation and Assembling",
}

phase_groups = {
    "Library Loading": ["Library Loading"],
    "Visualization": ["Visualization"],
    "Others": ["Others"],
    "Data Preparation": ["Data Preparation", "Data Profiling and Exploratory Data Analysis", "Exploratory Data Analysis" ,"Data Cleaning Filtering" ,"Data Sub-sampling and Train-test Splitting", "Data Loading"],
    "Feature Engineering": ["Feature Engineering", "Feature Transformation", "Feature Selection"],
    "Model Building and Training": ["Model Building and Training", "Model Training", "Model Parameter Tuning", "Model Validation and Assembling"]
}

def get_high_level_phases(read_json):
    high_level_combine = {}
    for _k, _v in read_json.items():
        high_level_combine[_k] = set()
        for _cat in _v:
            for _h_cat, h_cat_v in phase_groups.items():
                if _cat in h_cat_v:
                    high_level_combine[_k].add(_h_cat)

    return high_level_combine

def read_json(path):
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return json.loads(f.read())

def read_annotation_csv(path):
    if not os.path.exists(path):
        return None
    expected = {}        
    with open(path, "r") as f:
        annotations = csv.reader(f, delimiter=',')
        header = next(annotations)
        for row in annotations:
            expected[row[0]] =[short_forms[x] for x in row[1].split(";") if x in short_forms]
        return expected

def measure_precision(actual, expected):
    num_all = 0
    num_caught = 0
    # print("Precision...")
    for node in actual:
        num_all += len(actual[node])
        for item in actual[node]:
            if expected.get(node, None) == None:
                continue
            if item in expected[node]:
                num_caught += 1
            else:
                # print(node, ": ", item)
                pass

    if num_all == 0:
        num_all = 1

    return float(num_caught) / float(num_all)

def measure_recall(actual, expected):
    num_all = 0
    num_caught = 0
    # print("Recall...")
    for node in expected:
        num_all += len(expected[node])
        for item in expected[node]:
            if actual.get(node, None) == None:
                continue
            if item in actual[node]:
                num_caught += 1
            else:
                not_found_counter.append(item)
                # print(node, ": ", item)

    if num_all == 0:
        num_all = 1
    return float(num_caught) / float(num_all)

def write_results(data, results_path):
    header = ["Project", "Precision", "Recall"]
    prec_sum = 0
    rec_sum = 0
    cnt = 0
    with open(results_path, "w+") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(header)
        for project, dt in data.items():
            writer.writerow([project, dt["precision"], dt["recall"]])
            try:
                float(dt["precision"])
                float(dt["recall"])
                prec_sum += dt["precision"]
                rec_sum += dt["recall"]
                cnt += 1
            except:
                continue
        writer.writerow(["Average", round(prec_sum/cnt,1),
            round(rec_sum/cnt,1)])
        print("Precision:", round(prec_sum/cnt,1), "Recall:", round(rec_sum/cnt,1), "\n")

def compare(notebooks_path, actual_path, expected_path, results_path):
    projects = [nb.split(".ipynb")[0] for nb in sorted(os.listdir(notebooks_path)) if nb.endswith(".ipynb")]

    prec_sum = 0
    rec_sum = 0
    cnt = 0
    data = {}
    for project in projects:
        # print("\n# Project: ", project)

        actual = read_json(os.path.join(actual_path, project + "-headers.json"))
        expected = read_json(os.path.join(expected_path, project + ".json"))

        if HIGH_LEVEL_CLASSES:
            actual = get_high_level_phases(actual)
            expected = get_high_level_phases(expected)
            
        if not actual or not expected:
            data[project] = {
                "precision": "-",
                "recall": "-"
            }
            continue

        precision = measure_precision(actual, expected)
        recall = measure_recall(actual, expected)
        data[project] = {
            "precision": round(precision*100,1),
            "recall": round(recall*100,1)
        }

        # print("\n")
    write_results(data, results_path)


def main():
    script_dir = os.path.abspath(os.path.dirname(__file__))


    benchmark_path = f"{script_dir}/../callsites-jupyternb-real-world-benchmark"
    results_path = f"{script_dir}/../.scrapy/results"
    hg_path = f"{script_dir}/../.scrapy/results/annotated_notebooks"
    
    notebooks_path = f"{benchmark_path}/notebooks"
    ground_truth_path = f"{benchmark_path}/headers_ground_truth"

    hg_results = os.path.join(results_path, "headergen_headers_eval.csv")

    print ("\nComparing Headers for Real-world Benchmark...")
    compare(notebooks_path, hg_path, ground_truth_path, hg_results)
    # print ("\n")
    # print(Counter(not_found_counter))
    
if __name__ == "__main__":
    main()
