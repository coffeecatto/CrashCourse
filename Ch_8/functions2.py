# Chapter 8
# Functions continued

# Passing a List to a function
def greet_users(names):
    """Prints a greeting to each user on the list."""
    for name in names:
        print(f"This functions says hello to {name.title()}!")

usernames = ['john', 'vacool', 'kacper']
greet_users(usernames)

# Modifying a list in a Function
# Lists can be modified inside a function (permanently even)
print("\nLIST TEST 2:\n")

unprinted_designs = ['phone case', 'robot pendant', 'steam deck case']
printed_designs = []

# Simulate printing each designs untill none are left in unprinted_designs
# Move each design to printed_designs when done
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

print_models(unprinted_designs, printed_designs)
show_printed_designs(printed_designs)

# NOTE: Try to limit what functions do to one specific task (moving items,
# printing items, etc.). In other words - Keep It Simple, Stupid

# Preventing a Function from modifying a List
# This can be done by making the function use a COPY of the list with [:]
print("\nLIST TEST 3 (USING A COPY)\n")

unprinted_designs = ['phone case', 'robot pendant', 'steam deck case']
printed_designs = []

print_models(unprinted_designs[:], printed_designs)
show_printed_designs(printed_designs)
print(unprinted_designs)

# Passing an Arbitrary number of args
# Using an asterisk in front of a parameter makes Python accept multiple
# arguments (if provided)
# NOTE: Type of list created this way is a tuple (not sure if it matters yet)
def make_pizza(*toppings):
    """Print a list of toppings that have been provided in args."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('cheese', 'onions', 'red peppers')

# Mixing positional and arbitrary args
# Arbitrary args need to be specified at the end, just like args with
# default values
print("\nMIXED ARGS TEST\n")

def make_pizza(size, *toppings):
    """Summarize the pizza that is being made."""
    print(f"You've chosen a {size} sized pizza, with the following toppings:")
    for topping in toppings:
        print(f"\t- {topping}")

make_pizza('medium', 'pepperoni', 'jalapeno', 'tabasco')

# NOTE: Apparently it's common practice to define arbitrary arguments
# at the end as simply *args (I guess it makes sense)

# Using arbitrary keyword arguments
# If I want to use keyword arguments (for example: key-value pairs) in a
# similar manner, then I have to use two asterisks to create an empty
# dictionary for it
print("\nARBITRARY KEYWORD ARGS TEST\n")

def build_profile(firstname, lastname, **user_info): # Used often as **kwargs
    """Builds a profile dictionary with provided information."""
    user_info['first name'] = firstname
    user_info['last name'] = lastname

    return user_info

# Now to call the function and provide more information that firstname and
# lastname
user_profile = build_profile('dariusz', 'soplica', 
                            location = 'earth',
                            alcohol = 'whiskey')

print(user_profile)
