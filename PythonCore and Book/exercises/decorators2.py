# ======================================================================
# 🐍 PYTHON CLASS DECORATORS - COMPREHENSIVE EXERCISES
# ======================================================================
# Topics: @classmethod, @staticmethod, @property, @abstractmethod
# Instructions: Complete each exercise, test your solutions
# ======================================================================


# =====================================================================
#                    SECTION 1: @staticmethod
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 EASY 1: Basic Static Method
# Create a class MathUtils with static methods:
# - add(a, b) -> returns a + b
# - subtract(a, b) -> returns a - b
# - multiply(a, b) -> returns a * b
# - divide(a, b) -> returns a / b (handle division by zero, return None)
#
# Test: MathUtils.add(5, 3) -> 8
# Test: MathUtils.subtract(10, 4) -> 6
# Test: MathUtils.multiply(3, 7) -> 21
# Test: MathUtils.divide(15, 3) -> 5.0
# Test: MathUtils.divide(10, 0) -> None
# ----------------------------------------------------------------------

# Write your code below:


# class MathUtils:
#     @staticmethod
#     def add(a, b):
#         return a + b

#     @staticmethod
#     def subtract(a, b):
#         return a - b

#     @staticmethod
#     def multiply(a, b):
#         return a * b

#     @staticmethod
#     def divide(a, b):
#         if b != 0:
#             return a / b


# # Test your solution:
# print("🟢 MathUtils.add(5, 3):", MathUtils.add(5, 3))
# print("🟢 MathUtils.subtract(10, 4):", MathUtils.subtract(10, 4))
# print("🟢 MathUtils.multiply(3, 7):", MathUtils.multiply(3, 7))
# print("🟢 MathUtils.divide(15, 3):", MathUtils.divide(15, 3))
# print("🟢 MathUtils.divide(10, 0):", MathUtils.divide(10, 0))


# ----------------------------------------------------------------------
# 🟢 EASY 2: Validator Static Methods
# Create a class Validator with static methods:
# - is_positive(number) -> returns True if number > 0
# - is_even(number) -> returns True if number is even
# - is_valid_email(email) -> returns True if "@" and "." are in email
# - is_strong_password(pwd) -> returns True if len >= 8 and has digit
#
# Test: Validator.is_positive(5) -> True
# Test: Validator.is_positive(-3) -> False
# Test: Validator.is_even(4) -> True
# Test: Validator.is_even(7) -> False
# Test: Validator.is_valid_email("test@email.com") -> True
# Test: Validator.is_valid_email("invalid") -> False
# Test: Validator.is_strong_password("Pass1234") -> True
# Test: Validator.is_strong_password("weak") -> False
# ----------------------------------------------------------------------

# Write your code below:


# class Validator:
#     @staticmethod
#     def is_positive(number):
#         return number > 0

#     @staticmethod
#     def is_even(number):
#         return number % 2 == 0

#     @staticmethod
#     def is_valid_email(email):
#         return "@" in email

#     @staticmethod
#     def is_strong_password(password):
#         return len(password) >= 8 and any(char.isdigit() for char in password)


# # Test your solution:
# print("🟢 Validator.is_positive(5):", Validator.is_positive(5))
# print("🟢 Validator.is_even(4):", Validator.is_even(4))
# print("🟢 Validator.is_valid_email('test@email.com'):", Validator.is_valid_email("test@email.com"))
# print("🟢 Validator.is_strong_password('Pass1234'):", Validator.is_strong_password("Pass1234"))


# ----------------------------------------------------------------------
# 🟢 EASY 3: Converter Static Methods
# Create a class Converter with static methods:
# - celsius_to_fahrenheit(c) -> returns (c * 9/5) + 32
# - fahrenheit_to_celsius(f) -> returns (f - 32) * 5/9
# - km_to_miles(km) -> returns km * 0.621371
# - miles_to_km(miles) -> returns miles / 0.621371
#
# Test: Converter.celsius_to_fahrenheit(0) -> 32.0
# Test: Converter.celsius_to_fahrenheit(100) -> 212.0
# Test: Converter.fahrenheit_to_celsius(32) -> 0.0
# Test: Converter.km_to_miles(10) -> 6.21371
# ----------------------------------------------------------------------

# Write your code below:


# class Converter:
#     @staticmethod
#     def celsius_to_fahrenheit(c):
#         return (c * 9 / 5) + 32

#     @staticmethod
#     def fahrenheit_to_celsius(f):
#         return (f - 32) * 5 / 9

#     @staticmethod
#     def km_to_miles(km):
#         return km * 0.621371

#     @staticmethod
#     def miles_to_km(miles):
#         return miles / 0.621371


# # Test your solution:
# print("🟢 Converter.celsius_to_fahrenheit(0):", Converter.celsius_to_fahrenheit(0))
# print("🟢 Converter.celsius_to_fahrenheit(100):", Converter.celsius_to_fahrenheit(100))
# print("🟢 Converter.fahrenheit_to_celsius(32):", Converter.fahrenheit_to_celsius(32))
# print("🟢 Converter.km_to_miles(10):", Converter.km_to_miles(10))
# print(Converter.miles_to_km(0.621371))


