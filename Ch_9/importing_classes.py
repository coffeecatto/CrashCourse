# Importing Classes

# Testing importing Car class from file car.py 
# from car import Car # From 'file/module' import 'Class'

# Importing multiple classes from the same module
from car import Car, ElectricCar
# NOTE: Can also import the whole module with 'import filename' 
# NOTE 2: Can also import all classes from a file with 'import *' 
# NOTE 3: Can also use aliases, as with methods etc. 
# I.E import X as Y

# Now to test if the Class has been imported properly
my_new_car = Car('nissan', 'fairlady z', 1969)
print(my_new_car.get_descriptive_name())

# Testing functions
my_new_car.odometer_reading = 1250
my_new_car.read_odometer()

# Trying to roll back the odometer so I can sell the car at a higher price
my_new_car.update_odometer(-1000)

# ELECTRIC CAR TEST
# from car import ElectricCar

# Create a non-existing Tesla from the future
my_tesla = ElectricCar('tesla', 'roadster s', 2090)

# Functions test!
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()