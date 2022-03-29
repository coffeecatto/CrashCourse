# Chapter 11

# Unit Tests
import unittest # imports stuff for unit tests, obviously
from name_function import get_formatted_name

class NameTestClass(unittest.TestCase):
    """Tests for 'name_function.py'."""
    
    def test_first_last_name(self):
        """Do names like 'Steve Jobs' work?"""
        formatted_name = get_formatted_name('steve', 'jobs')
        self.assertEqual(formatted_name, 'Steve Jobs')
        # ^ this will fail the test if formatted_name is not equal to
        # 'Steve Jobs' (basically, compare THIS to THAT)
    def test_first_middle_last_name(self):
        """Tests if names with middle names work."""
        formatted_name = get_formatted_name('gabe', 'newell', 'logan')
        self.assertEqual(formatted_name, 'Gabe Logan Newell')
        
if __name__ == '__main__': # won't run if imported somewhere else. Will 
                           # only run if run from here (as in MAIN program?)
    unittest.main()