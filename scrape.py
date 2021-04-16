
import rpa
import os
import requests
import bs4
import selenium as s
import pandas as p
# from urllib.request import Request, urlopen


def set_url():
    """Prompts user for url"""
    url = input("Input URL: ")
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    check_url()
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    prog_name_raw = soup.select('#block-sit-2020-content > div > div.group-header.row--lg > header > div > div > '
                                'div.banner-header__overlay.wrap--center.wrap--xl > div > div > h1')
    prog_name = prog_name_raw[0].text.strip()
    prog_desc_raw = soup.select('#block-sit-2020-content > div > div.group-header.row--lg > header > div > div > '
                                'div.banner-header__overlay.wrap--center.wrap--xl > div > div > div.subtitle')
    prog_desc = prog_desc_raw[0].text.strip()
    duration_raw = soup.select(
        '#block-sit-2020-content > div > div.group-left-right-container > div > div > div.group-left > '
        'div.group-programme-details.row--md.paragraph-wrapper > div:nth-child(3)')
    duration = duration_raw[0].text.strip()
    print(prog_name)
    print(prog_desc)
    print(duration)


def check_url():
    """Checks, returns response if url is working"""
    url = input("Input URL: ")
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    print('<Url check>: ', url, '\n')
    print(r)
    print('\n<Start of url sample>: ',r.text[:1000])
    print('\n<r.raise_for_status>:', r.raise_for_status())


def request_http():
    """Saves downloaded webpage to binary text"""
    print('<----- START OF HTTP REQUESTS OUTPUT ----->\n')
    check_url()
    # wb: write binary to avoid unicode encode issues
    playfile = open('testFile.txt', 'wb')

    # writes url:'r' contents to 'playfile' in bytes of 100000
    for chunk in r.iter_content(100000):
        playfile.write(chunk)
    playfile.close()
    print('\n----- END OF HTTP REQUESTS OUTPUT ----->')

# --- from https://www.bestproxyreviews.com/scrapy-vs-selenium-vs-beautifulsoup-for-web-scraping/ --- #
# r = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(r).read()
# print(webpage)
