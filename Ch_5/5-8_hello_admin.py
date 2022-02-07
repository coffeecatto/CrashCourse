# 5-8 Hello Admin

# Make a list of five or more users, include 'admin' in it

user_list = ['admin', 'rose', 'john', 'andrew', 'mike', 'rebecca', 'george']

# Code with greetings message - special for admin, normal for everyone else
# Print for every user

for user in user_list:
    if user == 'admin':
        print("Welcome to your site, dear administartor!")
    else:
        print(f"Hi {user.title()}! You have been successfully logged in.")