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

### Branch Decision

**Branch B (fallback) is taken.** The deciding facts are:

1. **SLECA atlas data is NOT openly downloadable.** The Zenodo record
   (10.5281/zenodo.17698085) explicitly states: "The record is publicly
   accessible, but files are restricted." The h5ad files require an access
   request/approval and are not freely downloadable. This disqualifies
   Branch A, which requires open access to the SLECA integrated matrix.
2. **SLECA is a preprint** (bioRxiv, Feb 2026, not peer-reviewed), adding
   methodological uncertainty to any integration-derived annotations.
3. **No other large open PBMC scRNA-seq lupus cohort was identified** beyond
   GSE174188 (Perez) and GSE135779 (Nehar-Belaid). All other candidates
   (GSE162577, GSE142016, GSE193867) are too small (≤3 usable samples).

Branch A may be revisited if SLECA files become openly downloadable or if an
alternative large cohort is identified. This does not change the current
assignment.

---

### Assignment Table

| Cohort | Role | Task(s) supported | Documented shift axis vs. development | Assay + chemistry | n SLE | n HC | n inactive-SLE | Access tier | Justification |
|---|---|---|---|---|---|---|---|---|---|
| **GSE174188** — Perez et al. 2022, CLUES/ImmVar | **Development** | Task A (diagnosis, primary); Task B (activity, secondary/exploratory — internal only) | N/A (reference) | 10x Chromium 3' v2, mux-seq | 162 | ~99 | ~133 managed (SLEDAI ≤ 4 expected for many; exact count UNKNOWN — verify at acquisition) | Open (CELLxGENE h5ad); SLEDAI under dbGaP phs002812 | Largest available open lupus PBMC scRNA-seq cohort; multi-ancestry; contains both SLE and HC labels; flare/managed annotation openly available. |
| **GSE135779** — Nehar-Belaid et al. 2020 | **External** | Task A (diagnosis, primary external validation) | **Pediatric** (vs. adult development); different institution/site (Pascual/Banchereau lab vs. UCSF); independent recruitment; different 10x 3' library prep (non-multiplexed vs. mux-seq) | 10x Chromium 3', standard (non-mux) | 41 (33 pSLE + 8 aSLE) | 17 (11 pHC + 6 aHC) | UNKNOWN — verify SLEDAI distribution from paper supplementary; may be thin in pediatric cohort | Open (GEO processed counts); FASTQ controlled (dbGaP phs002048) | Only available independent SLE PBMC scRNA-seq cohort with adequate sample size. Pediatric-to-adult shift is a strong external-validation axis. |

#### Internal-External Validation Within Perez (GSE174188)

Because only one true external cohort (GSE135779) is available and it is
predominantly pediatric, **internal-external sub-splits within GSE174188** are
defined to provide additional supported-generalization evidence:

| Sub-split name | Held-out partition | Shift axis | Purpose |
|---|---|---|---|
| CLUES vs. ImmVar leave-one-source-out | Hold out ImmVar samples; train on CLUES (or vice versa) | Source cohort / recruitment site | Tests generalization across recruitment sites within the same study |
| Ancestry-stratified hold-out | Hold out one ancestry group (e.g., East Asian); train on remaining | Ancestry / genetic background | Tests robustness to population structure |

These internal-external sub-analyses are **supplementary** to the primary
GSE135779 external validation and do not replace it.

---

### Task B — Disease Activity: Feasibility Assessment (Secondary/Exploratory)

Task B (active vs. inactive SLE) is designated **secondary/exploratory** for
external validation. The feasibility assessment is as follows:

**Within GSE174188 (development, internal evaluation):**
- The open CELLxGENE/GEO metadata provides **flare vs. managed** annotations
  (derived from donor_id patterns: `FLARE*` → flare, numeric IDs → managed SLE).
- This provides a **proxy** for active/inactive, but the mapping to SLEDAI-2K > 4
  threshold is not directly available without dbGaP access.
- **Internal cross-validation** on flare vs. managed SLE is feasible using openly
  available labels. This is an exploratory analysis, not a validated external claim.

**Within GSE135779 (external):**
- SLEDAI scores are recorded for pediatric SLE patients, but the **inactive-SLE
  subset (SLEDAI ≤ 4) size is UNKNOWN** and may be thin given that pediatric SLE
  cohorts typically present with higher disease activity.
- Task B external validation on GSE135779 is **not confirmed feasible** until the
  SLEDAI distribution is verified from the paper's supplementary tables at
  acquisition time.

**Conclusion:** Task B external validation is **not guaranteed on open data**.
It will be reported as internal/exploratory (within-Perez flare vs. managed) unless
the GSE135779 SLEDAI distribution confirms a non-trivial inactive subset. This
assessment is honest; we do not overclaim external validation capability for Task B.

---

### Leakage & Overlap Controls

1. **Patient-level disjointness across development / external:**
   GSE174188 (Perez, UCSF CLUES/ImmVar) and GSE135779 (Nehar-Belaid,
   Baylor/Jackson Lab) are independent studies with no shared recruitment sites,
   no shared patient populations, and no shared donor IDs. Patient-level
   disjointness is guaranteed by study independence.

2. **No SLECA overlap risk:** SLECA is not used in this protocol. However, for the
   record: SLECA integrates both GSE174188 (Data-6) and GSE135779 (Data-1). Had
   SLECA been used, strict source-study-level provenance mapping per sample would
   have been required to prevent any source study from straddling the
   development/external boundary. This is documented but not activated.

3. **Internal-external sub-split disjointness within Perez:**
   CLUES vs. ImmVar splits are defined by the source cohort label in the metadata.
   Ancestry-stratified splits are defined by self-reported ancestry. Both splits
   guarantee that no donor appears in both the training and held-out partitions.

4. **No cell-level leakage:** Per the cross-cutting rules in Section 1, all
   predictions are per-patient. Cell-level data from a given patient never
   appears in both training and evaluation sets.


## 3. Harmonization & Labels

TBD (Step 4)

## 4. Metrics & Evaluation Plan

TBD (Step 5)
