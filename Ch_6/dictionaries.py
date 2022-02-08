# Chapter 6, Dictionaries

# Dictionary is basically a collection of 'keys' that have assigned values to
# them. For example: 'color': 'pink'
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# Working with dictionaries
# Can be used to easily look up various data and assign values based on it

earned_points = alien_0['points']
print(f"{earned_points} points awarded to you!")

# Adding new key-value pairs

print("\nAdding key-value pairs")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_pos'] = 25
alien_0['y_pos'] = 0
print(alien_0)

# Can existing key-value pairs be overwritten with the same code?

print("\nOverwrite test")
alien_0['x_pos'] = 50
alien_0['y_pos'] = 25
print(alien_0)

# Yep! This works!
# NOTE: As of Python 3.7, dictionaries retain order in which values have
#       been added to them. 

# Starting with an empty dictionary is possible - works similarly to
# empty lists
print("\nStarting from empty dictionary")

alien_0 = {}
print(alien_0)

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# Dictionaries combined with if statements can become powerful tools for
# modifying existing values based on what is currently happening

# Alien movement example

alien_0 = {'x_pos': 0, 'y_pos': 25, 'speed': 'medium'}
print(f"Original position: X{alien_0['x_pos']}, Y{alien_0['y_pos']}")

# Now to move the alien to the right (based on current speed)
if alien_0['speed'] == 'slow':
    x_incr = 1
elif alien_0['speed'] == 'medium':
    x_incr = 2
else:
    x_incr = 3 # Not slow, nor medium, so must be fast one, right?

# Calculating new position based on speed
alien_0['x_pos'] = alien_0['x_pos'] + x_incr
print(f"Current position: X{alien_0['x_pos']}, Y{alien_0['y_pos']}")

# Key-value pairs can be removed by 'del' statement

print("\nRemoval test")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['color']
print(alien_0)

# Dictionaries don't have to be oriented around one specific thing;
# They can store any information we want
print("\nOther info test")

fav_langs = {
    'kacper': 'python',
    'dariusz': 'python',
    'grzegorz': 'uninstall',
    'jakub': 'react',
    'steve': 'swift', # It's a good practice to include comma at the end
    }
print(fav_langs)

language = fav_langs['kacper'].title()
print(f"Kacper's favorite programming language is {language}.")

# Using get() to access values
# Get() can be used to set a default value for a key in case it doesn't exist 
# (this way code errors can be avoided)
print("\nGet() stuff")

alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points']) <- this would cause an error in this case

points_value = alien_0.get('points', 'No value assigned yet.')
print(points_value)

# Second part of get() does not need to be defined; in such case,
# it will simply return 'None' as a value
points_value = alien_0.get('points')
print(points_value)

alien_0['points'] = 5
points_value = alien_0.get('points')
print(points_value)

alien_0['points'] = 10
print(points_value)

# Get() will not make variables dynamic - it will only assign the existing
# (or none) value to the variable at the time of being called in the code. 

