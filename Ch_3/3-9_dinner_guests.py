# 3-9 Dinner Guests
# NOTE: Reusing code from 3-6 for this

guest_list = ['patryk', 'kacper', 'daniel']

# First set of invitations

print(f"Privet {guest_list[0].title()} mah boi, dawaj na LAN Party 13-go lutego!")
print(f"Privet {guest_list[1].title()} mah boi, dawaj na LAN Party 13-go lutego!")
print(f"Privet {guest_list[2].title()} mah boi, dawaj na LAN Party 13-go lutego!")

# Message about who can't make it

print(f"Niestety {guest_list[2].title()} nie da rady, bo siedzi w W-wie.")

# Replace absentee with another person

guest_list[2] = 'piotr'

# Print a new set of invitations based on the changed list

print(f"Privet {guest_list[0].title()} mah boi, dawaj na LAN Party 13-go lutego!")
print(f"Privet {guest_list[1].title()} mah boi, dawaj na LAN Party 13-go lutego!")
print(f"Privet {guest_list[2].title()} mah boi, dawaj na LAN Party 13-go lutego!")

# NOTE: Print for marking start of 3-6
print("\n\nACHTUNG!\n\n#########\n\nTu je start 3-6\n\n")
# ###

# Print a message about bigger table

print("Uwaga! Bedzie wiecej osob bo nie wiem, yy stol dodatkowy znalezlismy czy cos iksde.")

# Inserting new guest at the start of the list

guest_list.insert(0, 'grzesiek')

# In the middle of the list

guest_list.insert(2, 'kamil')

# Append, for adding to the end of the list (append does this by default, it seems)

guest_list.append('kokuslaw')

# Print a new set of messages for each person (just realized - this would be waaaay more efficient with a loop, probably)

print(f"Privet {guest_list[0].title()} mah boi, dawaj na LAN Party 13-go lutego!")
print(f"Privet {guest_list[1].title()} mah boi, dawaj na LAN Party 13-go lutego!")
print(f"Privet {guest_list[2].title()} mah boi, dawaj na LAN Party 13-go lutego!")
print(f"Privet {guest_list[3].title()} mah boi, dawaj na LAN Party 13-go lutego!")
print(f"Privet {guest_list[4].title()} mah boi, dawaj na LAN Party 13-go lutego!")
print(f"Privet {guest_list[5].title()} mah boi, dawaj na LAN Party 13-go lutego!")

# END OF ORIGINAL 3-6 CODE

# Now to print a message with amount of guests

print(f"\nCalkowita liczba osob zaproszonych na LAN PARTY: {len(guest_list)}.")