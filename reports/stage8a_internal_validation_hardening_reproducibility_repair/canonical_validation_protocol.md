# Canonical validation protocol

## Decision

All manuscript-facing internal validation must use one canonical protocol.

## Approved protocol

Use donor-level repeated stratified cross-validation with:

- donor-level split only;
- no cell-level leakage;
- fixed positive class: FLARE;
- fixed negative class: managed SLE;
- fixed model family: mean donor embedding, PCA(20), balanced logistic regression;
- fixed seed list recorded in the report;
- fixed metric set recorded before execution.

## Required reporting

Report:

- number of folds;
- number of repeats;
- seed list;
- per-fold class counts;
- per-fold ROC-AUC;
- per-fold AUPRC;
- per-fold balanced accuracy;
- per-fold sensitivity and specificity;
- mean, standard deviation, and confidence intervals;
- row-level predictions with donor IDs.

## Protocol conflict rule

If two historical reports used different protocols, do not mix their metrics in the manuscript.

A single final table must be regenerated under this canonical protocol.

## Small-positive-class caveat

Because the FLARE class has only 14 donors, fold-level metrics must be interpreted cautiously. ROC-AUC and AUPRC must be accompanied by fold stability and confidence intervals.
