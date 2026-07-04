# Dataset Audit — Candidate Cohorts for External Validation

> **Status:** Inventory only. No data has been downloaded, no cohort has been
> selected, and no development/external designation has been made. This audit
> feeds into Step 3 (Cohort Assignment) and Gate 1.
>
> **Date:** 2026-07-04  
> **Phase:** Pre-acquisition

---

## Methodology

Each candidate cohort was researched using the following authoritative sources:

1. The primary paper's Data Availability statement.
2. The GEO record landing page (ncbi.nlm.nih.gov/geo).
3. The CZ CELLxGENE Discover portal (cellxgene.cziscience.com).
4. The dbGaP / ImmPort study record (where applicable).

Fields that could not be verified from an authoritative source are marked
**UNKNOWN — \<what to check\>** rather than guessed.

---

## Cohort Inventory Table

> **Note on table width:** Due to the number of required columns, the table is
> split into three panels below. Each panel uses the same cohort identifiers
> (rows) so they can be cross-referenced.

### Panel A — Identity & Assay

| # | Cohort / Paper | Accession | Source repo | Assay + chemistry | Tissue / compartment |
|---|---|---|---|---|---|
| 1 | Perez et al. 2022, *Science* — CLUES/ImmVar mux-seq cohort | GSE174188 (GEO); also CELLxGENE dataset `218acb0f-9f2f-4f76-b90b-15a4b7c7f629`; raw/genotype under dbGaP phs002812 | GEO, CELLxGENE, dbGaP | 10x Chromium Single Cell **3' v2**, droplet-based (mux-seq multiplexed) | PBMC / peripheral blood — **in scope** |
| 2 | Nehar-Belaid et al. 2020, *Nature Immunology* — pediatric SLE + adult validation | GSE135779 (GEO — processed counts); raw FASTQ under dbGaP phs002048 | GEO, dbGaP | 10x Chromium **3'**, droplet-based | PBMC / peripheral blood — **in scope** |
| 3 | Spencer et al. 2022, *Science Immunology* — marginal zone B cells | GSE193867 (GEO) — **ACCESSION VERIFIED but cohort is NOT a lupus PBMC study**; it is a B-cell biology study with incidental SLE/HC samples | GEO | UNKNOWN — check paper for exact 10x chemistry (platform listed as GPL16791 = HiSeq 2500) | CD19+ B-cell-enriched PBMC fractions — partially in scope (sorted, not whole PBMC) |
| 4 | GSE162577 — "Single cell RNA sequencing reveals cellular heterogeneity of PBMC of SLE patients" | GSE162577 (GEO) — **ACCESSION VERIFIED** | GEO | 10x Chromium **3'**, droplet-based (GPL24676 = Illumina NovaSeq + 10x) | PBMC / peripheral blood — **in scope** |
| 5 | GSE142016 — "Transcriptomic, epigenetic and functional analyses implicate neutrophil diversity in the pathogenesis of SLE" (scRNA-seq sub-series) | GSE142016 (GEO) — part of super-series GSE139360; **ACCESSION VERIFIED** | GEO | UNKNOWN — check paper for exact 10x chemistry; platform listed as GPL24676 | PBMC + low-density granulocytes (LDGs) + normal-density neutrophils — **partially in scope** (PBMC fraction usable; neutrophil/LDG fractions may be separable) |
| 6 | Arazi et al. 2019, *Nature Immunology* — AMP SLE Phase I kidney biopsies | ImmPort SDY997; dbGaP phs001457 — **ACCESSION VERIFIED (ImmPort)**; no standard GEO accession | ImmPort, dbGaP | 10x Chromium, droplet-based; UNKNOWN — check paper for exact 3'/5' chemistry | **Kidney biopsy** — **OUT OF SCOPE** for primary evaluation (tissue compartment) |

### Panel B — Sample Counts & Labels

