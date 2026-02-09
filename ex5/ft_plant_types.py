#!/usr/bin/env python3
"""
Implement Inheritance for specialised plant types.
"""


class Plant:
    """Base class for all garden plants."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes common plant features."""
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    """Specialized plant that can bloom."""
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Uses super() to initialize common attributes and adds color."""
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        """Displays a blooming message."""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """Specialized plant that provides shade."""
    def __init__(self, name: str, height: int, age: int, diameter: int) -> None:
        """Adds trunk_diameter to the base plant."""
        super().__init__(name, height, age)
        self.trunk_diameter: int = diameter

    def produce_shade(self) -> None:
        """Calculates and displays shade area."""
        shade_area = self.trunk_diameter * 1.5  # Simple simulation logic
        print(f"{self.name} provides {shade_area} square meters of shade")


class Vegetable(Plant):
    """Specialized plant for harvesting."""
    def __init__(self, name: str, h: int, a: int, season: str, vit: str) -> None:
        """Adds harvest season and nutritional value."""
        super().__init__(name, h, a)
        self.harvest_season: str = season
        self.nutritional_value: str = vit

    def harvest_info(self) -> None:
        """Displays nutritional information."""
        print(f"{self.name} is rich in {self.nutritional_value}")


def main() -> None:
    """Creates instances of specialized plants and triggers behaviors."""
    print("=== Garden Plant Types ===")
    
    rose = Flower("Rose", 25, 30, "red")
    print(f"{rose.name} (Flower): {rose.height}cm, {rose.age} days, {rose.color} color")
    rose.bloom()

    oak = Tree("Oak", 500, 1825, 50)
    print(f"{oak.name} (Tree): {oak.height}cm, {oak.age} days, {oak.trunk_diameter}cm diameter")
    oak.produce_shade()

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    print(f"{tomato.name} (Vegetable): {tomato.height}cm, {tomato.age} days, {tomato.harvest_season} harvest")
    tomato.harvest_info()


if __name__ == "__main__":
    main()
