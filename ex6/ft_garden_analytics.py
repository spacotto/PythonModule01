#!/usr/bin/env python3
"""
Building a comprehensive Garden Analytics Platform.
"""


class Plant:
    """Base class for all plants"""
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age_days):
        if age > 0:
            self.__age = age

    def get_info(self):
        return f"{self.__name} (Age: {self.__age} days)"

    def grow(self, days=1):
        """Increase plant age"""
        self.__age += days
        print(f"{self.__name} grew {days} day(s). Now {self.__age} days old.")

    @staticmethod
    def get_plant_score():
        """Base score for a Plant"""
        return 10


class FloweringPlant(Plant):
    """A plant that has a color and can bloom"""

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.__color = color
        self.__is_blooming = False

    def get_color(self):
        return self.__color

    def is_blooming(self):
        return self.__is_blooming

    def set_blooming(self, status):
        self.__is_blooming = status

    def bloom(self):
        """Make the plant bloom"""
        if Plant.is_mature(self.get_age(), maturity_days=180):
            self.__is_blooming = True
            print(f"{self.get_name()} is now blooming with beautiful {self.__color} flowers!")
        else:
            print(f"{self.get_name()} is too young to bloom (needs 180+ days)")

    @staticmethod
    def get_flowering_plant_score():
        """Base score for a FloweringPlant"""
        return 20


class PrizeFlower(FloweringPlant):
    """A flowering plant that socred prize points"""

    def __init__(self, name, age, color, prize_points=0):
        super().__init__(name, age, color)
        self.__prize_points = prize_points

    def get_prize_points(self):
        return self.__prize_points

    def get_info(self):
        """Return prize flower information"""
        base_info = super().get_info()
        return f"{base_info}, Prize Points: {self.__prize_points}"

    @staticmethod
    def get__prize_flower_score():
        """Base score for a PrizeFlower"""
        return 30


class Garden:
    """Represents a garden with plants and statistics"""
    def __init__(self, name, location, size_sqm):
        self.__name = name
        self.__plants = []

    def get_name(self):
        return self.__name

    def get_plants(self):
        return self.__plants.copy()  # Return a copy

    def add_plant(self, plant_obj):
        """Add a plant to the garden"""
        self.__plants.append(plant_obj)
        print(f"Added {plant_obj.get_name()} to {self.__name}")

    def get_plant_count(self):
        """Return the number of plants"""
        return len(self.__plants)

    def get_flowering_plants(self):
        """Return only FloweringPlant and PrizeFlower objects"""
        return [p for p in self.__plants if isinstance(p, FloweringPlant)]

    def get_prize_flowers(self):
        """Return only PrizeFlower objects"""
        return [p for p in self.__plants if isinstance(p, PrizeFlower)]

    def get_plant_type_count(self):
        """Count plants by type"""
        regular_plants = 0
        flowering_plants = 0
        prize_flowers = 0

        for plant in self.__plants:
            if isinstance(plant, PrizeFlower):
                prize_flowers += 1
            elif isinstance(plant, FloweringPlant):
                flowering_plants += 1
            else:
                regular_plants += 1

        return {
            'Plant': regular_plants,
            'FloweringPlant': flowering_plants,
            'PrizeFlower': prize_flowers
        }

    def generate_report(self):
        """Generate comprehensive garden report"""
        print(f"\n{'='*60}")
        print(f"GARDEN REPORT: {self.__name}")
        print(f"{'='*60}")

        print(f"\nPLANT LIST ({len(self.__plants)} total):")
        print(f"{'-'*60}")
        for i, plant in enumerate(self.__plants, 1):
            print(f"{i}. {plant.get_info()}")

        type_counts = self.get_plant_type_count()
        print(f"\n{'-'*60}")
        print("PLANT TYPE BREAKDOWN:")
        for plant_type, count in type_counts.items():
            print(f"  • {plant_type}: {count}")

        print(f"{'='*60}\n")

    def calculate_score(self):
        """Calculate garden score based on plants"""
        total_score = 0

        for plant in self.__plants:
            if isinstance(plant, PrizeFlower):
                total_score += PrizeFlower.get_base_score()
                total_score += plant.get_prize_points()
            elif isinstance(plant, FloweringPlant):
                total_score += FloweringPlant.get_base_score()
            else:
                total_score += Plant.get_base_score()

            total_score += plant.get_age()

        return total_score


