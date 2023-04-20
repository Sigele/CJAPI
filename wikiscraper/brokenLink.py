# debugging broken/nonexistent link edge case

from bs4 import BeautifulSoup
from entryClass import *
from search import search
from doubledEntry import entries
from getEntries import *
import re
import requests

'''
broken links are identified in 2 ways:
  the "title" attribute includes "(page does not exist)"
  the "href" string ends with "redLink=1"

'''

brokenSoup = BeautifulSoup(html_text, 'lxml');
data = []
entries = []
def getEntries(url,list):
  tr = brokenSoup.find_all('tr')

  for line in tr:
    td = line.find_all('td')
    list.append(td)
  # each 'ele is an array of 3 'td' elements 
  doubles = []
  
  for ele in list:
    # if there are 2 characters for a single entry...
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
          if (brokenLinkCheck(ele) == True):
            e2.get_link('Sorry,' , 'the link is missing!')
          else:
            e2.get_link(hrefHead, name['href'])
          entries.append(e2)

    else:
      e = Entry()

      def populate(entry):
        entry.get_character(ele[2].find(class_='Hani').text)
        entry.get_qwerty(ele[1].text[1:-1])
        entry.get_radicals(ele[0].text)
        entry.get_level(len(e.radicals))
        if (brokenLinkCheck(ele) == True):
          entry.get_link('Sorry, ' , 'the link is missing!')
        else:
          entry.get_link(hrefHead, ele[2].find('a')['href'])
        entries.append(entry)
      populate(e)



#encapsulating link check logic
def brokenLinkCheck(listOf3Elements):
  if len(listOf3Elements[2].find('a')['title']) > 1:
    return True
  
getEntries(testURL, data)   
pp(entries[28].__dict__)