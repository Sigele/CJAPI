from bs4 import BeautifulSoup
import requests
import re

urls = requests.get('https://en.wiktionary.org/wiki/Appendix:Chinese_Cangjie').text


# need to loop through all <a> elements within <span> with class Zyyyy

url_soup = BeautifulSoup(urls, 'lxml')
span = url_soup.find(class_="Zyyy")
urls = span.contents
print(urls)
print(url_soup.find_all(href=re.compile('/wiki/Appendix:Chinese_Cangjie/')))