# Base User module - to be used with user_additional.py 
"""Basic file for User class."""

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
