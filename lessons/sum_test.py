"""This is how to test for the sum function from the sum.py file."""


from lessons.sum import sum

# Remember that test functions don't have parameters (at least for now), and 


def test_sum_empty() -> None:
    xs: list[float] = []
    # Line 10 says that xs is a list variable that is an empty list that is also a float.
    assert sum(xs) == 0.0

# This function will fail the test from pytest, because the assertion that it will return -1.0 can't
# happen if it is also told to output 0.0.


def test_sum_single_item() -> None:
    assert sum([110.0])
    # The notation in like 19 is functionally the same as that of line 10, just with 110.0 instead of an empty list.

    
# Using an if-else statement like this is an INCORRECT way to run the function, so note that:
# Just because a unit passes all of the tests from pytest DOES NOT automatically mean that it will run correctly.


def test_sum_many_items() -> None:
    xs: list[float] = [1.0, 2.0, 3.0]
    assert sum(xs) == 6.0

    # This test is built to fail because its implementation is too complex.
