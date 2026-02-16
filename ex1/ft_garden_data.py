#!/usr/bin/env python3
"""
Organize garden data into a structured registry using a Plant class.
"""


class Plant:
    """
    A class representing a plant in the garden.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes the plant with specific attributes."""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def display_info(self) -> None:
        """Displays the current status of the plant instance."""
        print(f" {self.name:<20}"
              f"{f'{self.height}cm':<20}"
              f"{f'{self.age} days':<20}")


def display_header() -> None:
    """Displays the registry header."""
    white = "\033[1;97m"
    reset = "\033[0m"

    """Columns titles"""
    c1, c2, c3 = "Name", "Height", "Age"

    """Prints register header"""
    print(f"\n{white} 🌱 Garden Plant Registry 🌱{reset}\n")
    print(f" {white}{c1:<20}{c2:<20}{c3:<20}{reset}")
    print(" " + "-" * 60)


def main() -> None:
    """
    Creates and displays a registry of garden plants.
    """
    garden: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]

    """Print the header once"""
    display_header()

    """Iterate through the list (the garden) using a unique variable name"""
    for p in garden:
        p.display_info()

    print(" ")


if __name__ == "__main__":
    main()
