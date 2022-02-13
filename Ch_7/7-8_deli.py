# 7-8 Deli
# Create a 'sandwich_orders' list and fill it with names of sandwiches
sandwich_orders = ['ham sandwich', 'cheese sandwich', 'spicy sandwich']

# Create an empty list 'finished_sandwiches' 
finished_sandwiches = []

# Create a loop: grab a sandwich and print about it, then move it to the
# second list. At the end, print a message with all finished sandwiches. 
while sandwich_orders: # Will auto-stop when list is empty
    grabbed_sandwich = sandwich_orders.pop()
    print(f"Preparing your {grabbed_sandwich} now...")

    finished_sandwiches.append(grabbed_sandwich)

print("\nAll ready! List of prepared sandwiches:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()}")