#!/bin/bash

# Ensure you're in the repo root when calling this script
# Run with: ./scripts/run.sh

source .venv/bin/activate
PYTHONPATH=src python3 -m web_search "$@"