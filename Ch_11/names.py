# Chapter 11

# Testing a Function
from name_function import get_formatted_name

print("Enter 'q' or 'quit' to exit at any time.")
while True:
    first = input("Enter your first name: ")
    if first == 'q' or first == 'quit':
        break
    last = input("Enter your last name: ")
    if last == 'q' or last == 'quit':
        break
    
    formatted_name = get_formatted_name(first, last)
    print(f"Hello, {formatted_name}!")