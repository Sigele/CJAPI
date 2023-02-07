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

  #within table (tbody):
  #tr, td, b displays radical input
  #tr, td (2nd) contains QWERTY input
  #tr, td (3rd), span, a "title" gives char output

  #trs dont have any class or other atributes...this is the best I can do
  #to find by class: class_="examplestring" as 2nd arg
  entries = soup.find_all('tr')
  for entry in entries: 
    rad_input = entry.td.b
    #not sure about this one...still no classes
    qwerty_input = entry.td.text
    characters = entry.td.span.a.text
