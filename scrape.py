import bs4
import csv
import requests


# from urllib.request import Request, urlopen

# 1. click on programme
# 2. extract prog name, prog desc, prog duration etc

# ----- urls ----- #
CEFT = 'https://www.singaporetech.edu.sg/undergraduate-programmes/chemical-engineering-and-food-technology'
DSB = 'https://www.singaporetech.edu.sg/undergraduate-programmes/design-and-specialised-businesses'
HSS = 'https://www.singaporetech.edu.sg/undergraduate-programmes/health-and-social-sciences'
ICT = 'https://www.singaporetech.edu.sg/undergraduate-programmes/infocomm-technology'
ENG = 'https://www.singaporetech.edu.sg/postgraduate-programmes/engineering'

# ----- RPA for python ----- #
# import rpa as r
# r.init()
# r.url(ENG)
# r.click('//*[@id="block-sit-2020-content"]/div/div[2]/div/div/div/div/div/ol/li[1]/div/span/div/a')
# r.url(ENG)

# ----- Selenium Webdriver ----- #
# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get(ENG)

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

        qualification_raw = soup.select('#block-sit-2020-content > div > div.group-left-right-container > div > div > '
                                        'div.group-left > div.group-programme-details.row--md.paragraph-wrapper > '
                                        'div:nth-child(1)')
        qualification = qualification_raw[0].text.strip()

        ou_raw = soup.select('#block-sit-2020-content > div > div.group-left-right-container > div > div > '
                             'div.group-left > div.group-programme-details.row--md.paragraph-wrapper > '
                             'div:nth-child(2)')
        ou = ou_raw[0].text.strip()

        duration_raw = soup.select('#block-sit-2020-content > div > div.group-left-right-container > div > div > '
                                   'div.group-left > div.group-programme-details.row--md.paragraph-wrapper > '
                                   'div:nth-child(3)')
        duration = duration_raw[0].text.strip()

        t_credits_raw = soup.select('#block-sit-2020-content > div > div.group-left-right-container > div > div > '
                                    'div.group-left > div.group-programme-details.row--md.paragraph-wrapper > '
                                    'div:nth-child(4)')
        t_credits = t_credits_raw[0].text.strip()

        location_raw = soup.select('#block-sit-2020-content > div > div.group-left-right-container > div > div > '
                                   'div.group-left > div.group-programme-details.row--md.paragraph-wrapper > '
                                   'div:nth-child(7)')
        location = location_raw[0].text.strip()

        print(prog_name)
        print(prog_desc)
        print(qualification)
        print(ou)
        print(duration)
        print(t_credits)
        print(location)

        with open('innovators.csv', 'a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([prog_name, prog_desc, qualification, ou, duration, t_credits])

    except IndexError:
        print('Url seems invalid. Please check that url is an SIT programme page.')


# row_list = [["SN", "Name", "Contribution"],
#             [1, "Linus Torvalds", "Linux Kernel"],
#             [2, "Tim Berners-Lee", "World Wide Web"],
#             [3, "Guido van Rossum", "Python Programming"]
#             ]

# with open('innovators.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow([, , ])


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
