"""EX03 - Wordle."""

__author__ = "730486473"

green_box = str("\U0001F7E9")
yellow_box = str("\U0001F7E8")
white_box = str("\U00002B1C")


def contains_char(char_many: str, char_one: str) -> bool:
    """A function to find matching characters in the user guess (ug) and secret word (sw)."""
    assert len(char_one) == 1
    if char_one in char_many:
        return(True)
    else:
        return(False)


def emojified(guess: str, secret: str) -> str:
    """This function is to "emojify" our user's guess"""
    assert len(guess) == len(secret)
    x: int = 0
    final: str = ""
    while x < len(secret):
        if contains_char(secret, guess[x]) is False:
            final = final + white_box
            x = x + 1
        elif contains_char(secret[x], guess[x]) is True:
            final = final + green_box
            x = x + 1
        elif contains_char(secret, guess[x]) is True:
            final = final + yellow_box
            x = x + 1
    return(final)


def input_guess(expected_length: int) -> str:
    """This is to make sure the user's guess is the right amount of letters"""
    user_guess = input(f"Enter a {expected_length} character word: ")
    while len(user_guess) != expected_length:
        user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    else:
        return(user_guess)


def main() -> None:
    """The entrypoint of the program and main game loop."""
    final: str = ""
    y: int = 1
    char_many: str = "codes"
    while y < 7:
        print(f"=== Turn {y}/6 ===")
        user_guess = (input_guess(len(char_many)))
        final = (emojified(user_guess, char_many))
        print(final)
        if user_guess == char_many:
            print(f"You won in {y}/6 turns!")
            y = 7
        elif y == 6 and user_guess != char_many:
            print("X/6 - Sorry, try again tomorrow!")
        y += 1


if __name__ == "__main__":
    main()