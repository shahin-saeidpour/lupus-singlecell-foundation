import scanpy as sc
import numpy as np
import pandas as pd
import scipy.sparse as sp
import os
import json
import hashlib
import pickle
from sklearn.metrics import roc_auc_score, average_precision_score, brier_score_loss, accuracy_score
from sklearn.calibration import calibration_curve

print("--- TASK 1: GENERATE HELD-OUT PREDICTIONS ---")
# Quickly re-aggregate pseudobulk since it wasn't saved
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
true_labels = (disease == 'systemic lupus erythematosus').astype(int)

fold1_test_mask = (ancestry == 'Asian')
fold2_test_mask = (ancestry == 'European')

os.makedirs('artifacts/step8_metrics', exist_ok=True)

def predict_fold(model_path, test_mask, save_name):
    with open(model_path, 'rb') as f:
        clf = pickle.load(f)
    
    X_test = pb_adata.X[test_mask]
    y_test = true_labels[test_mask]
    donors_test = donor_ids[test_mask]
    ancestry_test = ancestry[test_mask]
    
    # Check classes
    sle_idx = list(clf.classes_).index('systemic lupus erythematosus')
    pred_probas = clf.predict_proba(X_test)[:, sle_idx]
    
    df = pd.DataFrame({
        'donor_id': donors_test,
        'ancestry': ancestry_test,
        'true_label': y_test,
        'pred_proba_SLE': pred_probas
    })
    save_path = f'artifacts/step8_metrics/{save_name}.csv'
    df.to_csv(save_path, index=False)
    
    size = os.path.getsize(save_path)
    print(f"{save_name}: saved to {save_path}, row count: {len(df)}, size: {size} bytes")
    return df

df1 = predict_fold('artifacts/baseline_model/fold1_asia_heldout.pkl', fold1_test_mask, 'fold1_predictions')
df2 = predict_fold('artifacts/baseline_model/fold2_europe_heldout.pkl', fold2_test_mask, 'fold2_predictions')

df_pooled = pd.concat([df1, df2]).reset_index(drop=True)

print("\n--- TASK 2: DISCRIMINATION METRICS ---")
def calc_metrics(df, name):
    y_true = df['true_label'].values
    y_prob = df['pred_proba_SLE'].values
    
    auc = roc_auc_score(y_true, y_prob)
    auprc = average_precision_score(y_true, y_prob)
    n = len(y_true)
    n_pos = y_true.sum()
    n_neg = n - n_pos
    
    print(f"{name}:")
    print(f"  n = {n} (SLE: {n_pos}, HC: {n_neg})")
    print(f"  AUROC: {auc:.4f}")
    print(f"  AUPRC: {auprc:.4f}")
    return auc, auprc

auc1, auprc1 = calc_metrics(df1, "Fold 1 (Asian Held Out)")
auc2, auprc2 = calc_metrics(df2, "Fold 2 (European Held Out)")
auc_pool, auprc_pool = calc_metrics(df_pooled, "Pooled Out-Of-Fold")

print("\n--- TASK 3: CALIBRATION METRICS ---")
def calc_ece(y_true, y_prob, n_bins=10):
    prob_true, prob_pred = calibration_curve(y_true, y_prob, n_bins=n_bins)
    # Reconstruct ECE: we need bin sizes
    bins = np.linspace(0., 1., n_bins + 1)
    binids = np.digitize(y_prob, bins) - 1
    ece = 0.0
    for i in range(n_bins):
        bin_idx = binids == i
        if bin_idx.sum() > 0:
            acc = y_true[bin_idx].mean()
            conf = y_prob[bin_idx].mean()
            ece += (bin_idx.sum() / len(y_true)) * np.abs(acc - conf)
    return ece

def calc_calib(df, name):
    y_true = df['true_label'].values
    y_prob = df['pred_proba_SLE'].values
    ece = calc_ece(y_true, y_prob)
    bs = brier_score_loss(y_true, y_prob)
    print(f"{name}:")
    print(f"  ECE: {ece:.4f}")
    print(f"  Brier Score: {bs:.4f}")
    return ece, bs

