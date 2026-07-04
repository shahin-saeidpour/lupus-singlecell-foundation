# Stage 9A operator handoff

## What the operator must do locally

1. Pull the latest `main` branch.
2. Locate the real source artifact that can produce donor-level pseudobulk expression.
3. Copy ready baseline files into `artifacts/stage8g/baseline_inputs/`, or record the local source artifact in `artifacts/stage9a/local_source_registry.csv`.
4. Do not commit large source files.
5. Run the Stage 9A registry audit.
6. Run the Stage 8G baseline input package audit.

## Commands

```bash
git pull origin main
cp artifacts/stage9a/local_source_registry_template.csv artifacts/stage9a/local_source_registry.csv
# edit artifacts/stage9a/local_source_registry.csv with real local paths
python scripts/stage9a_local_artifact_registry_audit.py
python scripts/stage8g_baseline_input_package_audit.py
```

## Expected result before Stage 9B

The registry audit should report:

`ready_for_stage9b_audit`

The Stage 8G package audit should report ready only after the required files exist in `artifacts/stage8g/baseline_inputs/`.
