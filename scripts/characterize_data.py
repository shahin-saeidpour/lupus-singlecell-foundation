import scanpy as sc
import numpy as np

file_path = 'data/development/GSE174188.h5ad'
print(f"Loading {file_path} in backed mode...")
adata = sc.read_h5ad(file_path, backed='r')

print("\n--- TASK 1: DATA CHARACTERIZATION ---")

# 1. X
print("X:")
print(f"  type: {type(adata.X)}")
if hasattr(adata.X, 'dtype'):
    print(f"  dtype: {adata.X.dtype}")

# Take a sample of 10000 cells
try:
    sub = adata[:10000].to_memory()
    x_data = sub.X.data if hasattr(sub.X, 'data') else sub.X
    xmin = float(x_data.min()) if len(x_data) > 0 else 0.0
    xmax = float(x_data.max()) if len(x_data) > 0 else 0.0
    # adjust for sparsity
    if hasattr(sub.X, 'data'):
        xmin = min(0.0, xmin)
        xmax = max(0.0, xmax)
    print(f"  min (sample): {xmin}")
    print(f"  max (sample): {xmax}")
    print(f"  contains negatives: {xmin < 0}")
except Exception as e:
    print(f"  error getting min/max: {e}")

# 2. raw
print("\nraw:")
has_raw = adata.raw is not None
print(f"  exists: {has_raw}")
if has_raw:
    print(f"  type: {type(adata.raw.X)}")
    if hasattr(adata.raw.X, 'dtype'):
        print(f"  dtype: {adata.raw.X.dtype}")
    try:
        # adata.raw might not support chunking directly via anndata API easily if it's large, but we can do:
        raw_sub = adata.raw[:10000].to_adata()
        rx_data = raw_sub.X.data if hasattr(raw_sub.X, 'data') else raw_sub.X
        rmin = float(rx_data.min()) if len(rx_data) > 0 else 0.0
        rmax = float(rx_data.max()) if len(rx_data) > 0 else 0.0
        if hasattr(raw_sub.X, 'data'):
            rmin = min(0.0, rmin)
            rmax = max(0.0, rmax)
        print(f"  min (sample): {rmin}")
        print(f"  max (sample): {rmax}")
        
        is_non_negative = rmin >= 0
        is_int_like = np.all(np.equal(np.mod(rx_data, 1), 0)) if len(rx_data) > 0 else True
        print(f"  integer-like counts: {is_non_negative and is_int_like}")
    except Exception as e:
        print(f"  error reading raw: {e}")

# 3. layers
print("\nlayers:")
layer_keys = list(adata.layers.keys())
print(f"  keys: {layer_keys}")
for k in layer_keys:
    print(f"  layer '{k}':")
    lk = adata.layers[k]
    print(f"    type: {type(lk)}")
    if hasattr(lk, 'dtype'):
        print(f"    dtype: {lk.dtype}")
    try:
        sub_l = sub.layers[k]
        l_data = sub_l.data if hasattr(sub_l, 'data') else sub_l
        lmin = float(l_data.min()) if len(l_data) > 0 else 0.0
        lmax = float(l_data.max()) if len(l_data) > 0 else 0.0
        if hasattr(sub_l, 'data'):
            lmin = min(0.0, lmin)
            lmax = max(0.0, lmax)
        print(f"    min (sample): {lmin}")
        print(f"    max (sample): {lmax}")
        is_int_like = lmin >= 0 and np.all(np.equal(np.mod(l_data, 1), 0)) if len(l_data) > 0 else True
        print(f"    count-like: {is_int_like}")
    except Exception as e:
        print(f"    error getting min/max: {e}")

# 4. var / uns hints
print("\nvar columns:")
print(list(adata.var.columns))

print("\nuns keys:")
print(list(adata.uns.keys()))

print("\n--- TASK 2: RECONCILIATION ---")
# Just a placeholder, will make a manual decision based on output.
