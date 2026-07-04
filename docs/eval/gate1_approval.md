# Human Gate 1: Approval Record

**Date:** 2026-07-04
**Phase:** Pre-acquisition

## Decision
**APPROVED:** Acquisition of the DEVELOPMENT dataset (GSE174188, Perez et al.) is authorized to proceed.

**QUARANTINE ENFORCED:** The EXTERNAL cohort (GSE135779, Nehar-Belaid et al.) remains strictly quarantined. No data from the external cohort may be downloaded, opened, or processed until the development phase is complete, the model and pipeline are fully frozen, and Human Gate 2 (Post-Freeze) is passed (Protocol Step 9).

## Design-Complete Confirmation
- Sections 1–4 of the `external_validation_protocol.md` are locked and pre-registered.
- The evaluation metric list is strictly fixed.
- The single-use commitment for the external cohort is binding. 

## Justification for Single External Cohort
The Step 2–3b dataset audit established definitively that no second large, open-access PBMC SLE scRNA-seq cohort exists. GSE174188 (Perez) and GSE135779 (Nehar-Belaid) are the only two qualified cohorts. The SLECA atlas files are restricted access, and all other candidates audited are either out of compartment (e.g., skin/kidney biopsies), only contain healthy controls (GSE158055), or are too small to be meaningful (n ≤ 3). Therefore, the single-external-cohort design is the only viable option under open-science constraints.

## Known Limitations Accepted at Approval
The following limitations are explicitly accepted prior to development:
1. **One Small Pediatric External Cohort:** The external cohort (GSE135779) is small and predominantly pediatric, presenting a major population and age shift compared to the adult development cohort.
2. **Platform Constrained (3' → 3'):** Both development and external cohorts utilize 10x Genomics 3' single-cell RNA sequencing. The external validation demonstrates population and site shifts but does not evaluate cross-chemistry generalization (e.g., 3' to 5' or 10x to Parse).
3. **Sub-split Non-degeneracy Pending Verification:** The primary internal-external validation backbone (leave-one-ancestry-out within Perez) requires post-download verification to guarantee non-degeneracy (sufficient case and control counts per ancestry group).
4. **Task B is Proxy-Labeled and Internal-Only:** Disease activity prediction is scoped as a secondary/exploratory task evaluated exclusively on internal data using an openly available flare/managed proxy, rather than a strict numeric SLEDAI cutoff.
