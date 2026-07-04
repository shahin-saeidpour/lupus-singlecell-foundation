# Stage 8D decision

## Final decision

Stage 8D is complete as a partial local artifact intake and execution audit.

Status: `partial_local_artifacts_detected_canonical_execution_incomplete`.

## What was detected

Local artifacts were found for:

- primary evaluation summary metrics;
- primary split-level metrics;
- primary row-level predictions;
- donor inventory;
- robustness summary metrics;
- robustness split-level metrics;
- robustness row-level predictions;
- permutation summary;
- artifact-proxy audit.

## What was recorded

The repository now records:

- local artifact inventory with SHA256 hashes;
- metric snapshot from available local files;
- row-level prediction audit;
- remaining blockers.

## What was not completed

Stage 8D did not regenerate a new canonical run and did not run a direct baseline comparison.

## Scientific consequence

The project is stronger than before because row-level prediction artifacts were found and hashed.

However, the manuscript-grade hardening package remains incomplete until a single canonical run and a direct baseline comparison are executed.

## Recommended next stage

`Stage 8E — direct baseline acquisition and canonical rerun decision`.
