# Python Module 01: CodeCultivation, Object-Oriented Garden Systems
This module provides a structured pedagogical path that transitions students from basic Python execution to designing complex, scalable software architectures. By incrementally building a garden management system, it ensures that learners first master fundamental program structures (such as the `if __name__ == "__main__":` block) before introducing the more abstract concepts of **Object-Oriented Programming (OOP)** like **encapsulation**, **inheritance**, and **polymorphism**. The project requires students to implement **data validation** and **secure interfaces** to **prevent system corruption**.

## Instructions

## Exercises
### Exercise 0: Planting Your First Seed
* **Script Execution (Shebang)**: Understanding how the computer locates the Python interpreter to run the file (often marked by `#!` at the very top of a script).
* **The Entry Point (`if __name__ == "__main__":`)**: This pattern ensures that code inside the block only runs when the script is executed directly, preventing accidental execution when the file is imported as a module.
* **Variables and Type Hinting**: Using `variable: type = value` (e.g., `age: int = 30`) provides explicit documentation for the data types, aiding in code clarity and error prevention.
* **Docstrings**: Multi-line strings used at the start of modules and functions to describe their purpose and behavior.
* **Standard Output**: Utilizing the `print()` function to present formatted data to the user.

### Exercise 1: Garden Data Organiser
* **Classes as Blueprints**: Using the `class` keyword to define a template that represents real-world objects, allowing for the creation of multiple distinct instances with the same structure.
* **The `__init__` Method**: A special Python method (**constructor**) used to initialize an object's state by assigning values to its attributes when the object is created.
* **Instance Attributes**: Variables prefixed with `self` that belong to a specific instance of a class, ensuring each plant has its own unique data (e.g., its own height and age).
* **PascalCase vs. snake_case**: Adhering to Python naming conventions where classes use `PascalCase` and functions/variables use `snake_case` for professional readability.
* **Collection Management**: Using data structures like lists to store and iterate over multiple class instances efficiently.

### Exercise 2: Plant Growth Simulator
* **Instance Methods**: Functions defined inside a class that operate on instances of that class. They use the `self` parameter to access and modify the object's specific attributes.
* **Encapsulation of Behavior**: Moving logic (like growth calculations) inside the class rather than handling it in the main execution block. This ensures the object "knows" how to manage its own lifecycle.
* **State Mutation**: The process of changing an object's internal data (attributes) over time through method calls, representing real-world transitions like aging or physical growth.
* **Abstraction**: Providing a simple interface (like `grow()`) that hides the internal arithmetic from the user, making the code more readable and maintainable.
* **Looping with Objects**: Using `range()` and loops to trigger repetitive behaviors across class instances, simulating the passage of time in a system.

### Exercise 3: Plant Factory
* **The Constructor (`__init__`)**: A special method used to assign values to an object's attributes the moment it is created, ensuring the object is always in a valid starting state.
* **Parameterized Instantiation**: Passing specific arguments during object creation (e.g., `Plant("Rose", 25, 30)`) to allow for diverse instances from a single blueprint.
* **The `__str__` Dunder Method**: A "magic method" that defines how an object should be represented as a string, making it easier to print object information cleanly.
* **Factory Pattern Logic**: The concept of streamlining object creation to handle large volumes of data efficiently without repetitive manual assignments.

### Exercise 4: Garden Security System
* **Encapsulation**: The practice of bundling data and the methods that operate on that data into a single unit (the class) and restricting direct access to some of the object's components.
* **Access Modifiers (Internal Naming)**: Using a double underscore prefix (e.g., `__height`) as a convention to signal that an attribute is "protected" or intended for internal use only.
* **Getters and Setters**: Methods used to safely retrieve (`get`) and modify (`set`) the values of private/protected attributes, providing a layer of abstraction between the user and the data.
* **Data Validation**: Logic embedded within setter methods to ensure that only "clean" or "valid" data is stored, protecting the system from logical errors like negative physical dimensions.
* **Fail-Safe Design**: Programming the system to handle incorrect input by reporting an error (e.g., printing a rejection message) rather than crashing or allowing the state to become inconsistent.

### Exercise 5: Specialised Plant Types
* **Inheritance**: A mechanism where a new class (subclass) derives attributes and behaviors from an existing class (parent), facilitating code reuse and logical hierarchy.
* **The `super()` Function**: A built-in function that allows a subclass to call methods from its parent class, most commonly used to trigger the parent's `__init__` constructor.
* **Method Specialization**: Defining unique methods in subclasses (like `bloom()` or `produce_shade()`) that are only relevant to that specific type, not the general parent class.
* **Attribute Extension**: Adding specific data fields to a subclass (e.g., `trunk_diameter`) while still maintaining the common fields inherited from the base class.
* **DRY Principle (Don't Repeat Yourself)**: Using inheritance to avoid duplicating common code (like name/height initialization) across multiple related classes.

### Exercise 6: Garden Analytics Platform
