# Python Module 01
**CodeCultivation, Object-Oriented Garden Systems:** learn **Object-Oriented Programming (OOP)** by becoming a digital gardener—because apparently, the best way to understand classes is to grow virtual plants and realize you've been doing OOP all along! 🌱💻

## Instructions
Git clone the repository:
```
git clone https://github.com/spacotto/Python_Module01.git
```
Each file includes a main. Thus, you can directly execute the files. For example:
```
python3 ex/ft_garden_intro.py
```

## Theoretical Concepts

### Script Execution (Shebang)
The shebang (`#!`) is a special directive placed at the very first line of a script (e.g., `#!/usr/bin/env python3`) that tells the operating system which interpreter to use when the file is executed directly from the terminal. When you run a script with `./script.py`, the OS reads this line and locates the correct Python binary to hand off execution to. Without it, you would need to explicitly invoke the interpreter each time by typing `python3 script.py`. It is a Unix/Linux convention but is harmless on Windows, making it a good cross-platform habit.

### The Entry Point (`if __name__ == "__main__":`)
Every Python file has a built-in `__name__` variable. When a file is run directly, Python sets `__name__` to the string `"__main__"`. When the same file is imported as a module into another script, `__name__` is instead set to the file's module name. Wrapping your top-level execution logic in an `if __name__ == "__main__":` block leverages this behavior to create a clear entry point, ensuring that your script's main logic only fires when intentionally executed and not as a side effect of being imported elsewhere.

### Variables and Type Hinting
Python is a dynamically typed language, meaning variables do not require an explicit type declaration. However, PEP 484 introduced optional type hints using the syntax `variable: type = value` (e.g., `age: int = 30`), allowing developers to annotate the expected data type of a variable. These hints are not enforced at runtime but serve as powerful documentation for other developers and enable static analysis tools like `mypy` to catch type-related bugs before the code is ever executed, greatly improving code clarity and maintainability.

### Docstrings
A docstring is a string literal that appears as the very first statement inside a module, class, or function body, enclosed in triple quotes (`"""`). Unlike regular comments, docstrings are stored as the `__doc__` attribute of the object they describe, making them accessible at runtime via `help()`. They serve as the official, in-code documentation for your code's purpose, parameters, and return values. Following conventions like the Google or NumPy docstring styles ensures your documentation is consistent, readable, and compatible with automated documentation generators like Sphinx.

### Standard Output
The built-in `print()` function is Python's primary tool for writing data to the standard output stream (your terminal). It accepts any number of arguments, automatically converts them to strings, and separates them with a space by default, though both the separator (`sep`) and the line-ending character (`end`) are configurable keyword arguments. Python's f-strings (e.g., `f"Hello, {name}!"`) can be passed directly to `print()` to produce clean, formatted, and readable output, making it an essential tool for displaying program results to the user.

### Classes as Blueprints
In object-oriented programming (OOP), a `class` is a user-defined template or blueprint that bundles data (attributes) and functionality (methods) into a single logical unit. Defining a class with the `class` keyword does not create any data itself; instead, it describes the structure that each object created from it will follow. This allows you to instantiate multiple independent objects from one definition, each representing a distinct real-world entity with its own state, while sharing the same set of behaviors defined in the class.

### The `__init__` Method
The `__init__` method is a special "dunder" (double underscore) method in Python that acts as a class's constructor. It is automatically called by Python the moment a new object is instantiated from a class, making it the ideal place to assign initial values to an object's attributes. By accepting parameters in `__init__`, you can ensure that every new object is created with a meaningful and valid starting state, rather than relying on separate setup calls after the object is created.

### Instance Attributes
Instance attributes are variables that are bound to a specific object (instance) of a class rather than to the class itself. They are defined within methods using the `self` prefix (e.g., `self.height = 10`), where `self` is a reference to the particular object being operated on. Because they belong to the instance, each object created from the same class maintains its own independent copy of these attributes, meaning changes to one object's data have no effect on any other object's data.

### PascalCase vs. snake_case
Python's official style guide, PEP 8, defines clear naming conventions to keep codebases consistent and readable. Classes should be named using `PascalCase` (also known as `UpperCamelCase`), where each word begins with a capital letter and no separators are used (e.g., `FloweringPlant`). Functions, methods, and variables, on the other hand, should use `snake_case`, where words are all lowercase and separated by underscores (e.g., `calculate_growth`). Adhering to these conventions signals professionalism and makes it immediately clear from a name alone whether you are referring to a class or a callable.

### Collection Management
Python lists are ordered, mutable sequences that are well-suited for storing and managing multiple objects of the same type. When working with classes, a common pattern is to instantiate multiple objects and store them in a list, then iterate over that list with a `for` loop to apply operations uniformly across all instances. This approach scales cleanly—you can manage two or two thousand objects with the exact same looping logic—and is far more maintainable than tracking each instance in a separate variable.

