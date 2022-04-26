"""This is my response to #1 on the final prep question list (4/25/22)."""

# Here, i is initialized like that because it equals the full length of the list and literally reads it backwards.

# The while loop stops at 0, since i is starting from the max length int of the list and working backwards.


def reverse_multiply(input_list: list[int]) -> list[int]:
    """Doubles and reverses the input list."""
    reversed_list: list[int] = []
    i: int = len(input_list) - 1

    while i >= 0:
        reversed_list.append(input_list[i] * 2)
        i -= 1
    return reversed_list


# This is sloppy, but I'm also going to include a test in this file for this function.

def test_reverse_multiply_demo() -> None:
    """Checks this function according to the class example."""
    demo_list: list[int] = [1, 2, 3]
    assert reverse_multiply(demo_list) == [6, 4, 2]