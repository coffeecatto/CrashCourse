# 7-9 No Pastrami
# NOTE: Using code from 7-8
# Make sure that 'pastrami' appears in first list at least three times. 
# Add code at beginning that prints message about running out of pastrami,
# then remove pastramis from the list. 
# The goal here is for no pastramis to end in the finished_sandwiches list. 

sandwich_orders = ['ham sandwich', 'cheese sandwich', 'spicy sandwich', 
                    'pastrami', 'pastrami', 'pastrami']

# Create an empty list 'finished_sandwiches' 
finished_sandwiches = []

# Create a loop: grab a sandwich and print about it, then move it to the
# second list. At the end, print a message with all finished sandwiches. 
while sandwich_orders: # Will auto-stop when list is empty
    if 'pastrami' in sandwich_orders: # Checking if pastrami is ordered
        print("Sorry, we're out of Pastrami today!")

        while 'pastrami' in sandwich_orders: # Removing all pastrami
            sandwich_orders.remove('pastrami')
    
    grabbed_sandwich = sandwich_orders.pop()
    print(f"Preparing your {grabbed_sandwich} now...")

    finished_sandwiches.append(grabbed_sandwich)

print("\nAll ready! List of prepared sandwiches:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()}")