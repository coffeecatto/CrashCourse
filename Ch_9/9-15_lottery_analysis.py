# 9-15 Lottery Analysis

# Use code from 9-14. 
# Create a list of your winning combination of numbers and letters. 
# Then create a loop that rolls until this combination is the result. 
# It should also print how many tries it took to get there. 

from random import choice

# Changed the list to all str - Python gets mad at me when I want it to 
# compare lists that contain both int and str values
lottery_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
                'A', 'B', 'C', 'D', 'E']
lottery_results = []

num_to_grab = 5

while num_to_grab != 0:
    picked = choice(lottery_list)
    lottery_list.remove(picked)
    lottery_results.append(picked)
    num_to_grab += -1

lottery_results.sort() # Sorting it so that Python can compare results properly
print(f"Today's winning combination is: {lottery_results}!")

print("\nLOTTERY ANALYSIS - HOW MANY ROLLS TO WIN?\n")

# Winning combination gets stored here
my_ticket = ['2', '5', '7', '3', 'D']
my_ticket.sort() # Sorting for correct comparison with lottery_results
print(f"My ticket is this: {my_ticket}")

# Resetting lottery_list (since previous code removed some positions from it
# to prevent duplicate entries in lottery_results)
# NOTE: Could just rewrite this to use 'sample', but this seems like a good
# brainscratcher
lottery_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
                'A', 'B', 'C', 'D', 'E']

# Make a copy to use with code below (original list will be used for resets)
lottery_list_copy = lottery_list[:]
num_of_rolls = 1 # Starts at 1 since we've already rolled once for results
                 # with the previous WHILE loop

while my_ticket != lottery_results:
    # Same as before - grab 5 positions from the list
    if num_to_grab != 0:
        picked = choice(lottery_list_copy)
        lottery_list_copy.remove(picked)
        lottery_results.append(picked)
        num_to_grab += -1
        # Sort the results after grabbing all 5 positions from the list
        if num_to_grab == 0:
            lottery_results.sort()
    # Stop the loop if ticket's contents match the result
    elif my_ticket == lottery_results:
        break
    # Reset stuff to default values if my_ticket doesn't match lottery_results
    elif num_to_grab == 0:
        lottery_list_copy = lottery_list[:]
        lottery_results = []
        num_to_grab = 5
        num_of_rolls += 1 # Increments the roll counter by one

# Print a message if we won! With amount of rolls, of course!
if my_ticket == lottery_results:
    print(f"My ticket won after {num_of_rolls} rolls!")

# Just in case - print contents of my_ticket and lottery_results to verify
# if they are indeed the same
print(my_ticket, lottery_results)

# Also make Python check it as well, since I've slept like 4 hours today
# and do not trust myself with this code whatsoever
print(my_ticket == lottery_results)
