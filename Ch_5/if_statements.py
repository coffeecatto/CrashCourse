# Chapter 5 - IF statements

# Can be used in 'for' loops for setting conditions
# '==' means 'equals to' 

cars = ['audi', 'nissan', 'bmw', 'porsche', 'ferrari']

for i in cars:
    if i == 'bmw':
        print(i.upper())
    else:
        print(i.title())

# Conditional tests
# Checking for equality

# Most conditional tests compare current value of variable to the specific,
# provided value.
# If result of the statement is True, then program will proceed further
# with the code. If result is False, then any further actions within that
# IF statement are not executed. 

car = 'bmw'
if car == 'bmw':
    print("True")
else:
    print("False")

print("\nSeparator\n")

# NOTE: Testing for equality is case sensitive, but can be worked around
# (if necessary) by using, for example, .lower() stuff

car = 'Audi'
print(car)
if car.lower() == 'audi':
    print("\nYep, using lower() works!")
else:
    print("\nSomething is no yes...")

# Checking for inequality - use !=

print("\nChecking for inequality")

requested_topping = 'pepperoni'

if requested_topping != 'pineapple':
    print("Thank god it's not a pineapple pizza!")

# This also works with numbers (of course!)

print("\nNumbers test!")

answer = 21

if answer != 42:
    print("That's not the answer to question of life, universe and everything!")

# >, <, >=, <= also work

# Checking multiple conditions
# Can use 'and' to combine multiple conditions. If all are met, then
# the statement is True. If not, False.
# NOTE: Shift + Enter to run only selected lines. Useful when checking whether
#       a statement is True/False. 

age_0 = 22
age_1 = 18

age_0 >= 21 and age_1 >= 21
age_0 >= 21 and age_1 <= 21

# Parentheses can be used for improved readability!

(age_0 >= 21) and (age_1 <= 21)

# Using OR expression
# Will fail only if all tests fail/return false

age_0 = 22
age_1 = 18

age_0 >= 21 or age_1 >= 21

# Checking whether a value is in a list
# Use keyword 'in' for this

toppings = ['pepperoni', 'cheese', 'tuna', 'pineapple']

'mushrooms' in toppings
'pepperoni' in toppings

# Use 'not in' for the opposite

banned_users = ['kokuslaw', 'pigul', 'marek']
user = 'bluep'

if user not in banned_users:
    print(f"{user}, you are free to post a message!")

# Boolean expressions
# It can be either True or False, so it's useful for verifying states
# of various stuff (for example - is the game windows active)

game_window_active = True
can_edit = False