class GardenManager:
    """Manages multiple gardens and provides analytics"""

    class GardenStats:
        """Nested helper class for calculating garden statistics"""

        def __init__(self):
            self.__data_points = []

        def add_data(self, value):
            """Add a data point to the statistics tracker"""
            self.__data_points.append(value)

        def clear_data(self):
            """Clear all data points"""
            self.__data_points = []

        def get_data_count(self):
            """Get number of data points"""
            return len(self.__data_points)

        @staticmethod
        def calculate_average(values):
            """Calculate average of a list of values"""
            if not values:
                return 0
            return sum(values) / len(values)

        @staticmethod
        def calculate_min_max(values):
            """Return minimum and maximum values"""
            if not values:
                return None, None
            return min(values), max(values)

        @staticmethod
        def calculate_total(values):
            """Calculate total sum of values"""
            return sum(values) if values else 0

        def get_summary(self):
            """Get statistical summary of collected data"""
            if not self.__data_points:
                return "No data available"

            avg = GardenManager.GardenStats.calculate_average(self.__data_points)
            min_val, max_val = GardenManager.GardenStats.calculate_min_max(self.__data_points)
            total = GardenManager.GardenStats.calculate_total(self.__data_points)

            return f"Count: {len(self.__data_points)}, Total: {total}, Avg: {avg:.2f}, Min: {min_val}, Max: {max_val}"


    def __init__(self, manager_name):
        self.__manager_name = manager_name
        self.__gardens = {}
        self.__stats = GardenManager.GardenStats()

    def get_manager_name(self):
        return self.__manager_name

    def get_garden_count(self):
        """Return number of gardens in the network"""
        return len(self.__gardens)

    def add_garden(self, garden_name, garden_obj):
        """Add a garden to the manager"""
        self.__gardens[garden_name] = garden_obj
        print(f"Garden '{garden_name}' added to {self.__manager_name}")

    def get_garden(self, garden_name):
        """Retrieve a garden by name"""
        return self.__gardens.get(garden_name, None)

    def list_gardens(self):
        """List all managed gardens"""
        print(f"\n{self.__manager_name} manages {len(self.__gardens)} garden(s):")
        for name in self.__gardens:
            print(f"  - {name}")

    def calculate_all_garden_scores(self):
        """Calculate and display scores for all gardens"""
        print(f"\n{'='*60}")
        print(f"GARDEN NETWORK SCORES - {self.__manager_name}")
        print(f"{'='*60}")

        scores = {}
        for garden_key, garden in self.__gardens.items():
            score = garden.calculate_score()
            scores[garden_key] = score
            print(f"  {garden.get_name()}: {score} points")

        # Update stats
        self.__stats.clear_data()
        for score in scores.values():
            self.__stats.add_data(score)

        print(f"\n  Statistics: {self.__stats.get_summary()}")
        print(f"{'='*60}\n")

        return scores

    def generate_network_report(self):
        """Generate comprehensive report for entire network"""
        print(f"\n{'#'*60}")
        print(f"GARDEN NETWORK REPORT: {self.__manager_name}")
        print(f"Total Gardens in Network: {self.get_garden_count()}")
        print(f"{'#'*60}\n")

        for garden_key, garden in self.__gardens.items():
            garden.generate_report()

        self.calculate_all_garden_scores()

    @classmethod
    def create_default_manager(cls):
        """Factory method to create a default garden manager"""
        return cls("Default Garden Manager")

    @classmethod
    def create_garden_network(cls, network_name, garden_data_list):
        """
        Factory method to create a manager with multiple gardens

        garden_data_list format: [
            ('garden_key', 'Garden Name', 'Location', size_sqm),
            ...
        ]
        """
        manager = cls(network_name)

        for garden_key, name, location, size in garden_data_list:
            garden = Garden(name, location, size)
            manager.add_garden(garden_key, garden)

        print(f"\nGarden network '{network_name}' created with {len(garden_data_list)} gardens!")
        return manager

    @staticmethod
    def calculate_network_diversity_score(manager):
        """Utility function to calculate diversity across network"""
        total_plant_types = 0
        total_flowering = 0
        total_prize = 0

        for garden_key in manager._GardenManager__gardens:
            garden = manager.get_garden(garden_key)
            type_counts = garden.get_plant_type_count()
            total_plant_types += type_counts['Plant']
            total_flowering += type_counts['FloweringPlant']
            total_prize += type_counts['PrizeFlower']

        total_plants = total_plant_types + total_flowering + total_prize

        if total_plants == 0:
            return 0

        # Diversity score based on variety
        diversity = (total_plant_types > 0) + (total_flowering > 0) + (total_prize > 0)
        return (diversity / 3.0) * 100  # Percentage


def main() -> None:
    # Create a garden network using the class method
    network_data = [
        ('alice', "Alice's Garden", "Backyard", 50),
        ('bob', "Bob's Garden", "Rooftop", 30)
    ]
    
    manager = GardenManager.create_garden_network("Community Garden Network", network_data)
    
    # Get gardens from network
    alice_garden = manager.get_garden('alice')
    bob_garden = manager.get_garden('bob')
    
    # Add plants to Alice's garden
    alice_garden.add_plant(Plant("Oak Sapling", 365))
    alice_garden.add_plant(FloweringPlant("Red Tulip", 200, "red"))
    alice_garden.add_plant(PrizeFlower("Champion Rose", 500, "crimson", 75))
    alice_garden.add_plant(PrizeFlower.create_champion("Golden Orchid", "golden"))
    
    # Add plants to Bob's garden
    bob_garden.add_plant(Plant("Pine Tree", 730))
    bob_garden.add_plant(FloweringPlant("Blue Iris", 150, "blue"))
    bob_garden.add_plant(PrizeFlower("Prize Lily", 300, "white", 45))
    
    # Generate individual garden reports
    alice_garden.generate_report()
    bob_garden.generate_report()
    
    # Calculate scores for all gardens in network
    manager.calculate_all_garden_scores()
    
    # Compare two gardens directly
    Garden.compare_gardens(alice_garden, bob_garden)
    
    # Generate full network report
    manager.generate_network_report()
    
    # Calculate network diversity
    diversity_score = GardenManager.calculate_network_diversity_score(manager)
    print(f"Network Diversity Score: {diversity_score:.1f}%")
    
    # Show garden count
    print(f"\nTotal gardens in network: {manager.get_garden_count()}")

if __name__ == "__main__":
    main()
