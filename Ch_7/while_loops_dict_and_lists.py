# Using WHILE loops with dictionaries and lists
# NOTE: When modifying items inside lists that are in loops, use WHILE loops. 
# Python might get confused when doing so in FOR loops. 

# Moving items from one list to another
# Let's say, unconfirmed users to confirmed
unconfirmed_users = ['bluep', 'vacool', 'pidzej']
confirmed_users = []

while unconfirmed_users: # This will run until the list is empty
    current_user = unconfirmed_users.pop() # Goes from the end of the list

    print(f"Checking user '{current_user}'...")
    confirmed_users.append(current_user)
print("List of verified users:")
for user in confirmed_users:
    print(f"\t{user}")

# Removing all instances of specifiv values from a list
# Can be done with a WHILE loop
print("\nREMOVING test:\n")
pets = ['dog', 'cat', 'spider', 'goldfish', 'goldfish', 'rat', 'goldfish']
print(pets)

while 'goldfish' in pets:
    pets.remove('goldfish')

print(pets)

# Filling a dictionary with user input
responses = {} # Starting with an empty dictionary
poll_active = True # Will use this later to end the poll

while poll_active == True:
    name = input("What is your name?: ")
    response = input("What is your favorite city?: ")

    responses[name] = response # Store answers in the dictionary

    repeat = input("Continue polling (NO will quit the poll): ")
    if repeat == 'no':
        poll_active = False # Ends the loop

print("\nPoll complete. Printing results...")
for name, response in responses.items():
    print(f"{name.title()}'s favorite city is {response.title()}.")