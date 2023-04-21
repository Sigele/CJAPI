from entryClass import Entry
from brokenLink import brokenLinkCheck
from constants import *

def dblEntryCheck(three_tds):

    result = []
    
    if len(three_tds[2].find(class_='Hani').text) > 2:
      names = three_tds[2].find_all('a')
      for name in names:
         e2 = Entry()
         e2.get_character(name.text)
         e2.get_qwerty(three_tds[1].text[1:-1])
         e2.get_radicals(three_tds[0].text)
         e2.get_level(len(e2.radicals))
         #broken link SC: print data 21:31
         if(brokenLinkCheck(three_tds) == True):
            e2.get_link('Sorry, ', 'the link is missing!')
         else: 
            e2.get_link(hrefHead, name['href'])
         e2.get_doubled(True)
         result.append(e2)   
    if (len(result) == 0): return
    return result;