"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730465187"

selected_word: str = str(input("Enter a 5-character word: "))
selected_word_length = len(selected_word)


if selected_word_length != 5:
    print("Error: Word must contain 5 characters")
    exit()


character: str = str(input("Enter a single character: "))
character_length = len(character)

if character_length == 1:
    print("Searching for", character, "in", selected_word)
else:
    print("Error: Character must be a single character")
    exit()

character_instances = 0

if selected_word[0] == character:
    print(character, "found at index 0")
    character_instances = character_instances + 1

if selected_word[1] == character:
    print(character, "found at index 1")
    character_instances = character_instances + 1

if selected_word[2] == character:
    print(character, "found at index 2")
    character_instances = character_instances + 1

if selected_word[3] == character:
    print(character, "found at index 3")
    character_instances = character_instances + 1

if selected_word[4] == character:
    print(character, "found at index 4")
    character_instances = character_instances + 1

if character_instances == 0:
    print("No instances of", character, "found in", selected_word)
else:
    if character_instances == 1:
        print(character_instances, "instance of", character, "found in", selected_word)
    else:
        print(character_instances, "instances of", character, "found in", selected_word)