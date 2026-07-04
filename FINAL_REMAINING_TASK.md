# FINAL REMAINING TASK

This file replaces any further Stage 9D-style blocked handoff.

## Stop rule

Do not create more stages for the same missing-input blocker.

## The only remaining task

Place or register the real local artifact from the 1.2M-cell feature extraction workflow, then run the final completion task.

## Required files for completion

```text
artifacts/stage8g/baseline_inputs/pseudobulk_matrix.csv.gz
artifacts/stage8g/baseline_inputs/labels.csv
artifacts/stage8g/baseline_inputs/fold_assignments.csv
artifacts/stage8g/baseline_inputs/donor_inventory.csv
artifacts/stage8g/baseline_inputs/preprocessing_config.yaml
artifacts/stage8g/baseline_inputs/file_hashes.csv
artifacts/stage8g/baseline_inputs/environment.json
```

If the pseudobulk matrix does not exist yet, create:

```text
artifacts/stage9a/local_source_registry.csv
```

and point it to the real local source artifact. Large source artifacts must remain outside Git tracking.

## One command after files are placed

```bash
python scripts/final_complete_project_once_inputs_exist.py
```

## Completion rule

The project can only be called scientifically complete after the final task reports:

```text
project_completion_status,complete
```

Until then, the project status is:

```text
blocked_missing_real_local_baseline_artifact
```
