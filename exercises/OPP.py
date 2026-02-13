# ======================================================================
# 🐍 PYTHON OOP - COMPREHENSIVE EXERCISES
# ======================================================================
# Topics: Classes, Instances, 4 Pillars, Data Hiding, MRO, Diamond Problem
# Instructions: Complete each exercise, test your solutions
# ======================================================================


# =====================================================================
#                        SECTION 1: BASICS
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 EASY 1: Create Your First Class
# Create a class called Book with:
# - Class attribute: category = "Literature"
# - Instance attributes: title, author, pages (set via __init__)
# - No methods needed yet
#
# Test: book = Book("1984", "George Orwell", 328)
# Test: book.title -> "1984"
# Test: book.author -> "George Orwell"
# Test: book.pages -> 328
# Test: Book.category -> "Literature"
# ----------------------------------------------------------------------

# Write your code below:

# class Book:
#     category = "Literature"

#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages


# # Test your solution:
# nineteen_eighty_four = Book("1984", "George Orwell", 328)
# print("🟢 nineteen_eighty_four.title:", nineteen_eighty_four.title)
# print("🟢 nineteen_eighty_four.author:", nineteen_eighty_four.author)
# print("🟢 nineteen_eighty_four.pages:", nineteen_eighty_four.pages)
# print("🟢 Book.category:", Book.category)


# ----------------------------------------------------------------------
# 🟢 EASY 2: Add Methods
# Create a class called Rectangle with:
# - Instance attributes: width, height
# - Method: area() -> returns width * height
# - Method: perimeter() -> returns 2 * (width + height)
#
# Test: rect = Rectangle(5, 3)
# Test: rect.area() -> 15
# Test: rect.perimeter() -> 16
# Test: Rectangle(10, 10).area() -> 100
# ----------------------------------------------------------------------

# Write your code below:

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)


# # Test your solution:
# rect = Rectangle(5, 3)
# print("🟢 rect.area():", rect.area())
# print("🟢 rect.perimeter():", rect.perimeter())
# print("🟢 Rectangle(10, 10).area():", Rectangle(10, 10).area())

# ----------------------------------------------------------------------
# 🟢 EASY 3: Class with Default Values
# Create a class called Student with:
# - Instance attributes: name, grade (default: 0), subjects (default: empty list)
# - Method: add_subject(subject) -> adds subject to subjects list
# - Method: set_grade(grade) -> sets the grade
# - Method: display() -> returns "Name: {name}, Grade: {grade}"
#
# Test: s = Student("Alice")
# Test: s.display() -> "Name: Alice, Grade: 0"
# Test: s.set_grade(85)
# Test: s.display() -> "Name: Alice, Grade: 85"
# Test: s.add_subject("Math")
# Test: s.subjects -> ["Math"]
# ----------------------------------------------------------------------

# Write your code below:

# class Student:
#     def __init__(self, name, grade=0, subjects=[]):
#         self.name = name
#         self.grade = grade
#         self.subjects = subjects

#     def add_subject(self, subject):
#         self.subjects.append(subject)

#     def set_grade(self, grade):
#         self.grade = grade

#     def display(self):
#         return f"Name: {self.name}, Grade: {self.grade}"

# print(alicia.display())
# alicia.set_grade(10)
# print(alicia.display())
# alicia.add_subject("Math")
# alicia.add_subject("English")
# alicia.add_subject("French")
# print(alicia.subjects)

# Test your solution:
# s = Student("Alice")
# print("🟢 s.display():", s.display())
# s.set_grade(85)
# print("🟢 s.display() after grade:", s.display())
# s.add_subject("Math")
# print("🟢 s.subjects:", s.subjects)


# ----------------------------------------------------------------------
# 🟢 EASY 4: String Representation
# Create a class called Point with:
# - Instance attributes: x, y
# - Method: __str__() -> returns "Point(x, y)"
# - Method: __repr__() -> returns "Point(x={x}, y={y})"
#
# Test: p = Point(3, 5)
# Test: str(p) -> "Point(3, 5)"
# Test: repr(p) -> "Point(x=3, y=5)"
# Test: print(p) -> Point(3, 5)
# ----------------------------------------------------------------------

# Write your code below:

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self) -> str:
#         return f"Point({self.x}, {self.y})"

#     def __repr__(self) -> str:
#         return f"Point(x={self.x}, y={self.y})"


