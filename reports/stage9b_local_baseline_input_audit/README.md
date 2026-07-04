# Stage 9B local baseline input audit

Stage 9B audits whether the real local baseline input files have been placed or registered after Stage 9A.

## Scope

This stage verifies readiness for donor-level pseudobulk baseline construction.

It checks whether the project has:

- local artifact registry;
- source expression artifact or direct pseudobulk matrix;
- label table;
- fold assignment table;
- donor inventory;
- preprocessing config;
- file hashes;
- environment manifest.

## Current status

`blocked_local_baseline_inputs_not_placed`

## Reason

Stage 9A ended with `stage9b_ready=false`, meaning the real local files were not yet placed or registered.

## Lock

Stage 9B does not construct pseudobulk matrices, compute scores, generate predictions, fit models, or run external scoring.

## Next action

Place or register the real local files, then rerun Stage 9A and Stage 8G audit scripts locally.
