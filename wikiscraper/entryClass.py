class Entry: 
  def __init__(self):
    self.character = ''
    self.qwerty = ''
    self.radicals = []
    self.link = ''
    self.level = 0
  
  def get_character(self,string):
    self.character = string

  def get_qwerty(self, string):
    self.qwerty = string

  def get_radicals(self, string):
    self.radicals = list(string)

  def get_link(self, head, link):
    self.link = head + link

  def get_level(self):
    self.level = len(self.qwerty)