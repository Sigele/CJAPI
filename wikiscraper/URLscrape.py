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
data = []
for url in urls:
    data.append(entryURL + '/' + url.text)

print(data)
    
# print(url_soup.find_all(href=re.compile('/wiki/Appendix:Chinese_Cangjie/')))