# p = Point(0, 0)
# print(p.__str__())
# print(str(p))
# print(p.__repr__())
# print(repr(p))

# Test your solution:
# p = Point(3, 5)
# print("🟢 str(p):", str(p))
# print("🟢 repr(p):", repr(p))


# ----------------------------------------------------------------------
# 🟢 EASY 5: Counter Class
# Create a class called Counter with:
# - Instance attribute: count (starts at 0)
# - Method: increment() -> adds 1 to count
# - Method: decrement() -> subtracts 1 from count
# - Method: reset() -> sets count back to 0
# - Method: get_count() -> returns current count
#
# Test: c = Counter()
# Test: c.get_count() -> 0
# Test: c.increment(); c.increment(); c.get_count() -> 2
# Test: c.decrement(); c.get_count() -> 1
# Test: c.reset(); c.get_count() -> 0
# ----------------------------------------------------------------------

# Write your code below:

class Counter:
    def __init__(self, count=0):
        self.count = count

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count


# Test your solution:
c = Counter()
print("🟢 Initial count:", c.get_count())
c.increment()
c.increment()
print("🟢 After 2 increments:", c.get_count())
c.decrement()
print("🟢 After decrement:", c.get_count())
c.reset()
print("🟢 After reset:", c.get_count())


# ----------------------------------------------------------------------
# 🟢 EASY 6: Class vs Instance Attributes
# Create a class called Dog with:
# - Class attribute: species = "Canis familiaris"
# - Class attribute: dog_count = 0 (tracks how many dogs created)
# - Instance attributes: name, age
# - Increment dog_count in __init__ each time a Dog is created
#
# Test: Dog.dog_count -> 0
# Test: d1 = Dog("Buddy", 3)
# Test: Dog.dog_count -> 1
# Test: d2 = Dog("Max", 5)
# Test: Dog.dog_count -> 2
# Test: d1.species -> "Canis familiaris"
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# print("🟢 Initial dog_count:", Dog.dog_count)
# d1 = Dog("Buddy", 3)
# print("🟢 After d1:", Dog.dog_count)
# d2 = Dog("Max", 5)
# print("🟢 After d2:", Dog.dog_count)
# print("🟢 d1.species:", d1.species)


# =====================================================================
#                     SECTION 2: INHERITANCE
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 EASY 7: Simple Inheritance
# Create a class Animal with:
# - Instance attribute: name
# - Method: speak() -> returns "Some sound"
#
# Create a class Cat that inherits from Animal:
# - Override speak() -> returns "{name} says Meow!"
#
# Create a class Dog that inherits from Animal:
# - Override speak() -> returns "{name} says Woof!"
#
# Test: cat = Cat("Whiskers")
# Test: cat.speak() -> "Whiskers says Meow!"
# Test: dog = Dog("Buddy")
# Test: dog.speak() -> "Buddy says Woof!"
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# cat = Cat("Whiskers")
# dog = Dog("Buddy")
# print("🟢 cat.speak():", cat.speak())
# print("🟢 dog.speak():", dog.speak())


# ----------------------------------------------------------------------
# 🟡 MEDIUM 1: Using super()
# Create a class Vehicle with:
# - Instance attributes: brand, model, year
# - Method: info() -> returns "{year} {brand} {model}"
#
# Create a class Car that inherits from Vehicle:
# - Additional instance attribute: num_doors
# - Use super().__init__() to initialize parent attributes
# - Override info() -> returns "{year} {brand} {model} ({num_doors} doors)"
#
# Test: v = Vehicle("Toyota", "Camry", 2020)
# Test: v.info() -> "2020 Toyota Camry"
# Test: c = Car("Honda", "Civic", 2022, 4)
# Test: c.info() -> "2022 Honda Civic (4 doors)"
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# v = Vehicle("Toyota", "Camry", 2020)
# c = Car("Honda", "Civic", 2022, 4)
# print("🟡 v.info():", v.info())
# print("🟡 c.info():", c.info())


