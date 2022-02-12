# 6-7 People

# Starting by copying 6-1 code

# Store the following info about a person in a Python dictionary:
# first name, last name, age, current city. 
kacper = {
    'first name': 'kacper',
    'last name': 'niebieski',
    'age': 25,
    'city': 'slawacitropolis'
}

print(kacper)
print(f"Name: {kacper['first name'].title()},\n\
    Age: {kacper['age']},\n\
    City: {kacper['city'].title()}"
)

# Make two new dictionaries representing other people
vacool = {
    'first name': 'grzegorz',
    'last name': 'uninstall',
    'age': 999,
    'city': 'wilkowyje'
}

patryk = {
    'first name': 'patryk',
    'last name': 'pidzotto',
    'age': 29,
    'city': 'biala podlaska'
}

# Create a list containing these dictionaries
people = [kacper, vacool, patryk]

# Print all information about each person (create a loop for this)
for person in people:
    print(f"\nInformation about {person['first name'].title()}:")
    fullname = f"{person['first name']} {person['last name']}"
    print(f"\tFull name: {fullname.title()}")
    print(f"\tAge: {person['age']}")
    print(f"\tCity: {person['city'].title()}")