# =====================================================================
#                    SECTION 2: @classmethod
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 EASY 4: Basic Class Method
# Create a class Counter with:
# - Class attribute: count = 0
# - Instance attribute: name
# - In __init__, increment count by 1
# - Class method: get_count() -> returns current count
# - Class method: reset_count() -> sets count back to 0
#
# Test: Counter.get_count() -> 0
# Test: c1 = Counter("first")
# Test: Counter.get_count() -> 1
# Test: c2 = Counter("second")
# Test: Counter.get_count() -> 2
# Test: Counter.reset_count()
# Test: Counter.get_count() -> 0
# ----------------------------------------------------------------------

# Write your code below:


# class Counter:
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         Counter.count += 1

#     @classmethod
#     def get_count(cls):
#         return cls.count

#     @classmethod
#     def reset_count(cls):
#         cls.count = 0


# # Test your solution:
# print("🟢 Initial count:", Counter.get_count())
# c1 = Counter("first")
# print("🟢 After c1:", Counter.get_count())
# c2 = Counter("second")
# print("🟢 After c2:", Counter.get_count())
# Counter.reset_count()
# print("🟢 After reset:", Counter.get_count())


# ----------------------------------------------------------------------
# 🟡 MEDIUM 1: Alternative Constructors
# Create a class Date with:
# - Instance attributes: day, month, year
# - Method: __str__() -> returns "DD/MM/YYYY"
# - Class method: from_string(date_string) -> creates Date from "DD-MM-YYYY"
# - Class method: from_timestamp(timestamp) -> creates Date from Unix timestamp
# - Class method: today() -> creates Date with current date
#
# Test: d1 = Date(25, 12, 2023)
# Test: str(d1) -> "25/12/2023"
# Test: d2 = Date.from_string("15-06-2024")
# Test: str(d2) -> "15/06/2024"
# Test: d3 = Date.today()
# Test: str(d3) -> current date
# ----------------------------------------------------------------------

# Write your code below:

# import datetime
# import time


# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year

#     def __str__(self) -> str:
#         return f"{self.day}/{self.month}/{self.year}"

#     @classmethod
#     def from_string(cls, date_string):
#         new_date = cls(
#             int(date_string[0:2]), int(date_string[3:5]), int(date_string[6:])
#         )
#         return new_date

#     @classmethod
#     def from_timestamp(cls, timestamp):
#         t = datetime.datetime.fromtimestamp(timestamp)
#         t2 = cls(t.day, t.month, t.year)
#         return t2

#     @classmethod
#     def today(cls):
#         return cls.from_timestamp(time.time())


# # Test your solution:
# d1 = Date(25, 12, 2023)
# print("🟡 str(d1):", str(d1))
# d2 = Date.from_string("15-06-2024")
# print("🟡 str(d2):", str(d2))
# d3 = Date.today()
# print("🟡 str(d3):", str(d3))
# d4 = Date.from_timestamp(1771165132)
# print(d4)


# ----------------------------------------------------------------------
# 🟡 MEDIUM 2: Class Method for Configuration
# Create a class DatabaseConfig with:
# - Class attributes: host = "localhost", port = 5432, database = "default"
# - Class method: configure(host, port, database) -> updates all class attributes
# - Class method: from_dict(config_dict) -> updates from dictionary
# - Class method: from_url(url) -> parses "host:port/database" format
# - Class method: get_connection_string() -> returns "host:port/database"
#
# Test: DatabaseConfig.get_connection_string() -> "localhost:5432/default"
# Test: DatabaseConfig.configure("192.168.1.1", 3306, "mydb")
# Test: DatabaseConfig.get_connection_string() -> "192.168.1.1:3306/mydb"
# Test: DatabaseConfig.from_url("server:1234/production")
# Test: DatabaseConfig.get_connection_string() -> "server:1234/production"
# ----------------------------------------------------------------------

# Write your code below:


# class DatabaseConfig:
#     host = "localhost"
#     port = 5432
#     database = "default"

#     @classmethod
#     def configure(cls, host, port, database):
#         cls.host = host
#         cls.port = port
#         cls.database = database

#     @classmethod
#     def from_dict(cls, a_dict):
#         cls.host = a_dict["host"]
#         cls.port = a_dict["port"]
#         cls.database = a_dict["database"]

#         # for key, value in a_dict.items():
#         #     setattr(cls, key, value)
#         # You need to use setattr. Dot notation ALWAYS uses the literal name after the dot, not the variable's value.

#     @classmethod
#     def from_url(cls, url):
#         cls.host = url[0 : url.find(":")]
#         cls.port = url[url.find(":") + 1 : url.find("/")]
#         cls.database = url[url.find("/") + 1 :]

#     @classmethod
#     def get_connection_string(cls):
#         return f"{cls.host}:{cls.port}/{cls.database}"


# # Test your solution:
# print("🟡 Initial:", DatabaseConfig.get_connection_string())
# DatabaseConfig.configure("192.168.1.1", 3306, "mydb")
# print("🟡 After configure:", DatabaseConfig.get_connection_string())
# DatabaseConfig.from_url("server:1234/production")
# print("🟡 After from_url:", DatabaseConfig.get_connection_string())
# DatabaseConfig.from_dict({"host": 1, "port": 2, "database": 3})
# print("After from_dict:", DatabaseConfig.get_connection_string())


# ----------------------------------------------------------------------
# 🟡 MEDIUM 3: Factory Class Methods
# Create a class Employee with:
# - Instance attributes: name, role, salary
# - Class method: create_manager(name) -> Employee with role="Manager", salary=80000
# - Class method: create_developer(name) -> Employee with role="Developer", salary=70000
# - Class method: create_intern(name) -> Employee with role="Intern", salary=30000
# - Method: __str__() -> "{name} - {role} (${salary})"
#
# Test: mgr = Employee.create_manager("Alice")
# Test: str(mgr) -> "Alice - Manager ($80000)"
# Test: dev = Employee.create_developer("Bob")
# Test: str(dev) -> "Bob - Developer ($70000)"
# Test: intern = Employee.create_intern("Charlie")
# Test: str(intern) -> "Charlie - Intern ($30000)"
# ----------------------------------------------------------------------

