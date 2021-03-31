import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json", "r"))

def translate(w):
    w= w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("did you mean %s instead Y/N ? " % get_close_matches(w, data.keys())[0])
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        else:
            return "Check the word"
    else:
        return "the word doesn't exist"


word = input("enter a word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)