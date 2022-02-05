# 4-12 More Loops

# Choose two version from foods.py section of the book, then make 'for' loops to print the lists

# Copying code from the book...

print("Original code & prints from the book:")

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# END OF COPY

# Now, to print those lists with 'for' loops

print ("\nSame lists, but with 'for' loop:")

print("My favorite foods are:")
for fooditem in my_foods:
    print(fooditem.title())
print("\nMy friend's favorite foods are:")
for fooditem in friend_foods:
    print(fooditem.title())
