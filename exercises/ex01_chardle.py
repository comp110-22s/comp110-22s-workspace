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

if usercharacter == userword[0]:
    print(usercharacter + " found at index 0")
if usercharacter == userword[1]:
    print(usercharacter + " found at index 1")
if usercharacter == userword[2]:
    print(usercharacter + " found at index 2")
if usercharacter == userword[3]:
    print(usercharacter + " found at index 3")
if usercharacter == userword[4]:
    print(usercharacter + " found at index 4")

x = int(userword.count(usercharacter))
if x > 1:
    print("{0} instances of ".format(x) + usercharacter + " found in " + userword)
if x <= 1:
    print("{0} instance of ".format(x) + usercharacter + " found in " + userword)