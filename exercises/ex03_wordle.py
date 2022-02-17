"""Wordle -- This time using functions."""

__author__ = "730405989"


def contains_char(test_word: str, test_letter: str) -> bool:
    """Tests whether letter is contained in the word."""
    assert len(test_letter) == 1
    counter = 0 
    while counter < len(test_word):
        if ord(test_word[counter]) == ord(test_letter):
            counter = len(test_word)
            return True
        # Tests if letter is contained, going letter by letter, and returning true when/if a letter is found########
        else:
            counter += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Given guess and key word returns emoji string that represents correctness of the guess."""
    assert len(guess) == len(secret)
    emoji_string: str = str("")
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"   
    # Setting up string for boxes and empty emoji string that will be added to#################
    i = 0
    while i < len(secret):
        
        secret_test: str = secret[i]
        guess_test: str = guess[i]
        # Setting up tests to test via counter and while loop letter by letter#############
        if ord(secret_test) == ord(guess_test):
            emoji_string += green_box
            i += 1
        else:
            if contains_char(secret, guess_test):
                emoji_string += yellow_box
                i += 1
            else: 
                emoji_string += white_box
                i += 1
        # If letter is right(guess = secret), green box given, if not, use contains character function to test######
    return emoji_string


def input_guess(int_length: int) -> str:
    """Prompts user for input word."""
    input_word: str = str(input(f"Enter a {int_length} character word: "))
    while len(input_word) != int_length:
        input_word = str(input(f"That wasn't {int_length} chars! Try again: "))
    # Unsure if grader reads this part, but if you can add comments, add comment on how to store variable above without getting Safety Type Error####
    # Prompting input guess, and if guess not of proper length, reissue a prompt to reguess untill correct length########
    return input_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    n = 1
    lose = True
    # lose is variable used to indicate if the guess is incorrect######
    key_word: str = str("naomi")
    while n <= 6 and lose:
        print(f'=== Turn {n}/6 ===')
        guess_n: str = str(input_guess(len(key_word)))
        # guessn variable to store the input guess at the current guess######
        print(emojified(guess_n, key_word))               
        if guess_n == key_word:
            lose = False
        else: 
            n += 1
    
    if not lose:
        print(f"You won in {n}/6 turns!")
    else: 
        print("X/6 - Sorry, try again tomorrow!")
    return


if __name__ == "__main__":
    main()