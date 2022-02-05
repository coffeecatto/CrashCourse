# 4-11 My Pizzas, Your Pizzas

# Starting by making a copy of 4-1

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

# NOTE: END OF 4-1 COPY

# Make a copy of the original list

friend_pizzas = fav_pizzas[:]

# Add a new pizza to the original list, and a different pizza to the copied one

fav_pizzas.append('pineapple')
friend_pizzas.append('bacon')

# Prove that both lists are separate and have new items. Use 'for' loops to print the lists. 

print("\nPizza proof time\n")
print("My fav pizzas are:")
for pizza in fav_pizzas:
    print(pizza.title())
print("My friends fav pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())