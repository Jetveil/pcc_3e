class Restaurant:
    def __init__(self, restaurant_name, restaurant_cuisine):
        self.restaurant_name = restaurant_name.title()
        self.restaurant_cuisine = restaurant_cuisine

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Restaurant cuisine: {self.restaurant_cuisine} ")

    def open_restaurant(self):
        print(f"The Restaurant {self.restaurant_name} is open")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, restaurant_cuisine):
        super().__init__(restaurant_name, restaurant_cuisine)
        self.flavors = []

    def show_flavors(self):
        print(f"Avaliable flavors:")
        for flavor in self.flavors:
            print(f" - {flavor}")
