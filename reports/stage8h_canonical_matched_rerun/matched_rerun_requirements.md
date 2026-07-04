# Stage 8H matched rerun requirements

## Required matched comparison

The canonical rerun must compare the existing primary Geneformer evaluation against the direct baseline under one matched protocol.

## Required primary-side inputs

The primary side must provide:

- row-level out-of-fold donor predictions;
- split-level metrics;
- donor inventory;
- split and fold assignments;
- artifact hashes or source package manifest.

## Required baseline-side inputs

The baseline side must provide:

- donor-level pseudobulk matrix;
- label table;
- fold assignment table;
- donor inventory;
- baseline row-level out-of-fold predictions after execution;
- baseline metrics after execution;
- artifact hashes.

## Required matching keys

The rerun may proceed only if both sides match exactly on:

- donor IDs;
- labels;
- split IDs;
- fold IDs;
- seeds;
- target definition;
- held-out evaluation rows.

## Required output tables after a valid rerun

The following outputs are required after real execution:

- `primary_oof_predictions_matched.csv`
- `baseline_oof_predictions_matched.csv`
- `matched_metrics_by_split.csv`
- `matched_summary_metrics.csv`
- `fold_level_stability.csv`
- `confidence_intervals.csv`
- `artifact_manifest.csv`
- `execution_decision.csv`

## Current applicability

These outputs are not created in the current Stage 8H package because the baseline input package is missing.
