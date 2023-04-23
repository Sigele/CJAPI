'''
The Cangjie appendix on wiktionary starts with a root page. The cangjie for each individual character are listed according to the first radical of their input, and separated into 25 individual pages on that basis. 

EX: the character '烂' is typed by entering '火' first, and is therefore found on the 火 subpage. 

The logic here scrapes the root page and retrieves URL links (as strings) to all 25 subpages. 

This data shouldn't pass to the db per se but should be used as an entry point for a scrape of the entire appendix.


'''

from bs4 import BeautifulSoup
import requests
import re
from constants import *
##added functionailty to func block for export

def URLgrab(url):
  page_text = requests.get(url).text

  urlSoup = BeautifulSoup(page_text, 'lxml')

  #this returns a list of elements. the actual text of the link is extracted below. Can I combine these to simplify the function? (try monday)

  # for link in linkSoup:
    # links.append(hrefHead + link['href])


  linkSoup = urlSoup.findAll('a', href=re.compile('/wiki/Appendix:Chinese_Cangjie/%'))

  links = []

  for link in linkSoup:
    href = link['href']
    links.append(hrefHead + href)

  return links


testLinks = (URLgrab(entryURL))
print('hey now!!',testLinks)