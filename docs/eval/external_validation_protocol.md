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
| Ancestry-stratified hold-out | Hold out one ancestry group (e.g., East Asian); train on remaining | Ancestry / genetic background | Tests robustness to population structure |

*(Note: A "CLUES vs. ImmVar" leave-one-source-out axis was originally considered but removed. The ImmVar cohort was used in the primary study exclusively as a source of healthy controls, making a source-split degenerate for evaluating diagnosis generalization, as the hold-out would contain no SLE cases.)*

**Constraint on Internal-External Validation:** The ancestry sub-split must be patient-disjoint. The exact per-ancestry case and control counts must be verified post-download, but both Asian and European ancestries are confirmed to contain both cases and controls. These sub-analyses are **supplementary** to the primary GSE135779 external validation and do not replace it.

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

**CARDINAL RULE:** All harmonization statistics (feature vocabulary, highly variable genes [HVGs], normalization parameters, integration/reference model, cell-type reference, and label thresholds) are **FIT ON DEVELOPMENT DATA ONLY** and applied **FROZEN** to the external cohort. The external cohort is **PROJECTED THROUGH** the frozen pipeline and never participates in fitting any parameter. Any statistic derived even partly from external data constitutes leakage and is a protocol violation.

### 3.1 Feature-space harmonization (gene vocabulary)
- **Stable Identifier Space:** All genes must be mapped to a single stable identifier space using Ensembl gene IDs.
- **Reference Annotation:** Gene-symbol to Ensembl reconciliation will use a fixed reference annotation (GENCODE v44 / Ensembl release 110).
- **Frozen Vocabulary:** The model's input gene vocabulary is FROZEN from the development cohort.
- **External Mapping:** For the external cohort, genes are intersected onto the frozen vocabulary:
  - Genes absent in the external cohort but present in the vocabulary are **zero-filled** (or handled per the model's documented missing-gene policy).
  - Genes present in the external cohort but not in the frozen vocabulary are **DROPPED**.
- **HVG Selection:** Any selection of highly variable genes (HVGs) is computed on the development set only and never recomputed on the external cohort.

### 3.2 Normalization
- **Per-cell Normalization:** The standard pipeline is library-size normalization followed by log1p transformation (`log1p(counts / library_size * scale_factor)`).
- **Parameter Fitting:** These operations are performed per-cell and do not cause leakage. However, any dataset-level parameter (e.g., standardizing variance) must be **dev-fit and frozen**.
- **Order of Operations:** 1. Filter cells/genes (on external, filter only to frozen vocabulary), 2. Library-size normalize per cell, 3. log1p transform, 4. Apply frozen dataset-level scaling (if applicable).

### 3.3 Integration / batch handling (LEAKAGE-CRITICAL)
- **Joint Integration Prohibited:** Running joint integration (e.g., Harmony, scVI, Seurat anchor integration) over the pooled development and external datasets is strictly prohibited. This leaks external structure into the embedding.
- **Reference-Projection Approach:** The model/representation is fit entirely on the development cohort. The external cohort is mapped onto the frozen reference (e.g., using scArches/scVI reference mapping or the model's own frozen encoder) **WITHOUT** updating any parameters.
- **Within-Development Batch:** Within the development cohort, batch effects (donor/pool/run) are handled during training. The external cohort is treated as a single held-out batch mapped in at test time.

### 3.4 Cell-type annotation
- If cell-type labels are utilized by the pipeline, they must be derived via **label transfer** from a development-fit reference (frozen).
- Joint re-clustering of development and external data together is prohibited.
- *(Note: If no cell-type labels are explicitly used by the downstream prediction head, this step is omitted, but the projection rule remains.)*

### 3.5 Diagnosis label harmonization + classification-criteria reconciliation
- **Criteria Recorded:**
  - Perez (Development): 1997 ACR criteria.
  - Nehar-Belaid (External): Likely 1997 ACR or 2012 SLICC (standard clinical criteria).
- **Decision Rule:** For the binary case/control task (Task A) on clinically established SLE, samples meeting **ANY** accepted clinical criteria (1997 ACR, 2012 SLICC, or 2019 EULAR/ACR) are assigned a label of `SLE=1`.
- **Limitation & Sensitivity:** Criteria differences are DOCUMENTED as a study limitation. Where feasible, they will be addressed by a sensitivity analysis rather than by attempting a data transformation. We do not pretend the criteria are perfectly identical.
- **Exclusions:** Any sample that is not clearly an SLE case or a clearly healthy control (e.g., other autoimmune diseases, undetermined status) is **excluded** from Task A.

### 3.6 Healthy-control definition harmonization
- **HC Definition:** Healthy Controls (HC) are defined as having no known autoimmune disease.
- **Age Shift:** The age difference between the adult HC in Perez/ImmVar and the pediatric HC in Nehar-Belaid is documented as part of the external **SHIFT** and is not treated as a defect to correct.

### 3.7 Activity label harmonization (Task B, secondary/exploratory, internal-only)
- **Primary Target:** Active (SLEDAI-2K > 4) vs. Inactive (SLEDAI-2K ≤ 4).
- **Label Source (Open Annotation Only):**
  - **Perez:** If numeric SLEDAI scores are not available in the open metadata, the open `flare` vs. `managed` annotation is mapped as a PROXY (`flare` → active; `managed` → inactive). This is explicitly flagged as a proxy that is not identical to a strict SLEDAI cutoff.
  - **Other Indices:** Any external or alternative activity index (e.g., BILAG, PGA, SLAM) is deferred or excluded per the Section 1 fallback. No crosswalk will be invented.
- **Scope Reaffirmation:** Task B remains **internal/exploratory only**. No external activity claim is made.

### 3.8 Per-cohort harmonization worklist

| Cohort | Harmonization Actions Required | Post-download verifications |
|---|---|---|
| **Perez (GSE174188)** <br> *(Development)* | - Map gene symbols to GENCODE v44 / Ensembl 110. <br> - Fit vocabulary and HVGs. <br> - Extract `disease_status` for Task A. <br> - Extract `flare`/`managed` proxy for Task B. <br> - Exclude non-SLE/non-HC samples. | **UNKNOWN — resolve at acquisition:** Exact numeric SLEDAI availability in open metadata; exact per-ancestry case/control counts for sub-splits. |
| **Nehar-Belaid (GSE135779)** <br> *(External)* | - Intersect genes onto frozen development vocabulary. Zero-fill missing genes. <br> - Note chemistry difference (10x 3' non-mux). <br> - Extract SLE/HC labels for Task A. <br> - Exclude non-SLE/non-HC samples. | **UNKNOWN — resolve at acquisition:** Exact clinical classification criteria cited in supplementary; SLEDAI distribution size (active vs inactive subset). |

## 4. Metrics & Evaluation Plan

### 4.1 Prediction unit & aggregation (binding)
- **Patient-Level Unit:** All primary evaluations are performed at the patient/sample level. No cell-level metric is reported as a primary outcome.
- **Aggregation:** Cell-level model outputs (e.g., probabilities) are pooled to the sample level prior to metric computation (e.g., taking the mean of per-cell probabilities, or using the model's dedicated sample-level readout/attention head).

### 4.2 Primary metrics — Task A discrimination
- **Metrics:** Area Under the Receiver Operating Characteristic (AUROC) and Area Under the Precision-Recall Curve (AUPRC). AUPRC is the primary metric of the two, given the inherent case/control imbalance in real-world cohorts.
- **Evaluation Splits:** Metrics will be reported clearly and separately on:
  1. Internal-external leave-one-ancestry-out folds within Perez (GSE174188).
  2. The external cohort (Nehar-Belaid, GSE135779).
- **Operating Point:** The classification threshold is **SELECTED ON DEVELOPMENT** (e.g., Youden's J statistic computed on the development set), **FROZEN**, and then applied to the external cohort. Sensitivity, specificity, Positive Predictive Value (PPV), and Negative Predictive Value (NPV) will be reported at that frozen threshold.

### 4.3 Calibration (LEAKAGE-SENSITIVE, FIRST-CLASS)
- **Metrics:** Reliability curve, Expected Calibration Error (ECE), and Brier score.
- **Reporting:** Calibration metrics are reported **SEPARATELY** for internal, internal-external, and external evaluations.
- **Calibration Adjustment:** Any post-hoc calibration adjustment (e.g., temperature scaling) is **FIT ON DEVELOPMENT ONLY** and applied frozen. We will report BOTH pre- and post-calibration metrics on the external cohort to make calibration drift under shift explicitly visible. Fitting calibration on the external cohort is strictly prohibited.

### 4.4 Uncertainty & selective prediction (the core contribution)
- **Uncertainty Measure:** The specific uncertainty measure emitted by the model (e.g., predictive entropy, variance across MC dropout/ensemble, or a dedicated uncertainty head) will be tracked.
- **Selective Prediction:** Risk-coverage curves and selective accuracy/AUROC at predefined coverages (e.g., 100%, 90%, 75%, 50%) will be reported. The abstention threshold is **SET ON DEVELOPMENT** and frozen for the external cohort.
- **External Analysis:** We will report the abstention rate on the external cohort and analyze whether abstained cases concentrate in the shifted (e.g., pediatric) population, formally evaluating the model's "knows when it doesn't know" capability.

### 4.5 Out-of-distribution / shift behavior
- **OOD Signals:** We will report specific OOD signals, such as comparing the uncertainty distribution between the development and external cohorts, and assessing the detection of the pediatric external cohort as a higher-uncertainty population.
- **Framing:** The external cohort constitutes a covariate/population shift, not an adversarial out-of-distribution set. This will be framed honestly.

### 4.6 Task B (secondary/exploratory, internal-only) metrics
- **Metrics:** AUROC/AUPRC for active vs. inactive classification.
- **Evaluation Split:** Evaluated on **Perez internal splits only**, using the flare/managed PROXY labels (explicitly labeled as proxy).
- **Optional Metrics:** SLEDAI regression metrics (Spearman correlation, Mean Absolute Error [MAE]) will be computed **ONLY** if numeric SLEDAI is openly available (UNKNOWN — resolve at acquisition).
- **External Claim:** No external claim is made for Task B.

### 4.7 Uncertainty quantification of the estimates (statistics)
- **Patient-Level Bootstrap:** All primary metrics will be reported with 95% Confidence Intervals (CIs) calculated via patient-level bootstrap (resampling patients, not cells).
- **Parameters:** `n_bootstrap = 1000`; seed fixed (e.g., `seed = 42`).
- **Internal-External Aggregation:** For internal-external ancestry folds, metrics will be reported as the per-fold mean +/- spread across the folds.

### 4.8 Subgroup / stratified reporting
- **Strata:** Primary metrics will be reported stratified by ancestry, sex, and pediatric vs. adult (for the external cohort), where sample size allows.
- **Minimum-N Rule:** If a stratum contains fewer than 10 cases or controls, it will be reported as "n too small" rather than reporting an unstable point estimate.

### 4.9 Pre-registration & single-use commitments (binding)
- **Single-Use External Cohort:** The external cohort is evaluated **ONCE**, only after the model, pipeline, thresholds, and calibration parameters are fully frozen. No metric, threshold, or hyperparameter will be tuned on the external data.
- **Fixed Metric List:** This metric list is **FIXED** as of this protocol version. Any additional metrics added post-hoc will be explicitly labeled as exploratory/post-hoc in the final manuscript.
- **Reporting Standard:** The final write-up will be completed in accordance with the TRIPOD+AI reporting checklist.