# ----------------------------------------------------------------------
# 🟡 MEDIUM 2: Multi-Level Inheritance
# Create a hierarchy:
# - LivingThing: has attribute alive = True, method breathe() -> "Breathing"
# - Animal(LivingThing): has attribute can_move = True, method move() -> "Moving"
# - Mammal(Animal): has attribute warm_blooded = True, method feed_young() -> "Feeding milk"
# - Human(Mammal): has attribute name, method speak() -> "{name} is speaking"
#
# Test: h = Human("Alice")
# Test: h.alive -> True
# Test: h.can_move -> True
# Test: h.warm_blooded -> True
# Test: h.breathe() -> "Breathing"
# Test: h.move() -> "Moving"
# Test: h.feed_young() -> "Feeding milk"
# Test: h.speak() -> "Alice is speaking"
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# h = Human("Alice")
# print("🟡 h.alive:", h.alive)
# print("🟡 h.can_move:", h.can_move)
# print("🟡 h.warm_blooded:", h.warm_blooded)
# print("🟡 h.breathe():", h.breathe())
# print("🟡 h.speak():", h.speak())


# ----------------------------------------------------------------------
# 🟡 MEDIUM 3: isinstance and issubclass
# Using the classes from MEDIUM 2, predict and verify:
#
# Create a Human named "Bob" and check:
# 1. isinstance(bob, Human) -> ?
# 2. isinstance(bob, Mammal) -> ?
# 3. isinstance(bob, Animal) -> ?
# 4. isinstance(bob, LivingThing) -> ?
# 5. isinstance(bob, object) -> ?
# 6. issubclass(Human, Mammal) -> ?
# 7. issubclass(Human, LivingThing) -> ?
# 8. issubclass(Mammal, Human) -> ?
# 9. issubclass(Animal, Animal) -> ?
#
# Write your predictions first, then verify with code
# ----------------------------------------------------------------------

# Write your predictions:
# 1.
# 2.
# 3.
# 4.
# 5.
# 6.
# 7.
# 8.
# 9.

# Verify with code:
# bob = Human("Bob")
# print("🟡 isinstance(bob, Human):", isinstance(bob, Human))
# ... add more tests


# =====================================================================
#                    SECTION 3: ENCAPSULATION
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 MEDIUM 4: Protected Attributes
# Create a class BankAccount with:
# - Protected attribute: _balance (initialized to 0)
# - Protected attribute: _account_holder
# - Method: deposit(amount) -> adds to balance if amount > 0
# - Method: withdraw(amount) -> subtracts from balance if sufficient funds
# - Method: get_balance() -> returns current balance
#
# Test: acc = BankAccount("Alice")
# Test: acc.get_balance() -> 0
# Test: acc.deposit(100)
# Test: acc.get_balance() -> 100
# Test: acc.withdraw(30)
# Test: acc.get_balance() -> 70
# Test: acc.withdraw(100) -> should not change balance (insufficient funds)
# Test: acc._balance -> 70 (accessible but discouraged)
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# acc = BankAccount("Alice")
# print("🟡 Initial balance:", acc.get_balance())
# acc.deposit(100)
# print("🟡 After deposit 100:", acc.get_balance())
# acc.withdraw(30)
# print("🟡 After withdraw 30:", acc.get_balance())
# acc.withdraw(100)
# print("🟡 After withdraw 100 (insufficient):", acc.get_balance())


# ----------------------------------------------------------------------
# 🟡 MEDIUM 5: Private Attributes (Name Mangling)
# Create a class SecureAccount with:
# - Private attribute: __pin (4 digit string)
# - Private attribute: __balance
# - Method: verify_pin(pin) -> returns True if pin matches
# - Method: get_balance(pin) -> returns balance only if pin is correct, else "Access Denied"
# - Method: change_pin(old_pin, new_pin) -> changes pin if old_pin is correct
#
# Test: sa = SecureAccount("1234", 1000)
# Test: sa.verify_pin("1234") -> True
# Test: sa.verify_pin("0000") -> False
# Test: sa.get_balance("1234") -> 1000
# Test: sa.get_balance("0000") -> "Access Denied"
# Test: sa.__pin -> AttributeError
# Test: sa._SecureAccount__pin -> "1234" (name mangling)
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# sa = SecureAccount("1234", 1000)
# print("🟡 verify_pin('1234'):", sa.verify_pin("1234"))
# print("🟡 verify_pin('0000'):", sa.verify_pin("0000"))
# print("🟡 get_balance('1234'):", sa.get_balance("1234"))
# print("🟡 get_balance('0000'):", sa.get_balance("0000"))
# try:
#     print(sa.__pin)
# except AttributeError as e:
#     print("🟡 sa.__pin raises AttributeError")