ece1, bs1 = calc_calib(df1, "Fold 1 (Asian Held Out)")
ece2, bs2 = calc_calib(df2, "Fold 2 (European Held Out)")
ece_pool, bs_pool = calc_calib(df_pooled, "Pooled Out-Of-Fold")

print("\n--- TASK 4: SELECTIVE PREDICTION (RISK-COVERAGE) ---")
y_true = df_pooled['true_label'].values
y_prob = df_pooled['pred_proba_SLE'].values
# Confidence is distance from 0.5
confidence = np.maximum(y_prob, 1 - y_prob)
sort_idx = np.argsort(-confidence)
y_true_sorted = y_true[sort_idx]
y_prob_sorted = y_prob[sort_idx]
y_pred_sorted = (y_prob_sorted >= 0.5).astype(int)

print("Coverage | Accuracy | AUROC")
coverages = [1.0, 0.9, 0.75, 0.5]
for cov in coverages:
    n_samples = max(1, int(cov * len(y_true)))
    y_t = y_true_sorted[:n_samples]
    y_p = y_prob_sorted[:n_samples]
    y_pred = y_pred_sorted[:n_samples]
    
    acc = accuracy_score(y_t, y_pred)
    try:
        auc = roc_auc_score(y_t, y_p) if len(np.unique(y_t)) > 1 else np.nan
    except:
        auc = np.nan
    print(f"{cov*100:>8.0f}% | {acc:.4f}   | {auc:.4f}")

print("\n--- TASK 5: BOOTSTRAP CIs ---")
np.random.seed(42)
n_boot = 1000
aucs, auprcs, eces = [], [], []

n_samples = len(y_true)
for _ in range(n_boot):
    idx = np.random.randint(0, n_samples, n_samples)
    yt = y_true[idx]
    yp = y_prob[idx]
    if len(np.unique(yt)) > 1:
        aucs.append(roc_auc_score(yt, yp))
        auprcs.append(average_precision_score(yt, yp))
        eces.append(calc_ece(yt, yp))

def print_ci(name, point, arr):
    lo = np.percentile(arr, 2.5)
    hi = np.percentile(arr, 97.5)
    print(f"{name}: {point:.4f} (95% CI: {lo:.4f} - {hi:.4f})")

print_ci("Pooled AUROC", auc_pool, aucs)
print_ci("Pooled AUPRC", auprc_pool, auprcs)
print_ci("Pooled ECE", ece_pool, eces)

print("\n--- TASK 6: MANIFEST ---")
def sha256(fname):
    h = hashlib.sha256()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

manifest = {
    "fold1": {"AUROC": auc1, "AUPRC": auprc1, "ECE": ece1, "Brier": bs1},
    "fold2": {"AUROC": auc2, "AUPRC": auprc2, "ECE": ece2, "Brier": bs2},
    "pooled": {"AUROC": auc_pool, "AUPRC": auprc_pool, "ECE": ece_pool, "Brier": bs_pool},
    "bootstrap_CIs": {
        "AUROC": [np.percentile(aucs, 2.5), np.percentile(aucs, 97.5)],
        "AUPRC": [np.percentile(auprcs, 2.5), np.percentile(auprcs, 97.5)],
        "ECE": [np.percentile(eces, 2.5), np.percentile(eces, 97.5)]
    },
    "artifacts": [
        {
            "path": 'artifacts/step8_metrics/fold1_predictions.csv',
            "bytes": os.path.getsize('artifacts/step8_metrics/fold1_predictions.csv'),
            "sha256": sha256('artifacts/step8_metrics/fold1_predictions.csv')
        },
        {
            "path": 'artifacts/step8_metrics/fold2_predictions.csv',
            "bytes": os.path.getsize('artifacts/step8_metrics/fold2_predictions.csv'),
            "sha256": sha256('artifacts/step8_metrics/fold2_predictions.csv')
        }
    ]
}

with open('artifacts/step8_metrics/step8_manifest.json', 'w') as f:
    json.dump(manifest, f, indent=2)

print("Wrote artifacts/step8_metrics/step8_manifest.json")
