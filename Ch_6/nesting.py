# Chapter 6
# Nesting

# Dictionaries can be stored in a list, and vice versa

# A List of Dictionaries
# Let's make a dictionary for three aliens, and then create a list from them

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Using range() to generate a list of aliens automatically
print("\nGenerating aliens")
aliens = [] # Emptying the list for this

# Making 30 aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Print first 5 aliens
for alien in aliens[:5]:
    print(alien)

# Show how many aliens are in the list
print(f"Total number of aliens: {len(aliens)}")

# Changing first three aliens on the list
print("Alien changing stuff")

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)

# Lists in dictionaries
print("\nLists in dictionaries")

pizza = {
    'crust': 'thick',
    'toppings': ['cheese', 'pepperoni', 'mushroom'],
}

print(f"You have ordered a pizza with {pizza['crust']} crust."
    "\nChosen toppings:")

# Break lines in 'print' command by using indents and new quotation
# marks in a new line (wish I knew that beforehand)
for topping in pizza['toppings']:
    print("\t" + topping) # \t for 4 spaces in front

# Favorite languages dictionary, this time with lists

favorite_languages = {
    'dariusz': ['python', 'swift', 'arnold c'],
    'kacper': ['python', 'whisky'],
    'grzegorz': ['uninstall', 'marudzenie'],
    'jakub': ['react', 'php'],
    'kamil': ['none']
}

# Remember to use .items() so that Python will look at both keys and values
for person, langs in favorite_languages.items():
    print(f"\n{person.title()}, your favorite languages are:")
    for lang in langs:
        print(f"\t{lang.title()}")

# DICTIONARIES IN DICTIONARIES

users = {
    'bluep': {
        'firstname': 'kacper',
        'lastname': 'niebieski',
        'location': 'slawacitropolis',
    },
    'vacool': {
        'firstname': 'grzegorz',
        'lastname': 'uninstall',
        'location': 'pizzeria',
    },
}

for username, userinfo in users.items():
    print(f"\nUsername: {username}")
    fullname = f"{userinfo['firstname'].title()} {userinfo['lastname'].title()}"
    print(f"Full name: {fullname}")
    print(f"Location: {userinfo['location'].title()}")