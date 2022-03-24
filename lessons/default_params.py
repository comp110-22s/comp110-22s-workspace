"""This is an OOP practice file from the class lecture on 3/24/22."""


def add(x: int, y: int = 0, z: int = 0) -> int:
    """Default parameters give more flexibility to a function."""
    # Default parameters must follow required parameters.
    return(x + y)


# Here, you can provide 1 or both variable values in the print statement and still have the function print properly, since y and z are both intialized.
# However, note that when you add default parameters to a function definition, every parameter after that one MUST also have a default parameter.

print(add(1))
print(add(1, 2))