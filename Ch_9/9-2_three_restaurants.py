# 9-2 Three Restaurants
# Same as 9-1, but make three instances
class Restaurant:
    """Simple class with info about a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Prints restaurant's name and cuisine type info."""
        print(f"\nThe restaurant is called {self.restaurant_name}.")
        print(f"Type of food served here: {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Prints info about restaurant being open."""
        print(f"{self.restaurant_name} is currently open!")

# Creating an instance
restaurant_1 = Restaurant('Little Italy', 'pizza')

# Testing defined functions
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

# Now for the other two instances
restaurant_2 = Restaurant('Fat Slices', 'pizza, fastfood, spaghetti')
restaurant_3 = Restaurant('Sielska', 'traditional polish cuisine')

restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
