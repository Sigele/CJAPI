from bs4 import BeautifulSoup
import requests
import json
import random
from pprint import pprint as pp

from entryClass import Entry
from firstScrape import testLinks
from dblEntryCheck import dblEntryCheck
from brokenLink import brokenLinkCheck
from constants import *

testURL = testLinks[random.randrange(0,24,1)]
print(testURL)

html_text = requests.get(testURL).text
soup = BeautifulSoup(html_text, 'lxml')
table = soup.find_all('tr')

# grabbing all td elements
def getEntries(table):
    elements = []
    for trow in table:
        td = trow.find_all('td')
        elements.append(td) 

    return elements

#func to create a single new Entry
def populate(ele, list):
    entry = Entry()
    entry.get_character(ele[2].find(class_='Hani').text)
    entry.get_qwerty(ele[1].text[1:-1])
    entry.get_radicals(ele[0].text)
    entry.get_level(len(entry.radicals))
    if (brokenLinkCheck(ele) == True):
      entry.get_link('Sorry, ' , 'the link is missing!')
    else:
      entry.get_link(hrefHead, ele[2].find('a')['href'])
    list.append(entry)

#incorporating doubled edge case where needed
tripleTds = getEntries(table)
data = []

for ele in tripleTds:
   doubles = dblEntryCheck(ele)
   if hasattr(doubles, '__len__'):
      # print('working')
      # pp(doubles[1].__dict__)
      for dbl in doubles:
         data.append(dbl)   
   else:
      populate(ele,data)


#testing!!!
test_dict = []

for item in data[21:31]:
   test_dict.append(item.__dict__)

with open('wikiscraper/writetest.json', 'w')  as final:
   json.dump(test_dict, final, indent = 4, ensure_ascii=False)