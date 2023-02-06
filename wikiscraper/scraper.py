import os
from bs4 import BeautifulSoup
#only reading html from test file

with open('test.html', 'r') as html_file:
  content = html_file.read()
  print(content)