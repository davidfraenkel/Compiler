# Define the directory containing test files
TEST_DIR := test

# Define the directory containing output files
OUTPUT_DIR := test

# Define the command to run for each test file
TEST_COMMAND := ./main.exe

# Define the python command
PYTHON_COMMAND := python

# Find all .txt files recursively in the test directory
TEST_FILES := $(wildcard $(TEST_DIR)/*/*.txt)

build: 
	@echo "Compiling Files"
	@dune build

python:
	@python3 main.py
# Define a target to run the command for each test file
run_tests:
	@echo "Creating python files..."
	@for file in $(TEST_FILES); do \
		$(TEST_COMMAND) -silent $$file; \
		if [ $$? -ne 0 ]; then \
			echo "Error running test $$file"; \
			exit 1; \
		fi; \
	done
	@echo "Cormen Pseudocode successfully compiled."

run_debug:
	@echo "Creating python files..."
	@for file in $(TEST_FILES); do \
		$(TEST_COMMAND) $$file; \
		if [ $$? -ne 0 ]; then \
			echo "Error running test $$file"; \
			exit 1; \
		fi; \
	done
	@echo "Cormen Pseudocode successfully compiled."


test: build run_tests python
debug: build run_debug