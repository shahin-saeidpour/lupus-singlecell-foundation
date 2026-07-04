# Stage 9C Q1 item 9 batch/source/donor confounding status

Status: completed_q1_item_9_batch_source_donor_confounding_control

Q1 item 9 completed: batch/source/donor confounding control.

Scope:
- Task: FLARE vs managed_sle
- Donors: 162
- FLARE: 14
- managed_sle: 148
- Batch column: batch_cov
- Source/cohort column: Processing_Cohort
- Donor metadata columns: Age, Sex, pop_cov, n_cells
- Target leakage columns excluded: Status, SLE_status
- Same donors, labels, folds and seed as item 5: true

Key results:
- Batch/source-only ROC-AUC: 0.9961
- Batch/source-only AP: 0.9482
- Donor-metadata-only ROC-AUC: 0.8948
- Batch/source + donor metadata ROC-AUC: 0.9990
- Geneformer original ROC-AUC: 0.9986
- Geneformer score + batch/source/donor ROC-AUC: 0.9990
- Pseudobulk original ROC-AUC: 0.9942
- Pseudobulk score + batch/source/donor ROC-AUC: 0.9981

Interpretation flag:
- Batch/source/donor confounding risk: high_batch_source_confounding_risk

GitHub output path:
- artifacts/stage9c/item9_batch_source_donor_confounding/

Ready for Q1 item 10: true

This closes only Q1 item 9. Item 10 is not completed here.
