import os
from bs4 import BeautifulSoup
#only reading html from test file

with open('test.html', 'r') as html_file:
  content = html_file.read()
  print(content)
#create BS instance
  soup = BeautifulSoup(content, 'lxml')
  
  #find_all returns list of all matching elements
  tags = soup.find_all('text')

  for tag in tags:
    print(tag.text)
  print(tags)