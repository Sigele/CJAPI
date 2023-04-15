# currently refactoring successful(?) scrape functionality...there's a bit to much unecessary space being taken up

from bs4 import BeautifulSoup
import requests
import re
from pprint import pprint as pp

from entryClass import *

testURL = 'https://en.wiktionary.org/wiki/Appendix:Chinese_Cangjie/%E7%81%AB'

hrefHead = 'https://en.wiktionary.org';
html_text = requests.get(testURL).text

soup = BeautifulSoup(html_text, 'lxml')
table = soup.find_all('tr')

# returns list of 3-element sublists. Each sublist represents an entry for a single character.

def getEntries(url, table):
    elements = []
    for trow in table:
      td = trow.find_all('td')
      elements.append(td)

    return elements


def dblEntryCheck(three_tds):
    #if the element that holds the a elements contains 2 different ones, we need to save the titles but give everything else identical attributes
    result = []
    #should the entry building happen here? or in the main function?
    # uhhhh here to avoid redundancies in the main function
    if len(three_tds[2].find(class_='Hani').text) > 2:
      names = three_tds[2].find_all('a')
      for name in names:
         e2 = Entry()
         e2.get_character(name.text)
         e2.get_qwerty(three_tds[1].text[1:-1])
         e2.get_radicals(three_tds[0].text)
         e2.get_level(len(e2.radicals))
         if(brokenLinkCheck(three_tds) == True):
            e2.get_link('Sorry, ', 'the link is missing!')
         else: 
            e2.get_link(hrefHead, name['href'])
         result.append(e2)   
    if (len(result) == 0): return
    return result;

def brokenLinkCheck(listOf3Elements):
  if len(listOf3Elements[2].find('a')['title']) > 1:
    return True

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


tds = getEntries(testURL,table)
# print(len(tds))
data = []
for ele in tds:
   doubles = dblEntryCheck(ele)
   if hasattr(doubles, '__len__'):
      # print('working')
      # pp(doubles[1].__dict__)
      for dbl in doubles:
         data.append(dbl)   
   else:
      populate(ele,data)
# print(len(data))
   
pp(data[643].__dict__)
      
    


# pp(data[28].__dict__)
