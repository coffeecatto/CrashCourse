# 3-10 Every Function

# Basically: write a program that uses every function introduced in Chapter 3. Great.True
# Gonna go with spanish rivers. 

spanish_rivers = ['guadalquivir', 'guadiana', 'segura', 'jucar', 'ebro', 'douro']

# All right, we have a list. Let's go. 
# Let's print the list first in raw format, then with title() argument. 

print("Raw list:")
print(spanish_rivers)
print("Normal list:")
print(f"{spanish_rivers[0].title()}, {spanish_rivers[1].title()}, {spanish_rivers[2].title()}, {spanish_rivers[3].title()}, {spanish_rivers[4].title()}, {spanish_rivers[5].title()}")

# Add a river at the beginning and in the middle

spanish_rivers.insert(0, 'almanzora')
spanish_rivers.insert(3, 'velez')

print("\nList after inserts:")
print(spanish_rivers)

# Append (add to the end of list)

spanish_rivers.append('vinalopo')

print("\nList after append:")
print(spanish_rivers)

# Remove Almanzora with del

del spanish_rivers[0]

print("\nList after deleting Almanzora:")
print(spanish_rivers)

# Pop a river, then print what was popped

print(f"\nCurrent list: {spanish_rivers}")

# Popping 'Jucar'
popped_river = spanish_rivers.pop(4)

print(f"Deleting {popped_river} from the list...")
print(f"Updated list of rivers: {spanish_rivers}")

# Changing 'douro' to 'zadorra' 

print(f"\nChanging 'douro' to 'zadorra'...")
spanish_rivers[5] = 'zadorra'
print(f"List after changes: {spanish_rivers}")

# Removing river by value

nope_river = 'ebro'

print(f"\nList before removing 'ebro' with variable: {spanish_rivers}")
spanish_rivers.remove(nope_river)
print(f"List after removal: {spanish_rivers}")

# SNORTING TIME

print(f"\nCurrent raw list: {spanish_rivers}")
print(f"Sorted(): {sorted(spanish_rivers)}")
print(f"Sorted(reverse): {sorted(spanish_rivers, reverse=True)}")
print(f"Raw list again (should be the same as previous raw list): {spanish_rivers}")

print("\nTime to sort permanently...")
print(f"Current list: {spanish_rivers}")
spanish_rivers.sort()
print(f"List after sort(): {spanish_rivers}")
spanish_rivers.sort(reverse=True)
print(f"List after sort(reverse=True): {spanish_rivers}")

# Print the first and last river in list

print(f"\nFirst river on list: {spanish_rivers[0]}. Last river on list: {spanish_rivers[-1]}.")

# Finally, let's print how many items the list has

print("\nFINAL STUFF")
print(f"Current number of rivers in the list: {len(spanish_rivers)}")