# Write your code below:


# class Employee:
#     def __init__(self, name, role, salary):
#         self.name = name
#         self.role = role
#         self.salary = salary

#     @classmethod
#     def create_manager(cls, name):
#         return cls(name, role="Manager", salary=80000)

#     @classmethod
#     def create_developer(cls, name):
#         return cls(name, role="Developer", salary=70000)

#     @classmethod
#     def create_intern(cls, name):
#         return cls(name, role="Intern", salary=30000)

#     def __str__(self):
#         return f"{self.name} - {self.role} (${self.salary})"


# # Test your solution:
# mgr = Employee.create_manager("Alice")
# dev = Employee.create_developer("Bob")
# intern = Employee.create_intern("Charlie")
# print("🟡 Manager:", mgr)
# print("🟡 Developer:", dev)
# print("🟡 Intern:", intern)
# print(mgr.__str__())

# =====================================================================
#                      SECTION 3: @property
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 EASY 5: Basic Property (Getter Only)
# Create a class Circle with:
# - Instance attribute: radius
# - Property: diameter -> returns radius * 2
# - Property: area -> returns π * radius²
# - Property: circumference -> returns 2 * π * radius
#
# Test: c = Circle(5)
# Test: c.radius -> 5
# Test: c.diameter -> 10
# Test: c.area -> 78.53981633974483
# Test: c.circumference -> 31.41592653589793
# ----------------------------------------------------------------------

# Write your code below:
# import math


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     @property
#     def diameter(self):
#         return self.radius * 2

#     @property
#     def area(self):
#         return math.pi * self.radius**2

#     @property
#     def circumference(self):
#         return 2 * math.pi * self.radius


# # Test your solution:
# c = Circle(5)
# print("🟢 c.radius:", c.radius)
# print("🟢 c.diameter:", c.diameter)
# print("🟢 c.area:", c.area)
# print("🟢 c.circumference:", c.circumference)


# ----------------------------------------------------------------------
# 🟡 MEDIUM 4: Property with Setter
# Create a class Temperature with:
# - Private attribute: _celsius
# - Property: celsius (getter and setter)
# - Property: fahrenheit (getter and setter, converts automatically)
# - Property: kelvin (getter and setter, converts automatically)
# - Setter validation: celsius cannot be below -273.15 (absolute zero)
#
# Formulas: F = C * 9/5 + 32, K = C + 273.15
#
# Test: t = Temperature(25)
# Test: t.celsius -> 25
# Test: t.fahrenheit -> 77.0
# Test: t.kelvin -> 298.15
# Test: t.fahrenheit = 32
# Test: t.celsius -> 0.0
# Test: t.kelvin = 373.15
# Test: t.celsius -> 100.0
# Test: t.celsius = -300 -> should not change (below absolute zero)
# ----------------------------------------------------------------------

# Write your code below:


# class Temperature:
#     def __init__(self, celsius):
#         self._celsius = celsius

#     @property
#     def celsius(self):
#         return self._celsius

#     @celsius.setter
#     def celsius(self, value):
#         if value >= -273.15:
#             self._celsius = value

#     @property
#     def fahrenheit(self):
#         return self._celsius * 9 / 5 + 32

#     @fahrenheit.setter
#     def fahrenheit(self, value):
#         self._celsius = value

#     @property
#     def kelvin(self):
#         return self._celsius + 273.15

#     @kelvin.setter
#     def kelvin(self, value):
#         self._celsius = value


# # Test your solution:
# t = Temperature(25)
# print("🟡 t.celsius:", t.celsius)
# print("🟡 t.fahrenheit:", t.fahrenheit)
# print("🟡 t.kelvin:", t.kelvin)
# t.fahrenheit = 32
# print("🟡 After t.fahrenheit = 32, celsius:", t.celsius)
# t.kelvin = 373.15
# print("🟡 After t.kelvin = 373.15, celsius:", t.celsius)


# ----------------------------------------------------------------------
# 🟡 MEDIUM 5: Property with Validation
# Create a class Person with:
# - Private attributes: _name, _age, _email
# - Property: name (getter/setter, must be non-empty string)
# - Property: age (getter/setter, must be between 0 and 150)
# - Property: email (getter/setter, must contain "@")
# - Invalid values should print error message but not change the value
#
# Test: p = Person("Alice", 30, "alice@email.com")
# Test: p.name -> "Alice"
# Test: p.name = "" -> prints error, name stays "Alice"
# Test: p.age = 200 -> prints error, age stays 30
# Test: p.email = "invalid" -> prints error, email stays "alice@email.com"
# Test: p.name = "Bob" -> works, name is now "Bob"
# ----------------------------------------------------------------------

# Write your code below:


# class Person:
#     def __init__(self, name, age, email):
#         self._name = name
#         self._age = age
#         self._email = email

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         if len(value) != 0:
#             self._name = value
#         else:
#             print("Error: name must be non-empty")

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, value):
#         if 0 <= value <= 150:
#             self._age = value
#         else:
#             print("Error: age must be between 0 and 150")

#     @property
#     def email(self):
#         return self._email

