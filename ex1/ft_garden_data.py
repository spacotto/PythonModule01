#!/usr/bin/env python3
"""
Organize garden data into a structured registry using a Plant class.
"""


class Plant:
    """
    A class representing a plant in the garden.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes the plant with specific attributes.
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def display_info(self) -> None:
        """
        Displays the current status of the plant instance.
        """
        h_str: str = f"{self.height}cm"
        a_str: str = f"{self.age} days"
        print(f" {self.name:<13}{h_str:<13}{a_str:<13}")


def display_header() -> None:
    """
    Displays the registry header.
    """
    # ANSI Colors
    white = "\033[1;97m"
    reset = "\033[0m"

    # Columns titles
    c1, c2, c3 = "Name", "Height", "Age"

    # Prints register header
    print(f"\n{white} 🌱 Garden Plant Registry 🌱{reset}\n")
    print(f" {white}{c1:<13}{c2:<13}{c3:<13}{reset}")
    print(" --------------------------------------------------------")


def main() -> None:
    """
    Creates and displays a registry of garden plants.
    """
    # Garden plants stored in a list
    garden: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]

    # Print the header once
    display_header()

    # Iterate through the list using a unique variable name
    for p in garden:
        p.display_info()

    print(" ")
    
    
if __name__ == "__main__":
    main()
