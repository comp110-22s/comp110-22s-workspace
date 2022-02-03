"""EX02 - Creating a Wordle-like program. """

__author__: str = "730466987"

# pt. 1


def contains_char(input_guess: str, searched_character: str) -> bool:
    """This function exists to check the indices of the word for any instance of the character, and to return a corresponding bool value."""
    index: int = 0
    assert len(searched_character) == 1
    while index < len(input_guess):
        if input_guess[index] == searched_character:
            return True
        index = index + 1
    return False

# end of pt. 1

# pt. 2

# This function works fine, but I'm not sure where to add in the contains_char function. It's not included
# currently, but it needs to be for simplicity and for the rest of the assignment...


def emojified(guess_string: str, mystery_string: str) -> str:
    """This function tests the contains_char function to test for matching characters and their locations."""
    assert len(guess_string) == len(mystery_string)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    guess_index: int = 0
    emoji: str = ""

    while guess_index < len(mystery_string):
        if guess_string[guess_index] == mystery_string[guess_index]:
            emoji = emoji + GREEN_BOX
        else:
            matching_character: bool = False
            alternate_index: int = 0
            
            while matching_character is False and alternate_index < len(mystery_string):
                if mystery_string[alternate_index] == guess_string[guess_index]:
                    matching_character = True
                else:
                    alternate_index = alternate_index + 1
            if matching_character is True:
                emoji = emoji + YELLOW_BOX
            else:
                emoji = emoji + WHITE_BOX
        guess_index = guess_index + 1
    return emoji

# end of pt. 2

# start of pt. 3, untested, finish setting up the skeleton before you do anything else for this part!


def input_guess(expected_length: int) -> str:
    """This function checks the length of a user-guessed integer and returns the guess if it is the expected length."""
    guessed_int: str = input("Enter a 5 character word: ")
    ex_len_i: int = 0

    while ex_len_i < _____:
        if len(guessed_int) == expected_length:
            return guessed_int
        else:
            input(f"That wasn't {expected_length} chars! Try again: ")
    ex_len_i = ex_len_i + 1

# end of pt.3