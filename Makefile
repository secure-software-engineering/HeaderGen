# comment
# (note: the <tab> in the command line is necessary for make to work)
# target:  dependency1 dependency2 ...
#       <tab> command

export SNIPPETS_PATH = /app/HeaderGen/callsites-jupyternb-micro-benchmark/snippets

all: microbench realworldbench

microbench:
	@echo "#########################################"
	@echo "Running MicroBenchmark..."
	@echo "#########################################"

	cd /app/HeaderGen && \
	python3 callsites-jupyternb-micro-benchmark/micro_benchmark_report.py

realworldbench:
	@echo "#########################################"
	@echo "Running Real-world Bench..."
	@echo "#########################################"

	cd /app/HeaderGen/callsites-jupyternb-real-world-benchmark/scripts && \
	python3 generate_headergen_notebooks.py && \
	python3 compare_annotations.py && \
	python3 compare_macro_benchmark_cg.py

clean:
	rm -r /results/*
