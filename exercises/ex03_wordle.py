"""EX02 - Creating a Wordle-like program. """

__author__: str = "730466987"

# pt. 1
# In O.H., get the bool command to work in the 1st def and the str to work in the 2nd! It says that it's assigned to the "none" type, but it's not...


def contains_char(input_guess: str, searched_character: str) -> bool:
    """This function exists to check the indices of the word for any instance of the character, and to return a corresponding bool value."""
    index: int = 0
    assert len(searched_character) == 1
    while index > len(input_guess):
        if input_guess[index] == searched_character:
            return True
        else:
            return False
    index = index + 1

# end of pt. 1

# pt. 2, note that this part hasn't been tested at all yet!


def emojified(guess_string: str, mystery_string: str) -> str:
    """This function tests the contains_char function to test for matching characters and their locations."""
    assert len(guess_string) == (mystery_string)
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
    print(emoji)
    
# also, note that the while loop code is copied directly from EX02!

# end of pt. 2