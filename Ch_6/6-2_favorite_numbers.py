# 6-2 Favorite Numbers

# Store favorite numbers of 5 people in a dictionary. 
# Print each person's name and their favorite number (looping time!). 

fav_numbers = {
    'kacper': 69,
    'grzegorz': 3,
    'dariusz': 21,
    'patryk': 120,
    'kamil': 0.7,
}

for person in fav_numbers:
    print(f"{person.title()}'s favorite number is {fav_numbers[person]}!")

# So 'person' in the loop gets assigned a value from the dictionary, and then
# I can use the square brackets to get the value assigned to that key. Nice!