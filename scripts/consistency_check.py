import scanpy as sc
import sys

file_path = 'data/development/GSE174188.h5ad'

print(f"Loading local file: {file_path}")
adata = sc.read_h5ad(file_path, backed='r')
obs = adata.obs

print(f"Total cells: {len(obs)}")

unique_donors = obs['donor_id'].nunique()
print(f"Unique donors: {unique_donors}")

# Deduplicate by donor_id
donor_obs = obs.drop_duplicates(subset=['donor_id'])

# Disease counts
disease_counts = donor_obs['disease'].value_counts()
print("\nDisease counts:")
print(disease_counts)

sle_count = disease_counts.get('systemic lupus erythematosus', 0)
normal_count = disease_counts.get('normal', 0)

# Ancestry present
has_ancestry = 'self_reported_ethnicity' in obs.columns
print(f"\nAncestry column present: {has_ancestry}")
if has_ancestry:
    ancestry_counts = donor_obs['self_reported_ethnicity'].value_counts()
    print("Ancestry counts:")
    print(ancestry_counts)
    
# disease_state present
has_disease_state = 'disease_state' in obs.columns
print(f"\ndisease_state column present: {has_disease_state}")

# Verify consistency
discrepancies = []

if unique_donors != 261:
    discrepancies.append(f"Expected 261 donors, got {unique_donors}")
    
if sle_count != 162:
    discrepancies.append(f"Expected 162 SLE donors, got {sle_count}")
    
if normal_count != 99:
    discrepancies.append(f"Expected 99 Normal donors, got {normal_count}")
    
if not has_ancestry:
    discrepancies.append("Ancestry column is missing!")
else:
    top_ancestries = ancestry_counts.head(2).index.tolist()
    if 'European' not in top_ancestries or 'Asian' not in top_ancestries:
        discrepancies.append(f"Expected European+Asian dominant, got {top_ancestries}")
        
if not has_disease_state:
    discrepancies.append("disease_state column is missing!")

print("\n--- CONSISTENCY CHECK RESULT ---")
if len(discrepancies) == 0:
    print("PASS: Local file is perfectly consistent with 6a inventory.")
else:
    print("FAIL: Discrepancies found!")
    for d in discrepancies:
        print(" -", d)
    sys.exit(1)
