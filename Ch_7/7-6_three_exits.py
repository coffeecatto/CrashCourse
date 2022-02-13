# 7-6 Three Exits
# Use code from either 7-4 or 7-5, then make versions of it that use:
# - a conditional test in WHILE loop to stop it
# - an active variable to control how long the loop runs
# - a BREAK statement to stop the loop after typing 'quit' as input

# Using code from 7-4 - this already fulfills the 'quit' to BREAK requirement
print("BREAK version:\n")
toppings = []

prompt = "Type in your topping: "
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    toppings.append(topping)
    print(f"Topping {topping} added to the list...")

print("\nList of selected toppings:")
for topping in toppings:
    print(f"\t{topping}")

# Now for an active variable version
print("\nACTIVE VARIABLE version:\n")
toppings = []
program_active = True

prompt = "Type in your topping: "
while program_active == True:
    topping = input(prompt)
    if topping == 'quit':
        program_active = False
    else:
        toppings.append(topping)
        print(f"Topping {topping} added to the list...")

print("\nList of selected toppings:")
for topping in toppings:
    print(f"\t{topping}")

# Conditional test version
print("\nCONDITIONAL TEST version:\n")
toppings = []
topping = ""

prompt = "Type in your topping: "
while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        toppings.append(topping)
        print(f"Topping {topping} added to the list...")

print("\nList of selected toppings:")
for topping in toppings:
    print(f"\t{topping}")
