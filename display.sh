#!/bin/bash
cd "$(dirname "$0")"
echo $(uv run main.py $1)
