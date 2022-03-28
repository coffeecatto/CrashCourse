# 10-5 Programming Poll

# Write a WHILE loop that asks people why they like programming.
# Write responses to a file (it should store all responses).

# NOTE: I'm guessing I should also ask users for their name in here?
# It makes sense for a poll. Unless it's anonymous...

# Prompting users for name (with quit option)
while True:
    name = input("What is your name?: ")
    # Stop the loop if user wants to quit
    if name == 'q' or name == 'quit':
        break
    else:
        print(f"Hello and welcome, {name}!")
        opinion = input(f"Why do you like programming?: ")
        # Write results to file at the end of loop
        with open(r'text_files/programming_poll.txt', 'a') as file_object:
            file_object.write(f"Username: {name}. Opinion: {opinion}\n")