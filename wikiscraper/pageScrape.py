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
  'dictLink': '',
  'altLinks': []
}

# methods for grabbing each entry
