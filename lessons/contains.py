"""Example of a function thatt searches through a list."""


def main() -> None:
    print(contains("Kevin Bacon", ["Kanye West", "Pete Davidson"]))


# Define a function named contains
# Two parameters:
# 1. needle - the string we're looking for
# 2. haystack - the list we're searching for
def contains(needle: str, haystack: list[str]) -> bool:
    # Algorithm:
    #   For each item in the haystack
    #     Test if it is equal to the needle
    #       If so, return true
    for item in haystack:
        if item == needle:
            return True
#   After testing all items, return False, because not found
# Returns true if needle in haystack, false otherwise
    return False


if __name__ == "__main__":
    main()