# ----------------------------------------------------------------------
# 🟡 MEDIUM 6: Getters and Setters (Manual)
# Create a class Temperature with:
# - Private attribute: __celsius
# - Method: get_celsius() -> returns celsius value
# - Method: set_celsius(value) -> sets celsius (must be >= -273.15)
# - Method: get_fahrenheit() -> returns celsius converted to fahrenheit
# - Method: set_fahrenheit(value) -> converts fahrenheit to celsius and stores
#
# Formula: F = C * 9/5 + 32, C = (F - 32) * 5/9
#
# Test: t = Temperature(25)
# Test: t.get_celsius() -> 25
# Test: t.get_fahrenheit() -> 77.0
# Test: t.set_fahrenheit(32)
# Test: t.get_celsius() -> 0.0
# Test: t.set_celsius(-300) -> should not change (below absolute zero)
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# t = Temperature(25)
# print("🟡 get_celsius():", t.get_celsius())
# print("🟡 get_fahrenheit():", t.get_fahrenheit())
# t.set_fahrenheit(32)
# print("🟡 After set_fahrenheit(32), celsius:", t.get_celsius())


# =====================================================================
#                    SECTION 4: POLYMORPHISM
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 MEDIUM 7: Method Overriding (Polymorphism)
# Create a base class Shape with:
# - Method: area() -> returns 0
# - Method: describe() -> returns "I am a shape"
#
# Create class Circle(Shape):
# - Attribute: radius
# - Override area() -> returns π * radius²
# - Override describe() -> returns "I am a circle with radius {radius}"
#
# Create class Square(Shape):
# - Attribute: side
# - Override area() -> returns side²
# - Override describe() -> returns "I am a square with side {side}"
#
# Create a function total_area(shapes) that takes a list of shapes
# and returns the sum of all their areas
#
# Test: shapes = [Circle(5), Square(4), Circle(3)]
# Test: total_area(shapes) -> 78.53981633974483 + 16 + 28.274333882308138
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# shapes = [Circle(5), Square(4), Circle(3)]
# print("🟡 Circle(5).area():", Circle(5).area())
# print("🟡 Square(4).area():", Square(4).area())
# print("🟡 total_area(shapes):", total_area(shapes))


# ----------------------------------------------------------------------
# 🟡 MEDIUM 8: Duck Typing
# Create classes that don't inherit from each other but have same method:
#
# Class Duck: method sound() -> "Quack!"
# Class Person: method sound() -> "Hello!"
# Class Car: method sound() -> "Vroom!"
# Class Radio: method sound() -> "Music playing"
#
# Create function make_sound(obj) that calls obj.sound()
#
# Test: make_sound(Duck()) -> "Quack!"
# Test: make_sound(Person()) -> "Hello!"
# Test: make_sound(Car()) -> "Vroom!"
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# print("🟡 make_sound(Duck()):", make_sound(Duck()))
# print("🟡 make_sound(Person()):", make_sound(Person()))
# print("🟡 make_sound(Car()):", make_sound(Car()))


# ----------------------------------------------------------------------
# 🟡 MEDIUM 9: Operator Overloading
# Create a class Vector with:
# - Attributes: x, y
# - __add__(other) -> returns new Vector(self.x + other.x, self.y + other.y)
# - __sub__(other) -> returns new Vector with subtraction
# - __mul__(scalar) -> returns new Vector(self.x * scalar, self.y * scalar)
# - __eq__(other) -> returns True if x and y are equal
# - __str__() -> returns "Vector(x, y)"
#
# Test: v1 = Vector(3, 4)
# Test: v2 = Vector(1, 2)
# Test: v1 + v2 -> Vector(4, 6)
# Test: v1 - v2 -> Vector(2, 2)
# Test: v1 * 2 -> Vector(6, 8)
# Test: Vector(1, 1) == Vector(1, 1) -> True
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# v1 = Vector(3, 4)
# v2 = Vector(1, 2)
# print("🟡 v1 + v2:", v1 + v2)
# print("🟡 v1 - v2:", v1 - v2)
# print("🟡 v1 * 2:", v1 * 2)
# print("🟡 Vector(1,1) == Vector(1,1):", Vector(1, 1) == Vector(1, 1))


# =====================================================================
#               SECTION 5: MULTIPLE INHERITANCE & MRO
# =====================================================================


