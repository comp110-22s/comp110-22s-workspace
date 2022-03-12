"""Dictionary related utility functions."""

__author__ = "730466987"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """This function reads the rows of a csv file into a table."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table_rows: list[dict[str, str]], column_name: str) -> list[str]:
    """This function makes a list of values for input column keys."""
    result: list[str] = []
    
    for key in table_rows:
        item: str = key[column_name]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """This function makes a column-oriented table from an input row-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]

    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(input_table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """This function produces a column-based data table given input information."""
    final_table: dict[str, list[str]] = {}
    rows = 1

    for column in input_table:
        first_values: list[str] = []

        for __?__ in input_table:
            
            first_values += input_table[rows]
            rows += 1
        final_table += input_table[__?__]

    return final_table
