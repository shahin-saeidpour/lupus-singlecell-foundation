# Stage 8B execute canonical internal validation and baseline comparison

This package records the execution attempt for canonical internal validation and baseline comparison.

## Scope

Stage 8B is intended to execute the Stage 8A repair plan:

- regenerate canonical donor-level repeated stratified CV metrics;
- create row-level prediction tables;
- create fold assignment tables;
- run direct raw-count or pseudobulk baselines;
- record artifact manifests and hashes.

## Current execution result

Execution status: `blocked_missing_required_artifacts`.

The repository currently does not contain the raw donor embedding files, row-level prediction table, fold assignment table, or raw/pseudobulk baseline inputs needed to execute the repair inside the repository.

## What Stage 8B can complete now

Stage 8B can complete the execution gate and runbook:

- identify missing execution inputs;
- define exact required inputs;
- define exact required outputs;
- define canonical metric report format;
- define baseline result format;
- block manuscript-upgrade claims until real execution is complete.

## What Stage 8B cannot complete now

Stage 8B cannot honestly produce new canonical metrics or baseline results without the real input artifacts.

## Next requirement

Provide or generate the missing artifacts locally, then rerun this stage as a real execution stage.
