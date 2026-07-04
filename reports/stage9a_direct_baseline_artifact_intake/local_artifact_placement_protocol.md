# Stage 9A local artifact placement protocol

## Goal

Place the real local files needed for direct baseline construction without committing large source data into GitHub.

## Required local target directory

Use this directory for real baseline inputs:

```text
artifacts/stage8g/baseline_inputs/
```

## Required files

The later audit expects:

```text
artifacts/stage8g/baseline_inputs/pseudobulk_matrix.csv.gz
artifacts/stage8g/baseline_inputs/labels.csv
artifacts/stage8g/baseline_inputs/fold_assignments.csv
artifacts/stage8g/baseline_inputs/donor_inventory.csv
artifacts/stage8g/baseline_inputs/preprocessing_config.yaml
artifacts/stage8g/baseline_inputs/file_hashes.csv
artifacts/stage8g/baseline_inputs/environment.json
```

## If the pseudobulk matrix does not exist yet

Place the raw or normalized expression source artifact outside Git tracking and record its path in:

```text
artifacts/stage9a/local_source_registry.csv
```

The source artifact must not be committed if it is large.

## Expected source artifact types

Allowed source candidates:

- AnnData or h5ad file with donor IDs and gene expression;
- cell-level matrix plus cell metadata with donor IDs;
- already constructed donor-level pseudobulk matrix;
- controlled local export from the original 1.2M-cell feature extraction workflow.

## Prohibited placement

Do not commit large raw matrices, h5ad files, or full 1.2M-cell archives into GitHub.

Only commit small manifests, schemas, hashes, and decision files.

## Handoff

After local placement, run:

```bash
python scripts/stage9a_local_artifact_registry_audit.py
python scripts/stage8g_baseline_input_package_audit.py
```
