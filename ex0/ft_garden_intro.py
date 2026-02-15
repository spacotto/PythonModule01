#!/usr/bin/env python3
"""
Store and display plant information in simple variables (name, height, age).
"""


def display_info(name: str, height: int, age: int) -> None:
    """
    Displays the basic information of a plant in the garden.
    """
    print(f" {name:<20}{f'{height}cm':<20}{f'{age} days':<20}")


def display_header() -> None:
    """
    Displays the header of the plant registry.
    """
    white = "\033[1;97m"
    reset = "\033[0m"

    """Columns titles"""
    c1, c2, c3 = "Name", "Height", "Age"

    """Fixed start of program print"""
    print(f"\n{white} 🌱 Garden Plant Registry 🌱{reset}\n")
    print(f" {white}{c1:<20}{c2:<20}{c3:<20}{reset}")
    print(" " + "-" * 60)

def main() -> None:
    """Print header"""
    display_header()

    """Print plants data"""
    display_info("Rose", 25, 30)
    display_info("Sunflower", 80, 45)
    display_info("Cactus", 15, 120)

    """Signal the end of the program"""
    print(" " + "-" * 60)
    print(" End of Program\n")


if __name__ == "__main__":
    main()
