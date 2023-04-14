# contains the getEntries function and possibly(?) its helpers.
#NOT DONE. see original code in indvScrape2

from bs4 import BeautifulSoup
import requests
import re
from pprint import pprint as pp

from entryClass import *

testURL = 'https://en.wiktionary.org/wiki/Appendix:Chinese_Cangjie/%E7%81%AB'
hrefHead = 'https://en.wiktionary.org'
html_text = requests.get(testURL).text

tableSoup = BeautifulSoup(html_text, 'lxml')
data = []
entries = []
tr = tableSoup.find_all('tr')

for line in tr:
  td = line.find_all('td')
  data.append(td)

for ele in data:
  e = Entry()
  e.get_character(ele[2].find(class_='Hani').text)
  #this is not working.......por why
  e.get_qwerty(ele[1].text[1:-1])
  # print(e)
  e.get_radicals(ele[0].text)
  e.get_level(len(e.radicals))
  e.get_link(hrefHead, ele[2].find('a')['href'])
  entries.append(e)
pp(entries[0].__dict__)


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
  

