# 9-14 Lottery

# Make a list (or tuple) containing 10 numbers and 5 letters. 
# Randomly select 4 elements from it and print a message that this is the
# winning combination. 

from random import choice

lottery_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
lottery_results = []

num_to_grab = 5

while num_to_grab != 0:
    picked = choice(lottery_list)
    lottery_list.remove(picked)
    lottery_results.append(picked)
    num_to_grab += -1

print(f"Today's winning combination is: {lottery_results}!")