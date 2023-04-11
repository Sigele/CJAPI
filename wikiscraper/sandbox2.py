#importing bs4, requests module, regex module

from bs4 import BeautifulSoup
import requests
import re

from radLinks import URLgrab
from charGrab import charGrab
#grab all URLS

radEntry = 'https://en.wiktionary.org/wiki/Appendix:Chinese_Cangjie'
data = []

links = URLgrab(radEntry)

# DONE.
for link in links:
    data.append(charGrab(link));
print(data)
#for each URL, parse for characters

#DONE, but the Cyrillic bug is back :( might have to write a custom func since it's an edge case

