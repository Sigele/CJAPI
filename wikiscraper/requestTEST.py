#Notes:
# - need to implement scrape for ALL radical pages-- requests.get while parsing html for sub urls?
# - subURLS under href are incomplete, may need to concat within get requests.get
# - need to be able to filter results, either with character code or more specific attrs

from bs4 import BeautifulSoup
import requests
import re

# html_text points to 'sun' radical only
# request.get returns status code without text method
html_text = requests.get('https://en.wiktionary.org/wiki/Appendix:Chinese_Cangjie/%E6%97%A5').text

soup = BeautifulSoup(html_text, 'lxml')
chars = soup.find_all('a', href=re.compile('/wiki/%'))
for char in chars:
  char_name = char.text
  print(char_name)
