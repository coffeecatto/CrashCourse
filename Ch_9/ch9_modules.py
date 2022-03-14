# Modules for use with exercises in Chapter 9
"""A bunch of modules that can be used with exercises from Chapter 9."""

# Restaurant, from exercise 9-1
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

# User class, exercise 9-8
class User:
    """A simple class for creating users."""

    def __init__(self, first_name, last_name, age, gender, occupation, 
                 login_attempts):
        # Is there a better way to assign args to vars in such cases?
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.login_attempts = login_attempts
    
    def describe_user(self):
        """Print info about the user."""
        print(f"\nName: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Occupation: {self.occupation}")

    def greet_user(self):
        """A simple greeting message for the user."""
        print(f"Hello {self.first_name.title()}!")
    
    def increment_login_attempts(self):
        """Increase the value of login_attempts by one."""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset value of login_attempts to 0."""
        self.login_attempts = 0

# Privileges class (for use in Admin class)
class Privileges:
    """Stores info about user privileges."""

    def __init__(self, *privileges):
        """Stores privileges as strings in a list."""
        self.privileges = privileges

    def show_privileges(self):
        """Prints a list of admin's privileges."""
        print(f"Current privileges:")
        # Remember to use SELF goddammit
        for privilege in self.privileges:
            print(f"\t- {privilege}")

# Admin class goes here:
class Admin(User):
    """User with special administrative privileges (doh)."""

    def __init__(self, first_name, last_name, age, gender, occupation, 
                 login_attempts, *privileges):
        """Inheriting attributes from parent class."""
        super().__init__(first_name, last_name, age, gender, occupation, 
                         login_attempts)

        self.privileges = Privileges('can pin posts', 'can suspend users', 
                                     'can ban users', 'can modify user posts', 
                                     'can make backups', 'can make coffee',
                                     'can become dungeon master')
