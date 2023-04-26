import unittest
from secondScrape import *
# from constants import *
from entryClass import *

# check constants
# check val returned by get entries //list of 3 idx sublists
# check val returned dblEntryCheck  //list of entry class objects
# check return val populate // null
# check return val broken link //boolean
# check type entry 

class Test_scrape(unittest.TestCase):
  def test_URL(self):
      self.assertIsInstance(testURL, str)
  def test_href(self):
     self.assertEqual(Entry.hrefHead, 'https://en.wiktionary.org')
  def test_html(self):
     self.assertIsInstance(html_text, str)
  def test_soup(self):
     self.assertTrue(isinstance(soup, BeautifulSoup))


   #def test_getEntries(self):
      # should return a list
      # list length should be over 1000
      # each element in list should have length of 3
      # each element should (probably) be type BeautifulSoup

   #def test_populate(self):
      #after running on with a list of TD elements, should populate prev declared list with entry class objects 

   #def test_dblEntry
      #not really sure how to test this
     
if __name__ == '__main__':
    unittest.main()