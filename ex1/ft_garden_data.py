#!/usr/bin/env python3

"""
This program track multiple plants with their information.
"""


class Plant:
    """
    Each plant has:
    1. A name
    2. Height in centimeters
    3. Age in days
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

def ft_garden_intro(name: str, height: int, age: int) -> None:
    """
    Displays the basic information of a plant in the garden.
    """
    print(f" {name:<13}{f'{height}cm':<13}{f'{age} days':<13}")

if __name__ == "__main__":
    
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

    # Add data entries
    ft_garden_data("Rose", 25, 30)
    ft_garden_data("Sunflower", 80, 45)
    ft_garden_data("Cactus", 15, 120)

    # Fixed end of program print
    print("\n --------------------------------------------------------")
    print(" End of Program\n")

