# 4-1 Pizzas

# Make a list of at least three pizzas, then use a loop to print each item. 

fav_pizzas = ['pepperoni', 'chorizo', 'capricious']

for pizza in fav_pizzas:
    print(pizza)

# Modify the above loop so that there's a message for each item. 

print("\nPizza messages:")
for pizza in fav_pizzas:
    print(f"I could kill for a {pizza.title()} pizza. So hungry...")

# Same as above, but make an additional message AFTER the loop. 

print("\nPizza messages, with one after the loop:")
for pizza in fav_pizzas:
    print(f"I could kill for a {pizza.title()} pizza. So hungry...")
print("Pizza is great. What's not great is my growing lactose intolerance.")