# ----------------------------------------------------------------------
# 🔴 HARD 1: Multiple Inheritance
# Create:
# - Class Flyable: method fly() -> "Flying"
# - Class Swimmable: method swim() -> "Swimming"
# - Class Walkable: method walk() -> "Walking"
# - Class Duck(Flyable, Swimmable, Walkable): has attribute name
# - Class Penguin(Swimmable, Walkable): has attribute name
# - Class Sparrow(Flyable, Walkable): has attribute name
#
# Test: duck = Duck("Donald")
# Test: duck.fly() -> "Flying"
# Test: duck.swim() -> "Swimming"
# Test: duck.walk() -> "Walking"
# Test: penguin = Penguin("Pingu")
# Test: penguin.swim() -> "Swimming"
# Test: penguin.fly() -> AttributeError
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# duck = Duck("Donald")
# print("🔴 duck.fly():", duck.fly())
# print("🔴 duck.swim():", duck.swim())
# print("🔴 duck.walk():", duck.walk())
# penguin = Penguin("Pingu")
# print("🔴 penguin.swim():", penguin.swim())


# ----------------------------------------------------------------------
# 🔴 HARD 2: Diamond Problem - Predict the Output
# Given:
#
# class A:
#     def method(self):
#         return "A"
#
# class B(A):
#     def method(self):
#         return "B"
#
# class C(A):
#     def method(self):
#         return "C"
#
# class D(B, C):
#     pass
#
# class E(C, B):
#     pass
#
# Predict:
# 1. D().method() -> ?
# 2. E().method() -> ?
# 3. D.__mro__ -> ?
# 4. E.__mro__ -> ?
# ----------------------------------------------------------------------

# Write your predictions:
# 1.
# 2.
# 3.
# 4.

# Verify with code:
# class A:
#     def method(self):
#         return "A"
# class B(A):
#     def method(self):
#         return "B"
# class C(A):
#     def method(self):
#         return "C"
# class D(B, C):
#     pass
# class E(C, B):
#     pass
# print("🔴 D().method():", D().method())
# print("🔴 E().method():", E().method())
# print("🔴 D.__mro__:", D.__mro__)
# print("🔴 E.__mro__:", E.__mro__)


# ----------------------------------------------------------------------
# 🔴 HARD 3: Diamond Problem with super()
# Create:
#
# class Base:
#     def __init__(self):
#         self.value = "Base"
#         print("Base __init__")
#
# class Left(Base):
#     def __init__(self):
#         super().__init__()
#         self.left_value = "Left"
#         print("Left __init__")
#
# class Right(Base):
#     def __init__(self):
#         super().__init__()
#         self.right_value = "Right"
#         print("Right __init__")
#
# class Child(Left, Right):
#     def __init__(self):
#         super().__init__()
#         self.child_value = "Child"
#         print("Child __init__")
#
# Predict the output when: obj = Child()
# Also predict: Which attributes will obj have?
# ----------------------------------------------------------------------

# Write your predictions:
# Print order:
#
# Attributes obj will have:

# Verify:
# obj = Child()
# print("🔴 obj attributes:", obj.__dict__)


# ----------------------------------------------------------------------
# 🔴 HARD 4: MRO Analysis
# Create this hierarchy and analyze:
#
# class O: pass
# class A(O): pass
# class B(O): pass
# class C(O): pass
# class D(A, B): pass
# class E(B, C): pass
# class F(D, E): pass
#
# Tasks:
# 1. Draw the inheritance diagram (as comments)
# 2. Predict F.__mro__
# 3. Verify with code
# ----------------------------------------------------------------------

# Task 1 - Draw diagram:


# Task 2 - Predict MRO:


# Task 3 - Verify:
# class O: pass
# class A(O): pass
# class B(O): pass
# class C(O): pass
# class D(A, B): pass
# class E(B, C): pass
# class F(D, E): pass
# print("🔴 F.__mro__:", F.__mro__)


# =====================================================================
#                    SECTION 6: ABSTRACTION
# =====================================================================


