SHELL := /bin/bash
.POSIX:

help: ## Show this help
		@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

clean-dist:
		@if [ -d "dist" ]; then \
			echo "Removing 'dist' directory..."; \
			rm -rf dist; \
			echo "'dist' directory removed."; \
		else \
			echo "'dist' directory does not exist."; \
		fi

test-upload: ## Build and upload to Test PyPI
		rm dist/*
		python3 -m build
		twine upload --repository-url https://test.pypi.org/legacy/ --username __token__ --password $(TWINE_TOKEN) dist/*

test-install: ## Install the latest test version
		@echo "TestPyPI needs a moment..."
		sleep 10
		python3 -m pip uninstall chatgptmax -y
		python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps chatgptmax

publish: clean-dist ## Build and publish to PyPI
		python3 -m build
		twine upload dist/* --username __token__ --password $(PYPI_TOKEN)

test: test-upload test-install ## Run tests with TestPyPI version
		pytest