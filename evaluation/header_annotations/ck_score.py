import os
import sys
import json
import csv
from collections import Counter
from pathlib import Path

not_found_counter = []

RATER_IDS = ["r1", "r2", "r3", "r4"]
RESPONSES_PATH = '/tmp/evaluation/header_annotations/{RATER_ID}'
GROUND_TRUTH = "/tmp/evaluation/header_annotations/results"
PROJECT_BASED = f"/tmp/callsites-jupyternb-real-world-benchmark/headers_ground_truth"

COMBINE_PHASES = True

short_forms = {
    "LL": "Library Loading",
    "DL": "Data Loading",
    "VIS": "Visualization",
    "OTH": "*Others",
    "DP": "Data Preparation",
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
    "Data Preparation": ["Data Preparation", "Data Profiling and Exploratory Data Analysis" ,"Data Cleaning Filtering" ,"Data Sub-sampling and Train-test Splitting", "Data Loading"],
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

def translate_format(response_data, project_id):
    expected = {}
    for count, row in response_data.items():
        expected[f"{response.stem}:{count}"] = ":".join(sorted(row))

    return expected

RATER_RESPONSES = {}
for rater in RATER_IDS:
    responses = sorted(Path(RESPONSES_PATH.format(RATER_ID=rater)).rglob('*.json'))
    RATER_RESPONSES[rater] = {}
    for response in responses:
        # print("\n# Project: ", response.parent)
        response_data = read_json(response)
        if COMBINE_PHASES:
            response_data = get_high_level_phases(response_data)

        RATER_RESPONSES[rater] = RATER_RESPONSES[rater] | translate_format(response_data, response)


with open('{}/{}.json'.format(GROUND_TRUTH, "rater_responses_unified"), 'w') as outfile:
    json.dump(RATER_RESPONSES, outfile, indent=4)


# %%
# Calculate kappa score

import itertools

from sklearn.metrics import cohen_kappa_score
import numpy as np

rater1 = list(RATER_RESPONSES["r1"].values())
rater2 = list(RATER_RESPONSES["r2"].values())

print("(r1-r2) CKappa Score:", cohen_kappa_score(rater1, rater2))

rater3 = list(RATER_RESPONSES["r3"].values())
rater4 = list(RATER_RESPONSES["r4"].values())

print("(r3-r4) CKappa Score:", cohen_kappa_score(rater3, rater4))


# %%
# Merge files for ground truth
rater_1_2_merged = {}
for _cell in RATER_RESPONSES["r1"].keys():
    rater_1_2_merged[_cell] = list(set(RATER_RESPONSES["r1"][_cell].split(":") + RATER_RESPONSES["r2"][_cell].split(":")))

rater_3_4_merged = {}
for _cell in RATER_RESPONSES["r3"].keys():
    rater_3_4_merged[_cell] = list(set(RATER_RESPONSES["r3"][_cell].split(":") + RATER_RESPONSES["r4"][_cell].split(":")))

with open('{}/{}.json'.format(GROUND_TRUTH, "rater_1_2_merged"), 'w') as outfile:
    json.dump(rater_1_2_merged, outfile, indent=4)

with open('{}/{}.json'.format(GROUND_TRUTH, "rater_3_4_merged"), 'w') as outfile:
    json.dump(rater_3_4_merged, outfile, indent=4)


overall_headers_ground_truth = rater_1_2_merged | rater_3_4_merged
with open('{}/{}.json'.format(GROUND_TRUTH, "overall_headers_ground_truth"), 'w') as outfile:
    json.dump(rater_1_2_merged | rater_3_4_merged, outfile, indent=4)

# project based truth
project_based_headers_ground_truth = {}
for _project_cell, _annotations in overall_headers_ground_truth.items():
    project_name, _cell = _project_cell.split(":")[0], _project_cell.split(":")[1]
    if project_name not in project_based_headers_ground_truth:
        project_based_headers_ground_truth[project_name] = {}

    project_based_headers_ground_truth[project_name][_cell] = _annotations

for _project, _annotations in project_based_headers_ground_truth.items():
    with open('{}/{}.json'.format(PROJECT_BASED, _project), 'w') as outfile:
        json.dump(_annotations, outfile, indent=4)

    

print()
