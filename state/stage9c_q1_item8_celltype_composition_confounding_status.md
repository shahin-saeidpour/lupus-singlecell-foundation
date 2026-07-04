# Stage 9C Q1 item 8 cell-type composition confounding status

Status: completed_q1_item_8_cell_type_composition_confounding_control

Q1 item 8 completed: cell-type composition confounding control.

Scope:
- Task: FLARE vs managed_sle
- Donors: 162
- FLARE: 14
- managed_sle: 148
- Cell-type source: metadata column `cov` from `perez_sle_sobj_meta.csv.zip`
- Same donors, labels, folds and seed as item 5: true

Key results:
- Composition-only ROC-AUC: 0.6226
- Composition-only AP: 0.1674
- Geneformer original ROC-AUC: 0.9986
- Geneformer plus composition ROC-AUC: 0.9913
- Pseudobulk original ROC-AUC: 0.9942
- Pseudobulk plus composition ROC-AUC: 0.9846

Interpretation flag:
- Cell-type composition confounding risk: limited_by_this_control

GitHub output path:
- artifacts/stage9c/item8_celltype_composition_confounding/

Ready for Q1 item 9: true

This closes only Q1 item 8. Item 9 is not completed here.
