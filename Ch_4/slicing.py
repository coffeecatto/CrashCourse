# Slicing and stuff from Chapter 4

# Working with a specific group of items in a list is called a 'slice' 

# This can work similar to the range() function, for example: it will take items from position 1 to 5 in a list. 

players = ['kokuslaw', 'drewniak', 'rasiak', 'rivenomenaldo', 'henry']
print(players[0:3])

# If first index is omitted, Python will start at the beginning of the list by default

print("\nIndex omitted:")
print(players[:3])

# Omitting second index will make Python go to the end of the list

print("\nSecond index omitted:")
print(players[1:])

# As before - negative numbers can be used to go from the end of the list

print("\nGoing from the end of the list:")
print(players[-3:])

# Adding third argument is possible, for skipping items
# In this example, every second position will be skipped:

print("\nSkipping test:")
print(players[0:6:2])

# NOTE: SLICES AND LOOPS

# Using slices in loops is pretty straightforward. 

players = ['kokuslaw', 'drewniak', 'rasiak', 'rivenomenaldo', 'henry']

print("\nThe first three players on the list are:")
for player in players[:3]:
    print(player.title())

# COPYING A LIST
# Slices can be used to copy whole lists, or just a part of them. Seems really intuitive, too!

players = ['kokuslaw', 'drewniak', 'rasiak', 'rivenomenaldo', 'henry']
copied_players = players[:]
selected_players = players[::2]
print("\nSlicing and copying test:")
print(f"Player list: {players}\nCopied players list: {copied_players}\nSelected players: {selected_players}")

# These lists act independently of each other - let's add new items to them

players.append('czmiel')
copied_players.append('pszczola')

print("\nLists after append\n")
print(f"Players list: {players}")
print(f"Copied players list: {copied_players}")

# NOTE: DO NOT TRY TO COPY LISTS IN THIS WAY: LIST1 = LIST2
# This does not copy a list, but makes LIST1 point to LIST2. 
# Meaning that any changes made to LIST1 appear in LIST2 etc. 