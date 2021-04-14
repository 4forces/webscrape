
import rpa
import os
import requests
from bs4 import BeautifulSoup as soup
# import selenium as s
# import pandas as p
# from urllib.request import Request, urlopen
# from bs4 import BeautifulSoup  as soup


url = 'https://www.singaporetech.edu.sg/undergraduate-programmes/engineering'
badurl ='https://www.singaporetech.edu.sg/undergraduate-programmes/engineerin'


r = requests.get(url)
print(r, '\n ---')
print(r.text[:300])
# wb = write binary to avoid unicode encode issues
playfile = open('testFile.txt','wb')
# writes url:'r' contents to playfile in bytes of 100000
for chunk in r.iter_content(100000):
    playfile.write(chunk)
playfile.close()


# --- from https://www.bestproxyreviews.com/scrapy-vs-selenium-vs-beautifulsoup-for-web-scraping/ --- #
# r = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(r).read()
# print(webpage)
