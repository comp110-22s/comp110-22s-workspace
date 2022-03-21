"""Part 1 of ex05."""

__author__ = 730486473


def only_evens(a: list[int]) -> list[int]:
    """Function to identify all the even integers in the list."""
    final_list: list[int] = []
    i: int = 0
    while i < len(a):
        if a[i] % 2 == 0:
            final_list.append(a[i])
        i += 1
    return final_list


def sub(a: list[int], b: int, c: int) -> list[int]:
    """Function to return a limited list."""
    final_list2: list[int] = []
    if b > c:
        return final_list2
    if b <= 0:
        b = 0
    if c == len(a):
        c = len(a) - 1
    if c > len(a):
        c = len(a)
    while b < c:
        final_list2.append(a[b])
        b += 1
    return final_list2


def concat(a: list[int], b: list[int]) -> list[int]:
    """Function to concatenate 2 lists."""
    first_list: list[int] = a
    second_list: list[int] = b
    last_index: int = len(b)
    i: int = 0
    while i < last_index:
        first_list.append(second_list[i])
        i += 1
    return first_list