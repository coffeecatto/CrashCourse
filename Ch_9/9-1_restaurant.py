# 9-1 Restaurant
# Make a class called Restaurant with attributes restaurant_name and
# cuisine_type.
# Create a method describe_restaurant() that prints this info, and a method
# open_restaurant() that prints info about restaurant being open. 
class Restaurant:
    """Simple class with info about a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Prints restaurant's name and cuisine type info."""
        print(f"The restaurant is called {self.restaurant_name}.")
        print(f"Type of food served here: {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Prints info about restaurant being open."""
        print(f"{self.restaurant_name} is currently open!")

# Creating an instance
italian_restaurant = Restaurant('Little Italy', 'pizza')

# Testing defined functions
italian_restaurant.describe_restaurant()
italian_restaurant.open_restaurant()