import s3fs
import h5py
import pandas as pd
import json

url = 's3://cellxgene-data-public/cell-census/2023-12-15/h5ads/218acb0f-9f2f-4f76-b90b-15a4b7c7f629.h5ad'
fs = s3fs.S3FileSystem(anon=True)

try:
    print(f"Connecting to {url}...")
    with fs.open(url, 'rb') as f:
        with h5py.File(f, 'r') as h5:
            # Check obs columns
            obs = h5['obs']
            
            # Helper to read an entire categorical/string column
            def read_col(col_name):
                if col_name not in obs:
                    return None
                col_group = obs[col_name]
                if 'categories' in col_group:
                    cats = col_group['categories'][:]
                    codes = col_group['codes'][:]
                    return pd.Series(codes).map(dict(enumerate([c.decode('utf-8') for c in cats])))
                else:
                    return pd.Series([c.decode('utf-8') if isinstance(c, bytes) else c for c in col_group[:]])

            keys = list(obs.keys())
            print("\nobs columns exist:", keys)
            
            # Specific checks
            print("\nSpecific confirmations:")
            disease = read_col('disease')
            ancestry = read_col('self_reported_ethnicity')
            sex = read_col('sex')
            age = read_col('development_stage')
            donor_id = read_col('donor_id')
            
            print(f"disease / case-control status present: {disease is not None}")
            print(f"ancestry present: {ancestry is not None}")
            print(f"sex present: {sex is not None}")
            print(f"age present: {age is not None}")
            
            # Activity annotation check
            found_sledai = any('sledai' in k.lower() for k in keys)
            print(f"SLEDAI numeric present: {found_sledai}")
            
            found_proxy = False
            if donor_id is not None:
                flare_count = donor_id.str.contains('FLARE', case=False, na=False).sum()
                if flare_count > 0:
                    found_proxy = True
                    print(f"Flare/managed proxy present: YES ({flare_count} cells from flare donors)")
            
            if disease is not None:
                print("\nCase/control counts overall (cells):")
                print(disease.value_counts())
            
            if ancestry is not None and disease is not None:
                print("\nAncestry x (SLE/HC) contingency table (cells):")
                print(pd.crosstab(ancestry, disease))

except Exception as e:
    import traceback
    traceback.print_exc()