#     @email.setter
#     def email(self, value):
#         if "@" in value:
#             self._email = value
#         else:
#             print("Error: email must contain an '@'")


# # Test your solution:
# p = Person("Alice", 30, "alice@email.com")
# print("🟡 p.name:", p.name)
# p.name = ""
# print("🟡 After invalid name:", p.name)
# p.age = 200
# print("🟡 After invalid age:", p.age)
# p.name = "Bob"
# print("🟡 After valid name change:", p.name)
# p.email = "invalid"
# print(p.email)

# ----------------------------------------------------------------------
# 🟡 MEDIUM 6: Property with Deleter
# Create a class User with:
# - Private attributes: _username, _password
# - Property: username (getter, setter, deleter)
# - Property: password (getter returns "****", setter, deleter)
# - Deleting username sets it to "deleted_user"
# - Deleting password sets it to None
# - Method: verify_password(pwd) -> returns True if pwd matches _password
#
# Test: u = User("john_doe", "secret123")
# Test: u.username -> "john_doe"
# Test: u.password -> "****"
# Test: u.verify_password("secret123") -> True
# Test: del u.username
# Test: u.username -> "deleted_user"
# Test: del u.password
# Test: u.verify_password("secret123") -> False
# ----------------------------------------------------------------------

# Write your code below:


# class User:
#     def __init__(self, username, password):
#         self._username = username
#         self._password = password

#     @property
#     def username(self):
#         return self._username

#     @username.setter
#     def username(self, value):
#         self._username = value

#     @username.deleter
#     def username(self):
#         self._username = "deleted_user"

#     @property
#     def password(self):
#         return "*****"

#     @password.setter
#     def password(self, new_password):
#         self._password = new_password

#     @password.deleter
#     def password(self):
#         self._password = None

#     def verify_password(self, pwd):
#         return self._password == pwd


# # Test your solution:
# u = User("john_doe", "secret123")
# print("🟡 u.username:", u.username)
# print("🟡 u.password:", u.password)
# print("🟡 verify_password('secret123'):", u.verify_password("secret123"))
# del u.username
# del u.password
# print("🟡 After delete username:", u.username)
# print("🟡 After delete password:", u.password)


# ----------------------------------------------------------------------
# 🔴 HARD 1: Computed Properties with Caching
# Create a class Rectangle with:
# - Private attributes: _width, _height
# - Private cache: _area_cache, _perimeter_cache (initially None)
# - Property: width (getter/setter - setter clears cache)
# - Property: height (getter/setter - setter clears cache)
# - Property: area (calculates only if cache is None, otherwise returns cache)
# - Property: perimeter (calculates only if cache is None, otherwise returns cache)
# - Print "Calculating area..." or "Calculating perimeter..." when actually computing
#
# Test: r = Rectangle(5, 3)
# Test: r.area -> prints "Calculating area...", returns 15
# Test: r.area -> returns 15 (no print, uses cache)
# Test: r.width = 10
# Test: r.area -> prints "Calculating area...", returns 30 (cache was cleared)
# ----------------------------------------------------------------------

# Write your code below:


# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height
#         self._area_cache = None
#         self._perimeter_cache = None

#     @property
#     def width(self):
#         return self._width

#     @width.setter
#     def width(self, value):
#         self._width = value
#         self._area_cache = None
#         self._perimeter_cache = None

#     @property
#     def height(self):
#         return self._height

#     @height.setter
#     def height(self, value):
#         self._height = value
#         self._area_cache = None
#         self._perimeter_cache = None

#     @property
#     def area(self):
#         if self._area_cache is None:
#             print("Calculating area...")
#             self._area_cache = self.width * self.height
#             return self._area_cache
#         else:
#             print("Caching...")
#             return self._area_cache

#     @property
#     def perimeter(self):
#         if self._perimeter_cache is None:
#             print("Calculating perimeter...")
#             self._perimeter_cache = self.width * 2 + self.height * 2
#             return self._perimeter_cache
#         else:
#             print("Caching...")
#             return self._perimeter_cache


# # Test your solution:
# r = Rectangle(5, 3)
# print("🔴 First r.area call:")
# print("   Result:", r.area)
# print("🔴 Second r.area call:")
# print("   Result:", r.area)
# r.width = 10
# print("🔴 After changing width:")
# print("   Result:", r.area)
# print(r.perimeter)
# print(r.perimeter)


# =====================================================================
#                   SECTION 4: @abstractmethod
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 MEDIUM 7: Basic Abstract Class
# Create an abstract class Shape with:
# - Abstract method: area()
# - Abstract method: perimeter()
# - Concrete method: describe() -> returns "This shape has area {area} and perimeter {perimeter}"
#
# Create class Rectangle(Shape):
# - Attributes: width, height
# - Implement area() and perimeter()
#
# Create class Circle(Shape):
# - Attribute: radius
# - Implement area() and p1erimeter()
#
# Test: Shape() -> raises TypeError
# Test: r = Rectangle(4, 5)
# Test: r.area() -> 20
# Test: r.perimeter() -> 18
# Test: r.describe() -> "This shape has area 20 and perimeter 18"
# Test: c = Circle(3)
# Test: c.area() -> 28.274333882308138
# ----------------------------------------------------------------------

# Write your code below:

# from abc import ABC, abstractmethod


# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         raise NotImplementedError("You have to implement the perimeter() method")

#     def describe(self):
#         return f"This shape has area {self.area()} and perimeter {self.perimeter()}"


