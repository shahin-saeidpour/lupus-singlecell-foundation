# Dataset Audit — Candidate Cohorts for External Validation

> **Status:** Inventory complete; cohort assignment made (Step 3). No data has
> been downloaded. This audit feeds into Gate 1.
>
> **Date:** 2026-07-04 (created); 2026-07-04 (Step 3 update)
> **Phase:** Pre-acquisition

---

## Methodology

Each candidate cohort was researched using the following authoritative sources:

1. The primary paper's Data Availability statement.
2. The GEO record landing page (ncbi.nlm.nih.gov/geo).
3. The CZ CELLxGENE Discover portal (cellxgene.cziscience.com).
4. The dbGaP / ImmPort study record (where applicable).
5. Zenodo and GitHub repositories (for SLECA atlas).

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
| 4 | GSE162577 — "Single cell RNA sequencing reveals cellular heterogeneity of PBMC of SLE patients" | GSE162577 (GEO) — **ACCESSION VERIFIED**. GSM entries: GSM4954811 (SLE), GSM4954812 (SLE), GSM4954813 (HC). | GEO | 10x Chromium **3'**, droplet-based (GPL24676 = Illumina NovaSeq + 10x) | PBMC / peripheral blood — **in scope** |
| 5 | GSE142016 / Mistry et al. 2019 — "Transcriptomic, epigenetic and functional analyses implicate neutrophil diversity in the pathogenesis of SLE" (scRNA-seq sub-series of GSE139360) | GSE142016 (GEO) — **ACCESSION VERIFIED**. GSM entries: GSM4217718 (scRNA_SLE1_PBMC), GSM4217719 (scRNA_SLE2_PBMC), GSM4217720 (scRNA_SLE3_PBMC). **All 3 samples are SLE PBMC; 0 HC in scRNA-seq sub-series.** | GEO | 10x Chromium, droplet-based; platform GPL24676 (Illumina NovaSeq + 10x). Exact 3'/5' chemistry UNKNOWN — check paper methods. | PBMC (labeled "scRNA_SLEn_PBMC") — **in scope**. Note: the broader super-series GSE139360 also contains LDG and neutrophil bulk/ATAC data, but the scRNA-seq sub-series GSE142016 contains only PBMC. |
| 6 | Arazi et al. 2019, *Nature Immunology* — AMP SLE Phase I kidney biopsies | ImmPort SDY997; dbGaP phs001457 — **ACCESSION VERIFIED (ImmPort)**; no standard GEO accession | ImmPort, dbGaP | 10x Chromium, droplet-based; UNKNOWN — check paper for exact 3'/5' chemistry | **Kidney biopsy** — **OUT OF SCOPE** for primary evaluation (tissue compartment) |
| 7 | **SLECA** — Duan et al. 2026, bioRxiv preprint. "SLECA: a single-cell atlas of systemic lupus erythematosus enabling rare cell discovery using graph transformer." Integrates 8 source studies, 366 samples. | Zenodo DOI 10.5281/zenodo.17698085; GitHub Snnrriet/SLECA. **NO GEO super-series accession for the integrated atlas.** Source studies: GSE135779 (Data-1), GSE142016 (Data-2), GSE179633 (Data-3, **skin**), GSE162577 (Data-4), GSE186476 (Data-5, **skin**), GSE174188 (Data-6), plus 2 additional studies (accessions UNKNOWN — check preprint supplementary). | Zenodo (restricted), GitHub (code only) | Mixed — inherits assays from 8 source studies. Includes 10x 3' droplet PBMC and skin biopsy scRNA-seq. | **Mixed: PBMC + skin biopsy.** At least 2 of 8 source studies (GSE179633, GSE186476) are skin tissue, OUT OF SCOPE for primary evaluation. PBMC subset must be filtered by source-study provenance. |

### Panel B — Sample Counts & Labels

