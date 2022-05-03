"""This be the thing for Ex05, approved by Tyler, The Creator."""

__author__ = "730472535"


def only_evens(numbers: list[int]) -> list[int]:
    """Reports only the evens."""
    i: int = 0
    result: list[int] = list()
    while i < len(numbers):
        if numbers[i] % 2 == 0:
            result.append(numbers[i])
            i += 1
        else:
            i += 1
    return result


def sub(numbers: list[int], a: int, b: int) -> list[int]:
    """Reports only the items between index a and b."""
    result: list[int] = list()
    if len(numbers) == 0 or a > len(numbers) or b <= 0:
        return result
    if a < 0:
        a = 0
    if b > len(numbers):
        b = len(numbers)
    i: int = a
    while i < b and i <= len(numbers):
        result.append(numbers[i])
        i += 1
    return result


def concat(list_a: list[int], list_b: list[int]) -> list[int]:
    """Concats two lists."""
    i: int = 0
    result: list[int] = list_a
    while i < len(list_b):
        result.append(list_b[i])
        i += 1
    return result
