"""Examples of default parameters."""


# Once you start defining default parameters, every parameter after must be a default parameter.
def add(x: int, y: int = 0, z: int = 0) -> int:
    """Example of a default parameter, where y and z are 0 be default."""
    return x + y


print(add(1))
print(add(1, 2))
print(add(1, 2, 3))