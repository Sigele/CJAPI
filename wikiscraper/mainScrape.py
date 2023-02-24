#combining functionality of mainPage and radLinks files.

from bs4 import BeautifulSoup
import requests
import re

from radLinks import URLgrab
from mainPage import charGrab

#grab the page itself
#grab each subpage from urls
#grab chars in each subpage

entryURL = 'https://en.wiktionary.org/wiki/Appendix:Chinese_Cangjie'

entryGrab = URLgrab(entryURL)

masterList = []

for subGrabs in entryGrab:
  masterList.append(URLgrab(subGrabs))

print(len(masterList))