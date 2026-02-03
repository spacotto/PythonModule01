#!/usr/bin/env python3

"""
Store and display plant information in simple variables (name, height, age).
"""


def ft_garden_intro(name: str, height: int, age: int) -> None:
    """
    Displays the basic information of a plant in the garden.
    """
    print(f" {name:<13}{f'{height}cm':<13}{f'{age} days':<13}")

def display_header() -> None:
    """
    Displays the header of the plant registry.
    """
    # ANSI Color codes
    white = "\033[1;97m"
    reset = "\033[0m"

    # Columns titles
    c1 = "Name"
    c2 = "Height"
    c3 = "Age"

    # Fixed start of program print
    print(f"\n{white} 🌱 Garden Plant Registry 🌱{reset}\n")
    print(f" {white}{c1:<13}{c2:<13}{c3:<13}{reset}")
    print(" --------------------------------------------------------")

if __name__ == "__main__":

    # Print header
    display_header()

    # Print plants data
    ft_garden_intro("Rose", 25, 30)
    ft_garden_intro("Sunflower", 80, 45)
    ft_garden_intro("Cactus", 15, 120)

    # Signal the end of the program
    print("\n --------------------------------------------------------")
    print(" End of Program\n")
