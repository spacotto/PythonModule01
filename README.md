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


### Exercise 4: Garden Security System


### Exercise 5: Specialised Plant Types


### Exercise 6: Garden Analytics Platform
