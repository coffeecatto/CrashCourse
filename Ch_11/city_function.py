# 11-1 City, Country
# Main module file
def city_country(city, country, population=''):
    """Returns a neatly formatted string about a city and its country."""
    output = f"{city.title()}, {country.title()}"
    if population:
        output += f" - population {population}"
    return output