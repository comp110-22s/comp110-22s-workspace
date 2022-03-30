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


def head(origdict: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Display the first n rows of a data table."""
    head_dict: dict[str, list[str]] = {}
    for columns in origdict:
        store_list: list[str] = []
        i: int = 0
        if n > len(origdict[columns]):
            n = len(origdict[columns])
        while i < n:
            store_list.append(origdict[columns][i])
            i += 1
        head_dict[columns] = store_list
    return head_dict


def select(given: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """Select chosen columns from larger dataset."""
    select_dict: dict[str, list[str]] = {}
    for columns in col_names:
        select_dict[columns] = given[columns]
    return select_dict


def concat(dict1: dict[str, list[str]], dict2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two tables into one."""
    concat_dict: dict[str, list[str]] = {}
    for columns in dict1:
        concat_dict[columns] = dict1[columns]
    for columns in dict2:
        if columns in concat_dict:
            for values in dict2[columns]:
                concat_dict[columns].append(values)
        else:
            concat_dict[columns] = dict2[columns]
    return concat_dict


def count(given: list[str]) -> dict[str, int]:
    """Count frequncies fof all letters ina  list of strings."""
    counts: dict[str, int] = {}
    for value in given:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    return counts


def convert_to_list(given: dict[str, list[str]], list_name: str) -> list[str]:
    """Convert a column of your choice into a list of the values within that column."""
    built_list: list[str] = []
    built_list = given[list_name]
    return built_list


def countlist(given: list[str], string: str) -> int:
    """Counts wanted value within a list using count function."""
    counter = count(given)
    return counter[string]


def prop_finder(given: int, total: int) -> float:
    """Given value and total, computes proportion of that given value."""
    proportion: float = given / total
    return proportion


def mean(given: list[str]) -> float:
    """If given list with numerical values, find mean of the list."""
    tallies = count(given)
    total: int = 0
    for values in tallies:
        total += int(values) * tallies[values] 
    mean: float = total / len(given)
    return mean