#!/usr/bin/env python3
"""
Implement an efficient Plant Factory using class initialisation.
"""


class Plant:
    """
    A class representing a plant.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialises the plant with starting values.
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def __str__(self) -> str:
        """
        Returns a formatted string representing the plant.
        """
        h_str: str = f"{self.height}cm"
        a_str: str = f"{self.age} days"
        return f" {self.name:<13}{h_str:<13}{a_str:<13}"


def display_header() -> None:
    """
    Displays the factory output header.
    """
    # ANSI Colors
    white = "\033[1;97m"
    reset = "\033[0m"

    # Columns titles
    c1, c2, c3 = "Name", "Height", "Age"

    # Prints register header
    print(f"\n{white} 🌱 Plant Factory: List of Plants Created 🌱{reset}\n")
    print(f" {white}{c1:<13}{c2:<13}{c3:<13}{reset}")
    print(" --------------------------------------------------------")


def display_total(total: int) -> None:
    """
    Displays the total amount of created plants
    """
    # ANSI Colors
    white = "\033[1;97m"
    reset = "\033[0m"

    print(f"\n{white} 🌱 Total plants created{reset}: {total}\n")


def main() -> None:
    """
    Simulates the creation of a batch of plants
    """
    # List of plants to create
    factory_batch: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]

    # Init total
    total = 0

    # Print header
    display_header()

    # Iterate through the batch to display them
    for p in factory_batch:
        print(p)
        total += 1

    # Print total
    display_total(total)


if __name__ == "__main__":
    main()
