#searches a list for objects meeting provided criteria. This is for debugging purposes ONLY!

import re
import requests
from pprint import pprint as pp


def search(list, crit, str):
  for entry in list: 
      if (getattr(entry, crit) == str):
         return entry
  return "not found :("
# print(len(entries))      

# result = search(entries, 'qwerty', 'FAM')
# print(result.character)

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

#code below alters pythonpath to allow modules from parent folder to be imported into subfolders. Python is silly.

# export PYTHONPATH="${PYTHONPATH}:/Users/user/Desktop/CS/Codesmith/SoloProject/REFACTORED/wikiscraper/"