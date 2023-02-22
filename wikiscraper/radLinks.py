# experimenting to try and scrape each radical page. subsequent data will be parsed as in mainPage.py.

from bs4 import BeautifulSoup
import requests
import re

page_text = requests.get('https://en.wiktionary.org/wiki/Appendix:Chinese_Cangjie').text

soup = BeautifulSoup(page_text, 'lxml')

#this finds the radical elements in the page ONLY. need to grab hrefs from these!
rads = soup.findAll('a', href=re.compile('/wiki/Appendix:Chinese_Cangjie/%'))

