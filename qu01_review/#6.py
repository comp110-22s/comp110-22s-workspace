"""This is a practice run-through of question 6 from QU01!"""


def repeat(word: str, multip: int) -> str:
    """This function repeats each letter in "word" "multip" times."""
    i: int = 0
    repeated: str = ""

    while i < len(word):
        si: int = 0

        while si < multip:
            repeated += word[i] 
            si += 1
        i += 1
    return repeated


repeat("comp", 3)