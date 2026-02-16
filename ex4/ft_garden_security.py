#!/usr/bin/env python3
"""
Implement Encapsulation and Data Validation.
"""


class SecurePlant:
    """Readability colors."""
    m, c, w, r = "\033[1;95m", "\033[1;96m", "\033[1;97m", "\033[0m"

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
        f_name: str = f"{self.w}{self.name}{self.r}"
        accept: str = f"[{self.c}ACCEPTED{self.r}]"
        reject: str = f"[{self.m}REJECTED{self.r}]"

        if value < 0:
            print(f"\n Invalid operation attempted:"
                  f"height {value} days {reject}")
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
        f_name: str = f"{self.w}{self.name}{self.r}"
        accept: str = f"[{self.c}ACCEPTED{self.r}]"
        reject: str = f"[{self.m}REJECTED{self.r}]"

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

    def get_info(self) -> str:
        """Returns a formatted string of the plant's current status."""
        g_height: int = self.get_height()
        g_age: int = self.get_age()
        h_str: str = f"{g_height}cm"
        a_str: str = f"{g_age} days"
        return f" {self.name:<20}{h_str:<20}{a_str:<20}"

    def display_info(self) -> None:
        """Displays the current status of the plant."""
        print(self.get_info())


def display_header() -> None:
    """
    Displays the factory output header.
    """
    w, r = "\033[1;97m", "\033[0m"

    c1, c2, c3 = "Name", "Height", "Age"

    print(f"\n {w}🌱 Garden Security System: Plant Status{r}")
    print(f"\n {w}{c1:<20}{c2:<20}{c3:<20}{r}")
    print(" " + "-" * 60)


def main() -> None:
    w, r = "\033[1;97m", "\033[0m"

    """Initial Creation"""
    rose = SecurePlant("Rose", 25, 30)
    cactus = SecurePlant("Cactus", 5, 90)
    sunflower = SecurePlant("Sunflower", 80, 45)
    fern = SecurePlant("Fern", 15, 120)

    display_header()
    rose.display_info()
    cactus.display_info()
    sunflower.display_info()
    fern.display_info()

    """Test Cases Section"""
    print(f"\n {w}🌱 Garden Security System: Update Report{r}")

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
    print(f"\n {w}Direct Access Attempt{r}")
    try:
        print(f" Attempting to read rose.__height: {rose.__height}")
    except AttributeError:
        print(f" {w}Access Denied{r}: Attribute is private.")

    """Final Status"""
    display_header()
    rose.display_info()
    cactus.display_info()
    sunflower.display_info()
    fern.display_info()
    print(" ")


if __name__ == "__main__":
    main()
