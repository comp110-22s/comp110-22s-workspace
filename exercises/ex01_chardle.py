"""EX01 - Chardle - A cute step toward Worldle."""

__author__ = "730472535"

magic_word = input(str("Enter a 5-character word: "))
if len(magic_word) == 5:
    guess = input(str("Enter a single character: "))
    if len(guess) == 1:
        print("Searching for " + guess + " in " + magic_word)
    else:
        print("Error: Character must be a single character")
        exit()
else:
    print("Error: word must contain 5 charcters")
    exit()

instance = 0

if guess == magic_word[0]:
    print(guess + " found at index 0")
    instance = instance + 1
if guess == magic_word[1]:
    print(guess + " found at index 1")
    instance = instance + 1
if guess == magic_word[2]:
    print(guess + " found at index 2")
    instance = instance + 1
if guess == magic_word[3]:
    print(guess + " found at index 3")
    instance = instance + 1
if guess == magic_word[4]:
    print(guess + " found at index 4")
    instance = instance + 1

if instance == 0:
    print("No instances of " + guess + " found in " + magic_word)
else:
    if instance == 1:
        print("1 instance of " + guess + " found in " + magic_word)
    else:
        print(str(instance) + " instances of " + guess + " found in " + magic_word)


    