| # | n samples (total) | n SLE | n healthy control | n other-autoimmune control | Diagnosis label present? | Activity label present? (which index) | Inactive-SLE subset present & sized? |
|---|---|---|---|---|---|---|---|
| 1 | ~264 unique donors (per paper: 162 SLE + ~99 HC; some with longitudinal samples; project status records 261 donors) | 162 SLE (of which ~19 flare, ~10 post-treatment, remainder managed/inactive) | ~99 | 0 reported | Yes — SLE vs. healthy annotated in metadata (donor_id patterns and disease status field) | SLEDAI and SELENA-SLEDAI Flare Index referenced in paper; **however, per-donor SLEDAI scores may be under controlled access in dbGaP phs002812** — UNKNOWN whether numeric SLEDAI is in the open CELLxGENE/GEO metadata. Flare/managed status is annotated openly. | Yes — the managed SLE group (~133 donors per project status, SLEDAI ≤ 4 expected for many) constitutes a substantial inactive-SLE subset. **Exact SLEDAI distribution UNKNOWN — verify from dbGaP or supplementary tables.** |
| 2 | ~58 donors total (33 pediatric SLE + 11 pediatric HC + 8 adult SLE + 6 adult HC) | 41 SLE (33 pediatric + 8 adult) | 17 (11 pediatric + 6 adult) | 0 reported | Yes — SLE vs. healthy annotated | Yes — SLEDAI scores recorded for pediatric SLE patients; disease activity described as varying degrees. | UNKNOWN — check paper supplementary tables for SLEDAI distribution. Pediatric SLE cohorts tend to have higher baseline activity; **inactive subset (SLEDAI ≤ 4) may be thin**. |
| 3 | ~6 total (3 SLE + 3 HC per GEO record) | 3 | 3 | 0 | Yes (SLE vs. HC labeled) | UNKNOWN — unlikely; this is a B-cell biology study, not a disease-activity study | UNKNOWN — with only 3 SLE patients, subset analysis is not meaningful |
| 4 | **3 GSM entries total: 2 SLE + 1 HC** (GSM4954811 = SLE, GSM4954812 = SLE, GSM4954813 = HC). **Step 3 correction:** resolved from "UNKNOWN" to confirmed 2 SLE + 1 HC. | 2 | 1 | 0 reported | Yes — SLE vs. HC labeled in GSM titles | UNKNOWN — no disease-activity index mentioned in available metadata | Not applicable — only 2 SLE patients, no meaningful inactive subset possible |
| 5 | **3 scRNA-seq samples, all SLE PBMC, 0 HC** (GSM4217718 = scRNA_SLE1_PBMC, GSM4217719 = scRNA_SLE2_PBMC, GSM4217720 = scRNA_SLE3_PBMC). **Step 3 correction:** resolved from "UNKNOWN" to confirmed 3 SLE + 0 HC. Note: a 2024 *Autoimmunity* paper (doi:10.1080/08916934.2023.2281228) reportedly analyzed 10 adult SLE + 7 HC by combining GSE142016 with GSE135779 data; the 10 aSLE + 7 HC counts represent pooled cross-study totals, not GSE142016 alone. | 3 (SLE only) | 0 | 0 reported | **Diagnosis label: limited** — all 3 are SLE PBMC, no HC controls in this sub-series for SLE-vs-HC evaluation | UNKNOWN — paper focuses on neutrophil diversity, not activity scoring | Not applicable — no HC for diagnosis; activity labels absent |
| 6 | 34 total (24 LN kidney biopsies + 10 living-donor controls) | 24 (lupus nephritis) | 10 (living kidney donors) | 0 | Yes — LN vs. healthy control | UNKNOWN — check if ISN/RPS class or activity index is recorded; this is kidney tissue, not PBMC | Not applicable — kidney biopsy, out of scope for PBMC-based evaluation |
| 7 | **366 samples** across 8 source studies (per preprint). Exact per-condition breakdown UNKNOWN — check preprint Table 1 / supplementary. Includes PBMC and skin samples. | UNKNOWN — check preprint metadata tables | UNKNOWN — check preprint metadata tables | UNKNOWN | UNKNOWN — preprint states per-sample metadata includes disease status, but specific label schema not verified from h5ad obs columns. **Zenodo files are RESTRICTED; cannot verify metadata fields without access.** | UNKNOWN — preprint references disease activity but whether per-sample SLEDAI or equivalent index is standardized across all 8 source studies is not verifiable from restricted Zenodo data. | UNKNOWN — cannot determine inactive-SLE subset size without accessing restricted files. |

