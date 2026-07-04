# Baseline comparison plan

## Purpose

The Geneformer embedding result must be compared against direct non-foundation-model baselines before strong manuscript claims.

## Required baseline families

At minimum, run one direct biological baseline and one simple technical baseline.

### Required biological baseline

Preferred:

- donor-level pseudobulk raw-count baseline;
- normalize counts consistently;
- reduce features with PCA or a preregistered feature filter;
- fit balanced logistic regression under the same donor-level CV protocol.

Alternative acceptable biological baselines:

- cell-type proportion baseline;
- pseudobulk highly variable gene PCA baseline;
- pseudobulk differential-expression-score baseline.

### Required technical baseline

- dummy classifier;
- artifact proxy such as embedding norm or cell-count proxy;
- shuffled-label control.

## Required comparison rule

All baselines must use the same donor-level splits as the canonical Geneformer model.

## Reporting

Report for every model:

- ROC-AUC;
- AUPRC;
- balanced accuracy if threshold policy exists;
- confidence interval;
- fold-level stability;
- delta versus Geneformer model.

## Blocking rule

If no raw or pseudobulk baseline is available, the paper must not claim that foundation-model embeddings outperform conventional expression-based baselines.
