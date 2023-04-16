"""The Real Wordle."""

__author__ = "730465187"


def contains_char(word: str, chr: str) -> bool:
    """Checks if a character is in the word."""
    assert len(chr) == 1
    i = 0
    in_word = bool(False)
    while i < int(len(word)) and in_word is False:
        if word[i] == chr:
            in_word = True
        else:
            i += 1
    if in_word is True:
        return True
    else:
        return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Checks which letters are green, which are yellow, and which are white, and returns them in proper order."""
    assert len(guess) == len(secret)
    emojified_guess = str()
    i = 0
    while i < len(secret):
        if guess[i] == secret[i]:
            emojified_guess = (emojified_guess + GREEN_BOX)
        elif contains_char(word=secret, chr=guess[i]) is True:
            emojified_guess = (emojified_guess + YELLOW_BOX)
        else:
            emojified_guess = (emojified_guess + WHITE_BOX)
        i = i + 1
    return emojified_guess


def input_guess(expected_length: int) -> str:
    """Makes sure the guess is the same length as the secret word."""
    guess_length = str(input(f"Enter a {expected_length} character word: "))
    while len(guess_length) != expected_length:
        guess_length = str(input(f"That wasn't {expected_length} chars! Try again: "))
    return guess_length


def main() -> None:
    """The entrypoint of the program and the main game loop."""
    i: int = 1
    secret = str("candy")
    won = bool(False)
    while i <= 6 and won is False:
        print(f"=== Turn {i}/6 ===")
        guess: str = (input_guess(expected_length=len(secret)))
        result: str = emojified(guess=guess, secret=secret)
        print(result)
        if guess == secret:
            won = True
        else:
            i += 1
    if won is True:
        print(f"You won in {i}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
