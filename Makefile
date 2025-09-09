.PHONY: help install install-dev clean test test-cov lint format type-check docs build upload

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install the package
	pip install -e .

install-dev:  ## Install development dependencies
	pip install -e .[dev]
	pre-commit install

clean:  ## Clean up build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

test:  ## Run tests
	pytest tests/ -v

test-cov:  ## Run tests with coverage
	pytest tests/ --cov=delegated_qc --cov-report=html --cov-report=term

lint:  ## Run linting
	flake8 delegated_qc tests
	black --check delegated_qc tests
	isort --check-only delegated_qc tests

format:  ## Format code
	black delegated_qc tests
	isort delegated_qc tests

type-check:  ## Run type checking
	mypy delegated_qc

docs:  ## Build documentation
	cd docs && make html

docs-serve:  ## Serve documentation locally
	cd docs/_build/html && python -m http.server 8000

build:  ## Build package
	python -m build

upload:  ## Upload to PyPI (requires credentials)
	twine upload dist/*

upload-test:  ## Upload to Test PyPI
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

dev-setup: install-dev  ## Complete development setup
	@echo "Development environment setup complete!"
	@echo "Run 'make test' to verify everything works."

ci:  ## Run all CI checks locally
	make lint
	make type-check
	make test-cov