### Instance Methods
Instance methods are functions defined inside a class body that operate on a specific object. They always receive `self` as their first parameter, which Python automatically passes as a reference to the instance the method was called on. Through `self`, an instance method can read and modify any of the object's attributes, allowing the object to manage and update its own internal state. This keeps related behavior tightly coupled with the data it operates on, which is a foundational principle of OOP.

### Encapsulation of Behavior
Encapsulation of behavior refers to the practice of placing logic that relates to an object's data directly inside the class, rather than writing that logic externally in the main program. For example, instead of calculating a plant's growth outside the class and manually updating its attributes, a `grow()` method defined inside the class handles that entire process internally. This approach makes the object self-sufficient and intelligent—it "knows" how to manage its own lifecycle—and keeps the main program clean and free of low-level implementation details.

### State Mutation
State mutation is the process of changing the internal data of an object over time through method calls. Since instance attributes represent the current state of an object, invoking methods that modify those attributes simulates real-world transitions—such as a plant growing taller or aging by one year. Managing mutations through dedicated methods (rather than direct external attribute modification) ensures that changes always pass through any relevant validation or business logic, keeping the object in a consistent and meaningful state throughout its lifetime.

### Abstraction
Abstraction is the OOP principle of exposing only the necessary interface of an object while hiding the underlying complexity of its implementation. When a class exposes a simple method like `grow()`, the caller does not need to know that it involves updating multiple attributes and running arithmetic calculations—they simply call the method and trust it to work correctly. This separation between "what an object does" and "how it does it" makes code significantly easier to use, read, and maintain, and allows the internal implementation to change without affecting any code that relies on the public interface.

### Looping with Objects
Combining Python's `range()` function with `for` loops provides a clean and readable mechanism for triggering repetitive operations across one or more objects, effectively simulating the passage of time or repeated events in a system. For example, iterating `for year in range(10):` and calling `plant.grow()` inside the loop simulates ten years of growth without duplicating any code. This pattern is especially powerful when applied over a list of objects, allowing you to advance the state of an entire collection of instances simultaneously with minimal code.

### The Constructor (`__init__`)
The `__init__` constructor is the gateway through which every new object enters existence in a valid, initialized state. By defining required parameters in `__init__`, you enforce that the caller must provide the foundational data the object needs to function, preventing the creation of "empty" or incomplete objects that could cause errors later. This guarantee—that an object is always fully configured from the moment it is created—is a cornerstone of robust OOP design, as it eliminates a whole class of bugs related to uninitialized or missing data.

### Parameterized Instantiation
Parameterized instantiation is the practice of passing specific arguments to a class constructor at the time of object creation (e.g., `Plant("Rose", 25, 30)`), allowing a single class blueprint to produce many diverse and distinct instances. Each unique combination of arguments results in an object with its own specific starting data, making the class highly reusable and flexible. This is far superior to creating separate classes for each variation, as all common behavior is defined once and the variability is handled entirely through the data passed in at instantiation time.

### Factory Pattern Logic
The factory pattern is a design concept where a single function or method is responsible for the creation of objects, abstracting away the instantiation details from the rest of the program. Instead of manually writing `Plant(...)` for each new object—which becomes tedious and error-prone at scale—a factory function can accept raw data (e.g., from a list or file), handle any necessary pre-processing, and return fully constructed instances. This centralizes object creation logic into one place, making the codebase easier to modify and dramatically reducing repetition when generating large numbers of objects.

### Encapsulation
Encapsulation is one of the four fundamental pillars of OOP, referring to the practice of bundling an object's data (attributes) and the methods that operate on that data together within a single class, while restricting direct external access to the object's internal state. Rather than allowing outside code to freely read and write an object's attributes, encapsulation encourages interaction through a controlled, well-defined interface of methods. This protects the object's internal integrity, reduces unintended side effects, and creates a clear boundary between an object's public-facing behavior and its private implementation.

### Access Modifiers (Internal Naming)
Python does not have strict access modifiers like `private` or `protected` found in languages such as Java, but it follows a strong naming convention to signal developer intent. Prefixing an attribute name with a double underscore (e.g., `__height`) triggers Python's name mangling, making the attribute harder to access from outside the class and clearly communicating that it is an internal implementation detail not meant for direct external use. This convention serves as a social contract between developers: attributes named this way should be treated as private and accessed only through the class's designated methods.

### Getters and Setters
Getters and setters are methods specifically designed to read and write the values of an object's private or protected attributes, respectively. A getter method (e.g., `get_height()`) simply returns the current value of an attribute, while a setter method (e.g., `set_height(value)`) accepts a new value and assigns it—typically after running validation logic. This pattern gives the class full control over how its data is accessed and modified, allowing it to enforce rules, trigger side effects, or log changes whenever an attribute is read or written, without exposing the attribute directly.

### Data Validation
Data validation is the process of checking that incoming data meets certain criteria before it is stored or used, and it is most commonly embedded within setter methods. For example, a setter for a plant's height might verify that the new value is a positive number before assigning it, rejecting any value that would represent an impossible physical state. By validating data at the point of entry, the class guarantees that its internal attributes always hold meaningful, logically consistent values, preventing subtle bugs that might otherwise only surface much later in program execution.

