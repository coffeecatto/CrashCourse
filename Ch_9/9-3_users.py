# 9-3 Users
# Make a class called User. 
# Attributes: first_name, last_name, and some of my own
# Methods: describe_user(), greet_user()
class User:
    """A simple class for creating users."""

    def __init__(self, first_name, last_name, age, gender, occupation):
        # Is there a better way to assign args to vars in such cases?
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.occupation = occupation
    
    def describe_user(self):
        """Print info about the user."""
        print(f"\nName: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Occupation: {self.occupation}")

    def greet_user(self):
        """A simple greeting message for the user."""
        print(f"Hello {self.first_name.title()}!")

# Now for the instances (let's make three)
user_1 = User('grzengrzonrz', 'vacooninstall', 69, 'ginger', 'Dungeon Master')
user_2 = User('blue', 'niebieski', 26, 'chad', 'Code Master 3000')
user_3 = User('jacek', 'soplica', 90, 'N/A', 'Proffessional Alcoholic')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()