"""Utility functions that will be tested on."""

__author__ = "730405989"


def only_evens(a: list) -> list:
    i = 0
    empty_list: list = list()
    number: int = a[i]
    for number in a:
        if number % 2 == 0:
            empty_list.append(int(number))
    return empty_list


def sub(fullset: list, start: int, end: int) -> list:
    i = 0
    empty_list2: list = list()
    nums: int = fullset[i]
    if len(fullset) > 0:
        for nums in fullset:
            empty_list2.append(int(nums))
        return empty_list2
    else:
        return empty_list2