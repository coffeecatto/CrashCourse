# Additional classes for base file user_basemodule.py 
"""Additional classes extending the base User class."""

from user_basemodule import User

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
