"""Utility functions that will be tested on."""

__author__ = "730405989"


def only_evens(a: list) -> list:
    even_list: list = list()
    for number in a:
        if number % 2 == 0:
            even_list.append(int(number))
    return even_list


def sub(fullset: list, start: int, end: int) -> list:
    subset: list = list()
    if start < 0:
        start = 0
    if end > len(fullset):
        end = len(fullset) 
    elif end < 0:
        empty_list: list = []
        return empty_list
    i = 0
    for nums in fullset:
        if i >= start and i < end:
            subset.append(nums)
        i += 1
    return subset


def concat(list1: list, list2: list) -> list:
    i = 0
    sumlist = list()
    if len(list1) != 0:
        for items1 in list1:
            sumlist.append(items1)
    if len(list2) != 0:
        for items2 in list2:
            sumlist.append(items2)
    return sumlist


def main() -> None:
    print(only_evens([1, 2, 3]))
    print(only_evens([1, 5, 3]))
    print(only_evens([4, 4, 4]))
    a_list = [10, 20, 30, 40]
    print(sub(a_list, 1, 7))


main()