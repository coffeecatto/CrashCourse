# 4-8 Cubes

# Make a list of first 10 cubed numbers. Then use a for loop to print the value of each number 

print("First version:")
cubes = []
for value in range(1,11):
    number = value ** 3
    cubes.append(number)

for value in cubes:
    print(value)

# Trying to do it in one line

print("\nSecond version:")

cubes = [value ** 3 for value in range(1,11)]
for value in cubes:
    print(value)

# AAAND this also completes exercise 4-9 by accident, since second version uses list comprehension. Oops!