# Canonical execution runbook

## Purpose

This runbook defines the real execution steps required after the missing artifacts are available.

## Step 1: prepare inputs

Required local inputs:

- donor embedding archive;
- donor labels;
- canonical seed list;
- raw or pseudobulk expression matrix;
- sample metadata;
- artifact manifest template.

## Step 2: construct canonical folds

Use donor-level repeated stratified cross-validation.

For every repeat and fold, record:

- train donor IDs;
- test donor IDs;
- FLARE count in train and test;
- managed-SLE count in train and test;
- seed;
- split identifier.

## Step 3: run Geneformer embedding model

For each split:

- aggregate to mean donor embedding;
- fit PCA(20) only on train donors;
- transform test donors;
- fit balanced logistic regression only on train donors;
- score test donors;
- save row-level predictions.

## Step 4: run direct baseline

Use the same fold assignments.

Preferred baseline:

- donor-level pseudobulk raw-count baseline;
- normalized consistently;
- PCA or preregistered feature filter fitted only on train donors;
- balanced logistic regression;
- row-level predictions saved.

## Step 5: compute final metrics

Compute for each model:

- ROC-AUC;
- AUPRC;
- balanced accuracy if threshold policy exists;
- sensitivity;
- specificity;
- per-fold class counts;
- mean, standard deviation, and confidence interval.

## Step 6: write reproducibility package

Write:

- canonical metrics table;
- row-level prediction table;
- fold assignment table;
- baseline metrics table;
- artifact manifest with hashes;
- environment manifest;
- execution log.

## Stop rule

If any required input is missing, do not generate manuscript metrics.
