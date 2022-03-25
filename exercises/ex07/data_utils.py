"""Dictionary related utility functions."""

__author__ = "730465187"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list of strings of all the values in a single column whose name is the second parameter."""
    column_values: list[str] = []
    for row in table:
        item: str = row[column]
        column_values.append(item)
    return column_values


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table represented as a list of rows into one represented as a dictionary of columns."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column."""
    final_dict: dict[str, list[str]] = {}
    if rows <= len(table):
        for key in table:
            new_list: list[str] = []
            i: int = 0
            while i < rows:
                new_list.append(table[key][i])
                i += 1
            final_dict[key] = new_list
    else:
        final_dict = table
    return final_dict


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    final_dict: dict[str, list[str]] = {}
    for column in columns:
        final_dict[column] = table[column]
    return final_dict


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    final_dict: dict[str, list[str]] = {}
    for column in table_1:
        final_dict[column] = table_1[column]
    for column in table_2:
        if column in final_dict:
            final_dict[column] += table_2[column]
        else:
            final_dict[column] = table_2[column]
    return final_dict


def count(values: list[str]) -> dict[str, int]:
    """Given a list of values, count produces a dictionary where each key is a unique value in the list, and the value associated with the key is the number of times the value occurs in the list."""
    final_dict: dict[str, int] = {}
    for item in values:
        if item in final_dict:
            final_dict[item] += 1
        else:
            final_dict[item] = 1
    return final_dict