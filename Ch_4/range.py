# Chapter 4, range() stuff

# When using (range), it will start at a given number, and end when it 'reaches' the final number. 
# In this example, it stops when it reaches 5, and does not continue - meaning that it prints numbers up to 4 only (because when it sees number 5, it stops!)

print("Range(1-5):")
for value in range(1,5):
    print(value)

# If only one number is provided in (range), then it will start counting from 0. 

print("\nRange(6):")
for value in range(6):
    print(value)

# Range() can be used to create lists. 

print("\nRange list:")
numbers = list(range(1,6))
print(numbers)

# Using a third argument in range orders it to skip numbers. 
# For example, using (range(2,11,2)) results in the count starting at 2, and then going by 2 up, each time, until it reaches 10. 

print("\nRange list, third argument:")
numbers = list(range(2,11,2))
print(numbers)

# '**' represents exponents. Let's create a list of first 10 square numbers, for practice. 
# First, create an empty list, where the numbers will be stored. 

squares = []

# Now for the loop.
# NOTE: Writing this for my own sanity. What happens here is: 
# - 'for' is used to create a 'value' variable, and the loop will go through a 'range' from 1 to 10
# - variable 'square' is defined as being equal to value ** 2
# - after 'square' is calculated, it then gets added/appended to the 'squares' list
# - the loop now starts from the beginning, this time with the next number, and everything is repeated
# - this goes on until number 11 is reached by the program
# - at the end, we have a nice list of first 10 square numbers!

print("\nList of first 10 square numbers:")
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

# Optimization time! 
# No need to set 'square' variable, to be honest. In this case, the calculation can be done entirely within append()!

squares = []

print("\nList of first 10 square numbers (changed code):")
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

# NOTE: min(), max() and sum() functions
# The names are pretty self-explanatory. These work with lists consisting of numbers. 

print("\nMin, Max and Sum for a list:")
digits = range(10)
print(f"Lowest number: {min(digits)}\nHighest number: {max(digits)}\nSum of all numbers: {sum(digits)}\nDigits list contains: {digits}")

# List comprehensions
# When creating a list, loops with arguments and/or calculations can be done in one line

print("\nList comprehension test:")
squares = [value ** 2 for value in range (1,11)]
print(squares)