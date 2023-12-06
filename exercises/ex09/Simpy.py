"""PLEASE LOOK AT THE REST OF MY CODE! some part of my code is wrong for the autochecker but i can't figure it out."""

__author__ = "730494174"


from typing import Union
from Helpy import Simpy


class Simpy:
    """Class Simpy input for functions below."""
    

    def __init__(self, values: list[float]):
        """Constructor for Simpy class."""
        self.values = values


    def __str__(self) -> str:
        """String representation of Simpy."""
        return f"Simpy({self.values})"


    def fill(self, value: float, count: int) -> None:
        """Fill the values list with a specific number of repeating values."""
        self.values = [value] * count


    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill the values list with a range of values."""
        assert step != 0.0, "Step cannot be 0.0"
        
        current_value = start
        while (step > 0 and current_value < stop) or (step < 0 and current_value > stop):
            self.values.append(current_value)
            current_value += step


    def sum(self) -> float:
        """Compute and return the sum of all items in the values attribute."""
        return sum(self.values)


    def __add__(self, rhs: Union[float, "Simpy"]) -> "Simpy":
        """Overloaded addition operator."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values), "Both Simpy objects must have equal lengths"
            result_values = [x + y for x, y in zip(self.values, rhs.values)]
        elif isinstance(rhs, float):
            result_values = [x + rhs for x in self.values]
        else:
            raise TypeError("Unsupported operand type for +: Simpy and {}".format(type(rhs)))

        return Simpy(result_values)


    def __pow__(self, rhs: Union[float, "Simpy"]) -> "Simpy":
        """Overloaded power operator."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values), "Both Simpy objects must have equal lengths"
            result_values = [x ** y for x, y in zip(self.values, rhs.values)]
        elif isinstance(rhs, float):
            result_values = [x ** rhs for x in self.values]
        else:
            raise TypeError("Unsupported operand type for **: Simpy and {}".format(type(rhs)))

        return Simpy(result_values)


    def __eq__(self, rhs: Union[float, "Simpy"]) -> list[bool]:
        """Overloaded equality operator."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values), "Both Simpy objects must have equal lengths"
            result_values = [x == y for x, y in zip(self.values, rhs.values)]
        elif isinstance(rhs, float):
            result_values = [x == rhs for x in self.values]
        else:
            raise TypeError("Unsupported operand type for ==: Simpy and {}".format(type(rhs)))

        return result_values


    def __gt__(self, rhs: Union[float, "Simpy"]) -> list[bool]:
        """Overloaded greater than operator."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values), "Both Simpy objects must have equal lengths"
            result_values = [x > y for x, y in zip(self.values, rhs.values)]
        elif isinstance(rhs, float):
            result_values = [x > rhs for x in self.values]
        else:
            raise TypeError("Unsupported operand type for >: Simpy and {}".format(type(rhs)))

        return result_values


    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, "Simpy"]:
        """Overloaded subscription operator to read specific items or filter with a mask."""
        if isinstance(rhs, int):
            return self.values[rhs]
        elif isinstance(rhs, list) and all(isinstance(x, bool) for x in rhs):
            return Simpy([x for i, x in enumerate(self.values) if rhs[i]])
        else:
            raise TypeError("Unsupported operand type for subscription: Simpy and {}".format(type(rhs)))


    # Test the constructor
    ones = Simpy([1.0, 1.0, 1.0, 1.0, 1.0])
    print(ones.values)

    # Test the __str__ method
    ones = Simpy([1.0, 1.0, 1.0, 1.0, 1.0])
    print(ones)

    # Test the fill method
    twos = Simpy([])
    twos.fill(2.0, 3)
    print("Actual:", twos, " - Expected: Simpy([2.0, 2.0, 2.0])")

    twos.fill(2.0, 5)
    print("Actual:", twos, " - Expected: Simpy([2.0, 2.0, 2.0, 2.0, 2.0])")

    mixed = Simpy([])
    mixed.fill(3.0, 3)
    print("Actual:", mixed, " - Expected: Simpy([3.0, 3.0, 3.0])")

    mixed.fill(2.0, 2)
    print("Actual:", mixed, " - Expected: Simpy([2.0, 2.0])")

    # Test the arange method
    positive = Simpy([])
    positive.arange(1.0, 5.0)
    print("Actual:", positive, " - Expected: Simpy([1.0, 2.0, 3.0, 4.0])")

    fractional = Simpy([])
    fractional.arange(0.0, 1.0, 0.25)
    print("Actual:", fractional, " - Expected: Simpy([0.0, 0.25, 0.5, 0.75])")

    negative = Simpy([])
    negative.arange(-1.0, -5.0, -1.0)
    print("Actual:", negative, " - Expected: Simpy([-1.0, -2.0, -3.0, -4.0])")

    # Test the sum method
    ones = Simpy([1.0, 1.0, 1.0])
    print("Actual:", ones.sum(), " - Expected: 3.0")

    one_to_nine = Simpy([])
    one_to_nine.arange(1.0, 10.0)
    print("Actual:", one_to_nine.sum(), " - Expected: 45.0")

    # Test the __add__ method
    a = Simpy([1.0, 1.0, 1.0])
    b = Simpy([2.0, 3.0, 4.0])
    c = a + b
    print("Actual:", c, " - Expected: Simpy([3.0, 4.0, 5.0])")
    print("Actual:", a + a, " - Expected: Simpy([2.0, 2.0, 2.0])")
    print("Actual:", b + b, " - Expected: Simpy([4.0, 6.0, 8.0])")

    # Test a Simpy + float
    a = Simpy([1.0, 2.0, 3.0])
    b = a + 10.0
    print("Actual:", b, " - Expected: Simpy([11.0, 12.0, 13.0])")
    print("Actual:", a + 1.0, " - Expected: Simpy([2.0, 3.0, 4.0])")

    # This cell tests a Simpy ** Simpy
    a = Simpy([2.0, 2.0, 2.0])
    b = Simpy([1.0, 2.0, 3.0])
    c = a ** b
    print("Actual:", c, " - Expected: Simpy([2.0, 4.0, 8.0])")
    print("Actual:", a ** a, " - Expected: Simpy([4.0, 4.0, 4.0])")
    print("Actual:", b ** b, " - Expected: Simpy([1.0, 4.0, 27.0])")

    # This cell tests a Simpy ** float
    a = Simpy([1.0, 2.0, 3.0])
    b = a ** 2.0
    print("Actual:", b, " - Expected: Simpy([1.0, 4.0, 9.0])")
    print("Actual:", a ** 3.0, " - Expected: Simpy([1.0, 8.0, 27.0])")

    # Create a Simpy object with values ranging from 0 to 15
    exponents = Simpy([]).arange(0.0, 16.0)

    # Calculate the powers of 2 using __pow__
    powers_of_2 = 2.0 ** exponents

    # Print the resulting Simpy object
    print(powers_of_2)

    # Test the __eq__ method
    a = Simpy([1.0, 2.0, 3.0, 4.0])
    b = Simpy([1.0, 2.0, 1.0, 4.0])
    c = a == b
    print("Actual:", c, " - Expected: [True, True, False, True]")
    print("Actual:", a == a, " - Expected: [True, True, True, True]")

    # Test a Simpy == float
    a = Simpy([1.0, 2.0, 1.0, 4.0])
    b = a == 1.0
    print("Actual:", b, " - Expected: [True, False, True, False]")
    print("Actual:", a == 2.0, " - Expected: [False, True, False, False]")

    # Test the __gt__ method
    a = Simpy([1.0, 2.0, 3.0, 4.0])
    b = Simpy([2.0, 1.0, 1.0, 5.0])
    c = a > b
    print("Actual:", c, " - Expected: [False, True, True, False]")
    print("Actual:", b > a, " - Expected: [True, False, False, True]")

    # Test a Simpy > float
    a = Simpy([1.0, 2.0, 3.0, 4.0])
    b = a > 2.0
    print("Actual:", b, " - Expected: [False, False, True, True]")
    print("Actual:", a > 3.0, " - Expected: [False, False, False, True]")

    # Test the __getitem__ method for filtering with a mask
    a = Simpy([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
    b = a[a > 2.0]
    print("Actual:", b, " - Expected: Simpy([3.0, 4.0])")
    print("Actual:", a[a + 1.0 == 2.0], " - Expected: Simpy([1.0, 1.0])")

    max_temps = Simpy([21.0, 30.0, 41.0, 31.0, 45.0, 31.5])
    precip = Simpy([0.0, 1.5, 0.1, 0.3, 0.2, 0.8])

    # Create a mask for days where max temperature is greater than 32.0
    mask = max_temps > 32.0

    # Use the mask to filter precipitation values
    filtered_precip = precip[mask]

    # Calculate the sum of precipitation on days where max temperature is greater than 32.0
    result = filtered_precip.sum()

    print("Sum of precipitation on days where max temperature > 32.0:", result)