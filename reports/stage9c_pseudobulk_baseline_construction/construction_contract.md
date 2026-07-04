# Stage 9C construction contract

## Intended input

Stage 9C requires either:

1. a ready donor-level pseudobulk matrix; or
2. a local source expression artifact plus metadata sufficient to derive one donor-level row per donor.

## Required output after a valid construction run

A valid future construction run must produce:

- `artifacts/stage8g/baseline_inputs/pseudobulk_matrix.csv.gz`
- `artifacts/stage8g/baseline_inputs/labels.csv`
- `artifacts/stage8g/baseline_inputs/fold_assignments.csv`
- `artifacts/stage8g/baseline_inputs/donor_inventory.csv`
- `artifacts/stage8g/baseline_inputs/preprocessing_config.yaml`
- `artifacts/stage8g/baseline_inputs/file_hashes.csv`
- `artifacts/stage8g/baseline_inputs/environment.json`

## Construction rules

The pseudobulk matrix must:

- contain one row per donor;
- use donor IDs matching the primary evaluation universe;
- preserve the approved binary target labels;
- avoid cell-level train/test splits;
- avoid fitting PCA or any downstream model;
- avoid creating predictions or performance tables.

## Current applicability

This contract is not executed in the current Stage 9C closeout because Stage 9B did not pass.
