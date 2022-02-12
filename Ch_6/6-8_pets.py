# 6-8 Pets

# Create several dictionaries, each representing a different pet. 
# Include what kind of animal it is, and the owner's name. 

moskwa = {
    'name': 'moskwa',
    'kind': 'cat',
    'owner': 'kacper',
}

mietek = {
    'name': 'mietek',
    'kind': 'dog',
    'owner': 'patryk',
}

michal = {
    'name': 'michal',
    'kind': 'spider',
    'owner': 'dariusz',
}

# Store these in a list called 'pets' 
pets = [moskwa, mietek, michal]

# Loop print all info about each pet
for pet in pets:
    print(f"\nInfo about pet {pet['name'].title()}:")
    print(f"\tKind: {pet['kind'].title()}")
    print(f"\tOwner: {pet['owner'].title()}")