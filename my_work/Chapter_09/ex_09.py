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

class User:
    def __init__(self, first_name, last_name, user_name, user_age):
        self.name = first_name.title()
        self.surname = last_name.title()
        self.username = user_name
        self.age = user_age

    def describe_user(self):
        print(f"\nUser name: {self.name}")
        print(f"User last name: {self.surname}")
        print(f"User nickname: {self.username}")
        print(f"User age: {self.age}")

    def greet_user(self):
        print(f"Hello, {self.name} {self.surname} as {self.username}")


ermak = User('dim', 'erm', 'pustotely', 31)
dudar = User('gosha', 'dudar', 'cock teller', 27)

ermak.describe_user()
ermak.greet_user()

dudar.describe_user()
dudar.greet_user()
