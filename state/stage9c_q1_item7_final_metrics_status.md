# Stage 9C Q1 item 7 final metrics status

Status: completed_q1_item_7_final_metrics_ci_and_fold_stability

Q1 item 7 completed: final metrics with confidence intervals and fold-level stability.

Scope:
- Task: FLARE vs managed_sle
- Donors: 162
- FLARE: 14
- managed_sle: 148
- Confidence intervals: stratified donor bootstrap, n=1000, seed=42
- Paired deltas: paired stratified donor bootstrap, n=1000, seed=42

Key OOF metrics:
- Geneformer ROC-AUC: 0.9986
- Geneformer average precision: 0.9846
- Geneformer balanced accuracy @0.5: 0.9899
- Geneformer F1 FLARE @0.5: 0.9032
- Pseudobulk ROC-AUC: 0.9942
- Pseudobulk average precision: 0.9175
- Pseudobulk balanced accuracy @0.5: 0.9831
- Pseudobulk F1 FLARE @0.5: 0.8485

GitHub output path:
- artifacts/stage9c/item7_final_metrics_ci/

Ready for Q1 item 8: true

This closes only Q1 item 7. Items 8 and 9 are not completed here.