# class Rectangle(Shape):
#     def __init__(self, width, height):
#         super().__init__()
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return self.width * 2 + self.height * 2


# # Test your solution:
# try:
#     s = Shape()
# except TypeError as e:
#     print("🟡 Cannot instantiate Shape:", e)
# r = Rectangle(4, 5)
# print("🟡 r.area():", r.area())
# print("🟡 r.describe():", r.describe())


# ----------------------------------------------------------------------
# 🟡 MEDIUM 8: Abstract Class with Partial Implementation
# Create an abstract class Animal with:
# - Abstract method: speak()
# - Abstract method: move()
# - Concrete method: describe() -> returns "{class name} says {speak()} and {move()}"
# - Concrete attribute: is_alive = True
#
# Create concrete classes:
# - Dog: speak() -> "Woof!", move() -> "runs"
# - Cat: speak() -> "Meow!", move() -> "walks"
# - Bird: speak() -> "Chirp!", move() -> "flies"
#
# Test: d = Dog()
# Test: d.speak() -> "Woof!"
# Test: d.describe() -> "Dog says Woof! and runs"
# Test: d.is_alive -> True
# ----------------------------------------------------------------------

# Write your code below:

# from abc import ABC
# from abc import abstractmethod


# class Animal(ABC):
#     is_alive = True

#     @abstractmethod
#     def speak(self) -> str:
#         pass

#     @abstractmethod
#     def move(self) -> str:
#         pass

#     def describe(self):
#         return f"{type(self).__name__} says {self.speak()} and {self.move()}"


# class Dog(Animal):
#     def move(self):
#         return "runs"

#     def speak(self):
#         return "Woof!"


# class Cat(Animal):
#     def move(self):
#         return "walks"

#     def speak(self):
#         return "Meow!"


# class Bird(Animal):
#     def move(self):
#         return "flies"

#     def speak(self):
#         return "Chirp!"


# # Test your solution:
# d = Dog()
# c = Cat()
# b = Bird()
# print("🟡 d.describe():", d.describe())
# print("🟡 c.describe():", c.describe())
# print("🟡 b.describe():", b.describe())


# ----------------------------------------------------------------------
# 🔴 HARD 2: Abstract Properties
# Create an abstract class Vehicle with:
# - Abstract property: max_speed
# - Abstract property: fuel_type
# - Concrete method: info() -> returns "{class} - Max Speed: {max_speed}, Fuel: {fuel_type}"
#
# Create class Car(Vehicle):
# - Property max_speed returns 200
# - Property fuel_type returns "Gasoline"
#
# Create class ElectricCar(Vehicle):
# - Property max_speed returns 250
# - Property fuel_type returns "Electric"
#
# Create class Bicycle(Vehicle):
# - Property max_speed returns 30
# - Property fuel_type returns "Human Power"
#
# Test: Vehicle() -> raises TypeError
# Test: car = Car()
# Test: car.max_speed -> 200
# Test: car.info() -> "Car - Max Speed: 200, Fuel: Gasoline"
# ----------------------------------------------------------------------

# Write your code below:

# from abc import ABC
# from abc import abstractmethod


# class Vehicle(ABC):
#     @property
#     @abstractmethod
#     def max_speed(self) -> int:
#         pass

#     @property
#     @abstractmethod
#     def fuel_type(self) -> str:
#         pass

#     def info(self):
#         return f"{type(self).__name__} - Max Speed: {self.max_speed}, Fuel: {self.fuel_type}"


# class Car(Vehicle):
#     @property
#     def max_speed(self):
#         return 200

#     @property
#     def fuel_type(self):
#         return "Gasoline"


# class ElectricCar(Vehicle):
#     @property
#     def max_speed(self):
#         return 250

#     @property
#     def fuel_type(self):
#         return "Electric"


# class Bicycle(Vehicle):
#     @property
#     def max_speed(self):
#         return 30

#     @property
#     def fuel_type(self):
#         return "Human power"


# # Test your solution:
# car = Car()
# ecar = ElectricCar()
# bike = Bicycle()
# print("🔴 car.info():", car.info())
# print("🔴 ecar.info():", ecar.info())
# print("🔴 bike.info():", bike.info())


# ----------------------------------------------------------------------
# 🔴 HARD 3: Abstract Class with Mixed Methods
# Create an abstract class DataProcessor with:
# - Abstract method: read_data(source)
# - Abstract method: process_data(data)
# - Abstract method: write_data(data, destination)
# - Concrete method: run(source, destination) -> calls read, process, write in order
#
# Create class CSVProcessor(DataProcessor):
# - read_data() -> returns "Reading CSV from {source}"
# - process_data() -> returns "Processing CSV: {data}"
# - write_data() -> returns "Writing CSV to {destination}"
#
# Create class JSONProcessor(DataProcessor):
# - read_data() -> returns "Reading JSON from {source}"
# - process_data() -> returns "Processing JSON: {data}"
# - write_data() -> returns "Writing JSON to {destination}"
#
# Test: csv = CSVProcessor()
# Test: csv.run("input.csv", "output.csv") -> executes all three methods
# ----------------------------------------------------------------------

# Write your code below:

# from abc import ABC
# from abc import abstractmethod


# class DataProcessor(ABC):
#     @abstractmethod
#     def read_data(self, source) -> str:
#         pass

#     @abstractmethod
#     def process_data(self, data) -> str:
#         pass

#     @abstractmethod
#     def write_data(self, data, destination) -> str:
#         pass

