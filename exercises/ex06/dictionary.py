"""This is a practice project for working with dictionaries."""

__author__: str = "730466987"

# "The command to run your tests is python -m pytest exercises/ex06"

# Beginning of pt. 1:

# In O.H., how to you refer to the value part of the input? (See attempted usage in line ____.)

def invert(input: dict[str, str]) -> dict{str, str}:
    """This function inverts the keys and values of the input list."""
    i: int = 0
    switched: dict[str, str] = dict()

    while i < len(input):
        # switched = [value part of the input : key part of the input] <-- all at input[i]
        i += 1
    return switched

# End of pt. 1


# Beginning of pt. 2:

# Also, how can I track which 

def favorite_color(colors: dict[str, str]) -> str:
    """This function returns the most common color value in its input list."""
    i: int = 0
    favorite: str = ""

    while i < len(colors):
        for color in colors:
            # favorite += (the most common color within the length of the dictionary)
    return favorite
       

# End of pt. 2


# Beginning of pt. 3:



# End of pt. 3