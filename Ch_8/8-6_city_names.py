# 8-6 City Names
# Write a function called city_country() that takes name of a city and
# its country. Returned string should look like this:
# Santiago, Chile
# Call the function at least three times (with different values). 
def city_country(city, country):
    """Returns a string with city and its country - formatted."""
    city_country_result = f"{city}, {country}"

    return city_country_result.title()

# Print no 1
pair_1 = city_country('santiago', 'chile')
pair_2 = city_country('wroclaw', 'poland')
pair_3 = city_country('madrid', 'spain')

print(pair_1)
print(pair_2)
print(pair_3)