### Panel C — Criteria, Demographics, Access & Usability

| # | Case criteria used | Ancestry / age | Access tier (processed expression + labels) | Download format | Source link | **Usability flag** |
|---|---|---|---|---|---|---|
| 1 | **1997 ACR criteria** (CLUES cohort standard). Not 2019 EULAR/ACR. Reconciliation required per protocol Step 4. | Adult; multi-ancestry (cohort includes diverse self-reported ancestry) | Processed counts + cell-type annotations: **open** via CELLxGENE (h5ad) and GEO. Raw sequences + dense genotype + sensitive clinical metadata (including SLEDAI scores): **controlled** via dbGaP phs002812. | h5ad (CELLxGENE), supplementary files (GEO) | [GEO GSE174188](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE174188); [CELLxGENE](https://cellxgene.cziscience.com/) | **Diagnosis: usable** (SLE vs. HC labels present). **Activity: questionable** — flare/managed annotation available but numeric SLEDAI may require dbGaP access; inactive-SLE subset size needs verification. |
| 2 | UNKNOWN — check paper methods section for exact criteria cited. Study published 2020; likely 1997 ACR or 2012 SLICC (pre-dates 2019 EULAR/ACR widespread adoption). Reconciliation required per protocol Step 4. | **Pediatric** (primary cohort: children) + small **adult** validation subset | Processed counts (CellRanger outputs): **open** via GEO GSE135779. Raw FASTQ: **controlled** via dbGaP phs002048. | mtx / tsv.gz (GEO — CellRanger outputs) | [GEO GSE135779](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE135779); [GitHub](https://github.com/dnehar/SingleCells_SLE_paper) | **Diagnosis: usable** (SLE vs. HC labels present; note pediatric population). **Activity: questionable** — SLEDAI recorded but inactive-SLE subset size unknown and may be thin in pediatric cohort with predominantly active patients. |
| 3 | UNKNOWN — check paper methods | UNKNOWN — check paper for age/ancestry | **Open** via GEO (supplementary tar.gz files) | tar.gz (GEO supplementary) | [GEO GSE193867](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE193867) | **Neither** — too few samples (n=6), not a lupus disease study, sorted B-cell fractions rather than whole PBMC. |
| 4 | UNKNOWN — check paper methods | UNKNOWN — check paper | **Open** via GEO | UNKNOWN — check GEO supplementary files | [GEO GSE162577](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE162577) | **Neither** — too few samples (3 total: 2 SLE + 1 HC) for meaningful evaluation on either task. |
| 5 | UNKNOWN — check paper methods (Mistry et al. 2019 / Kaplan lab) | Adult; UNKNOWN ancestry | **Open** via GEO | UNKNOWN — check GEO supplementary files | [GEO GSE142016](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE142016) | **Neither** — 3 SLE-only PBMC samples with 0 HC. Cannot evaluate diagnosis (no controls) or activity (no labels, no inactive subset). |
| 6 | UNKNOWN — check paper methods (AMP consortium criteria) | Adult; UNKNOWN ancestry distribution | **Controlled** via ImmPort SDY997 (requires account) and dbGaP phs001457. | UNKNOWN — check ImmPort for available formats | [ImmPort SDY997](https://www.immport.org/); [dbGaP phs001457](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs001457) | **Neither (compartment out of scope)** — kidney biopsy tissue, not peripheral blood PBMC. |
| 7 | UNKNOWN — inherits from 8 source studies; standardization approach described in preprint methods but not independently verified | UNKNOWN — mixed across source studies; preprint states metadata includes age/sex but details not verified | **RESTRICTED.** Zenodo record 17698085 states: "The record is publicly accessible, but files are restricted." License: CC BY 4.0 (for metadata/description). **Actual h5ad files require access request/approval — NOT openly downloadable.** GitHub repo (Snnrriet/SLECA) contains code + example data only, not the full atlas. | h5ad (Zenodo, restricted) | [Zenodo 17698085](https://zenodo.org/records/17698085); [GitHub](https://github.com/Snnrriet/SLECA); [bioRxiv preprint](https://www.biorxiv.org/content/10.1101/2026.02.11.637246v1) | **NOT OPENLY USABLE.** Zenodo files are restricted. Additionally: (a) PREPRINT — integration not peer-reviewed; (b) mixes PBMC + skin tissue; (c) contains GSE174188 and GSE135779 → overlap/leakage risk with primary cohorts. Even if access were granted, we would rely on the underlying primary data rather than the atlas's derived annotations. |

---

## Summary of Usability Flags

| # | Cohort | Diagnosis (Task A) | Activity (Task B) | Overall | Key limitation |
|---|---|---|---|---|---|
| 1 | Perez et al. 2022 (GSE174188) | ✅ Usable | ⚠️ Questionable | **Diagnosis usable; activity uses open flare/managed labels** | Case criteria = 1997 ACR not 2019 EULAR/ACR; numeric SLEDAI may require dbGaP |
| 2 | Nehar-Belaid et al. 2020 (GSE135779) | ✅ Usable | ⚠️ Questionable | **Diagnosis usable; activity needs inactive-subset sizing** | Pediatric population; inactive-SLE subset may be thin; case criteria unknown |
| 3 | Spencer et al. 2022 (GSE193867) | ❌ Not usable | ❌ Not usable | **Neither** | Not a lupus study; only 6 samples; sorted B cells not whole PBMC |
| 4 | GSE162577 | ❌ Not usable | ❌ Not usable | **Neither** | Too few samples (2 SLE + 1 HC) for any meaningful evaluation |
| 5 | GSE142016 | ❌ Not usable | ❌ Not usable | **Neither** | 3 SLE-only PBMC samples, 0 HC — cannot evaluate diagnosis or activity |
| 6 | Arazi et al. 2019 (AMP SLE, SDY997) | ❌ Not usable | ❌ Not usable | **Neither (compartment out of scope)** | Kidney biopsy, not peripheral blood PBMC |
| 7 | SLECA atlas (Duan et al. 2026, preprint) | ❌ Not openly usable | ❌ Not openly usable | **Not usable (restricted access)** | Zenodo files restricted; preprint (not peer-reviewed); mixes PBMC + skin; overlaps GSE174188 + GSE135779 |

---

## SLECA Atlas — Detailed Verification Record (Step 3, Phase 1a)

### Open-access status
**NOT OPENLY DOWNLOADABLE.** Zenodo record 17698085 explicitly states: "The record
is publicly accessible, but files are restricted." The h5ad files require login
and presumably an access request/approval. The GitHub repository
(Snnrriet/SLECA) contains only SarsGT model code and small example data tarballs,
not the full 366-sample atlas.

### License
CC BY 4.0 listed on Zenodo (applies to metadata/description). Whether this
license applies to the restricted h5ad files themselves is unclear — the files
cannot be accessed to verify.

### Source studies integrated (verified list, partial)
Per bioRxiv preprint and search results:
- Data-1: **GSE135779** (Nehar-Belaid et al. 2020) — pediatric SLE PBMC ✅
- Data-2: **GSE142016** (Mistry et al. 2019) — SLE PBMC ✅
- Data-3: **GSE179633** — lupus **skin biopsies** (DLE/SLE epidermis+dermis) ⚠️ OUT OF SCOPE
- Data-4: **GSE162577** — SLE PBMC ✅
- Data-5: **GSE186476** — lupus **skin biopsies** (CLE lesional/non-lesional) ⚠️ OUT OF SCOPE
- Data-6: **GSE174188** (Perez et al. 2022) — SLE PBMC ✅
- Data-7: **GSE250024** — SLE PBMC, but only 3 patients total ❌ TOO SMALL
- Data-8: **GSE158055** (Ren et al. 2021) — COVID-19 dataset with healthy controls; used in SLECA for controls only, 0 SLE cases ❌ NO CASES

**Candidate Second External Assessment:** Neither of the remaining source studies qualifies as a candidate second external cohort. Both are either too small (n=3) or lack disease cases entirely (healthy controls only). Therefore, no new candidate is added to the audit table, and the **single-external design (GSE135779 only) stands.**

**Critical overlap:** SLECA integrates BOTH GSE174188 (our development anchor) AND
GSE135779 (our primary external candidate). Any use of SLECA for validation would
require strict source-study-level provenance mapping to prevent leakage.

### Per-sample metadata scope
Cannot be verified — files are restricted on Zenodo. The preprint abstract states
"standardized clinical and biological metadata" including age, sex, tissue origin.
Whether per-sample diagnosis labels (SLE/HC), disease-activity indices (SLEDAI),
assay chemistry, and source-study IDs are present as obs columns in the h5ad files
is **UNKNOWN — requires file access to verify**.

### PBMC vs. tissue
**Mixed.** At least 2 of 8 source studies are skin biopsy (GSE179633, GSE186476).
The remaining 4–6 are PBMC. The atlas would require filtering by tissue/source
study before use.

### Preprint caveat
**SLECA is a PREPRINT** (bioRxiv, Feb 2026, not peer-reviewed). The integration
methodology, cell-type annotations, and graph-transformer outputs are the authors'
work and have not been independently validated. For our purposes, the underlying
primary data (from the source GEO accessions) is what we would rely on — not the
atlas's derived embeddings, annotations, or conclusions.

---

## Step 3 Corrections — GSE162577 (#4) and GSE142016 (#5)

### GSE162577 (Row #4) — CORRECTED
**Previous:** "UNKNOWN — conflicting reports (some sources say 2 SLE, others 1 SLE + 1 HC)"
**Corrected:** 3 GSM entries confirmed:
- GSM4954811 = SLE patient
- GSM4954812 = SLE patient
- GSM4954813 = Healthy control (HC)
**Total: 2 SLE + 1 HC = 3 samples.** Still far too small for meaningful evaluation.
Usability remains "neither."

### GSE142016 (Row #5) — CORRECTED
**Previous:** "~3 scRNA-seq samples; UNKNOWN which are SLE vs. HC vs. neutrophil"
**Corrected:** 3 GSM entries confirmed, **all SLE PBMC, 0 HC:**
- GSM4217718 = scRNA_SLE1_PBMC
- GSM4217719 = scRNA_SLE2_PBMC
- GSM4217720 = scRNA_SLE3_PBMC

The broader super-series GSE139360 contains additional bulk RNA-seq, ATAC-seq, and
functional assay data, but the scRNA-seq sub-series (GSE142016) contains only
these 3 SLE samples.

**Note on the 2024 *Autoimmunity* paper** (doi:10.1080/08916934.2023.2281228): This
paper reports analyzing 10 adult SLE + 7 HC by combining GSE142016 with GSE135779.
The 10 aSLE / 7 HC counts are **pooled cross-study totals** (3 from GSE142016 +
remaining from GSE135779), not GSE142016 alone. GSE142016 contributes only 3
SLE-only samples; the HC samples came from GSE135779.

Usability remains "neither" — no HC controls, too small for standalone evaluation.

---

## Constraints Log

- No data was downloaded or fetched.
- No matrix, count table, or h5ad file was opened.
- No code was run.
- Zenodo restricted files were NOT accessed — metadata read from public record page only.
- Cohort assignment (Step 3) has been made based on the findings above.
