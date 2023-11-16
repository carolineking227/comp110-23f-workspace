"""File to define River class"""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

class River:
    
    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def view_river(self):
        """Print the river status."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
    
    def one_river_week(self):
        """Simulate one week of life in the river!"""
        for _ in range(7):
            self.one_river_day()

    def remove_fish(self, amount: int):
        """Removing frontmost fish!"""
        for _ in range(amount):
            if self.fish:
                self.fish.pop(0)
            else:
                print("No more fish to remove.")
                break

    def check_ages(self):
        """Removes old fish and bears!"""
        young_fish = [fish for fish in self.fish if fish.age <= 3]
        young_bears = [bear for bear in self.bears if bear.age <= 5]
        return None

    def bears_eating(self):
        """Bears eat 3 fish each if there are at least 5 fishies!"""
        for bear in self.bears:
            if len(self.fish) >= 5:
                """Removes 3 fish from river!"""
                self.remove_fish(3)
                """Bear eats fish!"""
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """Remove hungry bears from river because they starved!"""
        alive_bears = [bear for bear in self.bears if bear.hunger_score >= 0]

        self.bears = alive_bears
        return None
        
    def repopulate_bears(self):
        """Calculate the number of new Bears to be born"""
        new_bears_count = len(self.bears) // 2

        """Add new Bears to the river!"""
        for _ in range(new_bears_count):
            self.bears.append(Bear())
        return None
    
    def repopulate_fish(self):
        """Calculate number of fish born."""
        new_fish_count = (len(self.fish) // 2) * 4

        """Add new Fish to the rive!"""
        for _ in range(new_fish_count):
            self.fish.append(Fish())
        return None
    
    def view_river(self):
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
