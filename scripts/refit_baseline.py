import scanpy as sc
import numpy as np
import pandas as pd
import scipy.sparse as sp
import os
import pickle
from sklearn.linear_model import LogisticRegression

print("Re-aggregating pseudobulk for proper model fitting...")
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

# Preprocess
sc.pp.normalize_total(pb_adata, target_sum=1e4)
sc.pp.log1p(pb_adata)

# Splits
donor_ids = pb_adata.obs.index.values
ancestry = pb_adata.obs['self_reported_ethnicity'].values
disease = pb_adata.obs['disease'].values

fold1_train_mask = ~(ancestry == 'Asian')
fold2_train_mask = ~(ancestry == 'European')

os.makedirs('artifacts/baseline_model', exist_ok=True)

def train_and_save(fold_name, train_mask, save_name):
    X_train = pb_adata.X[train_mask]
    y_train = disease[train_mask]
    
    clf = LogisticRegression(max_iter=1000, C=1.0, random_state=42)
    clf.fit(X_train, y_train)
    
    save_path = f'artifacts/baseline_model/{save_name}.pkl'
    with open(save_path, 'wb') as f:
        pickle.dump(clf, f)
        f.flush()
        os.fsync(f.fileno())
        
    size = os.path.getsize(save_path)
    
    # Re-load check
    with open(save_path, 'rb') as f:
        loaded = pickle.load(f)
        
    print(f"\n{fold_name} Model:")
    print(f"  Path: {save_path}")
    print(f"  Size: {size} bytes")
    print(f"  Type: {type(loaded)}")
    print(f"  Has predict_proba: {hasattr(loaded, 'predict_proba')}")
    print(f"  Coef shape: {getattr(loaded, 'coef_', np.array([])).shape}")
    print(f"  Classes: {getattr(loaded, 'classes_', '?')}")

train_and_save("Fold 1 (Asian Held Out)", fold1_train_mask, "fold1_asia_heldout")
train_and_save("Fold 2 (European Held Out)", fold2_train_mask, "fold2_europe_heldout")
