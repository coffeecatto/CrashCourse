# 4-10 Slices

# Use one of the programs that I already wrote, then print a message with:
# - First three items from the list
# - Three items from the middle of the list
# - Last three items from the list
# Use slices for this. 

players = ['kokuslaw', 'drewniak', 'rasiak', 'rivenomenaldo', 'henry']
print(f"The first three players from the list are: {players[:3]}")
print(f"Three players from the middle of the list are: {players[1:4]}")
print(f"Three last players from the list are: {players[-3:]}")