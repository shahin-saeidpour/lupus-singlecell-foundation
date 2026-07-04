# Stage 8C local run order

## Order

1. Collect local input files.
2. Compute file hashes.
3. Validate table columns and row counts.
4. Build repeat and fold assignments.
5. Run primary model on fixed splits.
6. Run baseline model on the same splits.
7. Write row-level outputs.
8. Write metric tables.
9. Write final audit summary.

## Stop rule

If any required local input group is missing, stop before metrics are generated.

## Output rule

All generated result tables must include the run identifier, source commit, and input manifest hash.
