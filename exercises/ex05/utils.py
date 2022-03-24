"""List Utility Functions."""
__author__ = "730474722"


def only_evens(numbers: list[int]) -> list[int]:
    """Returns the even numbers in a list of integers."""
    new_list: list[int] = list()
    i: int = 0
    while i < len(numbers):
        if ((numbers[i] / 2) - (numbers[i] // 2)) > 0:
            i += 1
        else:
            new_list.append(numbers[i])
            i += 1
    return new_list

            
def sub(a_list: list[int], x: int, y: int) -> list[int]:
    """A list which is a subset of the given list, between the specified start index and the end index -1.212"""
    new_list: list[int] = list()
    for values in a_list[x: y]:
        new_list.append(values)
    return new_list
    

def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Returns a list containing all elements of the first list, followed by all elements of the second list."""
    new_list: list[int] = list_one
    i: int = 0
    while i < len(list_two):
        new_list.append(list_two[i])
        i += 1
    return new_list