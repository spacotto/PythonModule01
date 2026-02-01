#!/usr/bin/env python3

"""
This program:
1. runs when executed directly
2. stores plant information in simple variables (name, height, age)
3. displays the plant information using print()
"""


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
    ft_garden_intro("Rose", 25, 30)

    # Fixed end of program print
    print("\n --------------------------------------------------------")
    print(" End of Program\n")
