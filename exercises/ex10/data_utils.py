"""Dictionary related utility functions."""

__author__ = "730494174"

from csv import DictReader

DATA_DIRECTORY = "../../data"
DATA_FILE_PATH = f"{DATA_DIRECTORY}/nc_durham_2015_march_21_to_26.csv"


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with the headers as the keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Return a list of all values under a specific header."""
    result: list[str] = []
    # loop through each element (dictionary) of the list
    for elem in table:
        # for each dictionary (elem), get the value at key "header" and add that to result
        result.append(elem[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformat data so it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of the table to get the headers
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # for each key (header), make a dictionary entry with all the column values
        result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a column with only the first N rows of data for each column!"""
    result = {}
    for column, values in table.items():
        result[column] = values[:n]
    return result


def select(table: dict[str, list[str]], selected_columns: list[str]) -> dict[str, list[str]]:
    """Define function select."""
    result = {}
    for column in selected_columns:
        if column in table:
            result[column] = table[column]
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Define function concat."""
    result = {}
    for column in table1:
        result[column] = table1[column]
    for column in table2:
        if column in result:
            result[column] += table2[column]
        else:
            result[column] = table2[column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Define function count."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result