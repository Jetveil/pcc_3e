""""Класс для предоставления автомобиля"""


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 5

    def describe_car(self):
        fullName = f"\n{self.make}, {self.model}, {self.year}"
        return fullName.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} kilometeres on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self, gasAmount):
        fillGas = f"Filling gas tank with {gasAmount}cbm"
        return fillGas


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        # <-- Аргумент для задания значения батареи при создании экземпляра класса
        self.battery = Battery(battery_capacity)

    def fill_gas_tank(self, gasAmount):
        print("This car doesn't have a gas tank")


class Battery:
    def __init__(self, battery_capacity=40):
        self.battery_capacity = battery_capacity

    def describe_battery(self):
        print(f"Battery capacity: {self.battery_capacity}kW/h")
        return self.battery_capacity

    def get_range(self):
        if self.battery_capacity == 40:
            range = 150
        elif self.battery_capacity == 65:
            range = 225

        print(f"This car can go about {range}km on a full charge")
