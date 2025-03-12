from car import Car

myNewCar = Car('audi', 'a5', 2025)
print(myNewCar.describe_car())

myNewCar.odometer_reading = 23
myNewCar.read_odometer()
