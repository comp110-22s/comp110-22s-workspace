""" Example Excercise of Input, Variables, and Conditions """
__author__ = "730396857" 
input_word: str = input("Enter a 5-charcater word: ")
if len(input_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
character: str = input("Enter a single character: ")
count: int = 0
if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + character + " in " + input_word)
if character == input_word[0]:
    print(character + " found at index 0 ")
    count += 1
if character == input_word[1]:
    print(character + " found at index 1")
    count += 1
if character == input_word[2]:
    print(character + " found at index 2")
    count += 1
if character == input_word[3]:
    print(character + " found at index 3")
    count += 1
if character == input_word[4]:
    print(character + " found at index 4")
    count += 1
if count == 0:
    print("No instances of " + character + " found in " + input_word)
else:
    print(str(count) + " instances of " + character + " found in " + input_word)
