# HeaderGen

![HeaderGen](headergen.jpg)

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
      docker run -v ${PWD}/headergen_output:/results -it headergen bash

+ Windows

      docker build -t headergen .
      docker run -v "%cd%"/headergen_output:/results -it headergen bash


## 2. Run HeaderGen benchmarks from inside contatiner

Output generated from the following commands, such as annotated notebooks, reports, callsites, headers, etc, are stored in the local folder `headergen_output` after the following commands are done executing. 
      
+ Micro Benchmark (generates a csv file with results)

      make microbench

+ Real-world Benchmark (generates annotated notebooks and csv file that reproduce table 2)

      make realworldbench

+ Both Benchmarks

      make all

+ Clean generated output

      make clean

---

This repo contains code for the paper **"Enhancing Comprehension and Navigation in Jupyter Notebooks with Static Analysis"** published at the [SANER Conference 2023](https://arxiv.org/abs/2301.04419).
