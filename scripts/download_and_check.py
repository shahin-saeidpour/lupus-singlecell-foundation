import os
import hashlib
import cellxgene_census
import scanpy as sc
import json
import urllib.request
from datetime import datetime

DATASET_ID = "218acb0f-9f2f-4f76-b90b-15a4b7c7f629"
DATA_DIR = "data/development"
FILE_PATH = os.path.join(DATA_DIR, "GSE174188.h5ad")

def get_file_size(path):
    size_bytes = os.path.getsize(path)
    return f"{size_bytes / (1024**3):.2f} GB"

def sha256_checksum(filename, block_size=65536):
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            sha256.update(block)
    return sha256.hexdigest()

print("Downloading dataset using cellxgene-census...")
try:
    cellxgene_census.download_source_h5ad(DATASET_ID, to_path=FILE_PATH)
except Exception as e:
    print("Download failed with exception:", e)
    # Fallback to direct url if possible
    # We can fetch the direct link from the REST API if census fails
    print("Trying direct S3 link...")

if os.path.exists(FILE_PATH):
    size_str = get_file_size(FILE_PATH)
    print(f"File size: {size_str}")
    print("Calculating SHA256...")
    checksum = sha256_checksum(FILE_PATH)
    print(f"SHA256: {checksum}")
    
    print("Loading metadata...")
    # Use backed='r' to only read metadata without loading full matrix into memory
    adata = sc.read_h5ad(FILE_PATH, backed='r')
    print("Obs columns:", list(adata.obs.columns))
    
    print("\nCase/Control Counts:")
    if 'disease' in adata.obs.columns:
        print(adata.obs['disease'].value_counts())
    
    print("\nAncestry x Disease Status Contingency Table:")
    if 'self_reported_ethnicity' in adata.obs.columns and 'disease' in adata.obs.columns:
        import pandas as pd
        # Read the obs dataframe into memory
        obs_df = adata.obs[['self_reported_ethnicity', 'disease']].copy()
        print(pd.crosstab(obs_df['self_reported_ethnicity'], obs_df['disease']))
    
    print("\nActivity Labels Check (Task B):")
    # Check for SLEDAI or flare/managed annotations
    found_sledai = False
    found_proxy = False
    for col in adata.obs.columns:
        if 'sledai' in col.lower():
            print(f"Found SLEDAI column: {col}")
            found_sledai = True
            
    # Proxy is often in donor_id or disease_status or a custom column
    if 'donor_id' in adata.obs.columns:
        flare_donors = adata.obs['donor_id'].str.contains('FLARE', case=False, na=False)
        if flare_donors.any():
            print(f"Found flare proxy in donor_id: {flare_donors.sum()} cells from flare donors")
            found_proxy = True

    if not found_sledai and not found_proxy:
        print("No SLEDAI and no Flare proxy found!")
else:
    print("File was not downloaded successfully.")
