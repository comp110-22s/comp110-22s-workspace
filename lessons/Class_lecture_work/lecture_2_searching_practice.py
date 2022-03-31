"""This is an example question from in-person lecture 2. This function searches a list for a specific value."""

# Define a function named "contains"
# Parameters:
#   1. needle - the str we're searching for
#   2. haystack - the lst of str values we're searching through


def main() -> None:
    guess: str = input("What is the code word? ")
    possible_answers: list[str] = ["pokemon", "wordle"]
    if contains(guess, possible_answers):
        print("We're letting you in the secret club...")
    else:
        print("Go back to Davis")


def contains(needle: str, haystack: list[str]) -> bool:
    """Test if needle is found in haystack, skeleton code along the way explains how each step works."""
# Algorithm: for each item in the haystack:
#   Test if = needle
#       if so, return True
    for item in haystack:
        if item == needle:
            return True
#   After all items have been checked, that means needle is not found, return False
    return False
# Returns true iff (meaning if and only if) needle is found in haystack


print(__name__)

# "__name__" is a special variable in Python that lets you access/work with the specific name of a function.
# This program allows you to run the whole program AND to call specific functions, depending on what you ask in the REPL.

if __name__ == "__main__": 
    main()