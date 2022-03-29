# 10-13 Verify User

# Use code from remember_me_refactored.py. 
# Before printing a message in greet_user(), ask user first if the previous
# username is correct. If yes, print message. If not, prompt for new username. 
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
    username = get_stored_username()
    if username is not None: # check if any username has been retrieved
        verified = input(f"Is your username {username}? [Y/N]")
        if verified == 'y':
            print(f"Welcome back, {username}!")
            return # ends the call if there is any other answer than 'y'
    get_new_username()

greet_user()

# NOTE TO SELF: There's still a lot more to learn about loops and statements!
# Yay :D