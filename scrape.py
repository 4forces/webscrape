import rpa, os, requests, bs4, selenium as s, pandas as p
# from urllib.request import Request, urlopen

# 1. click on programme
# 2. extract prog name, prog desc, prog duration etc

# --- urls --- #
ENG = 'https://www.singaporetech.edu.sg/postgraduate-programmes/engineering'
CEFT = 'https://www.singaporetech.edu.sg/undergraduate-programmes/chemical-engineering-and-food-technology'
DSB = 'https://www.singaporetech.edu.sg/undergraduate-programmes/design-and-specialised-businesses'
HSS = 'https://www.singaporetech.edu.sg/undergraduate-programmes/health-and-social-sciences'
ICT = 'https://www.singaporetech.edu.sg/undergraduate-programmes/infocomm-technology'


def seturl(url):
    """Prompts user for url"""
    # url = input("Input URL: ")
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    def checkurl():
        """Checks, returns response if url is working"""
        # url = input("Input URL: ")
        # r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        print('<Url check>: ', url, '\n')
        print(r)
        print('\n<Start of url sample>: ', r.text[:1000])
        print('\n<r.raise_for_status>:', r.raise_for_status())

    checkurl()
    try:
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
    except IndexError:
        print('Url seems invalid. Please check that url is an SIT programme page.')


# def checkurl():
#     """Checks, returns response if url is working"""
#     # url = input("Input URL: ")
#     # r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
#     print('<Url check>: ', url, '\n')
#     print(r)
#     print('\n<Start of url sample>: ', r.text[:1000])
#     print('\n<r.raise_for_status>:', r.raise_for_status())


def urltotext(url):
    """Saves downloaded webpage to binary text"""
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    def checkurl():
        """Checks, returns response if url is working"""
        # url = input("Input URL: ")
        # r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        print('<Url check>: ', url, '\n')
        print(r)
        print('\n<Start of url sample>: ', r.text[:1000])
        print('\n<r.raise_for_status>:', r.raise_for_status())

    checkurl()

    # wb: write binary to avoid unicode encode issues
    playfile = open('testFile.txt', 'wb')

    # writes url:'r' contents to 'playfile' in bytes of 100000
    for chunk in r.iter_content(100000):
        playfile.write(chunk)
    playfile.close()

# --- from https://www.bestproxyreviews.com/scrapy-vs-selenium-vs-beautifulsoup-for-web-scraping/ --- #
# r = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(r).read()
# print(webpage)
