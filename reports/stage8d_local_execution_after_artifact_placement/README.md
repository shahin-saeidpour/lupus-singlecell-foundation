# Stage 8D local execution after artifact placement

This package records the Stage 8D local artifact intake and execution decision.

## Local artifact check

Local result artifacts were detected in the working environment:

- `lupus_primary_eval`;
- `lupus_internal_robustness_ultrafast`.

These artifacts include summary metrics, split-level metrics, row-level out-of-fold predictions, donor inventory, permutation summary, and artifact-proxy audit files.

## Current status

`partial_local_artifacts_detected_canonical_execution_incomplete`

## What is available

Available local artifacts partially address Stage 8A and Stage 8B reproducibility concerns because they include row-level prediction files and split-level metric files.

## What is still missing

Full canonical execution is still blocked because the local artifact set does not include a direct raw-count or pseudobulk baseline input/result package.

## Decision

Do not upgrade manuscript claims yet.

Stage 8D can record and hash the available artifacts, but the final canonical execution and baseline comparison remain incomplete until a direct baseline package is provided or generated.
