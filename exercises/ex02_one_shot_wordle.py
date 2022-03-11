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
# if they guess "python" at guess 3, they can get out of it and have their guess evaluated by the yes/no responses in lines 62 and 65.

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

gi: int = 0
emoji: str = ""

# The line below says that, while the guess index of the user guess is some int, if it matches the character at the same
# index point of the secret word, then it will print a green box. If not, it will print a white box (which is exactly what we want!!).
# Every time, the guess_index value increases by 1, so the program moves through each index of each word and does the above steps
# (which is also exactly what we want!!!).

# Brackets = part of an index. You can put int or str values defining int values in them!

while gi < len(secret_word):
    if user_guess[gi] == secret_word[gi]:
        emoji = emoji + GREEN_BOX
    else:
        matching_character: bool = False
        ai: int = 0
        
        while matching_character is False and ai < len(secret_word):
            if secret_word[ai] == user_guess[gi]:
                matching_character = True
            else:
                ai = ai + 1
        if matching_character is True:
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
    gi = gi + 1
print(emoji)

# Because the emoji variable gets redefined every time, the results get added together each time
# (like how i: int = 0
# >>> i = i + 1 for 3 iterations = 3, and not 0 again ( 0 + 1 + 1 + 1 = 3)!)

# Also, previously, there was an issue with line 44, where the wrong indexes were defined. Before, they were set without str indices,
# but this step checks whether or not the indices match, so it skipped a bunch of steps after that and messed up the printing of the
# yellow and white boxes. 

# Always check for the little things if there's an error in your code!!!

if user_guess == secret_word:
    print("Woo! You got it! ")

if user_guess != secret_word:
    print("Not quite. Play again soon! ")