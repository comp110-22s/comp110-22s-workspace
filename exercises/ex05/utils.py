"""List Utility Functions."""

__author__ = "730474722"


def only_evens(numbers: list[int]) -> list:
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
    """A list which is a subset of the given list, between the specified start index and the end index -1."""
    if x < 0:
        x = 0
    elif y > len(a_list):
        y = (len(a_list) - 1)
    elif (a_list == list()) or (x > len(a_list)) or (y <= 0):
        return a_list

    start = a_list[x]
    end = a_list[y]
    under: int = 0
    over: int = len(a_list) - 1
    copy_list: list[int] = list()
    other_copy_list: list[int] = a_list

    i: int = 0
    while i < len(a_list):
        copy_list.append(a_list[i])
        i += 1
    if end != (len(other_copy_list) - 1) and start != 0:
        while over > y:
            a_list.pop(over)
            over -= 1
        while under < x:
            a_list.pop(under)
            under += 1
        return a_list
    else:
        if end != (len(copy_list) - 1):
            while over > y:
                copy_list.pop(over)
                over -= 1
            return copy_list
        if start != 0:
            while under < x:
                a_list.pop(under)
                under += 1
            return a_list
    return a_list


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Returns a list containing all elements of the first list, followed by all elements of the second list."""
    new_list: list[int] = list_one
    i: int = 0
    while i < len(list_two):
        new_list.append(list_two[i])
        i += 1
    return new_list