"""EX02 - Creating a Wordle-like program."""

__author__: str = "730466987"

# This function set up the helper function for later in this program, where it was easier to call an index-scanning function than to do an index scan, by itself.


def contains_char(input_guess: str, searched_character: str) -> bool:
    """This function exists to check the indices of the word for any instance of the character, and to return a corresponding bool value."""
    index: int = 0

    assert len(searched_character) == 1
    while index < len(input_guess):
        if input_guess[index] == searched_character:
            return True
        index = index + 1
    return False

# Below, we used the same logic as that from EX02 to emojify the string, BUT, this time we had the contains_char function already set up, so we didn't need
# to include all of those if-else statements and while loops.

# The guess got a green box IF contains_char detected it in the goal string AND in the right place in the index (In word? Yes; In proper index? Yes.),
# It got a white box IF contains_char didn't detect it in the goal string at all (In word? NO; In proper index? NO.))
# It got a yellow box if anything else happened (which, logically, could only happen if; In word? Yes; In proper index? NO.)

# Note that it would be logically impossible for the character to NOT be in the word, but to still be in the right index of that word. :)


def emojified(guess_string: str, mystery_string: str) -> str:
    """This function tests the contains_char function to test for matching characters and their locations in the guess_string, compared to the mystery string."""
    assert len(guess_string) == len(mystery_string)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    guess_index: int = 0
    emoji: str = ""

    while guess_index < len(mystery_string):
        if guess_string[guess_index] == mystery_string[guess_index]:
            emoji = emoji + GREEN_BOX
        elif contains_char(mystery_string, guess_string[guess_index]) is False:
            emoji = emoji + WHITE_BOX
        else:
            emoji = emoji + YELLOW_BOX

        guess_index = guess_index + 1
    return emoji

# The below function is important because it lets us check the length of the word in a shorter way than we did in EX02.
# Rather than having a bunch of nested if-else statements and while loops, it can track the length of an input string by itself.

# When used in combination with the contains_char function, this function gets the program 1 step closer to operating like Wordle!


def input_guess(expected_length: int) -> str:
    """This function checks the length of a user-guessed string and returns the guess if it is the expected length."""
    guessed_str: str = input(f"Enter a {expected_length} character word: ")

    while len(guessed_str) != expected_length:
        guessed_str = input(f"That wasn't {expected_length} chars! Try again: ")
    return guessed_str


def main() -> None:
    """This function is the entrypoint of the main game loop for this Wordle-like game."""
    secret_word: str = "codes"
    game_turn: int = 1
    user_win: bool = False
    user_guess: str = ""
    
    while game_turn <= 6 and user_win is False:
        print(f" === Turn {game_turn}/6 === ")
        user_guess = input_guess(len(secret_word))

        print(emojified(user_guess, secret_word))

        if user_guess == secret_word:
            user_win = True
        else:
            game_turn = game_turn + 1

    if user_win is True:
        print(f"You won in {game_turn}/6 turns!")
        
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()