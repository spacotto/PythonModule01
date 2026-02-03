#!/usr/bin/env python3
"""
Implementing Inheritance for specialized plant types.
"""

class Plant:
    """Base class for all plants in the garden."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes common plant features."""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def display_base(self) -> str:
        """Returns a string with basic plant info."""
        return f"{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):
    """Specialized plant type that can bloom."""
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        # Requirement: Call the parent setup with super().__init__()
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        """Unique behavior for Flowers."""
        print(f"{self.name} is blooming beautifully in {self.color}!")


class Tree(Plant):
    """Specialized plant type that provides shade."""
    def __init__(self, name: str, height: int, age: int, diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = diameter

    def produce_shade(self) -> None:
        """Unique behavior for Trees."""
        shade_area = self.height * self.trunk_diameter // 100
        print(f"{self.name} provides {shade_area} square meters of shade.")


class Vegetable(Plant):
    """Specialized plant type with nutritional value."""
    def __init__(self, name: str, height: int, age: int, season: str, vitamins: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = season
        self.nutritional_value: str = vitamins

    def describe_nutrition(self) -> None:
        """Unique behavior for Vegetables."""
        print(f"{self.name} is harvested in {self.harvest_season} and is rich in {self.nutritional_value}.")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    # Requirement: Create at least 2 instances of each plant type
    garden: list[Plant] = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 15, 10, "yellow"),
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 300, 1000, 30),
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 20, 60, "autumn", "vitamin A")
    ]

    for p in garden:
        # Display common base info
        print(f"{p.display_base()}")
        
        # Check specific type to call unique behaviors
        if isinstance(p, Flower):
            p.bloom()
        elif isinstance(p, Tree):
            p.produce_shade()
        elif isinstance(p, Vegetable):
            p.describe_nutrition()
        print("-" * 30)