| # | n samples (total) | n SLE | n healthy control | n other-autoimmune control | Diagnosis label present? | Activity label present? (which index) | Inactive-SLE subset present & sized? |
|---|---|---|---|---|---|---|---|
| 1 | ~264 unique donors (per paper: 162 SLE + ~99 HC; some with longitudinal samples; project status records 261 donors) | 162 SLE (of which ~19 flare, ~10 post-treatment, remainder managed/inactive) | ~99 | 0 reported | Yes — SLE vs. healthy annotated in metadata (donor_id patterns and disease status field) | SLEDAI and SELENA-SLEDAI Flare Index referenced in paper; **however, per-donor SLEDAI scores may be under controlled access in dbGaP phs002812** — UNKNOWN whether numeric SLEDAI is in the open CELLxGENE/GEO metadata. Flare/managed status is annotated. | Yes — the managed SLE group (~133 donors per project status, SLEDAI ≤ 4 expected for many) constitutes a substantial inactive-SLE subset. **Exact SLEDAI distribution UNKNOWN — verify from dbGaP or supplementary tables.** |
| 2 | ~58 donors total (33 pediatric SLE + 11 pediatric HC + 8 adult SLE + 6 adult HC) | 41 SLE (33 pediatric + 8 adult) | 17 (11 pediatric + 6 adult) | 0 reported | Yes — SLE vs. healthy annotated | Yes — SLEDAI scores recorded for pediatric SLE patients; disease activity described as varying degrees. | UNKNOWN — check paper supplementary tables for SLEDAI distribution. Pediatric SLE cohorts tend to have higher baseline activity; **inactive subset (SLEDAI ≤ 4) may be thin**. |
| 3 | ~6 total (3 SLE + 3 HC per GEO record) | 3 | 3 | 0 | Yes (SLE vs. HC labeled) | UNKNOWN — unlikely; this is a B-cell biology study, not a disease-activity study | UNKNOWN — with only 3 SLE patients, subset analysis is not meaningful |
| 4 | UNKNOWN — conflicting reports (some sources say 2 SLE samples, others cite 1 SLE + 1 HC); **verify from GEO sample list: GSM4954811–GSM4954813 = 3 GSM entries** | UNKNOWN — check GEO sample metadata for exact SLE vs. HC counts | UNKNOWN — check GEO sample metadata | 0 reported | UNKNOWN — check sample annotations | UNKNOWN — no disease-activity index mentioned in available metadata | UNKNOWN — sample size too small for meaningful subset |
| 5 | ~3 scRNA-seq samples (per GEO record) | UNKNOWN — check which samples are SLE vs. HC vs. neutrophil fractions | UNKNOWN | 0 reported | UNKNOWN — check sample annotations for SLE/HC labels | UNKNOWN — paper focuses on neutrophil diversity, not activity scoring | UNKNOWN — sample size too small for meaningful subset |
| 6 | 34 total (24 LN kidney biopsies + 10 living-donor controls) | 24 (lupus nephritis) | 10 (living kidney donors) | 0 | Yes — LN vs. healthy control | UNKNOWN — check if ISN/RPS class or activity index is recorded; this is kidney tissue, not PBMC | Not applicable — kidney biopsy, out of scope for PBMC-based evaluation |

### Panel C — Criteria, Demographics, Access & Usability

