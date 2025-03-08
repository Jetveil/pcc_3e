# --- Создание класса Dog

# class Dog:

#     """Простая модель собаки."""

#     def __init__(self, name, age):
#         """Инициализирует атрибуты name и age."""
#         self.name = name
#         self.age = age

#     def sit(self):
#         """Имитирует, как собака садится по команде."""
#         print(f"{self.name} is now sitting.")

#     def roll_over(self):
#         """Имитирует, как собака перекатывается по команде."""
#         print(f"{self.name} rolled over!")


# --- Создание экземпляра класса

# my_dog = Dog('Willie', 6)
# print(f"My dog's name is {my_dog.name} and it's age is {my_dog.age}")
# my_dog.sit()

# your_dog = Dog('Zeigbee', 6)
# print(f"\nYour dog's name is {your_dog.name} and it's age is {your_dog.age}")
# your_dog.roll_over()

# --- Работа с классами. Класс Car

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def describe_car(self):
#         fullName = f"{self.make}, {self.model}, {self.year}"
#         return fullName.title()


# myCar = Car('audi', 'quattro', 1999)
# print(myCar.describe_car())

# --- Назначение атрибуту значения по умолчанию

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0 # <-- Here

#     def describe_car(self):
#         fullName = f"\n{self.make}, {self.model}, {self.year}"
#         return fullName.title()

#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} kilometeres on it")


# myCar = Car('audi', 'quattro', 1999)

# print(myCar.describe_car())
# myCar.read_odometer()


# --- Изменение значений атрибутов
# -- Прямое изменение значения

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def describe_car(self):
#         fullName = f"\n{self.make}, {self.model}, {self.year}"
#         return fullName.title()

#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} kilometeres on it")


# myCar = Car('audi', 'quattro', 1999)

# print(myCar.describe_car())
# myCar.odometer_reading = 23 # <-- Here
# myCar.read_odometer()

# -- С помощью метода

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 5

#     def describe_car(self):
#         fullName = f"\n{self.make}, {self.model}, {self.year}"
#         return fullName.title()

#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} kilometeres on it")

#     def update_odometer(self, mileage):  # <-- Here
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back the odometer!")


# myCar = Car('audi', 'quattro', 1999)

# print(myCar.describe_car())
# myCar.update_odometer(2)  # <-- Here
# myCar.read_odometer()

# -- Изменение значения атрибута с приращением

# --- Изменение значений атрибутов
# -- Прямое изменение значения

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def describe_car(self):
#         fullName = f"\n{self.make}, {self.model}, {self.year}"
#         return fullName.title()

#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} kilometeres on it")


# myCar = Car('audi', 'quattro', 1999)

# print(myCar.describe_car())
# myCar.odometer_reading = 23 # <-- Here
# myCar.read_odometer()

# -- С помощью метода

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 5

#     def describe_car(self):
#         fullName = f"\n{self.make}, {self.model}, {self.year}"
#         return fullName.title()

#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} kilometeres on it")

#     def update_odometer(self, mileage):  # <-- Here
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back the odometer!")


# myCar = Car('audi', 'quattro', 1999)

# print(myCar.describe_car())
# myCar.update_odometer(2)  # <-- Here
# myCar.read_odometer()

# -- Изменение атрибута с приращением

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 5

#     def describe_car(self):
#         fullName = f"\n{self.make}, {self.model}, {self.year}"
#         return fullName.title()

#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} kilometeres on it")

#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back the odometer!")

#     def increment_odometer(self, miles):
#         self.odometer_reading += miles


# myCar = Car('audi', 'quattro', 1999)

# print(myCar.describe_car())
# myCar.update_odometer(10)
# myCar.increment_odometer(100)
# myCar.read_odometer()
