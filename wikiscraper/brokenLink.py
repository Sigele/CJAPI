# debugging broken/nonexistent link edge case


#using testURL for manual testing

'''
broken/nonexistent links are identified in 2 ways:
  the "title" attribute includes "(page does not exist)"
  the "href" string ends with "redLink=1"
'''

# the 3rd TD element in a list of 3 (created by getEntries) will contain a title attribute.
#if the title attribute is longer than a single character, that means it contains a message that the link is broken.
def brokenLinkCheck(listOf3Elements):
  if len(listOf3Elements[2].find('a')['title']) > 1:
    return True
  
