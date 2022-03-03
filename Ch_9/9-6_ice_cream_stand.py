# 9-6 Ice Cream Stand
# Reuse code from 9-1 (Restaurant). 
# Write a class IceCreamStand that inherits from Restaurant class. 
# Add an attribute called 'flavors'. 
# Write a method that displays these flavors. 

# 9-1 Code goes here:
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

# END OF 9-1 CODE

# Ice Cream Stand class code
class IceCreamStand(Restaurant):
    """Provides simple information about Ice Cream Stands. Inherits from
    Restaurant class."""

    def __init__(self, restaurant_name, cuisine_type, *flavors):
        """Initialize attributes from parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def get_flavors(self):
        """Prints out the list of flavors."""
        print("Flavors on the list:")
        for flavor in self.flavors:
            print(f"\t- {flavor.title()}")

# Now to create an ice cream stand
mr_whoopee = IceCreamStand('mr whoopee', 'ice cream', 'vanilla', 'cherry', 
                           'chocolate', 'strawberry')

mr_whoopee.get_flavors()