#!/bin/bash

# Run sync script.
python parc.py

# Command.
if [ "$1" = 'noop' ]; then
  exec sleep 10000d
fi

exec "$@"
