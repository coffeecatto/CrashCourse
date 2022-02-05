# 4-2 Animals

# Create a list of animals that have at least one thing in common, then use a loop to print the name of each animal.

animals = ['dog', 'cat', 'horse']
for animal in animals:
    print(animal)

# Modify the above to make a statement about each animal. 

for animal in animals:
    print(f"{animal.title()}s can be very loyal and loving animals.")

# Once again, add a 'finishing line' outside the loop, at the end. 

print("\nSeperator print message, don't mind me!\n")
for animal in animals:
    print(f"{animal.title()}s can be very loyal and loving animals.")
print("Every countryside has at least one of these animals.")