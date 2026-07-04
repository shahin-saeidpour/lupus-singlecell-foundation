# Stage 9C Q1 item 4 main baseline status

Status: completed_q1_item_4_main_baseline

Completed item: Q1 item 4, donor-level pseudobulk plus fold-local PCA plus balanced logistic regression.

Analysis population:
- included labels: FLARE and managed_sle
- excluded labels: healthy and ICC_control
- modeling donors: 162
- class counts: managed_sle=148, FLARE=14

Input checks:
- labels.csv: PASS
- donor_inventory.csv: PASS
- preprocessing_config.json: PASS
- file_hashes.csv: PASS
- pseudobulk matrix shape: 261 rows x 25717 columns

Output path:
- artifacts/stage9c/item4_main_baseline/

Registered files:
- item4_input_checks.json
- item4_main_baseline_fold_metrics.csv
- item4_main_baseline_run_config.json
- item4_main_baseline_result_summary.md
- item4_output_manifest.csv

Metrics:
- ROC-AUC: 0.9942
- Average precision: 0.9175
- Accuracy at threshold 0.5: 0.9691
- Balanced accuracy at threshold 0.5: 0.9831
- Precision FLARE at threshold 0.5: 0.7368
- Recall FLARE at threshold 0.5: 1.0000
- F1 FLARE at threshold 0.5: 0.8485

Confusion matrix at threshold 0.5:
- TN=143
- FP=5
- FN=0
- TP=14

Ready for Q1 item 5: true

This closes only Q1 item 4. Items 5, 6, and 7 remain not completed here.
