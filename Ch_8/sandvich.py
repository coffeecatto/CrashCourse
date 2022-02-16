# For 8-16 Imports
def make_sandwich(*ARGS):
    """Print a list of specified sandwich ingredients."""
    print("List of ingredients for the sandwich:")
    for arg in ARGS:
        print(f"\t- {arg}")
