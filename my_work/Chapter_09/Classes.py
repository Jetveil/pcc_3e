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


# --- Наследование

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


# class ElectricCar(Car):  # <-- Класс наследует все атрибусы своего Супер-класса (родителя)
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)


# my_eclectric_car = ElectricCar('Renault', 'Model 5', 2025)
# print(my_eclectric_car.describe_car())


# --- Определение атрибутов и методов класса-потомка

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

#     def fill_gas_tank(self, gasAmount):
#         fillGas = f"Filling gas tank with {gasAmount}cbm"
#         return fillGas


# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery_capacity = 40

#     def describe_battery(self):
#         print(f"Battery capacity: {self.battery_capacity}kW/h")

#     def fill_gas_tank(self, gasAmount):
#         print("This car doesn't have a gas tank")


# my_eclectric_car = ElectricCar('Renault', 'Model 5', 2025)
# my_car = Car('VAZ', 'Gazelle', 2017)

# print(my_eclectric_car.describe_car())
# my_eclectric_car.describe_battery()
# my_eclectric_car.fill_gas_tank(20)

# print(my_car.describe_car())
# print(my_car.fill_gas_tank(5))

# --- Экземпляры как атрибуты (композиция)

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

#     def fill_gas_tank(self, gasAmount):
#         fillGas = f"Filling gas tank with {gasAmount}cbm"
#         return fillGas


# class ElectricCar(Car):
#     def __init__(self, make, model, year, battery_capacity):
#         super().__init__(make, model, year)
#         # <-- Аргумент для задания значения батареи при создании экземпляра класса
#         self.battery = Battery(battery_capacity)

#     def fill_gas_tank(self, gasAmount):
#         print("This car doesn't have a gas tank")


# class Battery:
#     def __init__(self, battery_capacity=40):
#         self.battery_capacity = battery_capacity

#     def describe_battery(self):
#         print(f"Battery capacity: {self.battery_capacity}kW/h")
#         return self.battery_capacity

#     def get_range(self):
#         if self.battery_capacity == 40:
#             range = 150
#         elif self.battery_capacity == 65:
#             range = 225

#         print(f"This car can go about {range}km on a full charge")


# my_eclectric_car = ElectricCar('Renault', 'Model 5', 2025, 40)
# my_eclectric_car.battery.describe_battery()
# my_eclectric_car.battery.get_range()
# my_car = Car('VAZ', 'Gazelle', 2017)
