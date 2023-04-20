# experimenting to try and scrape each radical page. subsequent data will be parsed as in mainPage.py.

from bs4 import BeautifulSoup
import requests
import re
from constants import *
##added functionailty to func block for export

def URLgrab(url):
  page_text = requests.get(url).text

  urlSoup = BeautifulSoup(page_text, 'lxml')

  linkSoup = urlSoup.findAll('a', href=re.compile('/wiki/Appendix:Chinese_Cangjie/%'))

  links = []

  for link in linkSoup:
    href = link['href']
    links.append(hrefHead + href)

  return links

print('hey now',URLgrab(entryURL))