#     def run(self, source, destination):
#         data = self.read_data(source)
#         processed = self.process_data(data)
#         self.write_data(processed, destination)


# class CSVProcessor(DataProcessor):
#     def read_data(self, source):
#         return f"Reading CSV from {source}"

#     def process_data(self, data):
#         return f"Processing CSV: {data}"

#     def write_data(self, data, destination):
#         return f"Writing CSV to {destination}"


# class JSONProcessor(DataProcessor):
#     def read_data(self, source):
#         return f"Reading JSON from {source}"

#     def process_data(self, data):
#         return f"Processing JSON: {data}"

#     def write_data(self, data, destination):
#         return f"Writing JSON to {destination}"


# # Test your solution:
# csv = CSVProcessor()
# print("🔴 CSVProcessor.run():")
# csv.run("input.csv", "output.csv")
# json_proc = JSONProcessor()
# print("🔴 JSONProcessor.run():")
# json_proc.run("input.json", "output.json")


# =====================================================================
#               SECTION 5: COMBINING DECORATORS
# =====================================================================


# ----------------------------------------------------------------------
# 🔴 HARD 4: All Decorators in One Class
# Create a class BankAccount with:
# - Class attribute: bank_name = "MyBank"
# - Class attribute: total_accounts = 0
# - Private instance attributes: _account_number, _balance, _owner
#
# Static methods:
# - generate_account_number() -> returns random 10-digit string
# - validate_amount(amount) -> returns True if amount > 0
#
# Class methods:
# - get_bank_info() -> returns "{bank_name} has {total_accounts} accounts"
# - change_bank_name(new_name) -> changes bank_name
#
# Properties:
# - balance (getter only, returns _balance)
# - owner (getter and setter with validation - non-empty string)
#
# Instance methods:
# - deposit(amount) -> adds to balance if valid
# - withdraw(amount) -> subtracts if valid and sufficient funds
#
# Test all features
# ----------------------------------------------------------------------

# Write your code below:

# import random


# class BankAccount:
#     bank_name = "MyBank"
#     total_accounts = 0

#     def __init__(self, owner, account_number="", balance=0):
#         self._account_number = BankAccount.generate_account_number()
#         self._balance = balance
#         self._owner = owner
#         BankAccount.total_accounts += 1

#     @staticmethod
#     def generate_account_number():
#         account = ""
#         for _ in range(0, 10):
#             account += str(random.randint(0, 9))
#         return account

#     @staticmethod
#     def validate_amount(amount):
#         return amount > 0

#     @classmethod
#     def get_bank_info(cls):
#         return f"{cls.bank_name} has {cls.total_accounts} accounts"

#     @classmethod
#     def change_bank_name(cls, name):
#         cls.bank_name = name

#     @property
#     def balance(self):
#         return self._balance

#     @property
#     def owner(self):
#         return self._owner

#     @owner.setter
#     def owner(self, owner):
#         if len(owner) > 0:
#             self._owner = owner

#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount

#     def withdraw(self, amount):
#         if amount <= self._balance:
#             self._balance -= amount


# # Test your solution:
# print("🔴 Initial bank info:", BankAccount.get_bank_info())
# acc = BankAccount("Alice")
# print("🔴 After creating account:", BankAccount.get_bank_info())
# print("🔴 Balance:", acc.balance)
# acc.deposit(1000)
# print("🔴 After deposit:", acc.balance)
# acc.withdraw(300)
# print("🔴 After withdraw:", acc.balance)


# ----------------------------------------------------------------------
# 🔴 HARD 5: Abstract Class with Class and Static Methods
# Create an abstract class Logger with:
# - Class attribute: log_level = "INFO"
# - Class method: set_log_level(level) -> sets log_level
# - Class method: get_log_level() -> returns log_level
# - Static method: format_message(level, message) -> "[{level}] {message}"
# - Abstract method: log(message)
#
# Create class ConsoleLogger(Logger):
# - log() -> prints formatted message to console
#
# Create class FileLogger(Logger):
# - Attribute: filename
# - log() -> returns "Would write to {filename}: {formatted_message}"
#
# Test: Logger.set_log_level("DEBUG")
# Test: ConsoleLogger().log("Test message")
# Test: FileLogger("app.log").log("Test message")
# ----------------------------------------------------------------------

# Write your code below:

# from abc import ABC
# from abc import abstractmethod


# class Logger(ABC):
#     log_level = "INFO"

#     @classmethod
#     def set_log_level(cls, level):
#         cls.log_level = level

#     @classmethod
#     def get_log_level(cls):
#         return cls.log_level

#     @staticmethod
#     def format_message(level, message):
#         return f"[{level}] {message}"

#     @abstractmethod
#     def log(self, message):
#         pass


# class ConsoleLogger(Logger):
#     def log(self, message):
#         print(self.format_message(self.log_level, message))


# class FileLogger(Logger):
#     def __init__(self, filename):
#         super().__init__()
#         self.filename = filename

#     def log(self, message):
#         return f"{self.filename}: {self.format_message(self.log_level, message)}"

# # Test your solution:
# Logger.set_log_level("DEBUG")
# print("🔴 Log level:", Logger.get_log_level())
# console = ConsoleLogger()
# console.log("Application started")
# file_logger = FileLogger("app.log")
# print("🔴 FileLogger:", file_logger.log("Application started"))


