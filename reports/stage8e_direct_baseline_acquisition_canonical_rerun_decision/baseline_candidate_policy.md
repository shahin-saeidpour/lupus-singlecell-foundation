# Baseline candidate policy

## Decision

A direct baseline is required before upgrading the manuscript claim.

## Preferred baseline

Use a donor-level expression baseline with the same labels and the same split policy as the primary model.

## Acceptable baseline candidates

1. donor-level pseudobulk matrix with PCA and balanced logistic regression;
2. donor-level selected-feature expression matrix with balanced logistic regression;
3. donor-level cell-type proportion table with balanced logistic regression as a secondary baseline.

## Required rule

The baseline must use the same donor IDs, labels, repeats, folds, and seeds as the primary model comparison.

## Block rule

If the direct baseline package is not available, do not claim superiority over conventional expression-derived features.
