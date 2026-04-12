# OOPs-inheritance
A structured reference covering Python's inheritance system with clean, runnable examples.

# Table of Contents
<br>
1.Inheritance
<br>
2.Multiple Inheritance
<br>
3.Multilevel Inheritance
<br>
4.super()
<br>
5.Instance Methods, Class Methods & Static Methods
<br>
6.Property Decorators
<br>
7.Operator Overloading

## Inheritance
A child class inherits attributes and methods from a parent class, allowing code reuse and extension.
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."


class Dog(Animal):
    def speak(self):                        # overrides parent method
        return f"{self.name} says: Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"


dog = Dog("Rex")
cat = Cat("Whiskers")

print(dog.speak())   # Rex says: Woof!
print(cat.speak())   # Whiskers says: Meow!
print(dog.name)      # Rex  ← inherited from Animal
```
**Key rule:** If the child defines a method with the same name as the parent, it overrides it.

## Multiple Inheritance
A class can inherit from more than one parent class.
```python
class Flyable:
    def fly(self):
        return "I can fly!"


class Swimmable:
    def swim(self):
        return "I can swim!"


class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name}: {self.fly()} AND {self.swim()}"


donald = Duck("Donald")
print(donald.describe())
# Donald: I can fly! AND I can swim!
```

## MRO — Method Resolution Order
When multiple parents share a method name, Python uses MRO (left → right) to decide which one runs.
```python
print(Duck.__mro__)
# (<class 'Duck'>, <class 'Flyable'>, <class 'Swimmable'>, <class 'object'>)
```
## Multilevel Inheritance
A chain of inheritance: Grandparent → Parent → Child.
```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        return f"Brand: {self.brand}"


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def info(self):
        return f"{super().info()}, Model: {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, range_km):
        super().__init__(brand, model)
        self.range_km = range_km

    def info(self):
        return f"{super().info()}, Range: {self.range_km} km"


tesla = ElectricCar("Tesla", "Model 3", 500)
print(tesla.info())
# Brand: Tesla, Model: Model 3, Range: 500 km
```
# super()
super() gives access to the parent class without hardcoding its name. Essential for safe inheritance chains.
```python
class Shape:
    def __init__(self, color):
        self.color = color

    def describe(self):
        return f"Color: {self.color}"


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)          # calls Shape.__init__
        self.radius = radius

    def describe(self):
        base = super().describe()        # calls Shape.describe
        return f"{base}, Radius: {self.radius}"


c = Circle("red", 5)
print(c.describe())
# Color: red, Radius: 5
```
super() always follows the MRO, making it safe for multiple and multilevel inheritance.

# Methods
## Instance Method
Operates on the instance (self). The default method type.
```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):         # instance method
        self.count += 1
        return self.count


c = Counter()
print(c.increment())   # 1
print(c.increment())   # 2
```

## Class Method
Operates on the class (cls), not the instance. Decorated with @classmethod.
Common use: **alternative constructors.**
```python
class Person:
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):    # alternative constructor
        age = 2024 - birth_year
        return cls(name, age)

    @classmethod
    def get_species(cls):
        return cls.species


p = Person.from_birth_year("Seven", 1995)
print(p.name, p.age)          # Seven 29
print(Person.get_species())   # Homo sapiens
```
## Static Method
No self or cls. A plain utility function namespaced inside the class.
```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0


print(MathUtils.add(3, 7))      # 10
print(MathUtils.is_even(4))     # True
```
## Property Decorators
@property lets you access a method like an attribute, with optional setter and deleter control.
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):                   # getter
        return self._celsius

    @celsius.setter
    def celsius(self, value):            # setter with validation
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):                # computed property (read-only)
        return self._celsius * 9 / 5 + 32


temp = Temperature(25)
print(temp.celsius)      # 25
print(temp.fahrenheit)   # 77.0

temp.celsius = 100
print(temp.fahrenheit)   # 212.0

# temp.celsius = -300    # raises ValueError
```

## Operator Overloading
Define how operators (+, -, ==, <, etc.) behave on your custom objects using dunder methods.
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):            # v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):            # v1 - v2
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):           # v * 3
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):             # v1 == v2
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):             # v1 < v2  (by magnitude)
        return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)

    def __len__(self):                   # len(v)
        return int((self.x**2 + self.y**2) ** 0.5)


v1 = Vector(2, 3)
v2 = Vector(1, 4)

print(v1 + v2)    # Vector(3, 7)
print(v1 - v2)    # Vector(1, -1)
print(v1 * 3)     # Vector(6, 9)
print(v1 == v2)   # False
print(v1 < v2)    # False
print(len(v1))    # 3
```

## How to Run

1. Make sure Python is installed on your system.
2. Clone this repository or download the file.
                             https://github.com/sabaansari7110-max/OOPs-inheritance.git
3. Open terminal in the project folder.
4. Run the code.

## Author
Created as part of Python learning journey to strengthen programming fundamentals and logical thinking.

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute this project with proper attribution.

## Contributing
1.Feel free to contribute!
<br>
2.Add more examples
<br>
3.Improve explanations
<br>
4.Fix bugs or add new OOP topics (Inheritance, Polymorphism, etc.)
<br>
5.Fork the repo
<br>
6.Create a feature branch
<br>
7.Commit your changes
<br>
8.Open a Pull Request
<br>
⭐ Star this repo if you found it helpful!

