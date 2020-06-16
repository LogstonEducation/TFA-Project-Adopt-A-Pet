#!/bin/bash

unset INSTANCE_CONNECTION_NAME
unset GAE_APPLICATION
unset PGHOST
unset PGPORT
unset PGDATABASE
unset PGUSER
unset PGPASSWORD

# Add environment variables from .env to environment
echo "Loading environment variables..."

if [ "$1" = "gae" ]; then

set -a
source .env
set +a

fi
