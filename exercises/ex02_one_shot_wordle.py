"""EX02 - One shot Wordle exercise."""

__author__ = "730466987"

secret_word: str = "python"
i: int = 0
user_guess: str = input("What is your 6-letter guess? ")

while len(user_guess) != len(secret_word):
    user_guess = input(f"That was not {len(secret_word)} letters! Try again: ")
    i = i + 1

# This command will be able to do 2 things at once: it will check the length of the user guess compared to the secret word REGARDLESS
# of how long the secret word is, and it will get the user out of the error loop if they put in a guess the correct length, so
# if they guess "python" at guess 3, they can get out of it and have their guiess evaluated by the yes/no responses below.

# start of pt. 2

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# How do I get the emoji string to concatenate all of the box emojis together after going through the while loop?

guess_index: int = 0
emoji: str = ""

while guess_index < len(secret_word):
    if user_guess[guess_index] == secret_word[guess_index]:
        print(GREEN_BOX)
    else:
        print(WHITE_BOX)
    guess_index = guess_index + 1

print(emoji)

# end of pt. 2

if user_guess == secret_word:
    print("Woo! You got it! ")

if user_guess != secret_word:
    print("Not quite. Play again soon! ")