# Chapter 11
# Name Function (for importing)

def get_formatted_name(first, last, middle=''):
    """Returns a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()