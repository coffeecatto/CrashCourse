# 6-10 Favorite Numbers

# Copying code from 6-2

fav_numbers = {
    'kacper': 69,
    'grzegorz': 3,
    'dariusz': 21,
    'patryk': 120,
    'kamil': 0.7,
}

for person in fav_numbers:
    print(f"{person.title()}'s favorite number is {fav_numbers[person]}!")

# Modify the code so that each person can have more than one fav number. Then
# print the info

fav_numbers = {
    'kacper': [69, 420],
    'grzegorz': [3],
    'dariusz': [6, 21, 42],
    'patryk': [120, 1],
    'kamil': [0.7, 0.5, 1],
}

for person, number in fav_numbers.items():
    print(f"{person.title()}'s favorite number(s): {number}")