# 9-7 Admin
# Reuse code from 9-3 Users or 9-5 Login Attempts. 
# Write an Admin class that inherits from User class. 
# Add an attribute 'privileges' that stores a list of strings (which describe
# these privileges). 
# Write a method called show_privileges() that lists what Admin can do. 

# Code from 9-5:
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

# END OF 9-5 CODE

# Admin class goes here:
class Admin(User):
    """User with special administrative privileges (doh)."""

    def __init__(self, first_name, last_name, age, gender, occupation, 
                 login_attempts, *privileges):
        """Inheriting attributes from parent class."""
        super().__init__(first_name, last_name, age, gender, occupation, 
        login_attempts)

        self.privileges = privileges
    
    def show_privileges(self):
        """Prints a list of admin's privileges."""
        print(f"Current privileges given to {self.first_name.title()}:")
        # Remember to use SELF goddammit
        for privilege in self.privileges:
            print(f"\t- {privilege}")

# Create an admin user
admin_1 = Admin('mister', 'president', 42, 'male', 'administrator', 
                0, 'can pin posts', 'can suspend users', 'can ban users',
                'can modify user posts', 'can make backups')

admin_1.show_privileges()