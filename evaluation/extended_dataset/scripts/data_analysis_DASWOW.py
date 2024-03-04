# %%
import errno
import json
import logging
import os
import shutil
import statistics
import time
import traceback
from pathlib import Path

import nbformat
import numpy as np
import pandas as pd
import simplejson as sjson

ROOT_DIR = Path(__file__).parent

daswow_notebooks_path = "/mnt/Projects/PhD/Research/Student-Thesis/5_Suvansh_LLMs/git_sources/master-thesis-of-suvansh-chawla/code/daswow_notebooks_fixed"
out_path = ROOT_DIR / "notebooks"
out_path_json = ROOT_DIR / "headers_ground_truth"
out_path_cs = ROOT_DIR / "ground_truth"
headergen_dataset_path = f"{ROOT_DIR}/DASWOW_stats.csv"

# Remove results dir and recreate
try:
    shutil.rmtree(out_path)
    shutil.rmtree(out_path_json)
    shutil.rmtree(out_path_cs)
except OSError:
    print("Removal of the directory %s failed" % out_path)

try:
    os.mkdir(out_path)
    os.mkdir(out_path_cs)
except OSError:
    print("Creation of the directory %s failed" % out_path)
else:
    print("Successfully created the directory %s " % out_path)

try:
    os.mkdir(out_path_json)
except OSError:
    print("Creation of the directory %s failed" % out_path)
else:
    print("Successfully created the directory %s " % out_path)

SAVE_HEADERGEN_OUTPUT = True

# Logging
logging.basicConfig(
    filename="{}/logs.log".format(ROOT_DIR),
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s",
    level=3,
)


# %%
# Find all notebooks in location
notebook_id = 1
count = 0
failures = 0
start = time.time()

no_markdown_nbs = []

for _file in (length_nb := sorted(Path(daswow_notebooks_path).rglob("*.ipynb"))):
    try:
        notebook_id += 1
        logging.debug("###################################################\n")
        logging.debug(_file.name)
        print(_file.name)
        comp_path = os.path.join(out_path)

        with open(_file, "r") as file:
            notebook = nbformat.read(file, as_version=4)

        code_cell_avg = statistics.median(
            [
                len(cell.source.strip().split("\n"))
                for cell in notebook.cells
                if cell.cell_type == "code"
            ]
        )
        md_count = len(
            [cell for cell in notebook.cells if cell.cell_type == "markdown"]
        )
        code_cell_count = len(
            [cell for cell in notebook.cells if cell.cell_type == "code"]
        )

        if md_count == 0:
            if code_cell_count >= 22:
                no_markdown_nbs.append(_file)
        # Filter out empty code cells
        notebook.cells = [
            cell
            for cell in notebook.cells
            if not (cell.cell_type == "code" and not cell.source)
        ]

        df_data = {
            "filename": _file.name,
            "code_cell_avg": code_cell_avg,
            "md_count": md_count,
            "code_cell_count": code_cell_count,
        }
        df = pd.DataFrame([df_data])

        # Check if file exists
        file_exists = os.path.exists(headergen_dataset_path)

        # Save the DataFrame to a CSV file, appending the new data
        with open(headergen_dataset_path, "a") as f:
            df.to_csv(
                f,
                mode="a" if file_exists else "w",
                index=False,
                header=not file_exists,
            )

        logging.debug("DONE")

    except Exception as e:
        logging.error("Root level Exception: {:02}-{}".format(notebook_id, _file.stem))
        logging.error(_file)
        logging.error(e)
        logging.error(traceback.format_exc())

        print(e)
        failures = failures + 1
    logging.debug("=======================================================\n")
    count = count + 1
    print(f"{count}/{len(length_nb)}")

print(f"Analysis took: {time.time() - start}")
print(f"Failed: {failures}/{count}")

# %%
# Move files with no markdown cells
import shutil

for _nb in no_markdown_nbs:
    destination_path = out_path / _nb.name
    shutil.copy(_nb, destination_path)

# %%
# Generate ground truth

import csv
import json

from headergen import headergen

daswow_notebooks_path = "/mnt/Projects/PhD/Research/HeaderGen/git_sources/HeaderGen_github/evaluation/extended_dataset/DASWOW_nomd_notebooks"
csv_file_path = "/mnt/Projects/PhD/Research/HeaderGen/git_sources/HeaderGen_github/evaluation/extended_dataset/DASWOW_dataset_fixed.csv"

taxonomy_map = {
    "helper_functions": "Others (helper_functions)",
    "load_data": "Data Preparation",
    "data_exploration": "Data Preparation",
    "data_preprocessing": "Data Preparation",
    "evaluation": "Model Building and Training",
    "modelling": "Model Building and Training",
    "prediction": "Model Building and Training",
    "result_visualization": "Visualization",
    "save_results": "Others (save_results)",
    "comment_only": "Others (comment_only)",
}

daswow_labels = [
    "helper_functions",
    "load_data",
    "data_exploration",
    "data_preprocessing",
    "evaluation",
    "modelling",
    "prediction",
    "result_visualization",
    "save_results",
    "comment_only",
]

df = pd.read_csv(csv_file_path)

for _nb in no_markdown_nbs:
    nb_headers = {}
    filtered_df = df[df["filename"] == _nb.name]

    for index, row in filtered_df.iterrows():
        # cell_headers = []
        nb_headers[row["cell_number"] + 1] = list(
            set([taxonomy_map[x] for x in daswow_labels if row[x] == 1])
        )

    with open(out_path_json / f"{_nb.stem}.json", "w") as f:
        f.write(json.dumps(nb_headers, indent=4))

    analysis_meta = headergen.start_headergen(str(_nb), out_path, debug_mode=False)
    with open(out_path_cs / f"{_nb.stem}.json", "w") as f:
        f.write(
            sjson.dumps(
                dict(sorted(analysis_meta["cell_callsites"].items())),
                indent=4,
                iterable_as_array=True,
            )
        )
