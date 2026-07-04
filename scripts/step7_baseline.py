import scanpy as sc
import numpy as np
import pandas as pd
import scipy.sparse as sp
import os
import json
import hashlib
from sklearn.linear_model import LogisticRegression
import joblib
import yaml

print("--- TASK 1: PSEUDOBULK AGGREGATION ---")
file_path = 'data/development/GSE174188.h5ad'
adata = sc.read_h5ad(file_path, backed='r')
obs = adata.obs
var = adata.raw.var if adata.raw is not None else adata.var

donors = obs['donor_id'].unique()
donor_to_idx = {d: i for i, d in enumerate(donors)}

num_donors = len(donors)
num_genes = adata.raw.shape[1]
pb_matrix = np.zeros((num_donors, num_genes), dtype=np.float32)

chunk_size = 50000
num_cells = adata.shape[0]

print(f"Aggregating {num_cells} cells into {num_donors} pseudobulk profiles...")
for start in range(0, num_cells, chunk_size):
    end = min(start + chunk_size, num_cells)
    
    # Read chunk from raw counts
    chunk_X = adata.raw.X[start:end]
    if sp.issparse(chunk_X):
        chunk_X = chunk_X.toarray()
    
    chunk_donors = obs['donor_id'].iloc[start:end].values
    
    # Sum counts per donor in this chunk
    for i in range(len(chunk_donors)):
        d_idx = donor_to_idx[chunk_donors[i]]
        pb_matrix[d_idx] += chunk_X[i]

# Create pseudobulk AnnData
# Aggregate metadata
donor_obs = obs.drop_duplicates('donor_id').set_index('donor_id').loc[donors]

pb_adata = sc.AnnData(X=pb_matrix, obs=donor_obs, var=var)
print(f"Pseudobulk shape: {pb_adata.shape}")
print("Donor-level disease counts:")
print(pb_adata.obs['disease'].value_counts().to_string())

print("\n--- TASK 2: FROZEN PREPROCESSING ---")
initial_genes = pb_adata.shape[1]
print(f"Initial gene count: {initial_genes}")

# Normalize pseudobulk (CPM + log1p)
sc.pp.normalize_total(pb_adata, target_sum=1e4)
sc.pp.log1p(pb_adata)

os.makedirs('artifacts/preprocessing', exist_ok=True)
genes_path = 'artifacts/preprocessing/gene_vocab.npy'
np.save(genes_path, pb_adata.var_names.values)

print(f"Preprocessing frozen to: {genes_path} (Size: {os.path.getsize(genes_path)} bytes)")

print("\n--- TASK 3: INTERNAL-EXTERNAL SPLITS ---")
donor_ids = pb_adata.obs.index.values
ancestry = pb_adata.obs['self_reported_ethnicity'].values
disease = pb_adata.obs['disease'].values

fold1_test_mask = (ancestry == 'Asian')
fold1_train_mask = ~fold1_test_mask

fold2_test_mask = (ancestry == 'European')
fold2_train_mask = ~fold2_test_mask

def check_fold(name, train_mask, test_mask):
    train_donors = set(donor_ids[train_mask])
    test_donors = set(donor_ids[test_mask])
    overlap = train_donors.intersection(test_donors)
    print(f"\n{name}:")
    print(f"  Disjointness assertion (overlap == 0): {len(overlap) == 0}")
    
    test_sle = np.sum((disease[test_mask] == 'systemic lupus erythematosus'))
    test_hc = np.sum((disease[test_mask] == 'normal'))
    print(f"  Test donors: {len(test_donors)}")
    print(f"  Test samples - SLE: {test_sle}, HC: {test_hc}")

check_fold("Fold 1 (Hold out Asian)", fold1_train_mask, fold1_test_mask)
check_fold("Fold 2 (Hold out European)", fold2_train_mask, fold2_test_mask)

print("\n--- TASK 4: TRAIN BASELINE ---")
# Train Fold 1 model
X_train = pb_adata.X[fold1_train_mask]
y_train = disease[fold1_train_mask]

# Baseline LogisticRegression outputs calibrated probabilities
clf = LogisticRegression(max_iter=1000, random_state=42)
clf.fit(X_train, y_train)

os.makedirs('artifacts/baseline_model', exist_ok=True)
model_path = 'artifacts/baseline_model/weights.pkl'
joblib.dump(clf, model_path)
model_size = os.path.getsize(model_path)
print(f"Baseline Model saved to: {model_path} (Size: {model_size} bytes)")

print("\n--- TASK 5: MANIFEST & LOGGING ---")
def sha256(fname):
    hash_sha256 = hashlib.sha256()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

manifest = {
    "model_type": "baseline_logreg",
    "pseudobulk_shape": pb_adata.shape,
    "gene_count": initial_genes,
    "per_fold_counts": {
        "Fold1_Test": {"Asian": int(fold1_test_mask.sum())},
        "Fold2_Test": {"European": int(fold2_test_mask.sum())}
    },
    "artifacts": [
        {
            "path": genes_path,
            "bytes": os.path.getsize(genes_path),
            "sha256": sha256(genes_path)
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

# Update state file
state_path = 'state/project_state.yaml'
with open(state_path, 'r') as f:
    state = yaml.safe_load(f)

state['step7_baseline'] = {
    'model_type': 'baseline_logreg',
    'counts_source': 'raw_pseudobulk',
    'pseudobulk_shape': list(pb_adata.shape),
    'dev_only': True,
    'external_touched': False,
    'probabilistic': True
}

# Remove step7_training if it exists to keep state clean (we are now doing step7_baseline)
if 'step7_training' in state:
    del state['step7_training']

with open(state_path, 'w') as f:
    yaml.dump(state, f, sort_keys=False)

print("Wrote artifacts/step7_manifest.json and updated state.")
