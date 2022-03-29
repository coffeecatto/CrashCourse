# 11-2 Population

# Same as 11-1, but create an optional 'population' parameter, and also
# a unit test for it. 
# The output should be like this: Santiago, Chile - population 500 000
import unittest
from city_function import city_country

class TestCityCountry(unittest.TestCase):
    """Tests if output generated by city_country() is correct."""
    
    def test_city_country(self):
        "Is the string from output formatted correctly?"
        tested_string = city_country('Barcelona', 'Spain')
        self.assertEqual(tested_string, 'Barcelona, Spain')
    
    def test_city_country_population(self):
        "Is the string from output formatted correctly with population number?"
        tested_string = city_country('Barcelona', 'Spain', '1602809')
        self.assertEqual(tested_string, 'Barcelona, Spain - population 1602809')

if __name__ == '__main__':
    unittest.main()