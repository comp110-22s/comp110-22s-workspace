"""One shot Wordle, a big step towards Wordle."""

__author__ = "730405989"

secret_word = "python"

guess: str = str(input(f"What is your {len(secret_word)} letter guess? "))
# Set up input string for guess to insure it is proper length and only made up of letters.############

while ((len(guess) != len(secret_word)) or not guess.isalpha()):
    guess = (input(f"That was not {len(secret_word)} letters! Try again: "))

counter = int(0)

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

box_response: str = ""
while counter < len(secret_word):
    secret_word_test = secret_word[counter]
    guess_test = guess[counter]

# Setting up while loop that tests whether each letter is contained in the secret word############
# Also should mention adding strings of the box together through a relative reassingment operator.##########
    if ord(secret_word_test) == ord(guess_test):
        box_response = str(box_response + green_box)
        counter += 1
    else:
        i = 0
        yellow_test = False
        while i < len(secret_word) and not yellow_test:
            if ord(guess_test) == ord(secret_word[i]):
                yellow_test = True
                i = 7
            else:
                i += 1
        if yellow_test:
            box_response = str(box_response + yellow_box)
        else: 
            box_response = str(box_response + white_box)
        counter += 1
print(box_response)

# Second while statement is if letter is not in the right index, while loop tests it at other indices to check whether that letter is######
# there, and if it is the variable yellow_letter is set to True, and I set it arbitrarily to 7 to get it to exit the loop######
# Then I tested whether yellow_test was true, and if it was printed a yellow box and if it was not printed the white box#######
if guess == secret_word:
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon! ")
# Easy part, if guess was the secret word, printed congratulatory statement versus if it was not, printed retry statement########