#THIS function has NOT been consolidated into secondScrape

#some ideographs share the same qwerty inputs and radicals. On wiktionary these are stored inside the same HTML element, but with current populating func only the first would be caught. This function returns completed entries for all chars that fit this edge case in a list.


from entryClass import Entry
from brokenLink import brokenLinkCheck
# from constants import *
from entryClass import *

def dblEntryCheck(three_tds):

    result = []
    
    #if the 3rd TD element (where character txt is stored) returns more than one 'Hani' class element, we know there are doubled entries
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
            e2.get_link(Entry.hrefHead, name['href'])
         e2.get_doubled(True)
         result.append(e2)   

    #not sure what this conditional is testing for? Seems like this check should happen before the function block is even entered     
    if (len(result) == 0): return
    return result;