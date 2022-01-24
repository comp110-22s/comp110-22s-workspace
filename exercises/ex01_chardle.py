"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730474722"

"""prompting for inputs"""
word: str = input("Enter a 5-character word: ")
if len(word) > 5:
    print("Error: Word must contain 5 characters")
    exit()
if len(word) < 5:
    print("Error: Word must contain 5 characters")
    exit()
character: str = input("Enter a single character: ")
if len(character) > 1:
    print("Error: Character must be a single character.")
    exit()
if len(character) < 1:
    print("Error: Character must be a single character.")
    exit()

"""exiting for invalid inputs"""

"""prompting for inputs continued"""
print("Searching for " + character + " in " + word)
match_maker = word.find(character, 0, 4)
if match_maker == 0:
    print(character, "found at index 0")

'''checking indices for matches'''
match_maker = word.find(character, 1, 4)
if match_maker == 1:
    print(character, "found at index 1")
match_maker = word.find(character, 2, 4)
if match_maker == 2: 
    print(character, "found at index 2")
match_maker = word.find(character, 3, 4)
if match_maker == 3:
    print(character, "found at index 3")
match_maker = word.find(character, 4, 5)
if match_maker == 4:
    print(character, "found at index 4")

"""counting matching indices"""
count: int = word.count(character)
if count == 0:
    print("No instances of", character, "found in", word)
else: 
    if count == 1:
        print(count, "instance of", character, "found in", word)
    else:
        if count > 1:
            print(count, "instances of", character, "found in", word)
