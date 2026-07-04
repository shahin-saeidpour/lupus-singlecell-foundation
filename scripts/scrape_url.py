import urllib.request
import re

url = 'https://cellxgene.cziscience.com/datasets/218acb0f-9f2f-4f76-b90b-15a4b7c7f629'
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    html = response.read().decode('utf-8')
    urls = re.findall(r'https://[^\s\"\']+\.h5ad', html)
    print('Found H5AD URLs:', list(set(urls)))
    
    api_urls = re.findall(r'https://api\.cellxgene\.cziscience\.com[^\s\"\']+', html)
    print('Found API URLs:', list(set(api_urls)))
