# experimenting to try and scrape each radical page. subsequent data will be parsed as in mainPage.py.

from bs4 import BeautifulSoup
import requests
import re


# page_text = requests.get('https://en.wiktionary.org/wiki/Appendix:Chinese_Cangjie').text

# soup = BeautifulSoup(page_text, 'lxml')

# #this finds the radical elements in the page ONLY. need to grab hrefs from these!
# rads = soup.findAll('a', href=re.compile('/wiki/Appendix:Chinese_Cangjie/%'))

# links = []

# # using string concatenation to build complete URLs. Should be 25 total links (YUP YUP)
# for rad in rads:
#   href = rad['href']
#   hrefHead = 'https://en.wiktionary.org'
#   links.append(hrefHead + href)

# # 

##added functionailty to func block for export

def URLgrab(url):
  page_text = requests.get(url).text

  urlSoup = BeautifulSoup(page_text, 'lxml')

  linkSoup = urlSoup.findAll('a', href=re.compile('/wiki/Appendix:Chinese_Cangjie/%'))

  links = []

  for link in linkSoup:
    href = link['href']
    hrefHead = 'https://en.wiktionary.org'
    links.append(hrefHead + href)

  return links

print(URLgrab('https://en.wiktionary.org/wiki/Appendix:Chinese_Cangjie'))