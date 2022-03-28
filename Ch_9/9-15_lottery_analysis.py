# 9-15B Lottery Analysis

# NOTE: Another attempt at this, since previous one was written while being
# barely awake (which resulted in a mess equal to being a crime against
# humanity). 
# NOTE 2: Stored the original file as 'sleep_deprived_mess(9-15).py'. 
from random import choice

# Storing numbers as strings so that sorting works
lottery_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
                'A', 'B', 'C', 'D', 'E']
lottery_results = []
my_ticket = ['2', '5', '7', '3', 'D']
my_ticket.sort() # Sorting for correct comparison with lottery_results
num_of_rolls = 0

while True:
    if len(lottery_results) < 5: # Stop once we've pulled enough elements
        picked = choice(lottery_list)
        if picked not in lottery_results: # Check for duplicate elements
            lottery_results.append(picked)
            lottery_results.sort()
    elif my_ticket == lottery_results:
        break
    else:
        lottery_results = [] # Resets the ticket so that we can roll again
        num_of_rolls += 1 # Increments the roll counter by one

# Print how many rolls it took
if my_ticket == lottery_results:
    print(f"My ticket won after {num_of_rolls} rolls!")