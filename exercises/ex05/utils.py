"""not sure yet what this will be."""

__author__ = "730405989"


def only_evens(a: list) -> list:
    i = 0
    empty_list: list = list()
    number: int = a[i]
    for number in a:
        if number % 2 == 0:
            empty_list.append(number)
        i += 1
    return empty_list

