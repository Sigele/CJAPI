import requests
#these values never change and are accessible everywhere. DO NOT use for tests; import from subject file only to avoid ref conflicts

entryURL = 'https://en.wiktionary.org/wiki/Appendix:Chinese_Cangjie';

hrefHead = 'https://en.wiktionary.org'

def radMap(input):
  rads = {
        "A":"日", "B":"月", "C":"金", "D":"木",
        "E":"水", "F":"火", "G":"土", "H":"竹",
        "I":"戈", "J":"十", "K":"大", "L":"中",
        "M":"一", "N":"弓", "O":"人", "P":"心",
        "Q":"手", "R":"口", "S":"尸", "T":"廿",
        "U":"山", "V":"女", "W":"田", "X":"難",
        "Y":"卜", "Z":"重"
    }
  
  u_input = input.upper()
  def get_key(val):
    for key, value in rads.items():
        if val == value:
          # print(key)
          return str(key)
        elif val == key:
          #  print(value)
           return str(value)
    return "not found :("
    
  get_key(u_input)

qty = "RBBE"
letRad = [
            "口",
            "月",
            "月",
            "水"
            ]
letMap = []
 

