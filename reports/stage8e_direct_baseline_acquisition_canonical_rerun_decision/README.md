# Stage 8E direct baseline acquisition and canonical rerun decision

This package records the decision gate for direct baseline acquisition and canonical rerun.

## Scope

Stage 8E checks whether the project has enough local or repository artifacts to run a direct baseline and then perform a single canonical rerun.

## Current status

`direct_baseline_missing_canonical_rerun_blocked`

## Current finding

The repository has local result artifacts from earlier evaluation and robustness runs, but no direct raw-expression or pseudobulk baseline result was found.

## Decision

Do not run a canonical rerun until the direct baseline package is available.

## Required next input

A direct baseline package must include:

- baseline input matrix or table;
- donor/sample label table;
- split policy or seed list;
- baseline row-level predictions;
- baseline metrics table;
- artifact hashes.
