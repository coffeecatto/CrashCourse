# Chapter 5, using 'if' with lists

# Making a loop for the list

print("Loop list of requested toppings:")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}...")
print("Finished making pizza!")

# If-else for unavailable topping

print("\nIf-else loop:")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now :(.")
    else:
        print(f"Adding {requested_topping}...")
print("Finished making pizza!")

# Empty list test

print("\nEmpty list loop:")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}...")
else:
    print("You sure you want a plain pizza?")

# NOTE: Now this is next thing is great :D
# Checking list's contents against another list!

print("\nLIST CONTENT CHECK IN OTHER LIST WOOO")

available_toppings = ['cheese', 'pepperoni', 'chicken', 'salami', 'tuna', \
    'pineapple', 'eggs', 'ham', 'red peppers', 'green peppers']
requested_toppings = ['pepperoni', 'onions', 'green peppers']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping} to your pizza...")
    else:
        print(f"Sorry, {requested_topping} is not currently available!")
print("Finished making your pizza!")