# ----------------------------------------------------------------------
# 🔴 HARD 5: Abstract Base Class
# Create an abstract class PaymentProcessor with:
# - Abstract method: process_payment(amount)
# - Abstract method: refund(amount)
# - Concrete method: validate_amount(amount) -> returns amount > 0
#
# Create class CreditCardProcessor(PaymentProcessor):
# - Attribute: card_number
# - Implement process_payment -> returns "Processing ${amount} on card {last 4 digits}"
# - Implement refund -> returns "Refunding ${amount} to card {last 4 digits}"
#
# Create class PayPalProcessor(PaymentProcessor):
# - Attribute: email
# - Implement process_payment -> returns "Processing ${amount} via PayPal ({email})"
# - Implement refund -> returns "Refunding ${amount} to PayPal ({email})"
#
# Test: PaymentProcessor() -> should raise TypeError (can't instantiate abstract)
# Test: cc = CreditCardProcessor("1234567890123456")
# Test: cc.process_payment(100) -> "Processing $100 on card 3456"
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# try:
#     p = PaymentProcessor()
# except TypeError:
#     print("🔴 Cannot instantiate abstract class")
# cc = CreditCardProcessor("1234567890123456")
# print("🔴 cc.process_payment(100):", cc.process_payment(100))
# pp = PayPalProcessor("user@email.com")
# print("🔴 pp.process_payment(50):", pp.process_payment(50))


# ----------------------------------------------------------------------
# 🔴 HARD 6: Abstract Properties
# Create an abstract class Animal with:
# - Abstract property: sound (must be implemented by subclasses)
# - Abstract property: movement (must be implemented by subclasses)
# - Concrete method: describe() -> returns "{class name} makes {sound} and {movement}"
#
# Create class Lion(Animal):
# - sound property returns "roar"
# - movement property returns "runs"
#
# Create class Eagle(Animal):
# - sound property returns "screech"
# - movement property returns "flies"
#
# Test: lion = Lion()
# Test: lion.sound -> "roar"
# Test: lion.describe() -> "Lion makes roar and runs"
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# lion = Lion()
# eagle = Eagle()
# print("🔴 lion.sound:", lion.sound)
# print("🔴 lion.describe():", lion.describe())
# print("🔴 eagle.describe():", eagle.describe())


# =====================================================================
#                 SECTION 7: ADVANCED CLASS FEATURES
# =====================================================================


# ----------------------------------------------------------------------
# 🔴 HARD 7: Property Decorator
# Create a class Circle with:
# - Private attribute: __radius
# - Property: radius (getter returns __radius)
# - Property setter: radius (sets __radius, must be positive)
# - Property: diameter (calculated: radius * 2)
# - Property: area (calculated: π * radius²)
# - Property setter: diameter (sets radius to diameter / 2)
#
# Test: c = Circle(5)
# Test: c.radius -> 5
# Test: c.diameter -> 10
# Test: c.area -> 78.53981633974483
# Test: c.diameter = 20
# Test: c.radius -> 10
# Test: c.radius = -5 -> should not change (invalid)
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# c = Circle(5)
# print("🔴 c.radius:", c.radius)
# print("🔴 c.diameter:", c.diameter)
# print("🔴 c.area:", c.area)
# c.diameter = 20
# print("🔴 After c.diameter = 20, radius:", c.radius)


# ----------------------------------------------------------------------
# 🔴 HARD 8: Class Methods and Static Methods
# Create a class Employee with:
# - Class attribute: company_name = "TechCorp"
# - Class attribute: employee_count = 0
# - Instance attributes: name, salary
# - Increment employee_count in __init__
#
# - Class method: get_company_info() -> returns "{company_name} has {count} employees"
# - Class method: change_company_name(new_name) -> changes company_name
# - Class method: from_string(string) -> creates Employee from "name-salary" format
#
# - Static method: is_valid_salary(salary) -> returns True if salary > 0
# - Static method: calculate_bonus(salary, percentage) -> returns salary * percentage / 100
#
# Test: Employee.is_valid_salary(50000) -> True
# Test: Employee.calculate_bonus(50000, 10) -> 5000.0
# Test: e = Employee.from_string("Alice-75000")
# Test: e.name -> "Alice", e.salary -> 75000
# Test: Employee.get_company_info() -> "TechCorp has 1 employees"
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# print("🔴 Employee.is_valid_salary(50000):", Employee.is_valid_salary(50000))
# print("🔴 Employee.calculate_bonus(50000, 10):", Employee.calculate_bonus(50000, 10))
# e = Employee.from_string("Alice-75000")
# print("🔴 e.name:", e.name)
# print("🔴 e.salary:", e.salary)
# print("🔴 Employee.get_company_info():", Employee.get_company_info())


