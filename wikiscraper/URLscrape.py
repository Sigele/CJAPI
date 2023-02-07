from bs4 import BeautifulSoup
import requests

urls = requests.get('https://en.wiktionary.org/wiki/Appendix:Chinese_Cangjie').text


# need to loop through all <a> elements within <span> with class Zyyyy

url_soup = BeautifulSoup(urls, 'lxml')


print(url_soup.span.a)
urls_text = url_soup.find_all('a')
for link in urls_text:
  print(link.get('href'))
