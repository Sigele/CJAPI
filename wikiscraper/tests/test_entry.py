# import sys
# sys.path.insert(1, '/CS/Codesmith/SoloProject/REFACTORED/wikiscraper')

import unittest
import re
from wikiscraper.constants import *
from wikiscraper.entryClass import Entry




class TestEntry(unittest.TestCase):

    def setUp(self):
        self.e_1 = Entry()


    def test_character(self):
        #ensure character is CJK ideograph
        self.e_1.get_character('鱼')
        self.assertTrue(re.search(u'[\u4e00-\u9fff]',self.e_1.character), 'character should be CJK ideograph')
        self.e_1.get_character('t')
        self.assertTrue(re.search(u'[\u4e00-\u9fff]', self.e_1.character) != True, 'character should be CJK ideograph')
        # ensure is singular character
        self.assertTrue(len(self.e_1.character) == 1, 'character prop should have length of 1')

    def test_qwerty(self):
        # ensure type string
        self.e_1.get_qwerty(['A','W','S'])
        self.assertNotIsInstance(self.e_1.qwerty, str)

        self.e_1.get_qwerty('AWS')
        self.assertIsInstance(self.e_1.qwerty, str, '"qwerty" property should be type str')
        # ensure only A-Z characters
        self.assertTrue(re.compile(r'^[A-Z]+$').match(self.e_1.qwerty), 'str should contain only characters A-Z, case sensitive')
        # ensure length less than 6
        self.assertTrue(len(self.e_1.qwerty) < 6, 'qwerty input string should be 5 characters or less')

    def test_radicals(self):
        # radicals should be a list of single character strings
        self.e_1.get_radicals(
            [
            "口",
            "月",
            "月",
            "水"
            ])
        
        self.assertIsInstance(self.e_1.radicals, list, '"radicals" should be a list')
        for char in self.e_1.radicals:
            self.assertIsInstance(char, str)
            self.assertTrue(len(char) == 1, 'each radical list element should be a single character')

        # radicals should be CJK values only
            self.assertTrue(re.search(u'[\u4e00-\u9fff]',char), 'each character in "radicals" should be CJK ideograph')

        # radicals length should match qwerty length
        self.e_1.get_qwerty("RBBE")
        self.assertEqual(len(self.e_1.qwerty), len(self.e_1.radicals))

        # radicals should map to qwerty exactly
        testMap = []
        for char in self.e_1.qwerty:
            testMap.append(rads[char])
        counter = 0
        for ele in testMap:
            self.assertEqual(ele, self.e_1.radicals[counter])
            counter += 1

    def test_link(self):
    #     # all links should go to wiktionary
        self.e_1.get_link(hrefHead,"/wiki/%E4%A8%9C")
        print(self.e_1.link)
        self.assertTrue(self.e_1.link.find(hrefHead))
    #     # link must not be broken
    #     # should be a string

    # def test_level(self):
    #     # level should be a number
    #     # level should equal length of qwerty and/or radicals

    # def test_doubled(self):
    #     # should be a boolean value
    #     # cannot be null
if __name__ == '__main__':
    unittest.main()