# Stage 8F execution scaffold

## Purpose

This scaffold defines how the later direct baseline execution must be organized. It is intentionally fail-closed and does not execute a numerical baseline in Stage 8F.

## Default paths

Expected Stage 8G input package:

```text
artifacts/stage8g/baseline_inputs/
  pseudobulk_matrix.csv.gz
  labels.csv
  fold_assignments.csv
  donor_inventory.csv
  preprocessing_config.yaml
  file_hashes.csv
  environment.json
```

Optional Stage 8G input package files:

```text
artifacts/stage8g/baseline_inputs/
  cell_type_proportions.csv
  selected_feature_matrix.csv
```

Expected Stage 8H output package after matched execution:

```text
reports/stage8h_canonical_matched_rerun/
  baseline_oof_predictions.csv
  baseline_metrics_by_split.csv
  baseline_summary_metrics.csv
  fold_level_stability.csv
  confidence_intervals.csv
  baseline_artifact_manifest.csv
  execution_decision.csv
```

## Execution sequence for the later runnable stage

1. Validate required input files exist.
2. Validate all donor IDs align between pseudobulk matrix, labels, fold assignments, and donor inventory.
3. Validate labels match the approved binary target.
4. Validate split IDs, fold IDs, and seeds match the primary evaluation policy.
5. Validate every fold has both classes in the training partition.
6. For each split and fold, fit preprocessing only on training donors.
7. Transform held-out donors using train-fold parameters only.
8. Fit balanced logistic regression on training donors.
9. Generate held-out donor-level predictions.
10. Write row-level predictions before metrics.
11. Compute metrics only from row-level predictions.
12. Write manifest and hashes.

## Stage 8F non-execution lock

Stage 8F only records the scaffold. It must not:

- load a real expression matrix;
- fit PCA;
- fit logistic regression;
- generate predictions;
- calculate metrics;
- create confidence intervals;
- perform external scoring;
- close Issue #57.

## Required implementation behavior

A future execution script must stop with a clear decision file when any required input is missing or mismatched. Silent fallback is not allowed.
