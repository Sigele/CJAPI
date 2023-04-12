from bs4 import BeautifulSoup
import re
import requests

class Entry: 
  def __init__(self):
    self.character = ''
    self.qwerty = ''
    self.radicals = []
    self.link = ''
    self.level = 0
  
  def get_character(self,string):
    self.character = string

  def get_qwerty(self, string):
    self.qwerty = ''

  def get_radicals(self, string):
    self.radicals = list(string)

  def get_link(self, head, link):
    self.link = head + link

  def get_level(self):
    self.level = len(self.qwerty)

# test page: fire radical
# URLS are incomplete, need to concat hrefHead
testURL = 'https://en.wiktionary.org/wiki/Appendix:Chinese_Cangjie/%E7%81%AB'
hrefHead = 'https://en.wiktionary.org'
html_text = requests.get(testURL).text

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

tableSoup = BeautifulSoup(html_text, 'lxml')
data = []
tr = tableSoup.find_all('tr')
for line in tr:
  data = line.find_all('td')

  rads = data[0].text
  qwerty = data[1].text
  name = line.find(class_='Hani').text
  link = hrefHead + line.find('a')['href']
  print(name, rads, qwerty, link)

  #FLY IN THE OINTMENT:
  # some of the entries have 2 or more characters that can be typed with a single input method; the only real way to account for that is to make an entry for each idx of the text, with the same values for rads and qwerty

  #in those cases I also need to account for the fact that there are 2 links by using find_all instead of find, but like. PROGRESS



    
    


