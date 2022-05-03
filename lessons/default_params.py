"""Example of default parameters>"""


def add(x: int, y: int = 0, z: int = 0) -> int:
    """Default paramaters give more flexibility to a function"""
    # DEFAULT PARAMETERS MUST FOLLOW REQUIRED PARAMETERS
    return x + y


print(add(1))
print(add(1,2))
print(add(1,2,3))