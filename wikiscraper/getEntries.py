# contains the getEntries function and possibly(?) its helpers.
#NOT DONE. see original code in indvScrape2

from bs4 import BeautifulSoup
import requests
import re
from entryClass import *

testURL = 'https://en.wiktionary.org/wiki/Appendix:Chinese_Cangjie/%E7%81%AB'
hrefHead = 'https://en.wiktionary.org'
html_text = requests.get(testURL).text

tableSoup = BeautifulSoup(html_text, 'lxml')
data = []
tr = tableSoup.find_all('tr')

def getEntries(ele):
  # accepts a list of HTML tr element
  # returns an Entry class object
  
  td = ele.find_all('td')

  #each tr element contains 3 tds.
  # the first contains the radicals
  # the second contains the QWERTY string
  # the third contains the href to the indv page, which may or may not work, and the UTC character itself.

  e = Entry()
  # get radicals
  e.get_radicals(data[0].text)

  # get QWERTY
  e.get_qwerty(data[1].text)[1:-1]

  chars = ele.find_all('a',class_='Hani').text
  # hand 2-char edge case
  if (len(chars) > 1):
    e2 = Entry()
    e2.get_radicals(e.radicals)
    e2.get_qwerty(e.qwerty)
    e2.get_character(chars[1])
    e2.get_link()