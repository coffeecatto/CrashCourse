# 7-3 Multiples of Ten
# Ask user for a number, then print a message whether the number
# is a multiple of 10 or not. 
# This is where the WHISKEY % operator can be used. 
prompt = "Let's check if a number is a multiple of 10 or not."
prompt += "\nType in a number: "

number = input(prompt)
number = int(number) # Changing value from str to int

if number % 10 == 0:
    print(f"\nNumber {number} is a multiple of 10!")
else:
    print(f"\nNumber {number} is not a multiple of 10.")