| # | Case criteria used | Ancestry / age | Access tier (processed expression + labels) | Download format | Source link | **Usability flag** |
|---|---|---|---|---|---|---|
| 1 | **1997 ACR criteria** (CLUES cohort standard). Not 2019 EULAR/ACR. Reconciliation required per protocol Step 4. | Adult; multi-ancestry (cohort includes diverse self-reported ancestry) | Processed counts + cell-type annotations: **open** via CELLxGENE (h5ad) and GEO. Raw sequences + dense genotype + sensitive clinical metadata (including SLEDAI scores): **controlled** via dbGaP phs002812. | h5ad (CELLxGENE), supplementary files (GEO) | [GEO GSE174188](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE174188); [CELLxGENE](https://cellxgene.cziscience.com/) | **Diagnosis: usable** (SLE vs. HC labels present). **Activity: questionable** — flare/managed annotation available but numeric SLEDAI may require dbGaP access; inactive-SLE subset size needs verification. |
| 2 | UNKNOWN — check paper methods section for exact criteria cited. Study published 2020; likely 1997 ACR or 2012 SLICC (pre-dates 2019 EULAR/ACR widespread adoption). Reconciliation required per protocol Step 4. | **Pediatric** (primary cohort: children) + small **adult** validation subset | Processed counts (CellRanger outputs): **open** via GEO GSE135779. Raw FASTQ: **controlled** via dbGaP phs002048. | mtx / tsv.gz (GEO — CellRanger outputs) | [GEO GSE135779](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE135779); [GitHub](https://github.com/dnehar/SingleCells_SLE_paper) | **Diagnosis: usable** (SLE vs. HC labels present; note pediatric population). **Activity: questionable** — SLEDAI recorded but inactive-SLE subset size unknown and may be thin in pediatric cohort with predominantly active patients. |
| 3 | UNKNOWN — check paper methods | UNKNOWN — check paper for age/ancestry | **Open** via GEO (supplementary tar.gz files) | tar.gz (GEO supplementary) | [GEO GSE193867](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE193867) | **Neither** — too few samples (n=6), not a lupus disease study, sorted B-cell fractions rather than whole PBMC. |
| 4 | UNKNOWN — check paper methods | UNKNOWN — check paper | **Open** via GEO | UNKNOWN — check GEO supplementary files | [GEO GSE162577](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE162577) | **Neither** — too few samples (≤3) for meaningful evaluation on either task. |
| 5 | UNKNOWN — check paper methods (Kaplan et al.) | Adult; UNKNOWN ancestry | **Open** via GEO | UNKNOWN — check GEO supplementary files | [GEO GSE142016](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE142016) | **Neither** — too few scRNA-seq samples (~3), mixed cell fractions (PBMC + LDG + neutrophils). |
| 6 | UNKNOWN — check paper methods (AMP consortium criteria) | Adult; UNKNOWN ancestry distribution | **Controlled** via ImmPort SDY997 (requires account) and dbGaP phs001457. | UNKNOWN — check ImmPort for available formats | [ImmPort SDY997](https://www.immport.org/); [dbGaP phs001457](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs001457) | **Neither (compartment out of scope)** — kidney biopsy tissue, not peripheral blood PBMC. |

---

## Summary of Usability Flags

| # | Cohort | Diagnosis (Task A) | Activity (Task B) | Overall | Key limitation |
|---|---|---|---|---|---|
| 1 | Perez et al. 2022 (GSE174188) | ✅ Usable | ⚠️ Questionable | **Diagnosis usable; activity needs SLEDAI verification** | Numeric SLEDAI may require dbGaP; case criteria = 1997 ACR not 2019 EULAR/ACR |
| 2 | Nehar-Belaid et al. 2020 (GSE135779) | ✅ Usable | ⚠️ Questionable | **Diagnosis usable; activity needs inactive-subset sizing** | Pediatric population; inactive-SLE subset may be thin; case criteria unknown |
| 3 | Spencer et al. 2022 (GSE193867) | ❌ Not usable | ❌ Not usable | **Neither** | Not a lupus study; only 6 samples; sorted B cells not whole PBMC |
| 4 | GSE162577 | ❌ Not usable | ❌ Not usable | **Neither** | Too few samples (≤3) for any meaningful evaluation |
| 5 | GSE142016 | ❌ Not usable | ❌ Not usable | **Neither** | Too few scRNA-seq samples (~3); mixed cell fractions |
| 6 | Arazi et al. 2019 (AMP SLE, SDY997) | ❌ Not usable | ❌ Not usable | **Neither (compartment out of scope)** | Kidney biopsy, not peripheral blood PBMC |

---

## Open Items for Step 3

1. **Perez et al. (GSE174188):** Verify whether per-donor numeric SLEDAI scores
   are available in the open CELLxGENE/GEO metadata or only under dbGaP
   controlled access. This determines Task B usability.

2. **Nehar-Belaid et al. (GSE135779):** Verify the SLEDAI distribution in the
   pediatric cohort from the paper's supplementary tables. Determine whether a
   non-trivial inactive-SLE subset (SLEDAI ≤ 4) exists.

3. **Classification criteria reconciliation:** Both usable cohorts (#1 and #2)
   likely used pre-2019 criteria (1997 ACR or 2012 SLICC). This is noted here
   and will be reconciled in Step 4 (Harmonization & Labels) per the protocol.

4. **Additional cohort search:** The audit identified only **two** cohorts with
   sufficient sample sizes for primary evaluation. Additional candidates should
   be sought on CELLxGENE Discover and GEO, particularly:
   - Any new large-scale PBMC scRNA-seq lupus datasets published 2023–2026.
   - CITE-seq PBMC datasets where the RNA layer is usable (protein/ATAC dropped).
   - The Caielli et al. 2025 pediatric SLE CD4+ T cell dataset (GSE298578) —
     accession needs verification; may be too cell-type-restricted for whole-PBMC
     evaluation.

5. **Tissue-biopsy cohorts:** Arazi et al. 2019 (AMP SLE kidney) is recorded but
   flagged out of scope. No additional kidney/skin biopsy cohorts were audited;
   they remain out of primary scope per the protocol.

---

## Constraints Log

- No data was downloaded or fetched.
- No matrix, count table, or h5ad file was opened.
- No code was run.
- No cohort was selected for development or external validation.
- No ranking or recommendation was made — this is a neutral inventory.
