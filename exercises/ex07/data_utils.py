"""Dictionary related utility functions."""

__author__ = "730405989"

# Define your functions belowfrom csv import DictReader
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    # r short for read, encoding some sort of parameter 
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    # Read that file

    # Prepare to read the data file as a CSV rather than just two strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)
    # Close the file whne we're done, to free its resources.
    file_handle.close()
    return result
