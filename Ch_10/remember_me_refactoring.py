# Chapter 10

# Refactoring
# Basically when you realize that the code you wrote would be more useful
# to you if you break it down into functions. So that's what you do!
# So for remember_me.py, that would be:
# - getting new username
# - reading username from file on demand
# - greeting the user
import json

def get_new_username():
    """Prompt user for a new username."""
    username = input("Please type in your desired username: ")
    filename = r'json/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"Username saved - we'll remember you the next time, {username}!")

def get_stored_username():
    """Read the username stored in JSON file."""
    filename = r'json/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        print("ERROR: Couldn't retrieve username from file.")
        return None
    else:
        return username

def greet_user():
    """Read username from file and print a welcome message."""
    filename = r'json/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
            print(f"Welcome back, {username}!")
    except FileNotFoundError:
        print("ERROR: Couldn't retrive username from file. \
            \nAre you sure that username was stored at all?")

# Testing error handling
get_stored_username()
greet_user()

# Get username, then test functions again
get_new_username()
print(get_stored_username())
greet_user()