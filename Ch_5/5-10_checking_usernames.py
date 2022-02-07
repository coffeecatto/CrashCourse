# 5-10 Checking Usernames

# Make a list of at least five users
current_users = ['John', 'Mike', 'Anna', 'Alexa', 'Dude']

# Now apparently I have to copy the above list, but make everything in
# lower case. 
# I totally forgot one can do this with list comprehension thingy...
current_users_namecheck = [name.lower() for name in current_users]

# Print to check if this works...
print(current_users_namecheck)

# Make a list of new users, with two names being the same as in the above list
# Needs to check in lowercase to work properly

new_users = ['snorlax', 'vacool', 'Anna', 'DUDE', 'beermaster9000']

for username in new_users:
    if username.lower() in current_users_namecheck:
        print(f"Sorry, username '{username}' is already taken. Choose another!")
    elif username.lower() not in current_users_namecheck:
        print(f"Username '{username}' is available!")

# NOTE TO SELF:
# Programming when I should be sleeping IS A BAD IDEA. 
# I'm prone to making really stupid mistakes in this state :(