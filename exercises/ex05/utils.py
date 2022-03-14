"""EX05: building and testing list utility functions."""

__author__: str = "730466987"


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
    if start_index < 0:
        start_index = 0
    if stop_index > len(a_list):
        stop_index = len(a_list)

    subset: list[int] = list()
    i: int = start_index

    while i < stop_index:
        subset.append(a_list[i])
        i += 1
    return subset
    

def concat(list_a: list[int], list_b: list[int]) -> list[int]:
    """This function concatenates the items in one list to the end of another."""
    i: int = 0
    list_c: list[int] = list()
    
    while i < len(list_a):
        list_c.append(list_a[i])
        i += 1

    i = 0
    while i < len(list_b):
        list_c.append(list_b[i])
        i += 1
    return list_c