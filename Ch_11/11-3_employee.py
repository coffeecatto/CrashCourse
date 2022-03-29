# 11-3 Employee

# Write a class called Employee. 
# __init__() should take: first name, last name, annual salary. 
# Store each of these attributes. 
# Write a method called give_raise(), default value: 5.000$. 

# Write a test case for class Employee in here.
# Write two methods: test_give_default_raise() and test_give_custom_raise(). 
# Use the setUp() method to create an Employee instance to be used in
# test methods. 
# ...I'm getting a deja vu here... 
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the Employee class."""
    
    def setUp(self):
        """Yes."""
        self.test_employee = Employee('Jan', 'Kowalski', 42000)

    def test_give_default_raise(self):
        """Tests giving the default raise (5000$)."""
        self.test_employee.give_raise()
        self.assertEqual(self.test_employee.annual_salary, 47000)
    
    def test_give_custom_raise(self):
        """Tests if giving a raise with custom amount works properly."""
        self.test_employee.give_raise(7200)
        self.assertEqual(self.test_employee.annual_salary, 49200)

if __name__ == '__main__':
    unittest.main()