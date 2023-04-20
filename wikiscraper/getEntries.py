# contains the getEntries function and possibly(?) its helpers.
#NOT DONE. see original code in indvScrape2

from bs4 import BeautifulSoup
import requests
import re
from pprint import pprint as pp

from entryClass import *
from constants import * 

#page for entries beginning with the 火 radical
testURL = 'https://en.wiktionary.org/wiki/Appendix:Chinese_Cangjie/%E7%81%AB'

#concat this with hrefs to build complete working URL
html_text = requests.get(testURL).text

tableSoup = BeautifulSoup(html_text, 'lxml')

# redundant, only need one list
data = []
entries = []

def getEntries(url,list):
  tr = tableSoup.find_all('tr')

  for line in tr:
    td = line.find_all('td')
    list.append(td)

  for ele in list:
    e = Entry()
    e.get_character(ele[2].find(class_='Hani').text)
    #this is not working.......por why
    e.get_qwerty(ele[1].text[1:-1])
    # print(e)
    e.get_radicals(ele[0].text)
    e.get_level(len(e.radicals))
    e.get_link(hrefHead, ele[2].find('a')['href'])
    entries.append(e)

getEntries(testURL, data)
print(type(tableSoup))
  # test print in readable format
# pp(entries[0].__dict__)


  # example of entry HTML structure. this file turns a 'tr' element into a list of entries

"""
  [
    [
      <td><b>火卜日女</b></td>, 
      <td>(FYAV)</td>, 
      <td>: <span class="Hani" style="font-size:large">
              <a href="/wiki/%E7%85%BA" title="煺">
              煺
              </a>
            </span>
      </td>
    ]
    [
      <td><b>火卜月金</b></td>, 
      <td>(FYBC)</td>, 
      <td>: <span class="Hani" style="font-size:large">
              <a class="new" href="/w/index.php?title=%F0%A4%8B%BA&amp;action=edit&amp;redlink=1" title="𤋺 (page does not exist)">
              𤋺
              </a>
            </span>
      </td>
    ]
  []
  ]

"""
    

