# 10-3 Guests

# Prompt user for their name. 
# Write the response to a file called guest.txt. 

# Prompt user for the name
name = input("What is your name?:")

# Write it to file
filename = r'text_files/guest.txt'

with open(filename, 'w') as file_object:
    file_object.write(name)

# NOTE: When writing to a file, Python will create it if it doesn't already
# exist.