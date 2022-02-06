"""Wordle -- This time using functions."""

__author__ = 730405989


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
        input_word: str = str(input(f"That was not {int_length} chars! Try again: "))
    # Prompting input guess, and if guess not of proper length, reissue a prompt to reguess untill correct length########
    return input_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    n = 1
    d = True
    # d is variable used to end loop if the guess is correct######
    key_word: str = str('codes')
    while n <= 6 and d:
        print(f'=== Turn {n}/6 ===')
        guessn: str = str(input_guess(len(key_word)))
        # guessn variable to store the input guess at the current guess######
        print(emojified(guessn, key_word))
        if guessn == key_word:
            d = False
        else: 
            n += 1
    
    if not d:
        print(f'You won in {n}/6 turns!')
    else: 
        print(f'{n}/6 - Sorry, try again tomorrow!')
    exit()


if __name__ == "__main__":
    main()