#combining functionality of mainPage and radLinks files.

from bs4 import BeautifulSoup
import requests
import re

from radLinks import URLgrab
from mainPage import charGrab

#charGrab accepts a URL and returns a list of all the Chinese characters within that page which link to subpages.
#URLgrab accepts a URL and returns a list of URLs that link to new pages

# 1: at main page, grab links to all radical subpages.
# 2: on each radical subpage:
#   grab all characters
#    grab their associated URLS

# this poses the question: wouldn't make more sense to grab both within the same logic to avoid errors and edge cases? This would also make adding DB entries much more efficient

entryURL = 'https://en.wiktionary.org/wiki/Appendix:Chinese_Cangjie'

entryGrab = URLgrab(entryURL)

masterList = []

for subGrabs in entryGrab:
  masterList.append(URLgrab(subGrabs))

print(len(masterList))