# Chapter 3, Lists

bikes = ["trek", "mountain", "city", "electric"]
print(bikes)

# Additional arguments for printing from list can be put in a square bracket, for example: position (0). Further modifiers work as before (after a dot).
# NOTE: I've known this for a long time, but just in case: index positions start at 0 - not 1 - in most programming languages.

print(bikes[0].title())

# '-1' can be used to pull the last item from the list (useful!). Putting a minus basically means that Python will go from the end of the list, so using -2 will use the second to last position, etc.

print(bikes[-1].title())
print(bikes[-2].title())

# This should go without saying, but - lists can also be used in messages.

print(f"I can't wait for spring to come around. I miss riding on my {bikes[0]} bike...")

# Practice mode - turn the above into a variable message

bike_msg = f"I can't wait for spring to come around. I miss riding on my {bikes[0]} bike..."
print(bike_msg)

# NOTE: Lists are dynamic! I can add, change and remove elements from it!

motorcycles = ['honda', 'suzuki', 'yamaha']
print(motorcycles)

# Now let's change Honda to Ducati. It's similar to how variables were changed in Chapter 2.

motorcycles[0] = 'ducati'
print(motorcycles)

# Start with an empty list, then use 'append' argument to add items

motorcycles2 = []
print(f"Before append:{motorcycles2}")

motorcycles2.append('honda')
motorcycles2.append('suzuki')
motorcycles2.append('yamaha')
print(f"After append:{motorcycles2}")

# Now let's try inserting stuff into the list.

motorcycles2.insert(0, 'nissan')
print(f"After insert:{motorcycles2}")

# Deleting from list - can be done through position number, or item name/value
# del is used when we want to use position for deleting

del motorcycles2[0]
print(f"After del:{motorcycles2}")

# Time to use 'pop()'. Items removed this way are stored in another list for future use. 

cars = ['porsche', 'nissan', 'bmw', 'ford']
print(cars)

# Now let's pop Ford from 'cars' into a new variable called 'removed_cars' 

removed_car = cars.pop()
print("pop test")
print(cars)
print(removed_car)

print(f"The last car I've removed from the list is {removed_car.title()}.")

# Can use index number in parentheses to pop specific position from the list

first_car = cars.pop(0)
print(f"First car from the 'cars' list used to be a {first_car.title()}, but that's now popped!")

# Can use 'remove' argument to remove by name/value

cars = ['porsche', 'nissan', 'bmw', 'ford']
print("Resetting 'cars' list...")
print(f"Default contents of 'cars' list: {cars}")

cars.remove('bmw')
print(f"List after removing BMW: {cars}")

# Now let's reset the list

cars = ['porsche', 'nissan', 'bmw', 'ford']
print("Resetting 'cars' list...")
print(f"Default contents of 'cars' list: {cars}")

# Set a variable with BMW, then remove by invoking the variable with remove argument?

shit_brand = 'bmw'
cars.remove(shit_brand)
print(f"Shit brand removed. Current list: {cars}")

# Yep, it works!
# NOTE: This removes only THE FIRST ENCOUNTERED OCCURENCE. If I want to remove ALL BMWs existing in a list, I'll need to create a loop. 
# That will come in Chapter 7. 