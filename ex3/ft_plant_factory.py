#!/usr/bin/env python3
"""
Implement an efficient Plant Factory using class initialisation.
"""


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialises the plant with starting values."""
        self.name = name
        self.height = height
        self.age = age

    def display_info(self) -> None:
        """Displays the current status of the plant instance."""
        print(f" {self.name:<20}"
              f"{f'{self.height}cm':<20}"
              f"{f'{self.age} days':<20}")


def display_header() -> None:
    """
    Displays the factory output header.
    """
    white = "\033[1;97m"
    reset = "\033[0m"
    """Columns titles"""
    c1, c2, c3 = "Name", "Height", "Age"
    """Prints register header"""
    print(f"\n{white} 🌱 Plant Factory 🌱{reset}\n")
    print(f" {white}{c1:<20}{c2:<20}{c3:<20}{reset}")
    print(" " + "-" * 60)


def display_total(total: int) -> None:
    """
    Displays the total amount of created plants
    """
    white = "\033[1;97m"
    reset = "\033[0m"

    print(f"{white} 🌱 Total plants created{reset}: {total}\n")


def main() -> None:
    """"Garden Center inventory"""
    batch = [
        ["Rose", 25, 30],
        ["Oak", 200, 365],
        ["Cactus", 5, 90],
        ["Sunflower", 80, 45],
        ["Fern", 15, 120]
    ]

    display_header()
    total = 0
    for data in batch:
        """Streamlined Creation"""
        p = Plant(data[0], data[1], data[2])
        Plant.display_info(p)
        total += 1

    print(" " + "-" * 60)
    display_total(total)


if __name__ == "__main__":
    main()
