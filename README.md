# Python Class - New Lesson 🚀

Welcome to the **CLASS_NEW_LESSON** repository! This project serves as an introductory guide and hands-on resource for learning **Class Creation** and **Object-Oriented Programming (OOP)** in Python.

---

## 📌 Overview

Object-Oriented Programming (OOP) is a fundamental programming paradigm that models real-world entities using **Classes** and **Objects**.

- **Class:** A blueprint or template defining the structure and behavior.
- **Object:** An instance of a class containing actual data.

---

## 🛠 Features Covered

- **Class Declaration:** How to define a class in Python using the `class` keyword.
- **Constructor (`__init__`):** Initializing instance attributes upon object creation.
- **Methods:** Defining custom functions inside a class to perform specific actions.
- **Instantiation:** Creating and interacting with multiple object instances.

---

## 💻 Code Example

Here is a quick look at how classes are implemented in Python:

```python
class Car:
    """Represents a basic car model."""

    def __init__(self, make: str, model: str, year: int):
        # Initialize instance attributes
        self.make = make
        self.model = model
        self.year = year

    def display_info(self) -> str:
        """Returns formatted string of car details."""
        return f"{self.year} {self.make} {self.model}"


# Instantiate an object
car1 = Car("Chevrolet", "Gentra", 2022)

# Call method
print(car1.display_info())
# Output: 2022 Chevrolet Gentra
