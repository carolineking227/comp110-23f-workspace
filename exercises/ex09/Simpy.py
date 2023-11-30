"""Utility class for numerical operations."""

from __future__ import annotations
from typing import Union

__author__ = "730494174"


class Simpy:
    """Create class Simpy!"""
    values: list[float]


def __init__(self, values):
    """Define init values."""
    self.values = values


def __str__(self):
    """Define str."""
    return f"Simpy({self.values})"
    

def fill(self, value, num_values):
    """Define fill."""
    self.values = [value] * num_values


def arange(self, start, stop=None, step=1.0):
    """Define arrange."""
    assert step != 0.0, "Step cannot be 0.0"
        
    if stop is None:
        start, stop = 0.0, start

    current_value = start
    while (step > 0 and current_value < stop) or (step < 0 and current_value > stop):
        self.values.append(current_value)
        current_value += step


def sum(self):
    """Define sum!"""
    return float(sum(self.values))
    

def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
    """Define add."""
    result_values = []

    if isinstance(rhs, float):
        # Addition with a float
        result_values = [item + rhs for item in self.values]
    elif isinstance(rhs, Simpy):
        # Addition with another Simpy object
        assert len(self.values) == len(rhs.values), "Both Simpy objects must have equal lengths"
        result_values = [a + b for a, b in zip(self.values, rhs.values)]
        return Simpy(result_values)
        

def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
    """Define pow values."""
    result_values = []

    if isinstance(rhs, float):
        # Exponentiation with a float
        result_values = [item ** rhs for item in self.values]
    elif isinstance(rhs, Simpy):
        # Exponentiation with another Simpy object
        assert len(self.values) == len(rhs.values), "Both Simpy objects must have equal lengths"
        result_values = [a ** b for a, b in zip(self.values, rhs.values)]

    return Simpy(result_values)
    

def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
    """Define eq."""
    result_values = []

    if isinstance(rhs, float):
        # Equality check with a float
        result_values = [item == rhs for item in self.values]
    elif isinstance(rhs, Simpy):
        # Equality check with another Simpy object
        assert len(self.values) == len(rhs.values), "Both Simpy objects must have equal lengths"
        result_values = [a == b for a, b in zip(self.values, rhs.values)]

    return result_values
    

def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
    """Define gt."""
    result_values = []

    if isinstance(rhs, float):
        # Greater than check with a float
        result_values = [item > rhs for item in self.values]
    elif isinstance(rhs, Simpy):
        # Greater than check with another Simpy object
        assert len(self.values) == len(rhs.values), "Both Simpy objects must have equal lengths"
        result_values = [a > b for a, b in zip(self.values, rhs.values)]

    return result_values
    
    
def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
    """Define getitem."""
    if isinstance(rhs, int):
        # Subscription with an int
        return self.values[rhs]
    elif isinstance(rhs, list) and all(isinstance(item, bool) for item in rhs):
        # Subscription with a list of bools (mask)
        result_values = [item for item, mask_value in zip(self.values, rhs) if mask_value]
        return Simpy(result_values)
    else:
        raise TypeError("Invalid subscription type. Must be int or list of bools.")
    
# TODO: Check for understanding 1

# Create a Simpy object with values from 0 to 15 using arange


powers_of_two_indices = Simpy([])  # This will hold the indices (0 to 15)
powers_of_two_indices.arange(0, 16)

# Create a Simpy object with base value 2.0
base_value = Simpy([2.0])

# Calculate the powers of 2 using the __pow__ method
powers_of_two = base_value ** powers_of_two_indices

# Print the result
print(powers_of_two)

# TODO: Check for Understanding 2

max_temps = Simpy([21.0, 30.0, 41.0, 31.0, 45.0, 31.5])
precip = Simpy([0.0, 1.5, 0.1, 0.3, 0.2, 0.8])

# Create a mask for days where max temperature is greater than 32.0
mask = max_temps > 32.0

# Use the mask to filter precipitation values
filtered_precip = precip[mask]

# Calculate the sum of precipitation on days where max temperature is greater than 32.0
result = filtered_precip.sum()

print("Sum of precipitation on days where max temperature is greater than 32.0:", result)