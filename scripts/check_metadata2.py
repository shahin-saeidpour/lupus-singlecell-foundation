import s3fs
import h5py
import pandas as pd

url = 's3://cellxgene-data-public/cell-census/2023-12-15/h5ads/218acb0f-9f2f-4f76-b90b-15a4b7c7f629.h5ad'
fs = s3fs.S3FileSystem(anon=True)

print(f"Connecting to {url}...")
try:
    with fs.open(url, 'rb') as f:
        with h5py.File(f, 'r') as h5:
            obs = h5['obs']
            keys = list(obs.keys())
            print("OBS_COLUMNS_START")
            print(keys)
            print("OBS_COLUMNS_END")

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

            # Read necessary columns
            disease = read_col('disease')
            ancestry = read_col('self_reported_ethnicity')
            sex = read_col('sex')
            age = read_col('development_stage')
            donor_id = read_col('donor_id')

            df = pd.DataFrame({
                'donor_id': donor_id,
                'disease': disease,
                'ancestry': ancestry,
                'sex': sex,
                'age': age
            })
            
            # Deduplicate by donor
            donor_df = df.drop_duplicates(subset=['donor_id'])

            print("TOTAL_UNIQUE_DONORS:", len(donor_df))
            
            print("\nDONOR_LEVEL_DISEASE_COUNTS:")
            print(donor_df['disease'].value_counts())

            print("\nDONOR_LEVEL_ANCESTRY_COUNTS:")
            print(donor_df['ancestry'].value_counts())

            print("\nDONOR_LEVEL_CONTINGENCY_TABLE (Ancestry x Disease):")
            print(pd.crosstab(donor_df['ancestry'], donor_df['disease']))
            
            print("\nTASK_B_CHECK:")
            found_sledai = [k for k in keys if 'sledai' in k.lower()]
            print("SLEDAI columns:", found_sledai)
            
            flare_proxy_donors = donor_df['donor_id'].str.contains('FLARE', case=False, na=False).sum()
            print("Flare proxy donors:", flare_proxy_donors)
            
            # Are there any disease_state or flare columns?
            found_disease_state = [k for k in keys if 'flare' in k.lower() or 'disease_state' in k.lower() or 'activity' in k.lower()]
            print("Other activity columns:", found_disease_state)

except Exception as e:
    import traceback
    traceback.print_exc()
