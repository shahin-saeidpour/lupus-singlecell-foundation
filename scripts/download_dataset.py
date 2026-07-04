import os
import urllib.request
import hashlib
import time

url = 'https://cellxgene-data-public.s3.us-west-2.amazonaws.com/cell-census/2023-12-15/h5ads/218acb0f-9f2f-4f76-b90b-15a4b7c7f629.h5ad'
dest = 'data/development/GSE174188.h5ad'
expected_size = 11288275886

os.makedirs('data/development', exist_ok=True)

print(f"Starting download from {url}")
print(f"Destination: {dest}")

start_time = time.time()
sha256 = hashlib.sha256()
downloaded = 0

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    # Check headers if possible
    content_length = response.getheader('Content-Length')
    if content_length:
        print(f"Reported Content-Length: {content_length}")
    
    with open(dest, 'wb') as f:
        while True:
            chunk = response.read(8192 * 1024) # 8MB chunks
            if not chunk:
                break
            f.write(chunk)
            sha256.update(chunk)
            downloaded += len(chunk)
            
            # Print progress every ~1GB
            if downloaded % (1024 * 1024 * 1024) < (8192 * 1024):
                print(f"Downloaded {downloaded / 1024**3:.2f} GB...")

end_time = time.time()
actual_size = os.path.getsize(dest)

print(f"\nDownload complete in {end_time - start_time:.2f} seconds")
print(f"Actual file size on disk: {actual_size}")

if actual_size != expected_size:
    print(f"ERROR: Size mismatch! Expected {expected_size}, got {actual_size}")
    os.remove(dest)
    print("Deleted corrupted file.")
else:
    print("Size perfectly matches expected!")
    print(f"SHA256: {sha256.hexdigest()}")
    
    with open('data/development/sha256.txt', 'w') as f:
        f.write(sha256.hexdigest())
