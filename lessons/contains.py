"""Example of a function that searches through a list."""


def contains(needle: str, haystack: list[str]) -> bool:
    for item in haystack:
        if item == needle:
            return True
    return False


def main() -> None:
    print(contains("Kevin Bacon", ["Kanye West", "Pete Davidson"]))


main()