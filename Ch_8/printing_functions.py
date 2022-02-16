# 8-15 Printing Models
# Functions for the exercise below
def print_models(unprinted_designs, printed_designs):
    """Simulate each design until none are left.
    Move each design to printed_designs after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        printed_designs.append(current_design)

def show_printed_designs(printed_designs):
    """Print each item on the printed_designs list."""
    print("\nList of completed designs:")
    for item in printed_designs:
        print(f"\t{item}")
