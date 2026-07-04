# Stage 8H canonical matched rerun

This package records the Stage 8H canonical matched rerun preflight.

## Intended scope

Stage 8H is intended to run the final matched internal comparison:

- Geneformer primary model outputs;
- direct donor-level pseudobulk baseline;
- identical donor IDs;
- identical labels;
- identical fold assignments;
- identical seeds;
- row-level outputs for both methods;
- fold-level stability review;
- confidence interval calculation;
- artifact manifest and hashes.

## Current status

`blocked_stage8g_inputs_missing`

## Decision

Do not run the canonical matched rerun.

## Reason

Stage 8G recorded that the required real baseline inputs are missing and that Stage 8H is not ready.

## Important lock

Stage 8H does not create predictions, metrics, confidence intervals, or manuscript claims while the direct baseline package is missing.

## Next required action

Return to Stage 8G input placement or construction, then rerun the Stage 8G audit.
