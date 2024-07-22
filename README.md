# HeaderGen

<p align="center">
<img src="headergen.png" width="500" align="center">
</p>

HeaderGen is a tool-based approach to enhance the comprehension and navigation of undocumented Python based Jupyter notebooks by automatically creating a narrative structure in the notebook.

Data scientists build an ML-based solution notebook by first preparing the data, then extracting key features, and then creating and training the model. HeaderGen leverages the implicit narrative structure of an ML notebook to add structural headers as annotations to the notebook.

## Preview

![](preview.gif)

## Install HeaderGen

```
pip install headergen
```

## Features

- **Automated Markdown Header Insertion:** Through a taxonomy for machine-learning operations, HeaderGen annotates code cells with relevant markdown headers.

- **Function Call Taxonomy:** Methodically classifies function calls based on a machine-learning operations taxonomy.

- **Advanced Call Graph Analysis:** Enhances PyCG framework with flow-sensitivity and external library return-type resolution.

- **Precision in External Libraries:** capability to accurately resolve function return types from external libraries using typestubs.

- **Syntax Pattern Matching:** Employs type data for pattern matching.

## CLI Usage

### `generate` Command:

Generate the HeaderGen annotated notebook in the current directory. Note that the caches will be created the first time HeaderGen is run.
```bash
headergen generate -i /path/to/input.ipynb
```
Generate a JSON metadata file that includes various analysis information, use the --json_output or -j flag.

```bash
headergen generate -i /path/to/input.ipynb -o /path/to/output/ -j
```

### `types` Command:

Run type inference on the file and fetch type information.
```bash
headergen types -i /path/to/input.ipynb
```
Generate a JSON file with type information, use the --json_output or -j flag.

```bash
headergen types -i /path/to/input.ipynb -o /path/to/output/ -j
```


### `server` Command:

Starting the server is straightforward:

```
headergen server
```

This will start the Uvicorn server listening on host 0.0.0.0 and port 54068.

#### get_analysis_notebook Endpoint:

This endpoint returns the analysis of the specified notebook or python script as a JSON response containing analysis data like cell_callsites and block_mapping.

Example using curl:

```
curl "http://0.0.0.0:54068/get_analysis_notebook?file_path=/absolute/path/to/your/file.ipynb"
```

#### get_types Endpoint:

This endpoint returns type information of the specified notebook or python script as a JSON response.

Example using curl:

```
curl "http://0.0.0.0:54068/get_types?file_path=/absolute/path/to/your/file.ipynb"
```

#### generate_annotated_notebook Endpoint:

This endpoint returns the annotated notebook based on the analysis. The response will be a file download.

Example using curl:

```
curl "http://0.0.0.0:54068/generate_annotated_notebook?file_path=/absolute/path/to/your/file.ipynb" --output annotated_file.ipynb
```

## Folder Structure

+ `callsites-jupyternb-micro-benchmark`: Micro benchmark
+ `callsites-jupyternb-real-world-benchmark`: Real-world benchmark
+ `evaluation`: Contains manual header annotation and user study results
+ `framework_models`: Function calls to ML Taxonomy mapping
+ `typestub-database`: Type-stbs for ML libraries
+ `headergen`: Source code of HeaderGen
+ `pycg_extended`: Source code of extended PyCG
+ `headergen-extension`: Jupyter notebook plugin for HG
+ `headergen_output`: Folder where the generated notebooks from the docker container are stored

--------
## 1. Build container

+ Get source files

      git clone --recursive
      git submodule update --init --recursive
      git pull --recurse-submodules

+ Linux

      docker build -t headergen .
      docker run -v {$PWD}/headergen_output:/headergen_output -it headergen bash

+ Windows

      docker build -t headergen .
      docker run -v "%cd%"/headergen_output:/headergen_output -it headergen bash


## 2. Run HeaderGen benchmarks from inside contatiner

Output generated from the following commands, such as annotated notebooks, reports, callsites, headers, etc, are stored in the local folder `headergen_output` after the following commands are done executing.

+ Micro Benchmark (generates a csv file with results)

      make ROOT_PATH=/app/HeaderGen microbench

+ Real-world Benchmark (generates annotated notebooks and csv file that reproduce table 2)

      make ROOT_PATH=/app/HeaderGen realworldbench

+ Both Benchmarks

      make ROOT_PATH=/app/HeaderGen all

+ Clean generated output

      make clean

---

## Building from Source

+ Get source files

      git clone --recursive
      git submodule update --init --recursive
      git pull --recurse-submodules

+ Clear cache if exists

      rm framework_models/models_cache.pickle
      rm pycg_extended/machinery/pytd_cache.pickle

+ Setup venv and dependencies with `setup.sh` script

      ./setup.sh -i

+ Micro Benchmark (generates a csv file with results)

      make ROOT_PATH=<path to repo root> microbench

+ Real-world Benchmark (generates annotated notebooks and csv file that reproduce table 2)

      make ROOT_PATH=<path to repo root> realworldbench

+ Both Benchmarks

      make ROOT_PATH=<path to repo root> all

+ Clean generated output

      make clean

---

This repo contains code for the paper **"Enhancing Comprehension and Navigation in Jupyter Notebooks with Static Analysis"** published at the [SANER Conference 2023](https://arxiv.org/abs/2301.04419).
