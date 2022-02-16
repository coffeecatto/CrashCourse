# Chapter 8
# For usage in modules_import.py 
# Pizza Function Module
def make_pizza(size, *toppings):
    """Prints out information about pizza."""
    print(f"You have selected a {size} sized pizza, with following toppings:")
    for topping in toppings:
        print(f"\t- {topping}")