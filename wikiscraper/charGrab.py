#Notes:
# - need to implement scrape for ALL radical pages-- requests.get while parsing html for sub urls?
# - subURLS under href are incomplete, may need to concat within get requests.get


from bs4 import BeautifulSoup
import requests
import re

# html_text points to 'sun' radical only
# request.get returns status code without text method
html_text = requests.get('https://en.wiktionary.org/wiki/Appendix:Chinese_Cangjie/%E6%97%A5').text

soup = BeautifulSoup(html_text, 'lxml')
chars = soup.find_all('a', href=re.compile('/wiki/%'))
#this was a test to see how to 'grab' text only from elements. saving for reference.
# for char in chars:
#   char_name = char.text
#   char_page = char['href']


# edge case for uneeded links. returns list of HTML elements
for char in chars:
  if char.find('lang') != -1:
    chars.remove(char)
    # print(char.text)
  
def charGrab(url):
  # define list to hold char text
  charText = []
  # make soup
  html_text = requests.get(url).text
  soup = BeautifulSoup(html_text, 'lxml')
  chars = soup.find_all('a', href=re.compile('/wiki/%'))

  for char in chars:
    if char.find('lang') != -1:
      chars.remove(char)
      charText.append(char.text)
  return charText


print(charGrab('https://en.wiktionary.org/wiki/Appendix:Chinese_Cangjie/%E6%97%A5'))

# this is working for the plain text of individual characters, but I need the rest of the data, i.e. separate functionality for scraping those strings as well as the link itself. Might be able to repurpose code in indvScrape.