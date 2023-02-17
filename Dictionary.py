import json
from difflib import get_close_matches

data = json.load(open('words.json'))
  
# translate the word in lowercase, since all the words in json file is in lower case.
word = input('Enter a word: ').lower()
    
# give three possible words similar to wrong input
possible = get_close_matches(word, data.keys())
      
