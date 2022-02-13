# 7-4 Pizza Toppings
# Write a loop for entering toppings (until user types 'quit'). 
# After each topping, print a message that it has been added. 
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