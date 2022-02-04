"""One shot wordle."""

__author__ = "730465187"

secret_word = str("light")

guess = str(input(f"What is your {len(secret_word)}-letter guess? "))

while len(guess) != len(secret_word):
    guess = str(input(f"That was not {len(secret_word)} letters! Try again: "))
# The user inputs their guess and it is stored as the variable guess.

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index_of_secret_word = 0
color_of_guess = str()

while index_of_secret_word < len(secret_word):
    if guess[index_of_secret_word] == secret_word[index_of_secret_word]:
        color_of_guess = (color_of_guess + GREEN_BOX)
        # This segment of code is used to determine if the letter of the guess is equal to the letter of the secret word in the same place. If so, a green box is added to that place in the word in the output.
    else:
        in_word = bool(False)
        i = 0
        while in_word is not True and i < len(secret_word):
            if secret_word[i] == guess[index_of_secret_word]:
                in_word = True
            else:
                i = i + 1
        # This loop determines whether a character in the guessed word equals a character in a different location in the secret word.
        if in_word is True:
            color_of_guess = (color_of_guess + YELLOW_BOX)
        else:
            color_of_guess = (color_of_guess + WHITE_BOX)
        # This if-else statement determines whether to add a yellow box or a white box for output at a given position based on the results of the previous while loop.
    index_of_secret_word = index_of_secret_word + 1
    # This line moves the program from one character to the next.
print(color_of_guess)

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")