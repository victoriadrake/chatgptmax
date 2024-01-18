SHELL := /bin/bash
.POSIX:

help: ## Show this help
		@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

make test-upload: ## Build and upload to Test PyPI
		rm dist/*
		python3 -m build
		twine upload --repository-url https://test.pypi.org/legacy/ --username __token__ --password $(TWINE_TOKEN) dist/*

make test-install: ## Install the latest test version
		@echo "TestPyPI needs a moment..."
		sleep 10
		python3 -m pip uninstall chatgptmax -y
		python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps chatgptmax

make publish: ## Build and publish to PyPI
		rm dist/*
		python3 -m build
		twine upload dist/* --username __token__ --password $(PYPI_TOKEN)

make test: test-upload test-install ## Run tests with TestPyPI version
		pytest