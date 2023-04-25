'''defines Entry class objects.

EXAMPLE: 

character -> '暧'
qwerty -> 'ABBE'
radicals -> ['日','月','月','水']
link -> 'https://en.wiktionary.org/wiki/%E6%9A%A7'
level -> 4
doubled -> True (another entry shares qwerty and radical values)

use getters to populate entry. No setters since...this data is more or less static


might combine with constants.py to minimize imports
'''

class Entry: 
  def __init__(self):
    self.character = ''
    self.qwerty = ''
    self.radicals = []
    self.link = ''
    self.level = 0
    self.doubled = False
  
  
  def get_character(self,string):
    self.character = string

  def get_qwerty(self, string):
    self.qwerty = string
  
  def get_radicals(self, string):
    self.radicals = list(string)

  def get_link(self, head, link):
    self.link = head + link

  def get_level(self, number):
    self.level = number

  def get_doubled(self, boolean):
    self.doubled = boolean

  entryURL = 'https://en.wiktionary.org/wiki/Appendix:Chinese_Cangjie'

  hrefHead = 'https://en.wiktionary.org'

  rads = {
        "A":"日", "B":"月", "C":"金", "D":"木",
        "E":"水", "F":"火", "G":"土", "H":"竹",
        "I":"戈", "J":"十", "K":"大", "L":"中",
        "M":"一", "N":"弓", "O":"人", "P":"心",
        "Q":"手", "R":"口", "S":"尸", "T":"廿",
        "U":"山", "V":"女", "W":"田", "X":"難",
        "Y":"卜", "Z":"重"
    }
