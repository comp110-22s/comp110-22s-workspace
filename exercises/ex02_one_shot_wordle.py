"""EX02 - One shot Wordle exercise."""

__author__ = "730466987"

secret_word: str = "python"
i: int = 0
user_guess: str = input(f"What is your {len(secret_word)} letter guess? ")

while len(user_guess) != len(secret_word):
    user_guess = input(f"That was not {len(secret_word)} letters! Try again: ")
    i = i + 1

# This command will be able to do 2 things at once: it will check the length of the user guess compared to the secret word REGARDLESS
# of how long the secret word is, and it will get the user out of the error loop if they put in a guess the correct length, so
# if they guess "python" at guess 3, they can get out of it and have their guiess evaluated by the yes/no responses below.

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

guess_index: int = 0
emoji: str = ""

# The line below says that, while the guess index of the user guess is some int, if it matches the character at the same
# index point of the secret word, then it will print a green box. If not, it will print a white box (which is exactly what we want!!).
# Every time, the guess_index value increases by 1, so the program moves through each index of each word and does the above steps
# (which is also exactly what we want!!!).

# Brackets = part of an index, whether there are int or str values in them; what matters more is the code preceding them,
# since that tells the computer what to check the index of and what to do with the results!

while guess_index < len(secret_word):
    if user_guess[guess_index] == secret_word[guess_index]:
        emoji = emoji + GREEN_BOX
    else:
        emoji = emoji + WHITE_BOX
    guess_index = guess_index + 1
print(emoji)

# ANNND, because the emoji variable gets redefined every time, the results get added together each time
# (like how i: int = 0
# >>> i = i + 1 for 3 iterations = 3, and not 0 again ( 0 + 1 + 1 + 1)!)

if user_guess == secret_word:
    print("Woo! You got it! ")

if user_guess != secret_word:
    print("Not quite. Play again soon! ")