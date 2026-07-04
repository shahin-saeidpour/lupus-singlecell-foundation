import scanpy as sc
import numpy as np
import scipy.sparse as sp
import os
import pickle
from sklearn.linear_model import LogisticRegression

print("Aggregating pseudobulk for final dev model...")
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

for start in range(0, num_cells, chunk_size):
    end = min(start + chunk_size, num_cells)
    chunk_X = adata.raw.X[start:end]
    if sp.issparse(chunk_X):
        chunk_X = chunk_X.toarray()
    chunk_donors = obs['donor_id'].iloc[start:end].values
    for i in range(len(chunk_donors)):
        d_idx = donor_to_idx[chunk_donors[i]]
        pb_matrix[d_idx] += chunk_X[i]

donor_obs = obs.drop_duplicates('donor_id').set_index('donor_id').loc[donors]
pb_adata = sc.AnnData(X=pb_matrix, obs=donor_obs, var=var)

# Save the gene vocab as the frozen preprocessing state
os.makedirs('artifacts/preprocessing', exist_ok=True)
np.save('artifacts/preprocessing/gene_vocab.npy', pb_adata.var_names.values)
print(f"Saved frozen preprocessing gene vocabulary ({len(pb_adata.var_names)} genes).")

# Apply identical frozen preprocessing from step 7/8
sc.pp.normalize_total(pb_adata, target_sum=1e4)
sc.pp.log1p(pb_adata)

disease = pb_adata.obs['disease'].values
y_train = (disease == 'systemic lupus erythematosus').astype(int)
X_train = pb_adata.X

# Fit final model on all 261 donors
clf = LogisticRegression(max_iter=1000, C=1.0, random_state=42)
clf.fit(X_train, y_train)

# Save
os.makedirs('artifacts/baseline_model', exist_ok=True)
save_path = 'artifacts/baseline_model/final_dev_model.pkl'

with open(save_path, 'wb') as f:
    pickle.dump(clf, f)
    f.flush()
    os.fsync(f.fileno())

size = os.path.getsize(save_path)

# Re-load check
with open(save_path, 'rb') as f:
    loaded = pickle.load(f)

print(f"\nFinal Dev Model (All {num_donors} Donors):")
print(f"  Path: {save_path}")
print(f"  Size: {size} bytes")
print(f"  Type: {type(loaded)}")
print(f"  Has predict_proba: {hasattr(loaded, 'predict_proba')}")
print(f"  Coef shape: {getattr(loaded, 'coef_', np.array([])).shape}")
print(f"  Classes: {getattr(loaded, 'classes_', '?')}")

import pandas as pd
np.save('artifacts/baseline_model/dev_X.npy', X_train)
np.save('artifacts/baseline_model/dev_y.npy', y_train)
pd.DataFrame({'donor_id': pb_adata.obs.index}).to_csv('artifacts/baseline_model/dev_donors.csv', index=False)

print('\n--- DATA EXPORT ---')
print('Mapping: 1 = systemic lupus erythematosus, 0 = normal')
print(f'dev_X.npy: artifacts/baseline_model/dev_X.npy, rows: {X_train.shape[0]}')
print(f'dev_y.npy: artifacts/baseline_model/dev_y.npy, rows: {y_train.shape[0]}')
print(f'dev_donors.csv: artifacts/baseline_model/dev_donors.csv, rows: {len(pb_adata.obs.index)}')
