"""File to define Fish class!"""
__author__ = "730494174"


class Fish:
    """Create a fish class."""
    
    def __init__(self, age=0):
        """Define fish age."""
        self.age = age
        return None
    
    def one_day(self):
        """Simulate one day for a fishy!"""
        self.age += 1
        return None