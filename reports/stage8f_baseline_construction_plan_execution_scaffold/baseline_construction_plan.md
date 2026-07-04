# Stage 8F baseline construction plan

## Goal

Stage 8F defines the direct baseline design needed before a later matched comparison against the existing Geneformer primary evaluation outputs.

Stage 8F is not an execution stage. It does not create predictions, metrics, confidence intervals, or manuscript claims.

## Primary direct baseline

Primary baseline: donor-level pseudobulk expression matrix, fold-local PCA, and balanced logistic regression.

Rationale: this baseline compares donor-level Geneformer embeddings against a direct donor-level expression representation while preserving the same unit of analysis.

Required construction rules:

1. Build one pseudobulk expression row per donor.
2. Use only the approved primary evaluation donor universe.
3. Preserve the approved binary target: managed versus FLARE.
4. Use the exact same split IDs, fold IDs, and seeds as the primary evaluation.
5. Fit all learned preprocessing only inside each training fold.
6. Apply train-fold PCA parameters to the held-out fold.
7. Fit balanced logistic regression only on training donors.
8. Produce held-out donor-level predictions only.

## Secondary baseline

Secondary baseline: donor-level cell-type proportion table and balanced logistic regression.

Role: this is a composition-control baseline. It must be reported separately and must not replace the primary direct expression baseline.

## Optional sensitivity baseline

Optional sensitivity baseline: selected-feature expression matrix and balanced logistic regression.

Allowed only if the selected feature list is fixed before the outcome comparison or is selected separately inside each training fold.

Disallowed feature choices:

- using all donors before splitting;
- using held-out outcomes to choose features;
- choosing features after inspecting held-out performance.

## Stage 8H matching contract

The later canonical matched rerun may proceed only if Geneformer and the direct baseline use:

- identical donor IDs;
- identical labels;
- identical split IDs;
- identical fold IDs;
- identical seeds;
- identical row-level prediction schema;
- a complete artifact hash manifest.

## Stage 8F status

`baseline_construction_scaffold_complete_execution_not_run`
