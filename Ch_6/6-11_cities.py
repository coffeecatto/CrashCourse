# 6-11 Cities

# Make a dictionary called 'cities' with three cities. 
# Info to include about each city: country, population, one fact

cities = {
    'sevilla': {
        'country': 'spain',
        'population': '~700.000',
        'fact': 'birthplace of Flamenco'
    },
    'warsaw': {
        'country': 'poland',
        'population': '~1.800.000',
        'fact': 'very expensive to live in',
    },
    'constantinople': {
        'country': 'turkey',
        'population': '~16.000.000',
        'fact': 'fifteenth largest city in the world'
    },
}

# Printing time
for city, cityinfo in cities.items():
    print(f"\nInfo about {city.title()}:")
    print(f"\tLocated in: {cityinfo['country'].title()}")
    print(f"\tPopulation: {cityinfo['population']}")
    print(f"\tRandom fact: {cityinfo['fact']}")