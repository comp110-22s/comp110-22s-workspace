"""EX02 - Creating a Wordle-like program."""

__author__: str = "730466987"

# This function is set up for later in this program, as it will be easier to call an index-scanning function than to do an index scan by itself every time.


def contains_char(input_guess: str, searched_character: str) -> bool:
    """This function exists to check the indices of the word for any instance of the character, and to return a corresponding bool value."""
    index: int = 0

    assert len(searched_character) == 1
    while index < len(input_guess):
        if input_guess[index] == searched_character:
            return True
        index = index + 1
    return False

# Below, there is same logic as that from EX02 used to emojify the string, BUT, this time we had the contains_char function already set up, so there aren't
# all of those if-else statements and while loops.

# The guess gets a green box IF contains_char detects it in the goal string AND if it's in the right place in the index.
# (In word? Yes; In proper index? Yes.),

# It got a white box IF contains_char didn't detect it in the goal string at all.
# (In word? NO; In proper index? NO.))

# It got a yellow box if anything else happened (which, logically, could only happen if; 
# In word? Yes; In proper index? NO.)

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


def input_guess(expected_length: int) -> str:
    """This function checks the length of a user-guessed string and returns the guess if it is the expected length."""
    guessed_str: str = input(f"Enter a {expected_length} character word: ")

    while len(guessed_str) != expected_length:
        guessed_str = input(f"That wasn't {expected_length} chars! Try again: ")
    return guessed_str

# Here, all of the functions defined above work together to create the main game!

# main() keeps track of the number of turns, checks the length of the word and gives the correct error if the length is wrong, emojifies the word 
# of the correct length, and acts accordingly with the bool value of user_win after each turn for ANY word length. :)

# Note that the game turns are controlled by an if-else statement and start at the int value 1, so they should start correctly at 1 and not 
# add another turn number after the correct word is guessed
# (earlier, the reassignment statement was in the while loop by itself, and it had the add-on issue).


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

# Lines 98-99 are also important because they declare this entire program as a module, so it can now be called without first importing it into the REPL!!


if __name__ == "__main__":
    main()