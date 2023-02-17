import json
from difflib import get_close_matches

data = json.load(open('words.json'))
  
# translate the word in lowercase, since all the words in json file is in lower case.
word = input('Enter a word: ').lower()
    
# give three possible words similar to wrong input
similar = get_close_matches(word, data.keys())
      
def translate(possible):
    if possible in data:
        return data[possible]
    elif len(similar) > 0:
        suggested = input(f"word not found! try these {similar}: ").lower() #translate input in lowercase
        return data[suggested]
    else:
        return "Word doesn't exist!"

print(translate(word))