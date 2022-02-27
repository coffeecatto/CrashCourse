# 9-4 Number Served
# Start with code from 9-1. 
# Add an atribute called number_served. 
# Create a method set_number_served() that sets the amount of customers
# which have been served. Call this method with a new number and print the
# value again.
# Create a method increment_number_served() that does the same as above,
# but increments the value instead of completely changing it. 
class Restaurant:
    """Simple class with info about a restaurant."""

    def __init__(self, restaurant_name, cuisine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    def describe_restaurant(self):
        """Prints restaurant's name and cuisine type info."""
        print(f"The restaurant is called {self.restaurant_name}.")
        print(f"Type of food served here: {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Prints info about restaurant being open."""
        print(f"{self.restaurant_name} is currently open!")
    
    def set_number_served(self, amount):
        """Set the number of customers that have been served."""
        self.number_served = amount
        print(f"\nChanged number of served people to {self.number_served}.")
    
    def increment_number_served(self, amount):
        """Increment the amount of people served today."""
        self.number_served += amount
        print(f"\nIncremented number of served people to {self.number_served}.")
        if self.number_served == 690:
            print("That's a nice number of customers!")

# Now to test if the code works properly
# Create an instance
test_place = Restaurant('Pepe Bar', 'beer', 200)

# Checking previous methods
test_place.describe_restaurant()
test_place.open_restaurant()
print(f"Value of served people before changes: {test_place.number_served}")

# set_number_served test
test_place.set_number_served(320)

# increment_number_served test
test_place.increment_number_served(370)