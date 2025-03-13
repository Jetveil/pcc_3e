# --- 9.1

# class Restaurant:
#     def __init__(self, restaurant_name, restaurant_cuisine):
#         self.restaurant_name = restaurant_name.title()
#         self.restaurant_cuisine = restaurant_cuisine

#     def describe_restaurant(self):
#         print(f"Restaurant name: {self.restaurant_name}")
#         print(f"Restaurant cuisine: {self.restaurant_cuisine} ")

#     def open_restaurant(self):
#         print(f"The Restaurant {self.restaurant_name} is open")


# restaurant = Restaurant('babaganush', 'Jewish')

# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# --- 9.2

# class Restaurant:
#     def __init__(self, restaurant_name, restaurant_cuisine):
#         self.restaurant_name = restaurant_name.title()
#         self.restaurant_cuisine = restaurant_cuisine

#     def describe_restaurant(self):
#         print(f"\nRestaurant name: {self.restaurant_name}")
#         print(f"Restaurant cuisine: {self.restaurant_cuisine} ")

#     def open_restaurant(self):
#         print(f"The Restaurant {self.restaurant_name} is open")


# restaurant = Restaurant('babaganush', 'Jewish')
# restaurant2 = Restaurant('allegro pizza', 'italian')
# restaurant3 = Restaurant('bratci kebabtci', 'serbian')

# restaurant.describe_restaurant()
# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()


# --- 9.3

# class User:
#     def __init__(self, first_name, last_name, user_name, user_age):
#         self.name = first_name.title()
#         self.surname = last_name.title()
#         self.username = user_name
#         self.age = user_age

#     def describe_user(self):
#         print(f"\nUser name: {self.name}")
#         print(f"User last name: {self.surname}")
#         print(f"User nickname: {self.username}")
#         print(f"User age: {self.age}")

#     def greet_user(self):
#         print(f"Hello, {self.name} {self.surname} as {self.username}")


# ermak = User('dim', 'erm', 'pustotely', 31)
# dudar = User('gosha', 'dudar', 'cock teller', 27)

# ermak.describe_user()
# ermak.greet_user()

# dudar.describe_user()
# dudar.greet_user()


# --- 9.4

# class Restaurant:
#     def __init__(self, restaurant_name, restaurant_cuisine):
#         self.restaurant_name = restaurant_name.title()
#         self.restaurant_cuisine = restaurant_cuisine
#         self.number_surved = 0

#     def describe_restaurant(self):
#         print(f"Restaurant name: {self.restaurant_name}")
#         print(f"Restaurant cuisine: {self.restaurant_cuisine} ")
#         print(f"Number surved: {self.number_surved}")

#     def open_restaurant(self):
#         print(f"The Restaurant {self.restaurant_name} is open")

#     def set_number_surved(self, numberServed):
#         self.number_surved = numberServed

#     def increment_number_surved(self, incrementNumberSurved):
#         self.number_surved += incrementNumberSurved


# restaurant = Restaurant('babaganush', 'Jewish')

# restaurant.set_number_surved(5)
# restaurant.increment_number_surved(40)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# --- 9.5

# class User:
#     def __init__(self, first_name, last_name, user_name, user_age):
#         self.name = first_name.title()
#         self.surname = last_name.title()
#         self.username = user_name
#         self.age = user_age
#         self.login_attempts = 0

#     def increment_login_attempts(self):
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         self.login_attempts = 0

#     def describe_user(self):
#         print(f"\nUser name: {self.name}")
#         print(f"User last name: {self.surname}")
#         print(f"User nickname: {self.username}")
#         print(f"User age: {self.age}")

#     def greet_user(self):
#         print(f"Hello, {self.name} {self.surname} as {self.username}")


# ermak = User('dim', 'erm', 'pustotely', 31)
# dudar = User('gosha', 'dudar', 'cock teller', 27)

# ermak.describe_user()
# ermak.greet_user()
# ermak.increment_login_attempts()
# ermak.increment_login_attempts()
# print(f"Login attempts: {ermak.login_attempts}")
# ermak.reset_login_attempts()
# print(f"Login attempts: {ermak.login_attempts}")

# dudar.describe_user()
# dudar.greet_user()


# --- ex 9.6

# class Restaurant:
#     def __init__(self, restaurant_name, restaurant_cuisine):
#         self.restaurant_name = restaurant_name.title()
#         self.restaurant_cuisine = restaurant_cuisine

#     def describe_restaurant(self):
#         print(f"Restaurant name: {self.restaurant_name}")
#         print(f"Restaurant cuisine: {self.restaurant_cuisine} ")

#     def open_restaurant(self):
#         print(f"The Restaurant {self.restaurant_name} is open")


# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, restaurant_cuisine):
#         super().__init__(restaurant_name, restaurant_cuisine)
#         self.flavors = []

#     def show_flavors(self):
#         print(f"Avaliable flavors:")
#         for flavor in self.flavors:
#             print(f" - {flavor}")


