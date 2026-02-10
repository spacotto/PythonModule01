#!/usr/bin/env python3
"""
Building a comprehensive Garden Analytics Platform.
"""

class Plant:
    """Base class for the plant family tree."""
    def __init__(self, name: str, height: int):
        self.name: str = name
        self.height: int = height

    def grow(self) -> None:
        """Instance method to increase height."""
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    """Middle layer of the inheritance chain."""
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color: str = color

    def bloom(self) -> None:
        """Unique behavior for flowering plants."""
        print(f"{self.name} is blooming in {self.color}!")


class PrizeFlower(FloweringPlant):
    """Terminal layer of the inheritance chain."""
    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self.prize_points: int = points


class GardenManager:
    """
    Manages multiple gardens and their analytics.
    """
    # Class-level attribute to track total gardens
    total_gardens: int = 0

    class GardenStats:
        """
        Nested helper class for calculating statistics.
        """
        @staticmethod
        def calculate_total_growth(plant_count: int, growth_per_plant: int) -> int:
            """Static Method: Utility function that doesn't need garden data."""
            return plant_count * growth_per_plant

    def __init__(self, owner_name: str):
        self.owner: str = owner_name
        self.plants: list[Plant] = []
        # Increment global garden count
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        """Instance Method: Adds a plant to this specific manager's collection."""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    @classmethod
    def get_global_report(cls) -> None:
        """Class Method: Operates on the class level to report global state."""
        print(f"Total gardens managed: {cls.total_gardens}")

    def generate_report(self) -> None:
        """Instance Method: Generates a detailed analytics report for one garden."""
        print(f"\n=== {self.owner}'s Garden Report ===")
        print(f"Plants in garden: {len(self.plants)}")
        for p in self.plants:
            status = f"- {p.name}: {p.height}cm"
            if isinstance(p, FloweringPlant):
                status += f", {p.color} flowers"
            if isinstance(p, PrizeFlower):
                status += f" (Prize points: {p.prize_points})"
            print(status)


def main() -> None:
    print("\n 🌱 Garden Management System Demo")
    print(" --------------------------------------------------------")
 
    # 1. Setup Managers
    alice_manager = GardenManager("Alice")
    bob_manager = GardenManager("Bob")

    # 2. Setup Plant Family Tree
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    # 3. Add plants to Alice
    alice_manager.add_plant(oak)
    alice_manager.add_plant(rose)
    alice_manager.add_plant(sunflower)

    # 4. Use Instance Methods
    print(f"{alice_manager.owner} is helping all plants grow...")
    for plant in alice_manager.plants:
        plant.grow()

    # 5. Use Analytics / Reports
    alice_manager.generate_report()
    
    # Use Static Method via Nested Class
    growth = GardenManager.GardenStats.calculate_total_growth(len(alice_manager.plants), 1)
    print(f"Total growth calculated by helper: {growth}cm")

    # 6. Use Class Method
    GardenManager.get_global_report()

if __name__ == "__main__":
    main()
