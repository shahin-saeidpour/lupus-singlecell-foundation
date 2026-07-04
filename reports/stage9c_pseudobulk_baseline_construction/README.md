# Stage 9C donor-level pseudobulk baseline construction

Stage 9C is the construction stage for the donor-level pseudobulk baseline package.

## Scope

Stage 9C may construct the direct baseline input only after Stage 9B confirms the required local inputs are present.

The intended construction target is:

`pseudobulk_matrix.csv.gz`

with one row per donor and expression-derived gene columns.

## Current status

`blocked_stage9b_inputs_missing`

## Reason

Stage 9B recorded that the local source registry, pseudobulk matrix, labels, fold assignments, donor inventory, file hashes, and environment manifest are missing.

## Lock

No pseudobulk matrix is constructed in this Stage 9C closeout.

No model is fit.

No predictions or scores are created.

## Required return point

Return to Stage 9A file placement and Stage 9B audit before attempting construction again.
