#!/usr/bin/env python3
"""
Building a comprehensive Garden Analytics Platform.
"""


class Plant:
    """Base class for all plants"""
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age
        self.type: str = "Plant"
        self.__score: int = 10

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int) -> None:
        if age > 0:
            self.__age = age

    def grow(self, days: int) -> None:
        self.__age += days
        print(f" {self.__name} grew {days} day(s).")

    def get_info(self) -> str:
        age_str: str = f"{self.__age} days"
        return f" {self.__name:<15}{age_str:<15}"

    @classmethod
    def get_plant_score(cls) -> int:
        return cls.__score


class FloweringPlant(Plant):
    """A plant that has a color and blooms"""

    def __init__(self, name: str, age: int, color: str) -> None:
        super().__init__(name, age)
        self.__color = color
        self.type: str = "FloweringPlant"
        self.__score: int = 20

    def get_color(self) -> str:
        return self.__color

    def bloom(self) -> None:
        print(f"\n 🌱 {self.get_name()} is blooming beautifully!")

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}{self.__color:<15}"

    @classmethod
    def get_plant_score(cls) -> int:
        return cls.__score


class PrizeFlower(FloweringPlant):
    """A flowering plant that socred prize points"""

    def __init__(self, name: str, age: int, color: str, prize_points: int) -> None:
        super().__init__(name, age, color)
        self.__prize_points = prize_points
        self.type: str = "PrizeFlower"
        self.__score: int = 10 + prize_points

    def get_prize_points(self) -> int:
        return self.__prize_points

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}{self.__prize_points:<10}"

    @classmethod
    def get_plant_score(cls) -> int:
        return cls.__score


class Garden:
    """Container for Plant objects"""
    def __init__(self, garden_name: str, owner_name: str) -> None:
        self.__name = garden_name
        self.__owner = owner_name
        self.__plants: list[Plant] = []
        self.__total_growth = 0

    def get_garden_name(self) -> str:
        return self.__name

    def get_owner_name(self) -> str:
        return self.__owner

    def plants(self) -> list[Plant]:
        return self._plants

    def add_growth(self, days: int) -> None:
        """Accumulate total growth days for this garden"""
        self.__total_growth += days

    def get_total_growth(self) -> int:
        """Retrieve the accumulated growth days"""
        return self.__total_growth


