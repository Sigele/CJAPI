#building out logic for broken link edge case

from bs4 import BeautifulSoup
import requests
import re
from pprint import pprint as pp

from entryClass import *


testURL = 'https://en.wiktionary.org/wiki/Appendix:Chinese_Cangjie/%E7%81%AB'

hrefHead = 'https://en.wiktionary.org'

html_text = requests.get(testURL).text

extraSoup = BeautifulSoup(html_text, 'lxml')

data = []
entries = []

def getEntries(url,list):
  tr = extraSoup.find_all('tr')

  for line in tr:
    td = line.find_all('td')
    list.append(td)
  # each 'ele is an array of 3 'td' elements 
  doubles = []
  # find all entries with multiple characters
  for ele in list:
    if len(ele[2].find(class_='Hani').text) > 2:
      doubles.append(ele)
      for double in doubles:
        names = double[2].find_all('a')
        for name in names: 
          e2 = Entry()
          e2.get_character(name.text)
          e2.get_qwerty(ele[1].text[1:-1])
          e2.get_radicals(ele[0].text)
          e2.get_level(len(e2.radicals))
          e2.get_link(hrefHead, name['href'])
          entries.append(e2)
    else:
      e = Entry()

      def populate(entry):
        entry.get_character(ele[2].find(class_='Hani').text)
        entry.get_qwerty(ele[1].text[1:-1])
        entry.get_radicals(ele[0].text)
        entry.get_level(len(e.radicals))
        entry.get_link(hrefHead, ele[2].find('a')['href'])
        entries.append(entry)
      populate(e)
    

getEntries(testURL, data)
# pp(entries[10].__dict__)


    
      
      