"""File to define Bear class."""
__author__ = "730494174"


class Bear:
    """Create a bear class."""
    
    def __init__(self, age=0, hunger_score=0):
        """Define age and hunger!"""
        self.age = age
        self.hunger_score = hunger_score
        return None
    
    def one_day(self):
        """Simulate one day for a bear!"""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Bear eats when it finds fish!"""
        self.hunger_score += num_fish