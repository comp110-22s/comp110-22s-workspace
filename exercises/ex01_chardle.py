"""EX01 - Chardle exercise."""

__author__ = "730466987"

user_chosen_word: str = input("Enter a 5-character word: ")
user_chosen_character: str = input("Enter a single character: ")
user_character_copies: int = 0
print("Searching for " + user_chosen_character + " in " + user_chosen_word)


# pt. 4!!

if len(user_chosen_word) != 5:
    print("Error: Word must contain 5 characters")
    quit()

if len(user_chosen_character) != 1:
    print("Error: Character must be a single character")
    quit()

# End of section for pt. 4!!

# These if statements combine 2 different tasks: tracking which indices particular characters appear in,
# AND counting how many times they appear in each of them.
# These values later add up to be the # of copies of the character.

if user_chosen_character == user_chosen_word[0]:
    print(user_chosen_character + " found at index 0")
    user_character_copies = user_character_copies + 1

# So now, there is 1 copy of the character, since we started with 0 copies.

if user_chosen_character == user_chosen_word[1]:
    print(user_chosen_character + " found at index 1")
    user_character_copies = user_character_copies + 1

# Now, there are 2 copies, since the computer added 1 to the PREVIOUS value of user_character_copies, not just the initial one.

if user_chosen_character == user_chosen_word[2]:
    print(user_chosen_character + " found at index 2")
    user_character_copies = user_character_copies + 1

# 2 + 1 = 3 copies

if user_chosen_character == user_chosen_word[3]:
    print(user_chosen_character + " found at index 3")
    user_character_copies = user_character_copies + 1

# 3 + 1 = 4 copies

if user_chosen_character == user_chosen_word[4]:
    print(user_chosen_character + " found at index 4")
    user_character_copies = user_character_copies + 1

# 4 + 1 = 5 copies

# Now that the program has counted how many copies of the input character there are,
# it uses that value to pick one of the following if statements.

# Remember that after the program goes through 1 if statement, if none of the other if statements are applicable to
# the number of copies of the character, then they won't be read and the program will stop on its own.

if user_character_copies == 0:
    print("No instances of " + user_chosen_character + " found in " + user_chosen_word)

if user_character_copies == 1:
    print("1 instance of " + user_chosen_character + " found in " + user_chosen_word)

if user_character_copies >= 2:
    print(str(user_character_copies) + " instances of " + user_chosen_character + " found in " + user_chosen_word)

# Here, the str command is used to change the int value of user_character_copies into a str,
# which allows it to be combined with the other strs in this print command, regardless of if there are 2, 3, 4, or 5 copies
# of the character in the word.