import json
from difflib import get_close_matches

# reading the json file containing words and its meaning
data = json.load(open('words.json'))

#function 1
def displayWords():
    letter = input("Enter a letter from a-z: ")
    for i in data:
        if i.startswith(letter):
            print(i)

#function 2:
def specificWord():
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
    
#function 3
def specificNumber():
    num = int(input("Enter number of length of the word: "))
    found = False
    for key in data:
        if len(key)==num:
            print(key)
            found = True
    if found == False:
        print("No words with specific length")

#function 4
def addWord():
    word = input("Enter the word you want to add: ").lower()
    if word in data:
        print("{} is already in the dictionary. \nIf you wish to update the meaning, press 3.".format(word))
    else:
        meaning = input("Enter the meaning of {}: ".format(word))
        data[word] = meaning
        print("The word added successfully!")

#function 5
def addMeaning():
    word = input("Enter the word you want to update: ").lower()
    if word in data:
        meaning = input("Enter the meaning of {}: ".format(word))
        data[word] = meaning
        print("The word added successfully!")
        
    else:
        print("{} is not in the dictionary. \nIf you wish to add the word, press 2.".format(word))

#Choices
while True:
    try:
        print("""
=========================================================
                  D I C T I O N A R Y
=========================================================
1. Display the words starts with a specific letter
2. Find specific word and its meaning
3. Search and display words by given value of letters
4. Add a word to the dictionary
5. Update meaning of the word in the dictionary
6. Exit
=========================================================
        """)
        choice = int(input("What you want to do (1-4): "))
        if choice == 1:
            displayWords()
        elif choice == 2:
            specificWord()
        elif choice == 3:
            specificNumber()
        elif choice == 4:
            addWord()
        elif choice == 5:
            addMeaning()
        elif choice == 6:
            break
        else:
            print("Invalid input! Enter number from 1-4: ")

    except:
        print("Invalid input")