# ice_cream_stand = IceCreamStand('CreamSpy', 'International')
# ice_cream_stand.flavors = [
#     'cream', 'amend', 'coca-cola']

# ice_cream_stand.show_flavors()
# ice_cream_stand.describe_restaurant()

# --- 9.7

# class User:
#     def __init__(self, first_name, last_name, user_name, user_age):
#         self.name = first_name.title()
#         self.surname = last_name.title()
#         self.username = user_name
#         self.age = user_age

#     def describe_user(self):
#         print(f"\nUser name: {self.name}")
#         print(f"User last name: {self.surname}")
#         print(f"User nickname: {self.username}")
#         print(f"User age: {self.age}")

#     def greet_user(self):
#         print(f"Hello, {self.name} {self.surname} as {self.username}")


# class Admin(User):
#     def __init__(self, first_name, last_name, user_name, user_age):
#         super().__init__(first_name, last_name, user_name, user_age)
#         self.privileges = []

#     def show_privileges(self):
#         print(f"Administrator privileges:")
#         for privilege in self.privileges:
#             print(f"- {privilege}")


# admin = Admin('Boss', 'Big', 'System228', 100)
# admin.privileges = ['ban users', 'delete users',
#                     'add messages', 'edit messages']

# admin.describe_user()
# admin.greet_user()
# admin.show_privileges()

# --- 9.8

# class User:
#     def __init__(self, first_name, last_name, user_name, user_age):
#         self.name = first_name.title()
#         self.surname = last_name.title()
#         self.username = user_name
#         self.age = user_age

#     def describe_user(self):
#         print(f"\nUser name: {self.name}")
#         print(f"User last name: {self.surname}")
#         print(f"User nickname: {self.username}")
#         print(f"User age: {self.age}")

#     def greet_user(self):
#         print(f"Hello, {self.name} {self.surname} as {self.username}")


# class Admin(User):
#     def __init__(self, first_name, last_name, user_name, user_age):
#         super().__init__(first_name, last_name, user_name, user_age)
#         self.privileges = Privileges()


# class Privileges():
#     def __init__(self):
#         self.privileges = ['ban users', 'delete users',
#                            'add messages', 'edit messages']

#     def show_privileges(self):
#         print(f"Administrator privileges:")
#         for privilege in self.privileges:
#             print(f"- {privilege}")


# admin = Admin('Boss', 'Big', 'System228', 100)
# admin.describe_user()
# admin.greet_user()
# admin.privileges.show_privileges()


# --- 9.9

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
#     def __init__(self, battery_capacity):
#         self.battery_capacity = battery_capacity

#     def describe_battery(self):
#         print(f"Battery capacity: {self.battery_capacity}kW/h")
#         return self.battery_capacity

#     def upgrade_battery(self):
#         if self.battery_capacity != 65:
#             self.battery_capacity = 65

#     def get_range(self):
#         if self.battery_capacity == 40:
#             range = 150
#         elif self.battery_capacity == 65:
#             range = 225

#         print(f"This car can go about {range}km on a full charge")


# my_eclectric_car = ElectricCar('Renault', 'Model 5', 2025, 40)
# my_eclectric_car.battery.describe_battery()
# my_eclectric_car.battery.get_range()
# my_eclectric_car.battery.upgrade_battery()
# my_eclectric_car.battery.get_range()


# --- ex 9.13

# from random import randint


# class Die:
#     def __init__(self, sides=6):
#         self.sides = sides

#     def roll_die(self):
#         result = randint(1, self.sides)
#         return print(result)


# six_side_die = Die(6)
# six_side_die.roll_die()
# six_side_die.roll_die()
# six_side_die.roll_die()
# six_side_die.roll_die()

# print('-----')

# ten_side_die = Die(10)
# ten_side_die.roll_die()
# ten_side_die.roll_die()
# ten_side_die.roll_die()
# ten_side_die.roll_die()


# --- 9.14

from random import choice

values = [1, 'a', 2, 3, 'w', 4, 5, 'z', 6, 'q', 7, 8, 9, 0, 'g']


def get_win_values():
    win_values = []
    val = 0

    while val < 4:
        result = choice(values)
        win_values.append(result)
        val += 1

    print(f"Get these values to win: \n{win_values}")
    return win_values


def generate_my_ticket():
    my_ticket = []
    val = 0
    while val < 4:
        result = choice(values)
        my_ticket.append(result)
        val += 1
    print(f"My ticket is: \n{my_ticket}")
    return my_ticket


def get_win_chance(win_values, my_ticket):
    guess_try = 0
    current_ticket = my_ticket
    while current_ticket != win_values:
        current_ticket = []
        for v in range(4):
            result = choice(values)
            current_ticket.append(result)
            guess_try += 1
    print(f"Attemps to match the winning values: \n{guess_try}")
    return guess_try


winning_values = get_win_values()
my_ticket = generate_my_ticket()

get_win_chance(winning_values, my_ticket)

# --- 9.15
