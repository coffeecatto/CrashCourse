# 10-4 Guest Book

# Write a WHILE loop that prompts users for their name. 
# Print a greeting after name is entered. 
# Store their name/visit in a file guest_book.txt. 
# Make sure each entry appears in a new line. 

# Prompting users for name (with quit option)
while True:
    name = input("What is your name?: ")
    # Stop the loop if user wants to quit
    if name == 'q' or name == 'quit':
        break
    else:
        print(f"Hello and welcome, {name}!")
        # Log the name in our guest book
        with open(r'text_files/guest_book.txt', 'a') as file_object:
            file_object.write(f"Visit logged. Username: {name}\n")