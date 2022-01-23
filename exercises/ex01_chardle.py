"""EX01 - Chardle - A cute step toward Wordle"""

__author__ = "730486473"

userword = input("Enter a 5-character word: ")
if len(userword) != 5:
    print("Error: Word must contain 5 characters")   
    exit()

usercharacter = input("Enter a single character: ")
if len(usercharacter) != 1:
    print("Error: Character must be a single character")
    exit()

print("Searching for " + usercharacter + " in " + userword)

new_word = str(userword + usercharacter)

if usercharacter == new_word[0]:
    print(usercharacter + " found at index 0")
if usercharacter == new_word[1]:
    print(usercharacter + " found at index 1")
if usercharacter == new_word[2]:
    print(usercharacter + " found at index 2")
if usercharacter == new_word[3]:
    print(usercharacter + " found at index 3")
if usercharacter == new_word[4]:
    print(usercharacter + " found at index 4")
if usercharacter == new_word[5]:
    print("No instances of " + usercharacter + " found in " + userword)
    exit()

x = int(userword.count(usercharacter))
print("{0} instances of ".format(x) + usercharacter)