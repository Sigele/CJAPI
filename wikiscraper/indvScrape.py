"""
What do I need from each page?

1. character string itself
2. QWERTY input string, all caps...probably needs to become an array later
3. radicals, if any
4. definition
5. link to wiktionary page
6. link to related/alternate characters, if any
* stretch: img breakdown of char construction, if any 


"""
from bs4 import BeautifulSoup
import re
import requests

# FOR NOW (2/24), pageScrape returns an object containing all the important properties of the chinese character page at a given url.
# charGrab needs to be modified for this function to work as intended
# the returned object is a mock DB entry
entry = {
  'name': '',
  'QWERTY': '',
  'radicals': [],
  'definition': '',
  'altLinks': []
}

#test page： 蟒 (python :))
testURL = 'https://en.wiktionary.org/wiki/%E8%9F%92'
# methods for grabbing each entry
# currently creates a list of all characters on a radical page.
radicalMap = {
  'A':'日', 'B': '月',
  'C': '金','D': '木',
  'E': '水','F': '火',
  'G': '土','H': '竹',
  'I': '戈','J': '十',
  'K': '大','L': '中',
  'M': '一','N': '弓',
  'O': '人','P': '心',
  'Q': '手','R': '口',
  'S': '尸','T': '廿',
  'U': '山','V': '女',
  'W': '田','Y': '卜',
  'X': '難'

}

for key in radicalMap:
  print(radicalMap[key])
def grabEntry(url):
  # define list to hold char text
  returnEntry = entry
  print(returnEntry)
  # make soup
  html_text = requests.get(url).text
  soup = BeautifulSoup(html_text, 'lxml')

  #grab character itself
  entry['name'] = soup.find('span', 'Hani').text

  #qwerty input string
  entry['QWERTY'] = soup.find('a', 'mw-redirect').text

  #grab radicals, turn into set/array thingy
  entry['radicals'] = []
  for key in entry['QWERTY']:
    entry['radicals'].append(radicalMap[key])
  altLinks = soup.find_all('a','disambig-see-also')
  print(altLinks)
  # entry['definition'] = soup.find('li','mw-body-content').text
  # for char in chars:
  #   if char.find('lang') != -1:
  #     chars.remove(char)
  #     charText.append(char.text)
  # return charText

  return returnEntry

print(grabEntry(testURL))