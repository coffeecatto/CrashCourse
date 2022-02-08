# 6-5 Rivers

# Create a dictionary with three keys(rivers) and values(countries) assigned
# to them

rivers = {
    'vistula': 'poland',
    'dnieper': 'ukraine',
    'nemen': 'lithuania',
}

# Use a loop to print a sentence about each river
print("Sentences about rivers:")

for river in rivers:
    print(f"{river.title()} runs through {rivers[river].title()}.")

# Use a loop to print the name of each river in the dictionary
print("\nRivers list:")

for river in rivers:
    print(river.title())

# Use a loop to print the name of each country in the dictionary
print("\nCountry list:")

for clay in rivers.values():
    print(clay.title())