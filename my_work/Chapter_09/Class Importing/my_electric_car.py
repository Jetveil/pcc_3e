from car import ElectricCar

myElectricCar = ElectricCar('Renault', 'Model 5', 2025, 40)
print(myElectricCar.describe_car())
myElectricCar.fill_gas_tank(100)
myElectricCar.read_odometer()
myElectricCar.update_odometer(20)
myElectricCar.read_odometer()
myElectricCar.battery.describe_battery()
myElectricCar.battery.get_range()
