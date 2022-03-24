"""This is the 2nd example file from the class lecture on 3/24/22. Union type gives flexibility to single variables."""

from typing import Union


def log(info: Union[str, int]) -> None:
    """Here, info can be a str or an int."""
    # Below, isinstance is a special command that we haven't covered in class yet, but it checks for all instances of x in y.
    # Union is also a new object type, so don't worry about it, it just means that x object can be type 1 or type 2, etc.
    if isinstance(info, str):
        print(f"str: {info}")
    else:
        print(f"int: {info}")


log("hello")
log(110)