### Fail-Safe Design
Fail-safe design is the philosophy of writing code that responds gracefully to invalid or unexpected input rather than crashing or silently entering a corrupt state. In practice, this means that when a validation check fails—such as a user attempting to set a plant's height to a negative number—the system should report a clear, descriptive error message and leave the object's state unchanged, rather than raising an unhandled exception or storing the bad value. This approach prioritizes system stability and provides useful feedback to the developer or user, making the overall application far more robust and debuggable.

### Inheritance
Inheritance is an OOP mechanism that allows a new class, called a subclass or child class, to automatically acquire the attributes and methods of an existing class, called the superclass or parent class. This promotes the DRY principle by centralizing shared logic in the parent and allowing subclasses to simply extend or specialize that behavior without rewriting it. The subclass can add its own unique attributes and methods on top of what it inherits, effectively saying "I am everything the parent is, plus more," which creates a natural, logical hierarchy that mirrors real-world categorical relationships.

### The `super()` Function
The `super()` built-in function provides a way for a subclass to delegate method calls up to its parent class, most commonly used inside `__init__` to ensure the parent's constructor is called and the inherited attributes are properly initialized. By calling `super().__init__(...)` with the required arguments, the subclass triggers the parent's setup logic before adding its own unique initialization, preventing code duplication. `super()` is also valuable for method overriding scenarios where the subclass wants to extend rather than completely replace a parent method's behavior.

### Method Specialization
Method specialization is the practice of defining methods in a subclass that are unique to that specific type and have no logical place in the parent class. While a generic `Plant` parent class might define common behaviors like `grow()`, a `FloweringPlant` subclass can define a `bloom()` method that is only meaningful for that category, and a `Tree` subclass might define `produce_shade()`. This keeps the parent class clean and general while allowing each subclass to express behaviors specific to its own nature, resulting in a well-organized hierarchy where each class is responsible only for what is relevant to it.

### Attribute Extension
Attribute extension is the process of a subclass adding new data fields that are specific to its type, on top of the attributes it already inherits from the parent. For example, a `Tree` subclass might inherit `name` and `height` from a `Plant` parent while also defining its own `trunk_diameter` attribute in its `__init__`. This allows the subclass to model more specific real-world details without modifying or polluting the parent class, keeping each level of the hierarchy responsible for only the data that is relevant to its particular level of abstraction.

### DRY Principle (Don't Repeat Yourself)
The DRY principle is a fundamental software engineering guideline stating that every piece of knowledge or logic should have a single, authoritative representation in a codebase. In the context of OOP and inheritance, DRY is achieved by placing shared logic—such as the initialization of common attributes like `name` and `height`—in a parent class once, so that all subclasses can inherit it without rewriting it. Violating DRY by duplicating code across multiple classes creates a maintenance burden where a single logical change must be applied in multiple places, increasing the risk of inconsistencies and bugs.

### Nested Classes (Inner Classes)
A nested class, or inner class, is a class defined inside the body of another class. This technique is used to logically group a helper class that is closely and exclusively tied to its enclosing outer class, signaling to other developers that the inner class has no meaningful existence outside of that context. For instance, a `GardenStats` class nested inside a `Garden` class makes it clear that `GardenStats` is a utility specifically designed to serve `Garden` and should not be used independently. Nesting keeps the outer class's namespace clean while maintaining a clear organizational relationship between the two.

### Class Methods (`@classmethod`)
A class method is a method decorated with `@classmethod` that receives the class itself as its first argument, conventionally named `cls`, rather than a specific instance. This means it can access and modify class-level attributes (shared across all instances) but cannot access instance-specific data. Class methods are ideal for use cases that concern the class as a whole, such as tracking how many instances have been created, providing alternative constructors (factory methods), or resetting class-wide state. They are called on the class directly (e.g., `Garden.get_total()`) rather than on an individual instance.

### Static Methods (`@staticmethod`)
A static method is a method decorated with `@staticmethod` that receives neither the instance (`self`) nor the class (`cls`) as an automatic first argument. It behaves exactly like a regular standalone function but lives inside a class's namespace because it is logically related to the class's purpose. Static methods are appropriate for utility or helper functions that do not need to read or modify any instance or class data—such as a pure mathematical growth calculator—keeping them organized within the relevant class rather than floating as disconnected module-level functions.

### Class Attributes
Class attributes are variables defined directly on the class body, outside of any method, and are shared equally across all instances of that class. Unlike instance attributes (which are unique per object), a class attribute holds a single value that every instance reads from the same source, making them ideal for tracking global or aggregate state, such as a counter of how many objects have ever been created. Modifying a class attribute via the class itself (e.g., `Garden.total_gardens_created += 1`) updates it for all instances simultaneously, whereas assigning to it on an instance would create a new, shadowing instance attribute instead.
