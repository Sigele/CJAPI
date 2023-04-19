import unittest
from sandbox2 import *

# inheriting from unittest.TestCase is standard

# basic example from python docs

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

class Test_basic(unittest.TestCase):
  def test_constants(self):
      self.assertEqual(hrefHead, 'https://en.wiktionary.org')
      self.assertIsInstance(testURL, str)

if __name__ == '__main__':
    unittest.main()