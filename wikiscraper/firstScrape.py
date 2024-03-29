'''
The Cangjie appendix on wiktionary starts with a root page. The cangjie for each individual character are listed according to the first radical of their input, and separated into 25 individual pages on that basis. 

EX: the character '烂' is typed by entering '火' first, and is therefore found on the 火 subpage. 

The logic here scrapes the root page and retrieves URL links (as strings) to all 25 subpages. 

This data shouldn't pass to the db per se but should be used as an entry point for a scrape of the entire appendix.


'''

from bs4 import BeautifulSoup
import requests
import re
# from constants import *
from entryClass import *
##added functionailty to func block for export

def URLgrab(url):
  page_text = requests.get(url).text

  urlSoup = BeautifulSoup(page_text, 'lxml')

  linkSoup = urlSoup.findAll('a', href=re.compile('/wiki/Appendix:Chinese_Cangjie/%'))

  links = []

  for link in linkSoup:
    links.append(Entry.hrefHead + link['href'])

  return links


testLinks = (URLgrab(Entry.entryURL))
# print('hey now!!',testLinks)