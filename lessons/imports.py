"""This is the 2nd program that goes with LS20 (along with helpers.py) that shows an example of importing in Python."""


# from lessons import helpers
from lessons import helpers as hp
from lessons.helpers import powerful, THE_ANSWER


def main() -> None:
    """This is the entrypoint of the program."""
    print(hp.powerful(2, 4))
    print(f"The answer: {hp.THE_ANSWER}")
    print(powerful(2, 4))
    print(THE_ANSWER)


if __name__ == "__main__":
    main()