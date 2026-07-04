# Stage 8G acquisition and construction plan

## Objective

Create a real donor-level direct baseline input package for the later Stage 8H matched comparison.

Stage 8G does not compare models. It only prepares and audits the baseline inputs.

## Required construction target

Primary target:

`donor_level_pseudobulk_expression_matrix`

The matrix must contain one row per donor and numeric gene-expression features as columns.

## Required donor universe

The donor universe must match the primary evaluation donor set exactly.

Expected class labels from the current primary evaluation context:

- managed
- FLARE

No additional class may be added in Stage 8G.

## Construction path

1. Locate the real source expression input or already constructed donor-level pseudobulk matrix.
2. Validate donor IDs before writing any derived table.
3. Build or import one donor-level pseudobulk row per approved donor.
4. Attach labels from the approved label table.
5. Attach fold assignments from the same policy used by the primary evaluation.
6. Write the donor inventory.
7. Write preprocessing config for fold-local PCA and balanced logistic regression.
8. Hash every input and generated artifact.
9. Write the Stage 8G construction decision.

## Required non-leakage rule

Stage 8G may construct input matrices and manifests only. It must not fit PCA, fit logistic regression, generate out-of-fold predictions, calculate metrics, or inspect held-out performance.

## Blocker

The repository currently does not contain the real source input needed to construct the donor-level pseudobulk matrix.

Therefore the current Stage 8G status is:

`required_real_baseline_inputs_missing_construction_blocked`
