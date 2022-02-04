# Lists part 2

# Organizing a list

# Sorting a list permanently with sort()
# By default, it will sort stuff in alphabetical order

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Sorting in reverse

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# Temporary sorting with sorted()

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nSorted() function outcome:")
print(sorted(cars))

# Using reverse=true; first type in list name, then argument

print("Sorted(reverse=true) outcome:")
print(sorted(cars, reverse=True))

print(f"Original order still exists - check: {cars}")

# Lists can be permanently reversed by using 'reverse()' argument\

print(f"\nOriginal list: {cars}")

cars.reverse()
print(f"Reversed list: {cars}")

# len() can be used to determine length of the list

print(len(cars))
print(f"Number of items on the list: {len(cars)}")