class GardenManager:
    """Manages multiple gardens and provides analytics"""
    def __init__(self):
        self.__network = [] 

    def create_garden_network(self) -> None:
        self.__network = []

    def create_garden(self, garden_name: str, owner_name: str) -> Garden:
        """Creates a Garden that had its owner's name"""
        new_garden = Garden(garden_name, owner_name)
        self.__network += [new_garden]
        return new_garden

    def add_plant(self, owner: str, garden: str, plant_obj: Plant) -> None:
        """
        Retrieves the garden list from the network list and adds the plant.
        """
        for target_garden in self.__network:
            """Check if the target Garden list is present in Networn list"""
            if target_garden.get_garden_name() == garden:
                target_garden.plants += [plant_obj]
                print(f" Added {plant_obj.get_name()} to {owner}'s garden")
                return
        print(f"Error: No garden found for {garden}")

    def grow_garden(self, garden_name: str, days: int) -> int:
        """Executes grow on all plants within a specific garden"""
        for target_garden in self.__network:
            if target_garden.get_garden_name() == garden_name:
                owner = target_garden.get_owner_name()
                print(f"\n 🌱 {owner} is helping all plants grow...")
                for plant in target_garden.plants:
                    plant.grow(days)
                    target_garden.add_growth(days) 
                return days
        print(f"Error: Garden '{garden_name}' not found in network.")

    class GardenStats:
        """Nested helper class for calculating garden statistics"""
        def __init__(self, manager: 'GardenManager'):
            self.__manager = manager

        def count_plants(self, garden_name: str) -> int:
            """Counts how many Plants are in a Garden"""
            counter = 0
            for target_garden in self.__manager._GardenManager__network:
                if target_garden.get_garden_name() == garden_name:
                    for plant in target_garden.plants:
                        if plant.type == "Plant":
                            counter += 1
            return counter

        def count_flowring_plants(self, garden_name: str) -> int:
            """Counts how many FloweringPlant are in a Garden"""
            counter = 0
            for target_garden in self.__manager._GardenManager__network:
                if target_garden.get_garden_name() == garden_name:
                    for plant in target_garden.plants:
                        if plant.type == "FloweringPlant":
                            counter += 1
            return counter

        def count_prize_flowers(self, garden_name: str) -> int:
            """Counts how many PrizeFlower are in a Garden"""
            counter = 0
            for target_garden in self.__manager._GardenManager__network:
                if target_garden.get_garden_name() == garden_name:
                    for plant in target_garden.plants:
                        if plant.type == "PrizeFlower":
                            counter += 1
            return counter

        def count_total_plants(self, garden_name: str) -> int:
            """Calculates how many plants are in the garden"""
            plants = 0
            for target_garden in self.__manager._GardenManager__network:
                if target_garden.get_garden_name() == garden_name:
                    for _ in target_garden.plants:
                        plants += 1
            return plants

        def calculate_growth(self, garden_name: str) -> None:
            """Display total growth days of all plants in a garden"""
            growth = 0
            for target_garden in self.__manager._GardenManager__network:
                if target_garden.get_garden_name() == garden_name:
                    growth = target_garden.get_total_growth()
            return growth

        def display_plants_list(self, garden_name: str) -> None:
            """Displays the list of plants and their data in a target garden"""
            w = "\033[1;97m"
            r = "\033[0m"
            c1, c2, c3, c4 = "Plant", "Age", "Color", "Points"
            for target_garden in self._GardenStats__manager._GardenManager__network:
                """Searches for the target garden in the network"""
                if target_garden.get_garden_name() == garden_name:
                    print(f"\n {w}{c1:<15}{c2:<15}{c3:<15}{c4:<15}{r}")
                    print(" --------------------------------------------------------")
                    for plant in target_garden.plants:
                        print(plant.get_info())
                    return
            print(f"Error: Garden '{garden_name}' not found for report.")

        def display_garden_report(self, garden_name: str) -> None:
            """Displays all the stats of a target Garden"""
            w = "\033[1;97m"
            r = "\033[0m"
            """ Retrieve stats using your existing methods"""
            total_added = self.count_total_plants(garden_name)
            total_growth = self.calculate_growth(garden_name)
            """Retrieve specific type counts"""
            regular = self.count_plants(garden_name)
            flowering = self.count_flowring_plants(garden_name)
            prize = self.count_prize_flowers(garden_name)
            """Find the owner of the Garden"""
            owner_name = "Unknown"
            for target_garden in self.__manager._GardenManager__network:
                if target_garden.get_garden_name() == garden_name:
                    owner_name = target_garden.get_owner_name()
                    break
            """Display the report"""
            print(f"\n{w} 🌱 {owner_name}'s Garden Report 🌱{r}")
            self.display_plants_list(garden_name)
            print(f"\n Plants added: {total_added}, Total growth: {total_growth} day(s)")
            print(f" Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers")
            print(" ")

    def check_age_integrity(self) -> bool:
        """Validates age > 0 for all plants in the network"""
        valid = True
        for garden in self._GardenManager__network:
            for plant in garden.plants:
                if plant.get_age() <= 0:
                    valid = False
        return valid

    def calculate_garden_score(self, garden: Garden) -> int:
        """Calculates the total score: sum of plant type scores + sum of ages."""
        total_score = 0
        for plant in garden.plants:
            """Get points based on the plant's class/type"""
            if plant.type == "PrizeFlower":
                total_score += plant.get_prize_flower_score()
            elif plant.type == "FloweringPlant":
                total_score += plant.get_flowering_plant_score()
            else:
                total_score += plant.get_plant_score()
            """Add the plant's age to the total score"""
            total_score += plant.get_age()
        return total_score

    def get_network_count(self) -> int:
        """Helper to count gardens without len()"""
        count = 0
        for _ in self._GardenManager__network:
            count += 1
        return count

    def display_garden_scores(self) -> None:
        """Display the scores of the gardens in the network"""
        w = "\033[1;97m"
        r = "\033[0m"
        """Print header"""
        t1, t2, t3 = "Garden", "Owner", "Score" 
        print(f"\n {w}{t1:<18}{t2:<18}{t3:<18}{r}")
        print(" --------------------------------------------------------")
        """Calculate garden scores"""
        for garden in self.__network:
            name = garden.get_garden_name()
            owner = garden.get_owner_name()
            score = self.calculate_garden_score(garden)
            print(f" {name:<18}{owner:<18}{score:<18}")
        """Total gardens managed"""
        network = "Total gardens managed"
        gardens = self.get_network_count()
        print(" --------------------------------------------------------")
        print(f" {w}{network}{r}: {gardens}")

    def display_network_report(self) -> None:
        """Displays stats for the entire garden network."""
        w = "\033[1;97m"
        r = "\033[0m"
        """Print report"""
        print(f" {w}🌱 Network Analytics Report 🌱{r}")
        self.check_age_integrity()
        self.display_garden_scores()
        print(" ")


def main() -> None:
    w = "\033[1;97m"
    r = "\033[0m"

    """Initialize manager, network, and stats"""
    manager = GardenManager()
    manager.create_garden_network()
    stats = GardenManager.GardenStats(manager)

    """Create a Garden via the manager"""
    manager.create_garden("Wonderland", "Alice")
    manager.create_garden("Backyard", "Bob")

    """Instantiate plants"""
    oak = Plant("Oak Tree", 101)
    rose = FloweringPlant("Rose", 26, "Red")
    sunflower = PrizeFlower("Sunflower", 51, "Yellow", 10)

    ash = Plant("Ash", 15)
    tulip = FloweringPlant("Tulip", 10, "Yellow")
    orchid = PrizeFlower("Orchid", 5, "Purple", 50)

    """Start Garden Demo"""
    print(f"\n{w} 🌱 Garden Management System Demo 🌱{r}\n")

    """Add plants to the garden in the network"""
    manager.add_plant("Alice", "Wonderland", oak)
    manager.add_plant("Alice", "Wonderland", rose)
    manager.add_plant("Alice", "Wonderland", sunflower)

    manager.add_plant("Bob", "Backyard", ash)
    manager.add_plant("Bob", "Backyard", tulip)
    manager.add_plant("Bob", "Backyard", orchid)

    """Execute grow on all the plants in target Garden"""
    manager.grow_garden("Wonderland", 1)

    """Garden Report"""
    stats.display_garden_report("Wonderland")

    """Network Report"""
    manager.display_network_report()


if __name__ == "__main__":
    main()
