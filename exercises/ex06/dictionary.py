"""This is a practice project for working with dictionaries."""

__author__: str = "730466987"

# The command to run your tests is python, from exercises.ex06.dictionary import (function name)


def invert(input: dict[str, str]) -> dict[str, str]:
    """This function inverts the keys and values of the input list."""
    switched: dict[str, str] = dict()

    for key in input:
        values: str = input[key]

        if values in switched:
            raise KeyError("Please eliminate duplicate values.")
        else:
            switched[values] = key
    return switched

# Here, a variable is declared that will eventually be filled by the switched values.
# Then, a command is set up that tells the computer to go through all keys in the given dictionary (in a for-in loop).
# Within that for-in loop, an identifying variable is set up to specify what the values are (since the computer already knows what a "key" is, conceptually).

# Now that you have the 2 variables set up for he keys and values (again , the computer knows what a key is but you need to tell it what a value is in this context),
# the computer is told to reverse the order of those values, which is what you want for your output.

# It has been told that, for every key value, if it has appeared before, then a KeyError should be raised (which is another command).
# If not, though, it's told to reverse the values and continue to the next key in the dictionary.

# Beginning of pt. 2:

# In O.H.: How can I edit the code on line 32 to say "if this key is the most common in the list..."?


def favorite_color(colors: dict[str, str]) -> str:
    """This function returns the most common key in its input list (in this case, each key is the name of a different color)."""
    favorite: str = ""

    for key in colors:
        # first, count the instances of each color in the dictionary. Each key should have its own "popularity" value!
        popularity: str = colors[key]
        
        # then, see which key has the highest counting variable.
        if popularity > len(colors):
            favorite += colors[key]

    return favorite
       
# End of pt. 2


# Beginning of pt. 3:

# In O.H. on Monday, check the logic of this function!


def count(count_list: list[str]) -> dict[str, str]:
    """This function tracks the frequency of each input key value. Each value tracks the number of times that the key value appears."""
    final_dict: dict[str, str] = dict()
    i: int = 0

    while i < len(count_list):
        if count_list[i] in count_list:
            i += 1
        else:
            i = 1
    return final_dict

# End of pt. 3