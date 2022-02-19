"""EX05: building and testing list utility functions."""

__author__: str = "730466987"

# This hasn't been checked in a basic REPL yet so don't forget to do that!

# In O.H., figure out why this function definition won't return a list of ints!
# Also, in utils_test, make sure your 3 tests are useful for testing this function!!


def only_evens(input: list[int]) -> list[int]:
    """This function returns only the even numbers in the argument list."""
    input_evens: list[int] = list()
    iterations: int = 0
    index: int = input[0]
 
    while iterations <= len(input):
        if index % 2 == 0:
            input_evens.append(index)
        index += 1
        iterations += 1
    print(input_evens)