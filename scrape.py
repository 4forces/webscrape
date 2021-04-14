
import rpa
import os
import requests
import bs4
import selenium as s
import pandas as p
# from urllib.request import Request, urlopen

# ----- Requests HTTP ----- #
url = 'https://www.singaporetech.edu.sg/undergraduate-programmes/engineering'

# -- badurl example -- #
# badurl ='https://www.singaporetech.edu.sg/undergraduate-programmes/engineerin'
# bad_r = requests.get(badurl)
# print(bad_r.raise_for_status())

def request_http()
    print('<----- START OF HTTP REQUESTS OUTPUT ----->')
    # r = requests.get(url)
    # print(r, '\n ---')
    # print(r.text[:300])
    #
    # # wb: write binary to avoid unicode encode issues
    # playfile = open('testFile.txt','wb')
    #
    # # writes url:'r' contents to 'playfile' in bytes of 100000
    # for chunk in r.iter_content(100000):
    #     playfile.write(chunk)
    # playfile.close()
    print('<----- END OF HTTP REQUESTS OUTPUT ----->')


print('<----- START OF BeautifulSoup OUTPUT ----->')
# --- from https://www.bestproxyreviews.com/scrapy-vs-selenium-vs-beautifulsoup-for-web-scraping/ --- #
# r = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(r).read()
# print(webpage)


# ---- BeautifulSoup Parsing ---- #
soup = bs4.BeautifulSoup(r.text, 'html.parser')
print('<----- END OF BeautifulSoup OUTPUT ----->')
