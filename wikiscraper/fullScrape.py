'''I won't move forward on this until secondScrape has been fully tested.

A tentative step towards combining scrape 1 and scrape 2

'''



import requests
import json

from pprint import pprint as pp
from bs4 import BeautifulSoup

from secondScrape import *
from entryClass import *
from firstScrape import *

#defined in firstScrape
links = URLgrab(Entry.entryURL)

allTds = []
dict = []
for link in links:
   linkSoup = BeautifulSoup(requests.get(link).text, 'lxml')
   linkTable = linkSoup.findAll('tr')
   linkTds = getEntries(linkTable)
   
   allTds.extend(linkTds)
#should be 27043
print(len(allTds))

for ele in allTds:
   doubles = dblEntryCheck(ele)
   if hasattr(doubles, '__len__'):
      # print('working')
      # pp(doubles[1].__dict__)
      for dbl in doubles:
         dict.append(dbl)   
   else:
      populate(ele,dict)

testy = []

for item in dict:
   testy.append(item.__dict__)
with open('wikiscraper/writetest.json', 'w') as final:
   json.dump(testy, final, indent=4, ensure_ascii=False)

#trying with smaller # first
# testLink = links[random.randrange(0,24,1)]
# print('testURL', testURL)

# testSoup = BeautifulSoup(requests.get(testLink).text, 'lxml')
# table = testSoup.findAll('tr')
# #???
# testLambda = []
# tds = getEntries(table)

# dict = []

# for ele in tds:
#     doubles = dblEntryCheck(ele)
#     if hasattr(doubles, '__len__'):
#       # print('working')
#       # pp(doubles[1].__dict__)
#       for dbl in doubles:
#          dict.append(dbl)   
#     else:
#       populate(ele,dict)

# testy = []

# for item in dict[:10]:
#    testy.append(item.__dict__)
# with open('wikiscraper/writetest.json', 'w') as final:
#    json.dump(testy, final, indent=4, ensure_ascii=False)
