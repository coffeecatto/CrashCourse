# 8-13 User Profile
# Copy code from page 149 (user_profile.py) and build a profile of yourself
# with at least three additional key-value pairs
def build_profile(firstname, lastname, **user_info): # Used often as **kwargs
    """Builds a profile dictionary with provided information."""
    user_info['first name'] = firstname
    user_info['last name'] = lastname

    return user_info

my_profile = build_profile('coffee', 'catto',
                            location = 'home', drinking = 'whiskey',
                            language = 'polish',)

print(my_profile)