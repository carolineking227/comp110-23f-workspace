"""Summing the elements of a list using different loops."""

__author__ = "730494174"

"""Version A."""


def w_sum(vals: list[float]) -> float:
    """Initialize the total sum to 0.0, and the index."""
    total = float(0.0)
    i = 0

    """use the while loop to add the element to the total and add one to the index."""
    while i < len(vals):
        total += vals[i]
        i += 1 

    return total


"""Version B."""


def f_sum(vals: list[float]) -> float:
    """Initialize the total sum to 0.0."""
    total = float(0.0)

    for value in vals:
        """Add the current element to the total."""
        total += float(value)

    """Return the final sum."""
    return total


"""Version C."""


def f_range_sum(vals: list[float]) -> float:
    """Initialize the sum to 0.0."""
    total = float(0.0)
    
    """Use a for...in range loop to iterate through the list indices."""
    for i in range(len(vals)):
        """Add the element at the current index to the total."""
        total += vals[i]
    
    """Return the final sum."""
    return total