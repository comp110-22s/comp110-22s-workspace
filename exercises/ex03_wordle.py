"""Wordle Baby!"""

__author__ = "730474722"


def contains_char(word: str, character: str) -> bool:
    """Scans for Matching Characters in a Word!"""
    assert len(character) == 1  
    i: int = 0
    p: int = 0
    tracker: bool = False
    while tracker is False and i < len(word):
        if word[i] == character[p]:
            tracker = True
        else:
            i += 1
    return tracker


"""The boxes."""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
g = GREEN_BOX
w = WHITE_BOX
y = YELLOW_BOX


def emojified(guess: str, secret: str) -> str:
    """Returns a Specific Emoji That Pertains to the Guess Index!"""
    assert len(guess) == len(secret)
    t: int = 0
    emojis: str = ""
    while t < len(secret):
        if guess[t] == secret[t]:
            emojis += g
        elif contains_char(secret, guess[t]):
            emojis += y
        else:
            emojis += w
        t += 1 
    return emojis


def input_guess(guess: int) -> str:
    """Asks the User for a Guess Until len of Guess Matches len of the Secret!"""
    attempt: str = input(f"Enter a {guess} character word: ")
    if len(attempt) == guess:
        return attempt
    else:
        while len(attempt) != guess:
            attempt = input(f"That wasn't {guess} chars! Try again: ")
    return attempt


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    tries: int = 1
    max_tries = 6
    win: bool = False
    win is False
    while tries <= 6 and win is False:
        print(f"=== Turn {tries}/{max_tries} ===") 
        player_input: str = input_guess(len(secret))
        print(emojified(player_input, secret))
        if player_input == secret:
            print(f"You won in {tries}/{max_tries} turns!")
            win = True
        tries += 1
    if tries > 6:
        print(f"X/{max_tries} - sorry, try again tomorrow!")


if __name__ == "__main__":
    main()