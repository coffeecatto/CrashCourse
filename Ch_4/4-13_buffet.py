# 4-13 Buffet

# Think of five basic foods, then store them in a tuple. 

foods = ('pasta', 'rice', 'soup', 'potatoes', 'salad')

# Use a loop to print each item

print("Menu:")
for food in foods:
    print(food.title())

# Trying to modify the tuple in order to fail

# foods[0] = 'cola'

# Restaurant changes two items on the menu. Rewrite the tuple, print the menu again

foods = ('spaghetti', 'pierogi', 'soup', 'potatoes', 'salad')

print("\nRevised menu:")
for food in foods:
    print(food.title())