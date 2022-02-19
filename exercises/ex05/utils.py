"""Functions for ex05."""

__author__ = "730465187"


def only_evens(nums: list[int]) -> list[int]:
    """Returns only the evens in a list."""
    i: int = 0
    while i < len(nums):
        if nums[i] % 2 != 0:
            nums.pop(i)
        i += 1
    return nums


def sub(nums: list[int], start: int, end: int) -> list[int]:
    """Returns the parts of a list between 2 indexes."""
    new_list: list[int] = list()
    i: int = start
    if start < 0:
        i = 0
    if end > len(nums) - 1:
        end = len(nums) - 1
    while i <= end:
        new_list.append(nums[i])
        i += 1
    return new_list


def concat(L1: list[int], L2: list[int]) -> list[int]:
    """Returns a new list made up of the first list combined with the second list."""
    new_list: list[int] = L1
    i: int = 0
    while i < len(L2):
        new_list.append(L2[i])
        i += 1
    return new_list