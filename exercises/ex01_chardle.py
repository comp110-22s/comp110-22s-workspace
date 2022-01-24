"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730488349"

five_letter_word = input("Enter a 5-character word: ")

if len(five_letter_word) <= 4:
    print("Error: Word must contain 5 characters")
    exit()
if len(five_letter_word) >= 6:
    print("Error: Word must contain 5 characters")
    exit()

single_character = input("Enter a single character: ")

if len(single_character) <=0:
    print("Error: Character must be a single character.")
    exit()
if len(single_character) >=2:
    print ("Error: Character must be a single character.")
    exit()

instances_found  = 0 

if single_character in five_letter_word:
    print ("Searching for " + single_character + " in " + five_letter_word)
else:
    print ("No instances of " + single_character + " found in " + five_letter_word)
    exit()

if single_character == five_letter_word[0]:
    print (single_character + " found at index 0 ")
    instances_found += 1
    
if single_character == five_letter_word[1]:
    print (single_character + " found at index 1 ")
    instances_found += 1

if single_character == five_letter_word[2]:
    print (single_character + " found at index 2 ")
    instances_found += 1

if single_character == five_letter_word[3]:
    print (single_character + " found at index 3 ")
    instances_found += 1

if single_character == five_letter_word[4]:
    print (single_character + " found at index 4 ")
    instances_found += 1

if instances_found > 1:
    print (instances_found, "instances of", single_character, "found in", five_letter_word)
if instances_found == 1:
    print (instances_found, "instance of", single_character, "found in", five_letter_word)