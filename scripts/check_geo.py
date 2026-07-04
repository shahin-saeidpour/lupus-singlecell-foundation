import urllib.request
import re

url = 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE135779'
req = urllib.request.Request(url)
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        links = re.findall(r'href=\"(/geo/download/\?acc=GSE135779[^\"]+)\"', html)
        for link in links:
            if 'format=file' in link:
                print('Found Download Link:', 'https://www.ncbi.nlm.nih.gov' + link)
except Exception as e:
    print('Error:', e)
