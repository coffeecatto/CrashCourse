# 6-9 Favorite Places

# Create a dicitonary called 'favorite_places'. 
# Assign from one to three places to each person. 
# Loop print at the end. 
favorite_places = {
    'kacper': ['warszawa', 'limsa lominsa'],
    'dariusz': ['sevilla', 'marakesh', 'palermo'],
    'vacool': ['pizzeria']
}

# Now for the print loop
for person, places in favorite_places.items():
    print(f"{person.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")