def remove_ws(word: str) -> str:
    """Removes white space."""
    new_word: str = ""
    i: int = 0
    while i < len(word):
        if (word[i] != " "):
            new_word += word[i]
        i += 1
    return new_word

wack: str = str("geronimo")


print(wack[len(wack) - 2])