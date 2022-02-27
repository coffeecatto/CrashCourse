# Chapter 9
# Classes

# Introduction to this chapter sounds interesting and confusing as fuck
# at the same time... 

# NOTE: Object-oriented programming stuff!

# CREATING A CLASS
# Dog Class
class Dog: # In Python, class names are capitalized (stylistic choice?)
    """A simple attempt to model a dog."""

    def __init__(self, name, age): # init as in initialize, create an instance
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over! Woof!")

# NOTE:
# Ah, fuck. I don't feel like the book does a good job with its initial
# description of classes. It gives quite lengthy explanations, but personally,
# I feel that it would be better to compare this to some basic, real-life
# concepts to make this easier to understand. 
# XXX: In simpler words:
# A class is basically a blueprint. It can be called upon to create things. 
# An instance is a thing created from a class (so, from a blueprint).
# That's what the __init__ thing is for - for creating an instance. 
# All 'def' stuff afterwards in the same code of block defines functions that
# can be used with this instance. 
# For example:
# my_dog = Dog('Reksio', 6) <- this creates an instance called my_dog. 
# Now, all functions defined for this class can be called in this way:
# my_dog.roll_over() <- just put the function's name after a dot.
# Many thanks to reddit user 'wolfgee' for an awesome explanation!

my_dog = Dog('Ciapek', 7)

print(f"My dog's name is {my_dog.name.title()}.")
print(f"He is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

# Classes can be used to create as many instances as one wants (of course)
# Let's create another instance
your_dog = Dog('Reksio', 5)

print("\nSECOND INSTANCE TEST\n")

print(f"My dog's name is {my_dog.name.title()}.")
print(f"He is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name.title()}.")
print(f"He is {your_dog.age} years old.")
your_dog.roll_over()

# Attributes in classes and instances
print(f"\nCLASS CAR TEST\n")

class Car:
    """A simple class representing a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # Adding a mileage counter (or however it is called - I'm bad with cars)
        self.odometer_reading = 0

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


my_car = Car('audi', 'a4', 2001)
print(my_car.get_descriptive_name())

# Modifying attributes
my_car.read_odometer()

# Direct modification
my_car.odometer_reading = 25
my_car.read_odometer()

# Change through a method
my_car.update_odometer(30)
my_car.read_odometer()

# Try to roll back the odometer (verifying the IF statement)
my_car.update_odometer(0)

# Increment through a method (result should be NICE in this case)
my_car.increment_odometer(39)
my_car.read_odometer()
