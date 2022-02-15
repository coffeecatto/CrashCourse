# Chapter 8
# Functions

# Use DEF to define a function (it will include anything indented)
def greet_user():
    """Display a simple greeting."""
    print("Privet!")

# NOTE: Triple quotations are called 'docstrings' - this is used for comments,
# which Python will later use to generate a documentation!

# Calling a function requires only it's name
greet_user()

# Passing information to functions
# By putting 'username' in parentheses we can later provide a value for it
# when calling the greet_user() function. 
# ('username' is just an example, anything can be typed there)
def greet_user(username):
    print(f"Privet, {username.title()}!")

greet_user('kacper')

# XXX
# Passing Arguments
# Sometimes multiple arguments need to be provided. There are multiple ways
# to go about that. 
print("\nPASSING ARGUMENTS\n")

# NOTE : Positional Arguments
# Providing arguments based on their order
def describe_pet(animal_type, animal_name):
    """Display information about a pet."""
    print(f"{animal_name.title()} is a {animal_type}.")

# Calling and providing time
# The order is the same as when defining arguments - so animal type goes first,
# animal name second
describe_pet('cat', 'moskwa')

# Multiple Function Calls
# Functions can be called upon as many times as we want
def describe_pet(animal_type, animal_name):
    """Display information about a pet."""
    print(f"\nKacper has a pet named {animal_name.title()}.")
    print(f"{animal_name.title()} is a {animal_type}.")

describe_pet('cat', 'moskwa')
describe_pet('cat (kinda old at this point at that)', 'benek')

# NOTE : Keyword Arguments
# Arguments can be provided by using key-value pairs. 
print("\nKEYWORD ARGUMENTS TEST\n")

def describe_pet(animal_type, animal_name):
    """Display information about a pet."""
    print(f"{animal_name.title()} is a {animal_type}.")

describe_pet(animal_type = 'cat', animal_name = 'moskwa')

# NOTE : Default Values
# It is possible to define default values when creating a function. 
# HOWEVER, ALL PARAMETERS THAT HAVE ASSIGNED DEFAULT VALLUES MUST BE
# WRITTEN AFTER ONES THAT DO NOT HAVE THEM (otherwise Python will get mad)
print("\nDEFAULT VALUES TEST\n")

def describe_pet(animal_type, animal_name = 'moskwa'):
    print(f"{animal_name.title()} is a {animal_type}.")

describe_pet('cat')

# NOTE: When providing values for arguments (during a function call) the order
# does not matter when using key-value pairs. 

# Returning a Simple Value
# Functions can be made to simplify my life. 
# For example, here's a function for outputting nicely formatted full names. 
def get_formatted_name(firstname, lastname):
    """Outputs a nicely formatted full name."""
    full_name = f"{firstname} {lastname}"

    return full_name.title() # Will return full_name value at the end of call

that_id_guy = get_formatted_name('john', 'carmack')
print(that_id_guy)

# NOTE : Making an Argument Optional
# Arguments can be made optional by assigning an empty default value to them
def get_formatted_name(firstname, lastname, middlename = ''):
    """Outputs a nicely formatted full name."""
    full_name = f"{firstname} {middlename} {lastname}"

    return full_name.title() # Will return full_name value at the end of call

guy_1 = get_formatted_name('adam', 'jensen')
guy_2 = get_formatted_name('george', 'michael', 'kyriacos')

print(f"\nOptional arg not provided: {guy_1}, "
      f"\nOptional arg provided: {guy_2}")

# NOTE: 'middlename' gets assigned a default value of an empty string. However,
# Python treats non-empty strings as 'True', which can be used
# with IF statements!
# For example:
def get_formatted_name(firstname, lastname, middlename = ''):
    """Outputs a nicely formatted full name."""
    if middlename:
        full_name = f"{firstname} {middlename} {lastname}"
    else:
        full_name = f"{firstname} {lastname}"

    return full_name.title() # Will return full_name value at the end of call

guy_1 = get_formatted_name('adam', 'jensen')
guy_2 = get_formatted_name('george', 'michael', 'kyriacos')

print(f"\nOptional arg not provided: {guy_1}, "
      f"\nOptional arg provided: {guy_2}")

# The result is the same, but this time the code does not need to even use
# middlename arg if it remains empty. 
# Definitely something to keep in mind when writing code in the future,
# since this smells like potential code optimization in more complex cases. 

# XXX: RETURNING A DICTIONARY
# Functions can return more complicated data structures if needed, such
# as lists and dictionaries!
def build_person(firstname, lastname):
    """Return a dictionary of information about a person."""
    person = {'first': firstname, 'last': lastname}

    return person

musician = build_person('krzysztof', 'krawczyk')
print(musician)

# Accepting optional values into dictionary
print("\nOPTIONAL VALUES TO DICTIONARY TEST\n")

def build_person(firstname, lastname, age = None):
    """Return a dictionary of information about a person."""
    person = {'first': firstname, 'last': lastname}

    if age:
        person['age'] = age # 'None' is treated as False in conditional tests

    return person

musician = build_person('krzysztof', 'krawczyk', 75)
print(musician)

# NOTE: Using functions with Loops
# Functions can be called in loops without any additional steps. 
print("\nFUNCTIONS WITH LOOPS TEST\n")

def get_formatted_name(firstname, lastname):
    """Return a neatly formatted name."""
    full_name = f"{firstname} {lastname}"

    return full_name.title()

# Infinite loop time!
while True:
    f_name = input("What is your first name?: ")
    if f_name == 'quit':
        break
    
    l_name = input("What is your last name?: ")
    if l_name == 'quit':
        break

    loop_result = get_formatted_name(f_name, l_name)
    print(f"\nYour full name is {loop_result}!")