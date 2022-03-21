"""This program goes with LS20 and focuses on importing functions between functions."""

THE_ANSWER: int = 42


def main() -> None:
    print(powerful(2, 10))
    print("helpers.py run as a module")


def powerful(x: float, n: float) -> float:
    """This function raises x to the power of n."""
    return x ** n


print("helpers.py was evaluated")


if __name__ == "__main__":
    main()
else:
    print(f"helpers.py was imported: {__name__}.")

# Here, name != main, so the else statement above is printed.