# ----------------------------------------------------------------------
# 🔴 HARD 6: Property in Abstract Class
# Create an abstract class Polygon with:
# - Abstract property: sides (returns number of sides)
# - Abstract property: angles (returns list of angles)
# - Concrete property: angle_sum -> returns sum of angles
# - Concrete method: is_valid() -> returns True if angle_sum equals (sides-2)*180
#
# Create class Triangle(Polygon):
# - Attributes: angle1, angle2, angle3
# - sides property returns 3
# - angles property returns [angle1, angle2, angle3]
#
# Create class Quadrilateral(Polygon):
# - Attributes: angle1, angle2, angle3, angle4
# - sides property returns 4
# - angles property returns all four angles
#
# Test: t = Triangle(60, 60, 60)
# Test: t.sides -> 3
# Test: t.angle_sum -> 180
# Test: t.is_valid() -> True
# Test: t2 = Triangle(90, 90, 90)
# Test: t2.is_valid() -> False (sum is 270, not 180)
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# t = Triangle(60, 60, 60)
# print("🔴 t.sides:", t.sides)
# print("🔴 t.angles:", t.angles)
# print("🔴 t.angle_sum:", t.angle_sum)
# print("🔴 t.is_valid():", t.is_valid())
# t2 = Triangle(90, 90, 90)
# print("🔴 t2.is_valid():", t2.is_valid())


# =====================================================================
#                  SECTION 6: REAL-WORLD SCENARIOS
# =====================================================================


# ----------------------------------------------------------------------
# 🔴 HARD 7: Plugin System with Abstract Base
# Create a plugin system:
#
# Abstract class Plugin:
# - Class attribute: registered_plugins = []
# - Abstract method: execute(data)
# - Abstract property: name
# - Abstract property: version
# - Class method: register(plugin_class) -> adds to registered_plugins
# - Class method: get_all_plugins() -> returns registered_plugins
# - Static method: validate_plugin(plugin) -> returns True if has name and version
#
# Create class UppercasePlugin(Plugin):
# - name = "Uppercase"
# - version = "1.0"
# - execute(data) -> returns data.upper()
#
# Create class ReversePlugin(Plugin):
# - name = "Reverse"
# - version = "1.0"
# - execute(data) -> returns data[::-1]
#
# Test: Plugin.register(UppercasePlugin)
# Test: Plugin.register(ReversePlugin)
# Test: Plugin.get_all_plugins() -> [UppercasePlugin, ReversePlugin]
# Test: UppercasePlugin().execute("hello") -> "HELLO"
# ----------------------------------------------------------------------

# Write your code below:
# from abc import ABC
# from abc import abstractmethod


# class Plugin(ABC):
#     registered_plugins = []

#     @abstractmethod
#     def execute(self, data):
#         pass

#     @property
#     @abstractmethod
#     def name(self):
#         pass

#     @property
#     @abstractmethod
#     def version(self):
#         pass

#     @classmethod
#     def register(cls, plugin):
#         cls.registered_plugins.append(str(plugin.__name__))

#     @classmethod
#     def get_all_plugins(cls):
#         return cls.registered_plugins

#     @staticmethod
#     def validate_plugin():
#         return (
#             True if (Plugin.name is not None and Plugin.version is not None) else False
#         )


# class UppercasePlugin(Plugin):
#     name = "Uppercase"  # type: ignore
#     version = "1.0"  # type: ignore

#     def execute(self, data):
#         return data.upper()


# class ReversePlugin(Plugin):
#     name = "Reverse"  # type: ignore
#     version = "1.0"  # type: ignore

#     def execute(self, data):
#         return data[::-1]


# # Test your solution:
# Plugin.register(UppercasePlugin)
# Plugin.register(ReversePlugin)
# print("🔴 Registered plugins:", (Plugin.get_all_plugins()))
# up = UppercasePlugin()
# print(up.validate_plugin())
# print("🔴 UppercasePlugin.execute('hello'):", up.execute("hello"))
# lo = ReversePlugin()
# print("🔴 ReversePlugin.execute('hello'):", lo.execute("hello"))
# print(lo.validate_plugin())

# ----------------------------------------------------------------------
# 🔴 HARD 8: ORM-Style Model
# Create a base class Model with:
# - Class attribute: _table_name = None
# - Class method: table_name() -> returns _table_name or class name lowercase
# - Class method: create_table() -> returns "CREATE TABLE {table_name} (...)"
# - Class method: find(id) -> returns "SELECT * FROM {table_name} WHERE id = {id}"
# - Class method: all() -> returns "SELECT * FROM {table_name}"
# - Static method: sanitize(value) -> removes quotes from strings
#
# Properties:
# - id (getter/setter)
#
# Instance methods:
# - save() -> returns "INSERT INTO {table_name} ..." or "UPDATE {table_name} ..."
# - delete() -> returns "DELETE FROM {table_name} WHERE id = {id}"
#
# Create class User(Model):
# - _table_name = "users"
# - Attributes: id, name, email
#
# Test: User.table_name() -> "users"
# Test: User.find(1) -> "SELECT * FROM users WHERE id = 1"
# Test: u = User(1, "Alice", "alice@email.com")
# Test: u.save() -> appropriate SQL
# ----------------------------------------------------------------------

# Write your code below:

# from abc import ABC
# from abc import abstractmethod


# class Model(ABC):
#     _table_name = None

#     @classmethod
#     def table_name(cls):
#         return cls._table_name

#     @classmethod
#     def create_table(cls):
#         return f'"CREATE TABLE {cls.table_name()}"'

#     @classmethod
#     def find(cls, id):
#         return f'"SELECT * FROM {cls.table_name()} WHERE ID = {id}"'

