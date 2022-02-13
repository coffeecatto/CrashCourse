# Chapter 7
# INPUTS

# Use input() function to prompt user for information
message = input("Input text that Python will then print: ")
print(message)

# Remember to tell user what information needs to be provided
# (and for what it will be used, if helpful)
name = input("Please state your name: ")
print(f"\nHello, {name}!")

# When defining a message in a variable, it is possible to add additional lines
# by using '+=' operator (I think that's how it's called?). 
# NOTE: The lines will be added at the end of the previous text by default. 
# To continue in a new line, use \n. 
# Example:
prompt = "Your name can blablabla something better info."
prompt += "\nWhat is your first name?: "

name = input(prompt)
print(f"Hello, {name}!")

# NOTE: By default, Python interprets anything obtained through input()
# as a string. This can be converted to an integer by using int() function. 
age = input("\nPlease enter your age: ")
age = int(age) # Obviously this will not work if the answer is not a number

print(f"Your age is: {age}")
if age >= 18:
    print("You are legally allowed to drink. Nice!")
else:
    print("Not allowed to drink yet. Too bad!")

# THE MODULO OPERATOR - '%'
# Divides one number by another and returns the remainder. 
# Useful for determining whether a number is even or odd. 
# Knowing me, I'll have an easier time remembering it if I'll call it the
# "Whiskey operator"... 
number = input("\nEnter a number - I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"The number {number} is even!")
else:
    print(f"The number {number} is odd!")