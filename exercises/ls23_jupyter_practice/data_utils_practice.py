"""Some helpful data utility functions for working with CSV files. This file goss along with the example from data_LS23."""

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """This function reads the rows of a csv into a table."""
    result: list[dict[str, str]] = []

    # The command below allows you to access this csv file data from your hard drive, which will make it easier to work with in the Jupyter file 'csv_demo'."
    
    # The weird variable declaration below is basically telling the computer to infer the type of variabl being declared, and then to use the "open" command
    # to access the filename data, read it, and encode it using some coding syntax that we don't need to worry about right now."

    file_handle = open(filename, "r", encoding="utf8")

    # The following code tells the computer to read the CSV file data as CSV data, instead of just
    csv_reader = DictReader(file_handle)

    # The following command will read each for of the CSV file line-by-line!

    for row in csv_reader:
        result.append(row)

    # How to read and close this file...

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result