from bs4 import BeautifulSoup
import requests
import re

entryURL = 'https://en.wiktionary.org/wiki/Appendix:Chinese_Cangjie'
urls = requests.get(entryURL).text


# need to loop through all <a> elements within <span> with class Zyyyy

url_soup = BeautifulSoup(urls, 'lxml')
span = url_soup.find(class_="Zyyy")
urls = span.find_all('a')
print(len(urls))
radData = []
for url in urls:
    radData.append(entryURL + '/' + url.text)

print(radData)
    