# ----------------------------------------------------------------------
# 🔴 HARD 9: __slots__ for Memory Optimization
# Create two classes:
#
# Class RegularPerson:
# - Attributes: name, age, email
#
# Class OptimizedPerson:
# - __slots__ = ['name', 'age', 'email']
# - Same attributes
#
# Tasks:
# 1. Create instances of both
# 2. Try to add a new attribute dynamically to both (person.new_attr = "value")
# 3. Compare what happens
# 4. Check if __dict__ exists on both
#
# Test: rp = RegularPerson("Alice", 30, "alice@email.com")
# Test: op = OptimizedPerson("Bob", 25, "bob@email.com")
# Test: rp.new_attr = "test" -> should work
# Test: op.new_attr = "test" -> should raise AttributeError
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# rp = RegularPerson("Alice", 30, "alice@email.com")
# op = OptimizedPerson("Bob", 25, "bob@email.com")
# rp.new_attr = "test"
# print("🔴 rp.new_attr:", rp.new_attr)
# try:
#     op.new_attr = "test"
# except AttributeError:
#     print("🔴 Cannot add new attribute to OptimizedPerson")


# ----------------------------------------------------------------------
# 🔴 HARD 10: Composition vs Inheritance
# Demonstrate composition by creating:
#
# Class Engine:
# - Attributes: horsepower, fuel_type
# - Method: start() -> returns "Engine started ({horsepower}hp, {fuel_type})"
#
# Class Wheels:
# - Attribute: count (default 4)
# - Method: rotate() -> returns "Wheels rotating"
#
# Class Car (using COMPOSITION, not inheritance):
# - Has an Engine object
# - Has a Wheels object
# - Attribute: brand
# - Method: start() -> calls engine.start()
# - Method: drive() -> returns "{brand} is driving" + wheels.rotate()
#
# Test: engine = Engine(200, "Gasoline")
# Test: wheels = Wheels()
# Test: car = Car("Toyota", engine, wheels)
# Test: car.start() -> "Engine started (200hp, Gasoline)"
# Test: car.drive() -> "Toyota is driving. Wheels rotating"
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# engine = Engine(200, "Gasoline")
# wheels = Wheels()
# car = Car("Toyota", engine, wheels)
# print("🔴 car.start():", car.start())
# print("🔴 car.drive():", car.drive())


# =====================================================================
#                   SECTION 8: REAL-WORLD SCENARIOS
# =====================================================================


# ----------------------------------------------------------------------
# 🔴 HARD 11: Complete Class System - Library
# Create a library management system:
#
# Class Book:
# - Attributes: title, author, isbn, is_available (default True)
# - Method: __str__() -> returns "{title} by {author}"
#
# Class Member:
# - Attributes: name, member_id, borrowed_books (list)
# - Method: borrow_book(book) -> adds book to borrowed_books if available
# - Method: return_book(book) -> removes book from borrowed_books
#
# Class Library:
# - Attributes: name, books (list), members (list)
# - Method: add_book(book)
# - Method: remove_book(book)
# - Method: register_member(member)
# - Method: find_book(title) -> returns book or None
# - Method: find_available_books() -> returns list of available books
#
# Test the system with multiple books and members
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# lib = Library("City Library")
# book1 = Book("1984", "George Orwell", "12345")
# book2 = Book("Brave New World", "Aldous Huxley", "67890")
# lib.add_book(book1)
# lib.add_book(book2)
# member = Member("Alice", "M001")
# lib.register_member(member)
# print("🔴 Available books:", [str(b) for b in lib.find_available_books()])
# member.borrow_book(book1)
# print("🔴 After borrowing, available:", [str(b) for b in lib.find_available_books()])


# ----------------------------------------------------------------------
# 🔴 HARD 12: Complete Class System - Game Characters
# Create a game character system:
#
# Abstract Class Character:
# - Attributes: name, health, max_health, level
# - Abstract method: attack(target)
# - Abstract method: special_ability()
# - Concrete method: take_damage(amount) -> reduces health
# - Concrete method: heal(amount) -> increases health up to max
# - Concrete method: is_alive() -> returns health > 0
#
# Class Warrior(Character):
# - Additional attribute: strength
# - attack() -> deals strength * 2 damage
# - special_ability() -> "Shield Bash" deals strength * 3 damage
#
# Class Mage(Character):
# - Additional attribute: mana
# - attack() -> deals mana damage
# - special_ability() -> "Fireball" deals mana * 4 damage, costs 20 mana
#
# Class Archer(Character):
# - Additional attribute: agility
# - attack() -> deals agility * 1.5 damage
# - special_ability() -> "Multi-shot" deals agility * 2 to target, 50% miss chance
#
# Create a battle simulation function
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# warrior = Warrior("Conan", 100, 20)
# mage = Mage("Gandalf", 70, 50)
# print("🔴 warrior.attack(mage)")
# print("🔴 Mage health after attack:", mage.health)


