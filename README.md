# Python Module 01: CodeCultivation
**CodeCultivation: Object-Oriented Garden Systems** is a Python-based project designed to transition learners from basic procedural programming to advanced Object-Oriented Programming (OOP) architectures. By building a digital garden ecosystem, students develop tools for community garden management, starting with simple program structures and progressing through complex data modelling. The curriculum emphasises practical skills such as **data encapsulation**, **inheritance**, and **system scalability**.

## Instructions

## Exercises
### Exercise 0: Planting Your First Seed
* **Entry Point Execution**: Understanding how Python identifies the main script being run.
* **Namespace Protection**: The logic behind the `if __name__ == "__main__":` block to prevent code execution during imports.
* **Standard Output**: Using `print()` to interface with the user terminal.
* **Variable Scope**: Storing basic data types in a local or global context.

### Exercise 1: Garden Data Organiser
* **Class Definition**: Creating a "blueprint" (Class) to represent real-world objects.
* **Object Instantiation**: Turning a class blueprint into unique physical entities (Instances).
* **Naming Conventions**: Applying PascalCase for classes and snake_case for attributes/functions.
* **Data Structures**: Using lists or objects to store and organise multiple records efficiently.

### Exercise 2: Plant Growth Simulator
* **Instance Methods**: Designing behaviours (functions) that allow an object to act upon itself.
* **State Mutation**: The theory of how an object's internal attributes (height, age) change over its lifecycle.
* **Type Hinting**: Implementing static type annotations to define expected input and output data.

### Exercise 3: Plant Factory
* **Constructors**: Understanding the `__init__` method's role in setting up an object's initial state.
* **Object Initialisation**: Efficiently assigning unique starting values during the creation process.
* **Scalable Creation**: The theory behind automating the generation of multiple object instances.

### Exercise 4: Garden Security System

* **Encapsulation**: Protecting internal data from direct external access to maintain integrity.
* **Validation Logic**: Implementing "gatekeeper" methods (setters) to reject invalid or impossible data.
* **Information Hiding**: The principle of exposing only necessary interfaces while hiding implementation details.

### Exercise 5: Specialised Plant Types

* **Inheritance (Is-A Relationship)**: Extending a base "Parent" class to create specialised "Child" classes.
* **Code Reusability**: Using inheritance to share common features without duplicating code across types.
* **Superclass Access**: Utilizing `super().__init__()` to properly initialize inherited attributes from parent classes.

### Exercise 6: Garden Analytics Platform
* **Composition**: Nesting classes (like `GardenStats` inside `GardenManager`) to manage complex relationships.
* **Method Scoping**: 
    * **Class Methods**: Logic that belongs to the class itself rather than a specific instance.
    * **Static Methods**: Utility functions that are grouped within a class for organisation but don't access state.
* **Multi-level Inheritance**: Building deep hierarchies (Plant → FloweringPlant → PrizeFlower).
* **System Architecture**: Organising multiple interacting components into a cohesive ecosystem.
