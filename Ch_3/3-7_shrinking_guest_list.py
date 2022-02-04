# 3-7 Shrinking Guest List

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

# NOTE: 3-7 STARTS HERE

# Message: change of plans, only two people invited after all

print("\nSorry, tylko dwie osoby jednak sie zmieszcza. Tak mi w ksiazce powiedzieli")

# Pop these guys, but let them know about it

popped_guest1 = guest_list.pop(0)
print(f"Sorry {popped_guest1.title()} - nie jestes juz w naszym skladzie xD")

popped_guest2 = guest_list.pop(3)
print(f"Sorry {popped_guest2.title()} - nie ma miejsca tyle")

popped_guest3 = guest_list.pop(1)
print(f"Sorry {popped_guest3.title()} - kanciapa za mala na nas tylu")

popped_guest3 = guest_list.pop(2)
print(f"Sorry {popped_guest3.title()} - nie istniejesz")

# Messages for those left on the list

print(f"Hej {guest_list[0].title()}, LAN Party aktualne jak cos!")
print(f"Hej {guest_list[1].title()}, jedziemy z tym LAN Party tylko w pomniejszonym skladzie!")

# Remove remaining guests from the list, then check if it is empty

del guest_list[0]
del guest_list[0]
print(guest_list)