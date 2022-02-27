# 9-5 Login Attempts
# Use code from 9-3.
# Add attribute login_attempts. 
# Add methods: increment_login_attempts(), reset_login_attempts()
class User:
    """A simple class for creating users."""

    def __init__(self, first_name, last_name, age, gender, occupation, login_attempts):
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

# Create an instance
user_1 = User('john', 'smith', 21, 'male', 'programmer', 0)

# Check current value of login_attempts
print(user_1.login_attempts)

# Call increment_login_attempts once, check if it works
user_1.increment_login_attempts()
print(user_1.login_attempts)

# Call increment_login_attempts multiple times, then print
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempts)

# Call reset_login_attempts, then print
user_1.reset_login_attempts()
print(user_1.login_attempts)
