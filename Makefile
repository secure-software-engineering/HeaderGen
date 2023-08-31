export ROOT_PATH ?= /app/HeaderGen
export TEST_SUITE_DIR ?= $(ROOT_PATH)/callsites-jupyternb-micro-benchmark/snippets
export MICRO_BENCH_PATH ?= $(ROOT_PATH)/callsites-jupyternb-micro-benchmark
export REALWORLD_BENCH_PATH ?= $(ROOT_PATH)/callsites-jupyternb-real-world-benchmark/scripts
export REALWORLD_SUITE_DIR ?= $(ROOT_PATH)/callsites-jupyternb-real-world-benchmark
export RESULTS_PATH ?= $(ROOT_PATH)/headergen_output

all: prepare clean microbench realworldbench

prepare:
	@echo "#########################################"
	@echo "Preparing environment..."
	@echo "#########################################"
	mkdir -p $(RESULTS_PATH)

microbench:
	@echo "#########################################"
	@echo "Running MicroBenchmark..."
	@echo "#########################################"
	cd $(MICRO_BENCH_PATH) && \
	python3 micro_benchmark_report.py --test_suite_dir $(TEST_SUITE_DIR) --results_dir $(RESULTS_PATH)

realworldbench:
	@echo "#########################################"
	@echo "Running Real-world Bench..."
	@echo "#########################################"
	cd $(REALWORLD_BENCH_PATH) && \
	python3 generate_headergen_notebooks.py --test_suite_dir $(REALWORLD_SUITE_DIR)/notebooks --results_dir $(RESULTS_PATH)/annotated_notebooks && \
	python3 compare_annotations.py --test_suite_dir $(REALWORLD_SUITE_DIR) --results_dir $(RESULTS_PATH) && \
	python3 compare_macro_benchmark_cg.py --test_suite_dir $(REALWORLD_SUITE_DIR) --results_dir $(RESULTS_PATH)

clean:
	rm -r $(RESULTS_PATH)/*
