# Chapter 10

# JSON continued
# A program that asks for username. If username was already provided before,
# greet the user instead. 
import json

filename = r'json/username.json'

try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your username?: ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you the next time, {username}!")
else:
    print(f"Welcome back, {username}!")