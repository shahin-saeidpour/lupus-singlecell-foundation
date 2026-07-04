# Stage 9C Q1 item 5 matched rerun status

Status: completed_q1_item_5_matched_rerun

Q1 item 5 completed: canonical matched rerun between Geneformer and pseudobulk baseline with identical donors, labels, folds, and seed.

Matched design:
- Task: FLARE vs managed_sle
- Modeling donors: 162
- Class counts: managed_sle=148, FLARE=14
- Folds: StratifiedKFold, 5 splits, shuffle true, random_state 42
- Seed: 42
- Identical donors, labels, folds, and seed: true

Geneformer artifact:
- file: all_embeddings.zip
- sha256: 3530908a141c172527184296ccafb496163cdb77f2b7ef3be3dcd57d9d484271
- npy payloads: 261
- per-donor embedding shape: 300 x 1152
- donor pooling: mean over axis 0 to one 1152-dimensional donor vector

Overall OOF metrics:
- Geneformer ROC-AUC: 0.9986
- Geneformer average precision: 0.9846
- Geneformer balanced accuracy @0.5: 0.9899
- Geneformer F1 FLARE @0.5: 0.9032
- Pseudobulk ROC-AUC: 0.9942
- Pseudobulk average precision: 0.9175
- Pseudobulk balanced accuracy @0.5: 0.9831
- Pseudobulk F1 FLARE @0.5: 0.8485

Ready for Q1 item 6: true

This closes only Q1 item 5. Items 6 and 7 remain not completed here.
