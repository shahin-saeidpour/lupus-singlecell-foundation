# Stage 8F baseline construction plan and execution scaffold

This package starts Stage 8F after the Stage 8E decision that direct baseline artifacts are missing and that the canonical matched rerun must remain blocked.

## Scope

Stage 8F is a design-and-gate stage for the direct baseline needed before the final internal manuscript-hardening comparison.

It defines:

- the primary direct baseline;
- secondary and optional baseline roles;
- required input schemas;
- required output schemas;
- execution scaffold expectations;
- fail-closed stop rules;
- the decision gate for Stage 8G.

## Selected baseline policy

Primary direct baseline: donor-level pseudobulk expression matrix followed by fold-local PCA and balanced logistic regression.

Secondary baseline: donor-level cell-type proportion table followed by balanced logistic regression.

Optional sensitivity baseline: selected-feature expression matrix followed by balanced logistic regression, only if the feature set is pre-registered or selected inside each training fold without label leakage.

## Current status

`baseline_construction_scaffold_complete_execution_not_run`

## Important lock

No numerical baseline execution is performed in Stage 8F.

No metric is invented, estimated, copied, or inferred.

Canonical rerun remains blocked until Stage 8G provides a real baseline input package with matching donor IDs, labels, folds, seeds, and artifact hashes.

## Next stage

Stage 8G — baseline data acquisition / construction.
