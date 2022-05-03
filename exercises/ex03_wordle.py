"""Wordle the real thing basically."""

__author__ = "730472535"


def contains_char(secret_word: str, character: str) -> bool:
    """Tests if letter exists in a the secret word."""
    assert len(character) == 1
    contains_char: bool = False
    i: int = 0  # counter variable to test each letter in the secret word
    while i < len(secret_word):
        if secret_word[i] == character:
            contains_char = True
            return (contains_char)
        else:
            i += 1 
            contains_char = False
    return(contains_char)


def emojified(guess: str, secret_word: str) -> str:
    """Tests for yellow or white box."""
    assert len(guess) == len(secret_word)
    h: int = 0  # another counter variable to test each letter of the guess
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result: str = ""
    
    while h < len(secret_word):  # repeats for each index of the guess
        if guess[h] == secret_word[h]:  # program should stop testing this index if this is true
            result += GREEN_BOX
            h += 1
        elif contains_char(secret_word, guess[h]):  # checks each letter of guess against all letters in teh secret word
            result += YELLOW_BOX
            h += 1
        else:
            result += WHITE_BOX
            h += 1
    return result


def input_guess(guess_length: int) -> str:
    """Ensures guess is the correct length."""
    guess: str = input(f"Enter a {guess_length} character word: ")
    while len(guess) != guess_length:
        guess = input(f"That wasn't {guess_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "cocks"
    guess_length: int = len(secret_word)
    turn: int = 1  # counter variable for turn

    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(guess_length)  # calls for a guess from the user
        print(emojified(guess, secret_word))  # prints emojis for the guess
        if guess == secret_word:
            print(f"You won in {turn}/6 turns!")
            return
        else:
            turn += 1
    print("X/6 - Sorry, try again tomorrow!")
    return


if __name__ == "__main__":
    main()
