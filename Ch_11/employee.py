# Chapter 11

# Employee class to be used in Exercise 11-3

# Write a class called Employee. 
# __init__() should take: first name, last name, annual salary. 
# Store each of these attributes. 
# Write a method called give_raise(), default value: 5.000$. 

class Employee:
    """Simple employee class for Exercise 11-3."""
    
    def __init__(self, firstname, lastname, annual_salary):
        self.firstname = firstname
        self.lastname = lastname
        self.annual_salary = annual_salary
        
    def give_raise(self, raise_amount=5000):
        """Gives a raise - 5000$ by default, but accepts custom values."""
        self.annual_salary += raise_amount
    
    def show_info(self):
        """
        Prints information about the employee.
        Created for verifying if this code even works before writing
        unit tests for it :D
        """
        print(f"Employee information: \
                \nName: {self.firstname.title()} {self.lastname.title()} \
                \nAnnual salary: {self.annual_salary}$")