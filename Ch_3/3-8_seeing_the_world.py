# 3-8 Seeing the World

# Make a list of at least five locations I want to visit. Make sure that my list is NOT in alphabetical order. 

places_to_visit = ['spain', 'morocco', 'algeria', 'france', 'sicily', 'greece']

# Print the list

print("Simple print of the list")
print(places_to_visit)

# Use sorted() to print the list in alphabetical order, then print the list normally to show that original order is still in place

print("\nSorted, and original list")
print(sorted(places_to_visit))
print(places_to_visit)

# The same, but sorted in reverse

print("\nSorted in reverse, then original")
print(sorted(places_to_visit, reverse=True))
print(places_to_visit)

# Use 'reverse()' to reverse the list, print it, then reverse to original, print again

print("\nReversed list:")
places_to_visit.reverse()
print(places_to_visit)

print("Re-reversed list:")
places_to_visit.reverse()
print(places_to_visit)

# Perm-sort alphabetically, then sort again but reversed

print("\nSort() normal:")
places_to_visit.sort()
print(places_to_visit)

print("Sort() reversed:")
places_to_visit.sort(reverse=True)
print(places_to_visit)