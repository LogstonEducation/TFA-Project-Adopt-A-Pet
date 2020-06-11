#!/bin/bash

# Start up virtualenv
echo "Staring virtualenv..."
source ../venv/bin/activate

# Add environment variables from .env to environment
echo "Loading environment variables..."
set -a
source .env
set +a

echo "Done."
