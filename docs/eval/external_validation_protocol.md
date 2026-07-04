# External Validation Protocol

## 1. Evaluation Targets

This section defines the prediction tasks against which external validation will
be conducted. It commits to no specific dataset, cohort, or accession. Data
acquisition and cohort assignment are deferred to later steps.

### Cross-Cutting Rules

The following rules apply uniformly to **both** Task A and Task B.

- **Prediction unit.** Every evaluation prediction is made at the
  **patient/sample level**, never at the cell level. When the model produces
  cell-level outputs, those outputs must be pooled (e.g., mean-pooled) to a
  single per-sample prediction before any metric is computed. No cell-level
  metric may be reported as primary evidence of model performance.

- **Input scope filter (record only; do not resolve here).** Both tasks assume
  the model input is **droplet-based scRNA-seq of PBMC / peripheral blood**.
  Other assay technologies (e.g., plate-based Smart-seq2, CITE-seq protein
  channels, spatial transcriptomics) and other tissue compartments (e.g., kidney
  biopsy, skin biopsy) are **out of scope for primary evaluation**. If candidate
  cohorts use out-of-scope assays or compartments, that will be recorded during
  cohort assignment (Step 3) and resolved during harmonization (Step 4); it is
  not addressed here.

- **No commitment to data.** This document defines evaluation targets only. It
  does not name, select, or commit to any dataset, accession, or result.

---

### Task A — Diagnosis (SLE vs. Healthy Control)

| Field | Specification |
|---|---|
| **Objective** | Classify a subject as systemic lupus erythematosus (SLE) versus healthy control. |
| **Positive class** | SLE. |
| **Negative class** | Healthy control (no known autoimmune disease). |
| **Case definition** | Subjects meeting the **2019 EULAR/ACR SLE classification criteria** (Aringer et al., 2019). If a candidate cohort used earlier classification criteria — specifically the 1997 ACR revised criteria or the 2012 SLICC criteria — this discrepancy will be **recorded at cohort assignment (Step 3)** and **reconciled during harmonization (Step 4)**. Earlier-criteria cohorts must never be silently mixed with 2019-criteria cohorts; the reconciliation strategy (e.g., re-adjudication, sensitivity analysis, exclusion) will be defined in Step 4. |
| **Output type** | A **calibrated probability** of the positive class (SLE), in the range [0, 1]. |

#### Optional / Secondary Arm — Disease-Control Discrimination

- **Objective:** Classify a subject as SLE versus **other autoimmune disease**
  (e.g., rheumatoid arthritis) serving as a disease control.
- **Status:** This arm is **optional and secondary**. It is included to assess
  diagnostic specificity against clinically confusable conditions, not as the
  primary evaluation target.
- **Positive class:** SLE.
- **Negative class:** Other autoimmune disease (specific disease(s) to be
  determined when cohorts are assigned in Step 3).
- **Output type:** Calibrated probability of SLE, in the range [0, 1].
- **Activation criterion:** This arm is evaluated only if at least one external
  cohort provides autoimmune-disease controls with adequate sample size. If no
  such cohort is available, this arm is omitted without affecting the primary
  evaluation.

---

### Task B — Disease Activity (Active vs. Inactive SLE)

| Field | Specification |
|---|---|
| **Objective** | Predict lupus disease activity for subjects with confirmed SLE. |
| **Primary formulation** | **Binary classification: active vs. inactive.** This is chosen as the primary formulation because it maps directly to the clinical decision boundary and simplifies metric interpretation across heterogeneous cohorts. |
| **Secondary formulation** | **Regression on SLEDAI-2K** (SLE Disease Activity Index 2000). This is retained as a secondary analysis to preserve ordinal information and enable calibration studies, but it is not the primary evaluation target. |
| **Activity threshold** | A subject is classified as **active** if SLEDAI-2K > 4 and **inactive** if SLEDAI-2K ≤ 4. This threshold aligns with widely used clinical cut-offs for clinically meaningful disease activity. |
| **Positive class** | Active SLE (SLEDAI-2K > 4). |
| **Negative class** | Inactive SLE (SLEDAI-2K ≤ 4). |
| **Case definition** | All subjects must have confirmed SLE (see Task A case definition). Healthy controls are excluded from Task B entirely. |
| **Output type** | A **calibrated probability** of "active" (SLEDAI-2K > 4), in the range [0, 1]. Additionally, because this model is **uncertainty-aware**, an explicit **abstention option** is provided: when model confidence falls below a pre-specified threshold (to be defined in Step 5), the prediction is withheld and the sample is flagged as "abstained" rather than assigned a forced class. Abstention rates and their impact on coverage will be reported alongside standard metrics. |

#### Fallback Rule for Non-SLEDAI Activity Indices

If a candidate external cohort provides a disease-activity index other than
SLEDAI-2K — for example, BILAG (British Isles Lupus Assessment Group), physician
global assessment (PGA), or SLAM (Systemic Lupus Activity Measure) — the
following rule applies:

1. The cohort is **not assumed usable** for Task B until an explicit mapping from
   the alternative index to the active/inactive binary defined above has been
   defined and justified.
2. The mapping strategy (e.g., validated concordance thresholds, published
   cross-walk tables, or exclusion of the cohort from Task B) is **deferred to
   Step 4 (Harmonization & Labels)**.
3. The availability of a non-SLEDAI index will be **recorded at cohort
   assignment (Step 3)** so that harmonization planning can proceed, but the
   cohort will not contribute to Task B evaluation until Step 4 is complete.

---

## 2. Cohort Assignment (development vs. external)

TBD (Step 3)

## 3. Harmonization & Labels

TBD (Step 4)

## 4. Metrics & Evaluation Plan

TBD (Step 5)
