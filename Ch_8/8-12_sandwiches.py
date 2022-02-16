# 8-12 Sandwiches
# Write a function that accepts ingredients for a sandwich. 
# It should have one parameter that accepts as many args as needed. 
# Also, the function should print a message at the end with the whole list. 
def make_sandwich(*ARGS):
    """Print a list of specified sandwich ingredients."""
    print("List of ingredients for the sandwich:")
    for arg in ARGS:
        print(f"\t- {arg}")

make_sandwich('ham')
make_sandwich('cheese', 'pepperoni')
make_sandwich('garlic', 'chicken filet', 'red peppers')