"""EX01 - Chardle - A cute step towards Wordle."""
__author__ = "730472840"

word: str = input("Enter a 5-character word: ")

if len(word) < 5:
    print("Error: Word must contain 5 characters")
    exit()
if len(word) > 5:
    print("Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ")

if len(character) < 1:
    print("Error: Character must be a single character.")
    exit()

if len(character) > 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + character + " in " + word)
matching_characters: int = 0

if character == word[0]:
    print(character + " found at index 0")
    matching_characters = matching_characters + 1

if character == word[1]:
    print(character + " found at index 1")
    matching_characters = matching_characters + 1

if character == word[2]:
    print(character + " found at index 2")
    matching_characters = matching_characters + 1

if character == word[3]:
    print(character + " found at index 3")
    matching_characters = matching_characters + 1

if character == word[4]:
    print(character + " found at index 4")
    matching_characters = matching_characters + 1


if matching_characters == 1:
    print(str(matching_characters) + " instance of " + character + " found in " + word)

if matching_characters == 0:
    print("No instances of " + character + " found in " + word)

if matching_characters > 1:
    print(str(matching_characters) + " instances of " + character + " found in " + word)














