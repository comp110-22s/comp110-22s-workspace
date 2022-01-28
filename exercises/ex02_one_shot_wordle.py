"""EX02 - One shot Wordle exercise."""

__author__ = "730466987"

secret_word: str = "python"
i: int = 0
user_guess: str = input("What is your 6-letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# user_guess_index: int = (int(user_guess[0]))
# emoji_box: str = ""

# (start of pt. 2)

# while user_guess_index < len(secret_word):
#      if user_guess_index == secret_word[0]:
#        print(GREEN_BOX)
#    else:
#        print(WHITE_BOX)
#    user_guess_index = user_guess_index + 1
#    print(emoji_box)

# TEST THIS!!

# (end of pt. 2)


# (pt. 1 below)
# python -m exercises.ex02_one_shot_wordle

# During O.H.: 
# How do I get the f-string format to work? And how do I get the "that was not 6 letters" statement and the "try again" statement 
# on the same line?
# Also, how do I make it so that if the user guesses the secret word, then they get out of the loop before using 5 tries?

retry: str = input("Try again: ")

if len(user_guess) != len(secret_word):
    print("That was not 6 letters!")
    i = i + 1
    while i < 4:
        retry = input("Try again: ")
        print("That was not 6 letters!")
        i = i + 1
    if i >= 4:
        # and user_guess != secret_word:
        print("Not quite. Play again soon! ")
        quit()

if user_guess == secret_word:
    print("Woo! You got it! ")

if user_guess != secret_word:
    print("Not quite. Play again soon! ")