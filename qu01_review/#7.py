"""This is a practice run-through of question 7 from QU01!"""


def indices_of(word: str, char: str) -> str:
    """This function lists the indices in the input word where the input character appears."""
    i: int = 0
    all_indices: str = ""

    while i <= len(word):
        if char == word[i]:
            all_indices += char
            i += 1
        else:
            all_indices = ""
            i += 1
    return all_indices