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
  # as above, each "double is a list of 3 td elements"
  # print(doubles)

  # make a new Entry class obj for each character 
  for double in doubles:
    names = double[2].find_all('a')
    for name in names:
      print(name.find('title'))
    print(names)

  # make array of alternate titles and links

  # insert each into a new Entry object, build rest of object as normal
      
      
      

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
pp(entries[0].__dict__)