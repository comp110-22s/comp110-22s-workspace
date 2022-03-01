"""This is a practice project for working with dictionaries."""

__author__: str = "730466987"


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


def favorite_color(colors: dict[str, str]) -> str:
    """This function returns the most common key in its input list (in this case, each key is the name of a different color)."""
    favorite: str = ""
    popularity: dict[str, int] = dict()
    frequency: int = 0

    for key in colors:
        if colors[key] in popularity:
            popularity[colors[key]] += 1
        else:
            popularity[colors[key]] = 1

    for key in popularity:
        if popularity[key] > frequency:
            frequency = popularity[key]
            favorite = key
    return favorite
       
# "Favorite" is made to be filled in with the final result key,
# "Popularity" tracks the values being worked through, and
# "Frequency" tracks the number of times a key appears in "popularity".

# Remember: colors[key] is the VALUE of colors at a specific key, so it can have repeated values!

# Here, the first for-in loop tracks the count of each key, and the second loop tracks the highest count.
# As the 2nd for-in loop goes through each key, it checks to see if the previous key had a higher frequency value than the current one.
# Once it moves through all of the keys in a list, it returns the name of the one with the highest frequency value.


def count(count_list: list[str]) -> dict[str, int]:
    """This function tracks the frequency of each input key value."""
    counted: dict[str, int] = dict()
    i: int = 0

    while i < len(count_list):
        if count_list[i] in counted:
            counted[count_list[i]] += 1
        else:
            counted[count_list[i]] = 1
        i += 1

    return counted

# The above function uses a similar loop as favorite_color to track the frequency of each item in the list, and it functionally does the same thing
# as that function, just from a list to a dictionary, instead of a dictionary to a dictionary :).