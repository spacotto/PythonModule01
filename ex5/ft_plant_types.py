#!/usr/bin/env python3
"""
Implement Inheritance for specialised plant types.
"""


class Plant:
    """Base class for all garden plants."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialises common plant features."""
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    """Specialised plant that can bloom."""
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Uses super() to initialize common attributes and adds color."""
        super().__init__(name, height, age)
        self.type: str = "Flower"
        self.color: str = color

    def bloom(self) -> None:
        """Displays a blooming message."""
        print(f"\n 🌱 {self.name} is blooming beautifully!")


class Tree(Plant):
    """Specialised plant that provides shade."""
    def __init__(self, name: str, height: int, age: int,
                 diameter: int) -> None:
        """Adds trunk_diameter to the base plant."""
        super().__init__(name, height, age)
        self.type: str = "Tree"
        self.trunk_diameter: int = diameter

    def produce_shade(self) -> None:
        """Calculates and displays shade area."""
        shade_area = self.trunk_diameter * 1.5
        print(f"\n 🌱 {self.name} provides {shade_area} square meters of shade")


class Vegetable(Plant):
    """Specialised plant for harvesting."""
    def __init__(self, name: str, h: int, a: int,
                 harvest_time: str, nutriscore: str) -> None:
        """Adds harvest season and nutritional value."""
        super().__init__(name, h, a)
        self.type: str = "Vegetable"
        self.harvest_season: str = harvest_time
        self.nutritional_value: str = nutriscore

    def harvest_info(self) -> None:
        """Displays nutritional information."""
        print(f"\n 🌱 {self.name} is rich in {self.nutritional_value}")


def main() -> None:
    """Colors"""
    white = "\033[1;97m"
    reset = "\033[0m"

    """Titles"""
    f1 = "Name"
    f2 = "Height"
    f3 = "Age"
    f4 = "Color"
    f5 = "Diameter"
    f6 = "Harvest Season"
    f7 = "Nutritional Value"

    """Printing"""
    print(f"\n {white}🌱 Garden Plant Types{reset}")
    print(" --------------------------------------------------------\n")

    rose = Flower("Rose", 25, 30, "Red")
    print(f" {white}{f1:<20}{reset}{rose.name} ({rose.type})")
    print(f" {white}{f2:<20}{reset}{rose.height}cm")
    print(f" {white}{f3:<20}{reset}{rose.age} days")
    print(f" {white}{f4:<20}{reset}{rose.color}")
    rose.bloom()

    print("\n --------------------------------------------------------\n")

    sunflower = Flower("Sunflower", 80, 45, "Yellow")
    print(f" {white}{f1:<20}{reset}{sunflower.name} ({sunflower.type})")
    print(f" {white}{f2:<20}{reset}{sunflower.height}cm")
    print(f" {white}{f3:<20}{reset}{sunflower.age} days")
    print(f" {white}{f4:<20}{reset}{sunflower.color}")
    sunflower.bloom()

    print("\n --------------------------------------------------------\n")

    oak = Tree("Oak", 500, 1825, 50)
    print(f" {white}{f1:<20}{reset}{oak.name} ({oak.type})")
    print(f" {white}{f2:<20}{reset}{oak.height}cm")
    print(f" {white}{f3:<20}{reset}{oak.age} days")
    print(f" {white}{f5:<20}{reset}{oak.trunk_diameter}")
    oak.produce_shade()

    print("\n --------------------------------------------------------\n")

    bonsai = Tree("Bonsai", 15, 3650, 5)
    print(f" {white}{f1:<20}{reset}{bonsai.name} ({bonsai.type})")
    print(f" {white}{f2:<20}{reset}{bonsai.height}cm")
    print(f" {white}{f3:<20}{reset}{bonsai.age} days")
    print(f" {white}{f5:<20}{reset}{bonsai.trunk_diameter}")
    bonsai.produce_shade()

    print("\n --------------------------------------------------------\n")

    tomato = Vegetable("Tomato", 80, 90, "Summer", "Vitamin C")
    print(f" {white}{f1:<20}{reset}{tomato.name} ({tomato.type})")
    print(f" {white}{f2:<20}{reset}{tomato.height}cm")
    print(f" {white}{f3:<20}{reset}{tomato.age} days")
    print(f" {white}{f6:<20}{reset}{tomato.harvest_season}")
    print(f" {white}{f7:<20}{reset}{tomato.nutritional_value}")
    tomato.harvest_info()

    print("\n --------------------------------------------------------\n")

    carrot = Vegetable("Carrot", 20, 70, "Autumn", "Vitamin A")
    print(f" {white}{f1:<20}{reset}{carrot.name} ({carrot.type})")
    print(f" {white}{f2:<20}{reset}{carrot.height}cm")
    print(f" {white}{f3:<20}{reset}{carrot.age} days")
    print(f" {white}{f6:<20}{reset}{carrot.harvest_season}")
    print(f" {white}{f7:<20}{reset}{carrot.nutritional_value}")
    carrot.harvest_info()

    print("\n --------------------------------------------------------")
    print(f" {white}🌱 End of Garden Plant Types List{reset}\n")


if __name__ == "__main__":
    main()
