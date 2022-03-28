# 10-6 Addition

# Write a program that asks user for two numbers, then adds them together. 
# Make it handle a ValueError that pops when user enters str instead of int 
# as an answer.

print("Let's add two numbers together.")
try:
    num1 = int(input("Type in the first number: "))
    num2 = int(input("Type in the second number: "))
except ValueError:
    print("ERROR: Type in numbers, not letters, you dummy!")
else:
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")