"""Example of writing a function to search a list."""

# define a function named contains
# parameters:
#   !. needle - the str we r searching for
#   2. haystack - the list of str values we're searching therough

def main() -> None:
    guess: str = input("What is the code word? ")
    possible_answers: list[str] = ["pokemon", "wordle"]
    if contains(guess, possible_answers):
        print("you in da club")
    else:
        print("hell nah")


def contains(needle: str, haystack: list[str]) -> bool:
    """test if needle is in da haystack"""
    for item in haystack:
        if item == needle:
            return True
    return False

print(__name__)

if __name__ == "__main__":
    main()
# algorithm: for each item in haystack
#       test if equal to needle
#           if so, return true
#   after all items checked, that means needle not found, return falso

# Returns True iff needle is found in haystack