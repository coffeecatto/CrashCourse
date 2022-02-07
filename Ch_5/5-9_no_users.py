# 5-9 No users

# NOTE: Reusing code from 5-8

# Make a list of five or more users, include 'admin' in it

user_list = ['admin', 'rose', 'john', 'andrew', 'mike', 'rebecca', 'george']

# Code with greetings message - special for admin, normal for everyone else
# Print for every user
# Outcome when user_list has any contents
print("User list not empty:")

if user_list == []:
    print("We need to find some users!")
elif user_list != []:
    for user in user_list:
        if user_list == []:
            print("We need to find some users!")
        elif user == 'admin':
            print("Welcome to your site, dear administartor!")
        else:
            print(f"Hi {user.title()}! You have been successfully logged in.")

# Outcome when user_list is empty
print("\nUser list empty:")

user_list = []

if user_list == []:
    print("We need to find some users!")
elif user_list != []:
    for user in user_list:
        if user_list == []:
            print("We need to find some users!")
        elif user == 'admin':
            print("Welcome to your site, dear administartor!")
        else:
            print(f"Hi {user.title()}! You have been successfully logged in.")