#     @classmethod
#     def all(cls):
#         return f'"SELECT * FROM {cls.table_name()}"'

#     @property
#     def id(self):
#         return self.identification

#     @id.setter
#     def id(self, value):
#         self.identification = value

#     def save(self):
#         return f'"INSERT INTO {self._table_name}"'

#     def delete(self):
#         return f'"DELETE FROM {self._table_name} WHERE id = {self.id}"'

#     @staticmethod
#     def sanitize(value):
#         return value.replace('"', "")


# class User(Model):
#     _table_name = "users"

#     def __init__(self, identification, name, email):
#         super().__init__()
#         self.identification = identification
#         self.name = name
#         self.email = email


# # Test your solution:
# print("🔴 User.table_name():", User.table_name())
# print("🔴 User.find(1):", User.find(1))
# print("🔴 User.all():", User.all())
# u = User(1, "Alice", "alice@email.com")
# u.id = 2
# print("🔴 User.table_name():", u.id)
# print("🔴 u.save():", u.save())
# print("🔴 User.all():", u.delete())
# print(User.sanitize(u.find(1)))


# ----------------------------------------------------------------------
# 🔴 HARD 9: Serialization System
# Create an abstract class Serializable with:
# - Abstract method: to_dict() -> converts object to dictionary
# - Abstract class method: from_dict(data) -> creates object from dictionary
# - Concrete method: to_json() -> converts to JSON string (use json module)
# - Concrete class method: from_json(json_string) -> creates from JSON
#
# Create class Product(Serializable):
# - Attributes: name, price, quantity
# - Implement to_dict() and from_dict()
#
# Test: p = Product("Laptop", 999.99, 5)
# Test: p.to_dict() -> {"name": "Laptop", "price": 999.99, "quantity": 5}
# Test: p.to_json() -> '{"name": "Laptop", "price": 999.99, "quantity": 5}'
# Test: p2 = Product.from_dict({"name": "Phone", "price": 599.99, "quantity": 10})
# Test: p2.name -> "Phone"
# ----------------------------------------------------------------------

# Write your code below:

# from abc import ABC
# from abc import abstractmethod
# import json


# class Serializable(ABC):
#     @abstractmethod
#     def to_dict(self):
#         pass

#     @classmethod
#     def from_dict(cls, a_dict):
#         pass

#     def to_json(self):
#         return json.dumps(self.to_dict())

#     @classmethod
#     def from_json(cls, json_string):
#         a_dict = json.loads(json_string)
#         return cls.from_dict(a_dict)


# class Product(Serializable):
#     def __init__(self, name, price, quantity):
#         super().__init__()
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def to_dict(self):
#         a_dict = dict()
#         a_dict["name"] = self.name
#         a_dict["price"] = self.price
#         a_dict["quantity"] = self.quantity
#         return a_dict

#     @classmethod
#     def from_dict(cls, a_dict):
#         return cls(a_dict["name"], a_dict["price"], a_dict["quantity"])


# # Test your solution:
# p = Product("Laptop", 999.99, 5)
# print("🔴 p.to_dict():", p.to_dict())
# print("🔴 p.to_json():", p.to_json())
# p2 = Product.from_dict({"name": "Phone", "price": 599.99, "quantity": 10})
# print("🔴 p2.name:", p2.name)


# ----------------------------------------------------------------------
# 🔴 HARD 10: Configuration Manager
# Create a class Config with:
# - Private class attribute: _instance = None (for singleton)
# - Private class attribute: _settings = {}
# - Class method: get_instance() -> returns singleton instance
# - Class method: load_from_dict(settings) -> updates _settings
# - Class method: get(key, default=None) -> gets setting value
# - Class method: set(key, value) -> sets setting value
# - Static method: validate_key(key) -> returns True if key is non-empty string
# - Property: all_settings -> returns copy of _settings
#
# Implement as Singleton (only one instance ever exists)
#
# Test: Config.set("debug", True)
# Test: Config.get("debug") -> True
# Test: Config.get("missing", "default") -> "default"
# Test: c1 = Config.get_instance()
# Test: c2 = Config.get_instance()
# Test: c1 is c2 -> True
# ----------------------------------------------------------------------

# Write your code below:


# Test your solution:
# Config.set("debug", True)
# Config.set("version", "1.0.0")
# print("🔴 Config.get('debug'):", Config.get("debug"))
# print("🔴 Config.get('missing', 'default'):", Config.get("missing", "default"))
# c1 = Config.get_instance()
# c2 = Config.get_instance()
# print("🔴 c1 is c2:", c1 is c2)


# ======================================================================
# 📊 EXERCISE SUMMARY
# ======================================================================
# 🟢 EASY (5):     Basic @staticmethod, basic @classmethod, basic @property
# 🟡 MEDIUM (8):   Alternative constructors, validation, setters, ABC basics
# 🔴 HARD (10):    Combined decorators, abstract properties, real-world systems
#
# Total: 23 Exercises
#
# Decorator Coverage:
# - @staticmethod: Utility functions, validators, converters
# - @classmethod: Factory methods, alternative constructors, class state
# - @property: Getters, setters, deleters, computed properties
# - @abstractmethod: Abstract classes, interfaces, abstract properties
#
# Patterns Covered:
# - Factory Pattern (class methods)
# - Singleton Pattern (class methods)
# - Template Method (abstract methods)
# - Plugin System (abstract + class methods)
# ======================================================================
