#!/usr/bin/env python3
"""
Implementing Encapsulation and Data Validation.
"""


class SecurePlant:
    """
    A class that protects its data from corruption through encapsulation.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialises a plant while ensuring valid starting values (setter methods).
        """
        self.name: str = name
        self._height: int = 0
        self._age: int = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> int:
        """
        Safe way to access plant height (height encapsulation).
        """
        return self._height

    def set_height(self, value: int) -> None:
        """
        Controlled way to modify height with validation.
        """
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = value
            print(f"Height updated: {value}cm [OK]")

    def get_age(self) -> int:
        """
        Safe way to access plant age (age encapsulation).
        """
        return self._age

    def set_age(self, value: int) -> None:
        """
        Controlled way to modify age with validation.
        """
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = value
            print(f"Age updated: {value} days [OK]")

    def display_status(self) -> None:
        """
        Displays the current secure status of the plant.
        """
        print(f"Current plant: {self.name} ({self._height}cm, {self._age} days)")


def main() -> None:
    print("=== Garden Security System ===")
    
    # Create a plant
    rose = SecurePlant("Rose", 25, 30)
    print(f"Plant created: {rose.name}")

    # Test valid updates
    rose.set_height(35)
    rose.set_age(40)

    # Test invalid updates (Requirement: Print error messages for invalid values)
    rose.set_height(-5)
    rose.set_age(-10)

    # Final status check
    rose.display_status()


if __name__ == "__main__":
    main()
