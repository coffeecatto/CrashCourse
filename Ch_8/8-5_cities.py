# 8-5 Cities
# Write a function called describe_city(). 
# Make it accept name of the city and its country. 
# It should print a simple message using both parameters. 
# Create a value for default country.
# Print three messages, with at least one city not being in the default country. 
def describe_city(city, country = 'poland'):
    """Print information about city and its country."""
    print(f"{city.title()} is located in {country.title()}.")

# Print no 1
describe_city('warsaw')

# Print no 2
describe_city('sevilla', 'spain')

# Print no 3
describe_city(city = 'kiev', country = 'ukraine')