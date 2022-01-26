"""EX02 - One shot Wordle exercise"""

__author__ = "730466987"

secret_word: str = "python"
word_retry: int = 0

user_guess: str = input("What is your 6-letter guess? ")

# python -m exercises.ex02_one_shot_wordle

if len(user_guess) != 6:
    word_retry = word_retry + 1
    while word_retry <= 4:
        print("That was not 6 letters!")
        input("Try again: ")
        word_retry = word_retry + 1

        if word_retry > 4:
            print("Not quite. Play again soon! ")
            quit()

if user_guess == secret_word:
    print("Woo! You got it! ")

if user_guess != secret_word:
    print("Not quite. Play again soon! ")