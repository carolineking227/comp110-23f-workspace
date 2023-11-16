"""File to define Fish class"""

class Fish:
    
    def __init__(self, age = 0):
        self.age = age
        return None
    
    def one_day(self):
        """Simulate one day for a fishy!"""
        self.age += 1
        return None