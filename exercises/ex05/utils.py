"""EX05: building and testing list utility functions."""

__author__: str = "730466987"

# REPL command for testing: python -m pytest exercises/exercises/ex05

# To do: fix functions 1 and 2, THEN for the tests, follow the format and make new tests for the edge cases that are too hard.
# Also, for 2/23/22 go through functions 2 and 3 to check for any syntax errors; the logic of the body blocks make sense but you may be able to shorten them.


def only_evens(input: list[int]) -> list[int]:
    """This function returns only the even numbers in the argument list."""
    input_evens: list[int] = list()
    iterations: int = 0
 
    while iterations < len(input):
        if input[iterations] % 2 == 0:
            input_evens.append(input[iterations])
        iterations += 1
    return input_evens


def sub(a_list: list[int], start_index: int, stop_index: int) -> list[int]:
    """This function returns the items in a given string at the specified index."""
    subset: list[int] = list()
    start: int = a_list[start_index]
    stop: int = len(a_list)
    i: int = 0

    subset.append(start)

    while i < stop_index:
        subset.append(stop)
        i += 1
    return subset
    

def concat(list_a: list[int], list_b: list[int]) -> list[int]:
    """This function concatenates the items in one list to the end of another."""
    iterations: int = 0
    list_c: list[int] = list()
    
    while iterations < len(list_a):
        list_c.append(list_a[iterations])
        iterations += 1

    while iterations < len(list_a):
        list_c.append(list_a[iterations])
        iterations += 1
    return list_a