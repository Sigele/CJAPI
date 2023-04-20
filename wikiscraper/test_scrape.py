import unittest
from sandbox2 import *


# class TestSandbox2 (unittest.TestCase):

#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')

#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())

#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

# if __name__ == '__main__':
#     unittest.main()

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