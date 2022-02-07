# Chapter 5, continuation

# Looks like more of the same for now

age = 18

if age >= 18:
    print("You are old enough to vote!")
else:
    print("Nah, not old enough to vote or seep beer yet.")

# if-elif-else chain (elif = else if)

age = 18

if age < 1:
    print("IF = True")
elif age < 1:
    print("ELIF = True")
else:
    print("This should be printed if all previous checks fail!")

# NOTE: This seems to go step-by-step, that is: if the first IF returns FALSE,
#       then - and only then - will the program run ELIF part. If ELIF part 
#       returns FALSE as well, then it will move on to the next part - in this 
#       case, ELSE. Since code is set up that both checks return FALSE,
#       the program prints out the ELSE part.

# IF statement with checking a variable, and setting a variable

age = 6

if age < 4:
    price = 5
elif age < 12:
    price = 15
elif age < 18:
    price = 20
else:
    price = 25

print(f"Since you're {age} years old, the ticket costs ${price}.")

# ELSE does not have to be used. If the IF and ELIF statements all return
# FALSE result, the block will simply not do anything (without ELSE at the end). 
# In some situations, ending with ELIF is also a viable option.
# Example:

print("\nFollowing code ends with ELIF:")

age = 21

if age < 4:
    price = 5
elif age < 12:
    price = 15
elif age < 18:
    price = 20
elif age > 18:
    price = 25

print(f"That will be {price} dollars, buddy.")

# Pizza IF tests (this part seems to hammer home the point 
# that code has to be written with purpose in mind)

print("\nPizza toppings test:")

requested_topping = ['pineapple', 'pepperoni', 'cheese']

if 'pepperoni' in requested_topping:
    print("Adding pepperoni to pizza...")
if 'cheese' in requested_topping:
    print("Adding cheese to pizza...")
if 'tuna' in requested_topping:
    print("Adding tuna to pizza...")

print("Pizza done!")

# NOTE: Can't this be optimized with 'for' statement?
# Actually, I'm gonna have some fun with this!

print("\nFUN PIZZA TEST:\n")

available_toppings = ['pepperoni', 'cheese', 'chicken', 'tuna', 'pineapple',\
     'avocado']
selected_toppings = []

order_finished = False

print("Please select your toppings...")

selected_toppings = available_toppings[:3]

if order_finished == False:
    for topping in selected_toppings:
        print(f"Adding {topping} to your pizza...")
    selected_toppings = [] # Emptying the list after all toppings are added.

if selected_toppings == []:
    order_finished = True # List is empty after printing -> set order to done

if order_finished == True:
    print("Your pizza is ready!")
    order_finished = False # Reset order status after the code runs its course


# I've just spent 15 minutes wondering why this code didn't fully work.
# Turns out that I've put one '=' too many in one place. Oops!
# Also, this is written just for fun. It would make more sense to allow user to
# somehow input these toppings to the list, but that will probably come later
# in the book (I hope).