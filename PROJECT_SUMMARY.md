# Lupus Single-Cell Foundation — External Evaluation

## Goal
Evaluate a single-cell lupus (SLE vs. healthy) diagnosis model, with a focus on
rigorous EXTERNAL validation on an independent cohort.

## Data
- Development: GSE174188 (Perez et al. 2022), 261 donors (162 SLE / 99 HC), adult, PBMC. Verified real (1,263,676 cells x 30,933 genes).
- External (held out, single-use): GSE135779 (Nehar-Belaid et al. 2020), 56 donors (40 SLE / 16 HC), pediatric + small adult subset. Scored ONCE.

## Method
- Per-donor pseudobulk aggregation of raw counts.
- Baseline model: LogisticRegression (probabilistic).
- Frozen preprocessing: normalize_total(1e4) + log1p. Genes matched to development vocabulary by Ensembl ID (100% overlap).
- Model frozen before external data was accessed; hash recorded; verified unchanged after scoring.

## Internal validation (leave-one-ancestry-out within development)
- Asian held out:    AUROC 0.990
- European held out: AUROC 0.903
- Pooled out-of-fold: AUROC 0.943

## External validation (GSE135779, single-use)
- POOLED    AUROC 0.936  95% CI [0.864, 0.985]  n=56
- ADULT     AUROC 0.914  95% CI [0.657, 1.000]  n=12  (primary like-for-like; small n, wide CI)
- PEDIATRIC AUROC 0.937  95% CI [0.850, 0.991]  n=44  (harder age shift; firmer estimate)
- Brier ~0.16 (calibration is the honest weak point)
- Known failure mode: confident false-negatives on interferon-low / low-activity SLE.

## What is NOT done (future work)
- Geneformer foundation model NOT built (this is a baseline only).
- Disease-activity task (Task B) NOT completed.
- Only one external cohort available (audit found no second large open PBMC SLE dataset).

## Reproducibility
- Model hash: 0D62CEF1ADA017D500ACAE684D8B3DF4E2CDA44EC4731835DBF8D3754138E0FA
- External raw data kept outside the repo; scored once by hand.
