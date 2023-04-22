import unittest
from secondScrape import *
from constants import *

# check constants
# check val returned by get entries //list of 3 idx sublists
# check val returned dblEntryCheck  //list of entry class objects
# check return val populate // null
# check return val broken link //boolean
# check type entry 

class Test_basic(unittest.TestCase):
  def test_URL(self):
      self.assertIsInstance(testURL, str)
  def test_href(self):
     self.assertEqual(hrefHead, 'https://en.wiktionary.org')
  def test_html(self):
     self.assertIsInstance(html_text, str)
  def test_soup(self):
     self.assertTrue(isinstance(soup, BeautifulSoup))
     

if __name__ == '__main__':
    unittest.main()