# 10-11 & 10-12 Favorite Number(s)

# Prompt user for favorite number.
# Use json.dump() to store it in a file.
# Write a separate program that reads the file and prints a message. 
import json

def get_new_fav_number():
    """Prompt user for favorite number, then store it in a JSON file."""
    filename = r'json/favorite_number.json'
    number = int(input("What is your favorite number?: "))
    with open(filename, 'w') as f:
        json.dump(number, f)
        print("Saved your favorite number!")

def get_stored_fav_number():
    """Reads favorite number from a file, then prints it."""
    filename = r'json/favorite_number.json'
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        print("ERROR: Couldn't read the file. \
            \nAre you sure that it exists?")
    else:
        print(f"Your favorite number is {number}!")
        
get_new_fav_number()
get_stored_fav_number()