# ----------------------------------------------------------------------
# 🔴 HARD 13: Singleton Pattern
# Create a class DatabaseConnection that:
# - Only allows ONE instance to exist (Singleton pattern)
# - Has attribute: connection_string
# - Has method: query(sql) -> returns "Executing: {sql}"
# - Multiple calls to constructor return the SAME instance
#
# Test: db1 = DatabaseConnection("localhost:5432")
# Test: db2 = DatabaseConnection("different:1234")
# Test: db1 is db2 -> True (same instance)
# Test: db1.connection_string == db2.connection_string -> True
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# db1 = DatabaseConnection("localhost:5432")
# db2 = DatabaseConnection("different:1234")
# print("🔴 db1 is db2:", db1 is db2)
# print("🔴 db1.connection_string:", db1.connection_string)


# ----------------------------------------------------------------------
# 🔴 HARD 14: Factory Pattern
# Create a ShapeFactory class:
# - Static method: create_shape(shape_type, **kwargs)
# - If shape_type == "circle": return Circle with radius from kwargs
# - If shape_type == "rectangle": return Rectangle with width, height from kwargs
# - If shape_type == "triangle": return Triangle with base, height from kwargs
# - If invalid type: raise ValueError
#
# Each shape class should have area() method
#
# Test: circle = ShapeFactory.create_shape("circle", radius=5)
# Test: circle.area() -> 78.53981633974483
# Test: rect = ShapeFactory.create_shape("rectangle", width=4, height=5)
# Test: rect.area() -> 20
# Test: ShapeFactory.create_shape("hexagon") -> raises ValueError
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# circle = ShapeFactory.create_shape("circle", radius=5)
# rect = ShapeFactory.create_shape("rectangle", width=4, height=5)
# print("🔴 circle.area():", circle.area())
# print("🔴 rect.area():", rect.area())


# ----------------------------------------------------------------------
# 🔴 HARD 15: Observer Pattern
# Create an observer pattern implementation:
#
# Class Subject:
# - Has private list of observers
# - Method: attach(observer) -> adds observer to list
# - Method: detach(observer) -> removes observer
# - Method: notify() -> calls update() on all observers
#
# Class Observer (abstract):
# - Abstract method: update(subject)
#
# Class NewsPublisher(Subject):
# - Attribute: latest_news
# - Method: publish_news(news) -> sets latest_news and calls notify()
#
# Class NewsSubscriber(Observer):
# - Attribute: name
# - Method: update(subject) -> prints "{name} received: {subject.latest_news}"
#
# Test: publisher = NewsPublisher()
# Test: sub1 = NewsSubscriber("Alice")
# Test: sub2 = NewsSubscriber("Bob")
# Test: publisher.attach(sub1)
# Test: publisher.attach(sub2)
# Test: publisher.publish_news("Breaking News!") -> both subscribers notified
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# publisher = NewsPublisher()
# sub1 = NewsSubscriber("Alice")
# sub2 = NewsSubscriber("Bob")
# publisher.attach(sub1)
# publisher.attach(sub2)
# print("🔴 Publishing news...")
# publisher.publish_news("Breaking: Python is awesome!")


# ======================================================================
# 📊 EXERCISE SUMMARY
# ======================================================================
# 🟢 EASY (6):     Basic classes, attributes, methods, __str__, __repr__
# 🟡 MEDIUM (9):   Inheritance, super(), encapsulation, polymorphism
# 🔴 HARD (15):    MRO, diamond problem, abstract classes, design patterns
#
# Total: 30 Exercises
#
# Concepts Covered:
# - Classes and Instances          - Class vs Instance Attributes
# - __init__ and self             - Methods (instance, class, static)
# - Inheritance (single, multi)   - super() usage
# - Encapsulation (_protected)    - Data hiding (__private)
# - Polymorphism                  - Duck typing
# - Operator overloading          - Abstract base classes
# - Properties (@property)        - MRO and diamond problem
# - __slots__                     - Composition vs Inheritance
# - Design Patterns (Singleton, Factory, Observer)
# ======================================================================
