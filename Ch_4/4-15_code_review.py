# 4-15 Code Review

# Style the code of three of previous programs so that they are compliant with
# rules of PEP 8. 
# I've already added rulers to my IDE, btw. 

# NOTE: Here begins code from '4-8 Cubes'

# Make a list of first 10 cubed numbers. 
# Then use a for loop to print the value of each number 

print("First version:")
cubes = []
for value in range(1,11):
    number = value ** 3
    cubes.append(number)

for value in cubes:
    print(value)

# Trying to do it in one line

print("\nSecond version:")

cubes = [value ** 3 for value in range(1,11)]
for value in cubes:
    print(value)

# AAAND this also completes exercise 4-9 by accident, since second version 
# uses list comprehension. Oops!

# NOTE: Here starts code from '4-11 My Pizzas, Your Pizzas'

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

# Prove that both lists are separate and have new items. Use 'for' loops 
# to print the lists. 

print("\nPizza proof time\n")
print("My fav pizzas are:")
for pizza in fav_pizzas:
    print(pizza.title())
print("My friends fav pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())

# NOTE: Here starts code from 4-13 Buffet

# Think of five basic foods, then store them in a tuple. 

foods = ('pasta', 'rice', 'soup', 'potatoes', 'salad')

# Use a loop to print each item

print("Menu:")
for food in foods:
    print(food.title())

# Trying to modify the tuple in order to fail

# foods[0] = 'cola'

# Restaurant changes two items on the menu. 
# Rewrite the tuple, print the menu again

foods = ('spaghetti', 'pierogi', 'soup', 'potatoes', 'salad')

print("\nRevised menu:")
for food in foods:
    print(food.title())