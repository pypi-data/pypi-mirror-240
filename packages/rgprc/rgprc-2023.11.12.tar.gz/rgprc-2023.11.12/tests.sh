#!/bin/bash

# Lint Source with Ruff
ruff check ./rgrpc

# Format Source with Ruff
ruff format ./rgrpc

# Check types in Source with mypy
mypy ./rgrpc/*.py

# Run Tests with pytest
pytest --cov=rgrpc tests/
