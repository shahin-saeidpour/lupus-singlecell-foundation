# Stage 8G decision

## Decision summary

Stage 8G attempted to open the direct baseline acquisition and construction gate.

The real baseline input package is not present.

## Construction decision

`not_run`

## Current status

`required_real_baseline_inputs_missing_construction_blocked`

## Required package before Stage 8H

Stage 8H remains blocked until these files exist and pass audit:

- `artifacts/stage8g/baseline_inputs/pseudobulk_matrix.csv.gz`
- `artifacts/stage8g/baseline_inputs/labels.csv`
- `artifacts/stage8g/baseline_inputs/fold_assignments.csv`
- `artifacts/stage8g/baseline_inputs/donor_inventory.csv`
- `artifacts/stage8g/baseline_inputs/preprocessing_config.yaml`
- `artifacts/stage8g/baseline_inputs/file_hashes.csv`
- `artifacts/stage8g/baseline_inputs/environment.json`

## Prohibited actions

The following remain prohibited in Stage 8G:

- baseline prediction generation;
- baseline metric computation;
- matched canonical rerun;
- external scoring;
- closing Issue 57.

## Next stage status

Stage 8H is not ready.

The next practical action is to place or construct the real Stage 8G baseline input package, then rerun the readiness gate.
