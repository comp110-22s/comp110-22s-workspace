"""EX01 - Chardle - A cute step toward Wordle."""

___author___ = "730405989"

key_word: str = str(input("Enter a 5-character word: "))

if len(key_word) != 5:
    print("ERROR, WORD INPUT IS NOT 5 CHARACTERS IN LENGTH.")
    exit()

if not key_word.isalpha():
    print("ERROR, INPUT IS NOT ALL LETTERS.")
    exit()
key_letter: str = str(input("Enter a single character: "))

searching_statement: str = "Searching for " + key_letter + " in " + key_word
if not key_letter.isalpha():
    print("ERROR, INPUT IS NOT A LETTERS.")
    exit()

if len(key_letter) != 1:
    print("ERROR, CHARACTER INPUT IS  ONE CHARACTER IN LENGTH.")
    exit()
else:
    print(searching_statement)
    if ord(key_letter) == ord(key_word[0]):
        index_zero = 1
        print(key_letter + " found at index 0")
    else: 
        index_zero = int(0)
    if ord(key_letter) == ord(key_word[1]):
        index_one = int(1)
        print(key_letter + " found at index 1")
    else: 
        index_one = int(0)
    if ord(key_letter) == ord(key_word[2]):
        index_two = int(1)
        print(key_letter + " found at index 2")
    else: 
        index_two = int(0)
    if ord(key_letter) == ord(key_word[3]):
        index_three = int(1)
        print(key_letter + " found at index 3")
    else: 
        index_three = int(0)
    if ord(key_letter) == ord(key_word[4]):
        index_four = int(1)
        print(key_letter + " found at index 4")
    else: 
        index_four = int(0)
number_instances: int = int(index_one + index_two + index_three + index_zero + index_four)
if number_instances == 0: 
    print("No instances of " + key_letter + " found in " + key_word)
else:
    if number_instances == 1:
        print("1 instance of " + key_letter + " found in " + key_word)
    else:
        print(str(number_instances) + " instances of " + key_letter + " found in " + key_word)