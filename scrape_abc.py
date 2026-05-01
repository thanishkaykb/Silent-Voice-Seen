import urllib.request
import re

url = "https://www.lifeprint.com/asl101/fingerspelling/index.htm"
try:
    html = urllib.request.urlopen(url).read().decode('utf-8', errors='ignore')
    imgs = re.findall(r'<img[^>]+src=[\"\']([^\'\"]+)[\"\']', html)
    print("Found images:", list(set(imgs)))
except Exception as e:
    print('Error:', e)
