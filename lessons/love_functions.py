def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name}!"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note: str = ""
    xo = 0
    while xo < n:
        love_note += f"{love(to)}\n"
        xo += 1
    return love_note

    


