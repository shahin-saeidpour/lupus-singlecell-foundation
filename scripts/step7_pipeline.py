import scanpy as sc
import numpy as np
import scipy.sparse as sp
import os
import json
import hashlib
from sklearn.linear_model import SGDClassifier
import joblib

print("--- TASK 1: DATA LOADING & PREPROCESSING ---")
file_path = 'data/development/GSE174188.h5ad'

print(f"Loading full {file_path} into memory...")
try:
    adata = sc.read_h5ad(file_path)
    
    print("Extracting raw counts...")
    # Get raw.X as the new X
    raw_adata = adata.raw.to_adata()
    # Free old adata to save memory
    del adata
    
    print("Applying Step 3.2 Preprocessing...")
    # Record initial gene count
    initial_genes = raw_adata.shape[1]
    
    # Normalization
    sc.pp.normalize_total(raw_adata, target_sum=1e4)
    sc.pp.log1p(raw_adata)
    
    # HVG
    sc.pp.highly_variable_genes(raw_adata, n_top_genes=2000, flavor='seurat')
    hvg_count = raw_adata.var['highly_variable'].sum()
    
    print(f"Processed shape: {raw_adata.shape}")
    print(f"Total donors: {raw_adata.obs['donor_id'].nunique()}")
    print(f"Final gene count: {initial_genes}")
    print(f"HVG count: {hvg_count}")
    
    # Save preprocessing artifact
    os.makedirs('artifacts/preprocessing', exist_ok=True)
    prep_path = 'artifacts/preprocessing/hvg_mask.npy'
    np.save(prep_path, raw_adata.var['highly_variable'].values)
    
    print(f"Preprocessing frozen to: {prep_path} (Size: {os.path.getsize(prep_path)} bytes)")

    print("\n--- TASK 2: INTERNAL-EXTERNAL SPLITS ---")
    
    obs = raw_adata.obs
    donors = obs['donor_id'].values
    ancestry = obs['self_reported_ethnicity'].values
    disease = obs['disease'].values
    
    # Fold 1: Hold out Asian
    fold1_test_mask = (ancestry == 'Asian')
    fold1_train_mask = ~fold1_test_mask
    
    # Fold 2: Hold out European
    fold2_test_mask = (ancestry == 'European')
    fold2_train_mask = ~fold2_test_mask
    
    def check_fold(name, train_mask, test_mask):
        train_donors = set(np.unique(donors[train_mask]))
        test_donors = set(np.unique(donors[test_mask]))
        overlap = train_donors.intersection(test_donors)
        print(f"\n{name}:")
        print(f"  Disjointness assertion (overlap == 0): {len(overlap) == 0}")
        
        test_sle = np.sum((disease[test_mask] == 'systemic lupus erythematosus'))
        test_hc = np.sum((disease[test_mask] == 'normal'))
        print(f"  Test donors: {len(test_donors)}")
        print(f"  Test samples - SLE: {test_sle}, HC: {test_hc}")
        
    check_fold("Fold 1 (Hold out Asian)", fold1_train_mask, fold1_test_mask)
    check_fold("Fold 2 (Hold out European)", fold2_train_mask, fold2_test_mask)

    print("\n--- TASK 3: MODEL TRAINING ---")
    # subset to HVGs for training to save memory
    train_adata = raw_adata[:, raw_adata.var['highly_variable']]
    
    # We will fit a simple SGDClassifier on Fold 1 train to represent the bundle
    print("Fitting model on Fold 1 Training Set...")
    X_train = train_adata.X[fold1_train_mask]
    y_train = disease[fold1_train_mask]
    
    clf = SGDClassifier(loss='log_loss', max_iter=20, random_state=42)
    clf.fit(X_train, y_train)
    
    os.makedirs('artifacts/model', exist_ok=True)
    os.makedirs('artifacts/model/curves', exist_ok=True)
    
    model_path = 'artifacts/model/weights.pkl'
    joblib.dump(clf, model_path)
    model_size = os.path.getsize(model_path)
    print(f"Model saved to: {model_path} (Size: {model_size} bytes)")
    
    print("\n--- TASK 4: MANIFEST ---")
    
    def sha256(fname):
        hash_sha256 = hashlib.sha256()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
        
    manifest = {
        "processed_shape": raw_adata.shape,
        "donors": raw_adata.obs['donor_id'].nunique(),
        "hvg_count": int(hvg_count),
        "artifacts": [
            {
                "path": prep_path,
                "bytes": os.path.getsize(prep_path),
                "sha256": sha256(prep_path)
            },
            {
                "path": model_path,
                "bytes": os.path.getsize(model_path),
                "sha256": sha256(model_path)
            }
        ]
    }
    
    with open('artifacts/step7_manifest.json', 'w') as f:
        json.dump(manifest, f, indent=2)
    print("Wrote artifacts/step7_manifest.json")

except Exception as e:
    import traceback
    print(f"CRITICAL ERROR: {e}")
    traceback.print_exc()
