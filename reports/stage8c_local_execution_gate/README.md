# Stage 8C local execution gate

This package records the local-input gate for the next execution pass.

## Status

`required_local_inputs_missing`

## Required input groups

- model input archive;
- sample target table;
- baseline input table;
- seed list;
- file hash manifest;
- environment manifest.

## Decision

The next execution pass cannot produce final tables until these input groups are available locally.
