import unittest
import re
from constants import *
from entryClass import Entry

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
        
        # ensure length less than 5

if __name__ == '__main__':
    unittest.main()