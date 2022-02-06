"""Given a name as a paramater, returns a loving string."""


def love(name: str) -> str:
    """Given what we got then we got to do it."""
    return f"I love you {name}!"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repats a loving message n times."""
    love_note: str = ""
    i: int = 0
    while i < n:
        love_note += love(to) + "\n"
        i += 1
    return love_note
