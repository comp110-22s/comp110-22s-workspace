"""EX02 - One Shot Wordle."""
__author__ = "730486473"
secret_word = "python"
user_guess = input(f"What is your {len(secret_word)}-letter guess? ")
while len(user_guess) != len(secret_word):
    user_guess = input(f"That was not {len(secret_word)} letters! Try again: ")
while len(user_guess) == len(secret_word):
    x = int(0)
    final = ""
    green_box = str("\U0001F7E9")
    yellow_box = str("\U0001F7E8")
    white_box = str("\U00002B1C")
    while x < len(secret_word):
        if user_guess[x] == secret_word[x]:
            final = final + green_box
        else:
            char_guess = False
            secret_check = int(0)
            while char_guess is not True and secret_check < len(secret_word):
                if user_guess[x] == secret_word[secret_check]:
                    char_guess = True
                else:
                    secret_check = secret_check + 1
            if char_guess is True:
                final = final + yellow_box
            else:
                final = final + white_box
        x = x + 1
    if user_guess != secret_word:
        print(final)
        print("Not quite. Play again soon!")
        exit()
    elif user_guess == secret_word:
        print(final)
        print("Woo! You got it!")
        exit()