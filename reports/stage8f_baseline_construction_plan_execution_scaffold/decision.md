# Stage 8F decision

## Decision summary

Stage 8F defines the direct baseline design and opens the Stage 8G acquisition and construction gate.

## Primary baseline

`donor_level_pseudobulk_pca_balanced_logistic_regression`

This is the required primary direct baseline for the later matched internal comparison.

## Secondary baseline

`donor_level_cell_type_proportion_balanced_logistic_regression`

This is a secondary composition-control baseline only.

## Optional sensitivity baseline

`selected_feature_expression_balanced_logistic_regression`

This is allowed only when the feature list is pre-registered or created inside each training fold.

## Canonical rerun decision

`not_run`

Reason: Stage 8E recorded that the direct baseline package is missing. Stage 8F defines the construction plan and scaffold but does not provide real baseline inputs.

## Numerical execution permission

`blocked_until_stage8g_inputs_exist`

Stage 8H may not run until Stage 8G provides:

- donor-level pseudobulk matrix;
- label table;
- fold assignment table;
- donor IDs matching the primary evaluation;
- file hashes;
- environment manifest.

## Issue policy

Issue #57 remains open. Stage 8F does not perform external scoring.

## Next stage

Stage 8G — baseline data acquisition / construction.
