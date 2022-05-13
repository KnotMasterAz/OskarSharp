#!/usr/bin/env bash

# Delete the build directory
[ -d "build" ] && rm -rf build

# Create structure (should probably check if directory exist already)
mkdir build

# Combine all ".oskar" files into one a single file called "knot" excluding "project.oskar" (should search for files recursively)
find . -iname '*.oskar' -not -name 'project.oskar' -exec cat {} +> knot

# Move the knot file to build knot
mv knot build/knot

# Run the python transpiler with flags for running after compile (--run) logging to console (--log) and targeting Console export (--Console)
./az/az.py build/knot --Console --log --run