# Car CLass
"""A class representing a car or something. I prefer bikes to be honest."""

class Car:
    """A simple class representing a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # Adding a mileage counter (or however it is called - I'm bad with cars)
        self.odometer_reading = 0
        self.gas_tank_status = 20

    def get_descriptive_name(self):
        """Return a formatted description."""
        # Mistake in code in the book here - author used 'manufacturer' 
        # instead of 'model' in this function. What the heck?
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
    
    def read_odometer(self):
        """Print how many miles there are on the odometer."""
        print(f"Current mileage: {self.odometer_reading}")
    
    def update_odometer(self, mileage):
        """Change mileage on the odometer."""
        # Added a simple check for rolling back the odometer
        # (Isn't rolling it back illegal?)
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"Hey! No rolling back the odometer!")
    
    def increment_odometer(self, mileage):
        """Add mileage to the odometer."""
        self.odometer_reading += mileage
    
    def fill_gas_tank(self, gas_amount):
        """Increases the amount of available gas in the car's tank."""
        self.gas_tank_status += gas_amount
        print(f"Added {gas_amount} units to the tank ({self.gas_tank_status} total).")

# BATTERY CLASS
class Battery:
    """Provides information about the electric car's battery."""

    def __init__(self, battery_size=75):
        """Stores battery size info (unit: kWh)."""

        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print info about the car's battery size."""
        print(f"This car's battery capacity is {self.battery_size} kWh.")
    
    def get_range(self):
        """Calculate car's range based on battery's capacity."""
        range = self.battery_size * 3.14
        print(f"Car's max range: {range} (based on battery's capacity).")

# ELECTRIC CAR CLASS
class ElectricCar(Car):
    """Stores information about electric types of cars."""

    def __init__(self, make, model, year):
        """Initialize attributes of parent class."""
        super().__init__(make, model, year) # super as in superclass (PARENT)

        # Initializing Battery class as an attribute in ElectricCar
        self.battery = Battery()
    
    def fill_gas_tank(self, gas_amount):
        """Override; electric cars don't have gas tanks!"""
        print("Electric cars do not use gas, dummy!")
