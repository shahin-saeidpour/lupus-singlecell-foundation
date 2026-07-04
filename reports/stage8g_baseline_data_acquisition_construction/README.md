# Stage 8G baseline data acquisition / construction

This package records the Stage 8G gate for direct baseline data acquisition and construction.

## Scope

Stage 8G is responsible for acquiring or constructing the real donor-level baseline input package required before a canonical matched rerun.

Required real baseline package:

- donor-level pseudobulk expression matrix;
- donor label table;
- fold assignment table matching the primary evaluation;
- donor inventory;
- preprocessing configuration;
- artifact hash manifest;
- environment manifest.

## Current status

`required_real_baseline_inputs_missing_construction_blocked`

## Decision

Do not run the canonical matched rerun.

Do not compute baseline metrics.

Do not generate baseline predictions.

## Reason

Stage 8G defines the expected acquisition and construction package, but the real source input needed to construct the donor-level pseudobulk matrix is not present in the repository.

## Next allowed action

Place or generate the real baseline input package under:

```text
artifacts/stage8g/baseline_inputs/
```

Then run the readiness audit before Stage 8H.
