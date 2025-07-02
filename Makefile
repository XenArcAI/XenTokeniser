.PHONY: install test lint format typecheck clean

# Variables
PYTHON ?= python3.8
PIP ?= pip3
PYTEST ?= pytest
COVERAGE ?= coverage
MYPY ?= mypy
BLACK ?= black
ISORT ?= isort
FLAKE8 ?= flake8

# Source and test directories
SRC = xen_tokenizer
TESTS = tests

install:
	@echo "Installing package in development mode..."
	$(PIP) install -e ".[dev]"
	pre-commit install

test:
	@echo "Running tests..."
	$(PYTEST) $(TESTS) -v --cov=$(SRC) --cov-report=term-missing

lint:
	@echo "Checking code style with flake8..."
	$(FLAKE8) $(SRC) $(TESTS)

format:
	@echo "Formatting code with Black..."
	$(BLACK) $(SRC) $(TESTS)
	@echo "Sorting imports with isort..."
	$(ISORT) $(SRC) $(TESTS)

typecheck:
	@echo "Type checking with mypy..."
	$(MYPY) $(SRC) $(TESTS)

check: lint typecheck test

clean:
	@echo "Cleaning up..."
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]'`
	rm -f `find . -type f -name '*~'`
	rm -f `find . -type f -name '.*~'`
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf htmlcov
	rm -f .coverage
	rm -f .coverage.*
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

.PHONY: docs
docs:
	@echo "Building documentation..."
	$(MAKE) -C docs html

.PHONY: release
release: clean
	@echo "Creating source and wheel distributions..."
	$(PYTHON) -m build

.PHONY: publish
publish: release
	@echo "Uploading package to PyPI..."
	twine upload dist/*

.PHONY: all
all: install check
