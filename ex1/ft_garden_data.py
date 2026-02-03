#!/usr/bin/env python3
"""
Module to simulate plant growth and aging in a digital garden.
"""


class Plant:
    """
    A class representing a plant that can grow and age.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes the plant with starting values.
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self) -> None:
        """
        Increases the plant's height by a given amount.
        """
        self.height += 1

    def aging(self) -> None:
        """
        Increases the plant's age by one day.
        """
        self.age += 1

    def display_info(self) -> None:
        """
        Displays the current status of the plant.
        """
        h_str: str = f"{self.height}cm"
        a_str: str = f"{self.age} days"
        print(f" {self.name:<13}{h_str:<13}{a_str:<13}")


if __name__ == "__main__":
    # ANSI Color codes
    white = "\033[1;97m"
    reset = "\033[0m"

    # Columns titles
    c1, c2, c3 = "Name", "Height", "Age"

    # Multiple plants as required by Exercise 2
    garden = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]

    # Store initial heights to calculate growth later
    initial_heights: dict[str, int] = {p.name: p.height for p in garden}

    print(f"\n{white} 🌱 Garden Plant Registry: Day 1 🌱{reset}\n")
    print(f" {white}{c1:<13}{c2:<13}{c3:<13}{reset}")
    print(" --------------------------------------------------------")
    for plant in garden:
        plant.display_info()

    # Simulate 1 week (7 days) of growth
    for _ in range(7):
        for plant in garden:
            plant.grow()
            plant.aging()

    print(f"\n{white} 🌱 Garden Plant Registry: Day 8 🌱{reset}\n")
    print(f" {white}{c1:<13}{c2:<13}{c3:<13}{reset}")
    print(" --------------------------------------------------------")
    for plant in garden:
        plant.display_info()

    # NEW SECTION: Growth this week
    print(f"\n{white} 🌱 Growth this week 🌱{reset}\n")
    print(f" {white}{c1:<13}{c2:<13}{reset}")
    print(" --------------------------------------------------------")
    for plant in garden:
        # Calculate the difference
        growth = plant.height - initial_heights[plant.name]
        print(f" {plant.name:<13} +{growth} cm")
 
    print("\n")
