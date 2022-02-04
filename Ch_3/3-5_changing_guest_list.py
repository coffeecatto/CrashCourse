# 3-5 Changing Guest List

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