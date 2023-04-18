from sandbox2 import *
from getEntries import hrefHead
import unittest

def test_entry(entry):
    assert type(entry.character) == 'str'
    assert type(entry.qwerty) =='str'
    assert type(entry.radicals) == 'list'
    assert type(entry.link) == "string"
    assert (entry.link.find(hrefHead) != -1 or entry.link.find("Sorry") != -1)
    assert type(entry.level) == 'int' 

item = data[0]

print(type(item.character))
# if __name__ == "__main__":
#     test_entry(item)
#     print("Everything passed")

