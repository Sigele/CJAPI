import json

dict = {
    "character": "火",
    "qwerty": "F",
    "radicals": "火",
    "level": 1
}

outfile = open("wikiscraper/writetest.json", "w")
json.dump(dict, outfile, ensure_ascii=False,indent = 4)
outfile.close()

# json_obj = json.dump(dict, ensure_ascii=True)

# with open("wikiscraper/writetest.json", "w", encoding="utf-16") as outfile:
#     outfile.write(json_obj)
#     outfile.flush()
#     print('write successful')

