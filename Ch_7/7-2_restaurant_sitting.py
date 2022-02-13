# 7-2 Restaurant Sitting
# Ask user about how many people are in their dinner group. 
# If the answer is more than eight -> they need to wait for a table. 
# Else, table is ready. 
message = "\nLet's see if we can get you a table straight away."
message += "\nHow many people are in your dinner group?: "

group = input(message)
group = int(group) # Changing value from str to int

if group >= 8:
    print(f"I'm sorry, all tables for {group} people are currently taken."
    "\nYou'll need to wait for a bit before we have a free table.")
else:
    print(f"We do have a table for {group} people free right now!")