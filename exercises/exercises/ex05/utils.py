"""EX05: building and testing list utility functions."""

__author__: str = "730466987"

# This hasn't been checked in a basic REPL yet so don't forget to do that!

# In O.H., look at utils_test and make sure those tests are in the correct format!


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
    return input_evens

# for pt. 2


def sub(a_list: list[int], start_index: int, stop_index: int) -> list[int]:
    """This function returns the items in a given string at the specified index."""
    subset: list[int] = list()
    start: int = a_list[start_index]
    stop: int = len(a_list) - 1
    iterations: int = 0

    subset.append(start)

    while iterations <= stop:
        subset.append(stop)
        iterations += 1
    return subset
    

# for pt. 2

# for pt. 3 - INCOMPLETE SKELETON

# end of pt. 3