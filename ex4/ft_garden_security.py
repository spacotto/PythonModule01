#!/usr/bin/env python3
"""
Implement Encapsulation and Data Validation.
"""


class SecurePlant:
    """
    A class that protects its data from corruption through encapsulation.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialises a plant with valid starting values.
        """
        self.name: str = name
        self.__height: int = height
        self.__age: int = age

    def set_height(self, value: int) -> None:
        """
        Controlled way to modify height with validation.
        """
        magenta = "\033[1;95m"
        cyan = "\033[1;96m"
        white = "\033[1;97m"
        reset = "\033[0m"

        f_name: str = f"{white}{self.name}{reset}"
        accept: str = f"[{cyan}ACCEPTED{reset}]"
        reject: str = f"[{magenta}REJECTED{reset}]"

        if value < 0:
            print(f"\n Invalid operation attempted: height {value} days {reject}")
            print(f" Security: {f_name} negative height rejected")
        else:
            self.__height = value
            print(f"\n Operation successful: height {value}cm {accept}")
            print(f" Security: {f_name} status updated to {value}cm")

    def get_height(self) -> int:
        """
        Safe way to access plant height (height encapsulation).
        """
        return self.__height

    def set_age(self, value: int) -> None:
        """
        Controlled way to modify age with validation.
        """
        magenta = "\033[1;95m"
        cyan = "\033[1;96m"
        white = "\033[1;97m"
        reset = "\033[0m"

        f_name: str = f"{white}{self.name}{reset}"
        accept: str = f"[{cyan}ACCEPTED{reset}]"
        reject: str = f"[{magenta}REJECTED{reset}]"

        if value < 0:
            print(f"\n Invalid operation attempted: age {value} days {reject}")
            print(f" Security: {f_name} negative age rejected")
        else:
            self.__age = value
            print(f"\n Operation successful: age {value} days {accept}")
            print(f" Security: {f_name} status updated to {value}cm")

    def get_age(self) -> int:
        """
        Safe way to access plant age (age encapsulation).
        """
        return self.__age

    def __str__(self) -> str:
        """
        Returns a formatted string representing the current plant status.
        """
        g_height: int = self.get_height()
        g_age: int = self.get_age()
        h_str: str = f"{g_height}cm"
        a_str: str = f"{g_age} days"
        return f" {self.name:<13}{h_str:<13}{a_str:<13}"


def display_header() -> None:
    """
    Displays the factory output header.
    """
    white = "\033[1;97m"
    reset = "\033[0m"

    c1, c2, c3 = "Name", "Height", "Age"

    print(f"\n {white}{c1:<13}{c2:<13}{c3:<13}{reset}")
    print(" --------------------------------------------------------")


def main() -> None:
    white = "\033[1;97m"
    reset = "\033[0m"

    print(f"\n{white} 🌱 Garden Security System: Plant Status{reset}")

    """Initial Creation"""
    rose = SecurePlant("Rose", 25, 30)
    cactus = SecurePlant("Cactus", 5, 90)
    sunflower = SecurePlant("Sunflower", 80, 45)
    fern = SecurePlant("Fern", 15, 120)

    display_header()
    print(rose)
    print(cactus)
    print(sunflower)
    print(fern)

    """Test Cases Section"""
    print(f"\n {white}🌱 Garden Security System: Update Report{reset}")

    """Both valid"""
    rose.set_height(5)
    rose.set_age(37)

    """Only height valid"""
    cactus.set_height(2)
    cactus.set_age(-97)

    """Only age valid"""
    sunflower.set_height(-6)
    sunflower.set_age(52)

    """None valid"""
    fern.set_height(-10)
    fern.set_age(-127)

    """Attempt to access data directly"""
    print(f"\n {white}Direct Access Attempt{reset}")
    try:
        print(f" Attempting to read rose.__height: {rose.__height}")
    except AttributeError:
        print(f" {white}Access Denied{reset}: Attribute is private.")

    """Final Status"""
    print(f"\n {white}🌱 Garden Security System: Plant Status{reset}")
    display_header()
    print(rose)
    print(cactus)
    print(sunflower)
    print(fern)
    print(" ")


if __name__ == "__main__":
    main()
