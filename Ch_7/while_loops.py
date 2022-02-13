# Chapter 7
# WHILE loops
# FOR loops are executed only once. WHILE loops are executed as long as
# conditions to do so are met. 
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1 # +1 to 'current_number' at the end of loop

# NOTE: operator '+=' here basically equals to 'current_number + 1'. 
# Kind of a shortcut. Very nice and clean!

# Making a program run non-stop unless user ends it
prompt = "This program will print back anything you type in"
prompt += "\nNOTE: Type in 'quit' to exit the program."
prompt += "\nType in message: "

message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
    else:
        print("Quitting the program...")

# USING A FLAG
# WHILE loops can be made to run unless as long as specified variable
# is set to TRUE (or FALSE)
print("\nFLAG TEST BELOW\n")

flag_active = True
while flag_active == True:
    message = input(prompt)

    if message == 'quit':
        flag_active = False
        print("Exiting...")
    else:
        print(message)
    
# Using 'break' to exit a loop
# 'break' stops code execution - useful when we don't want to test for
# specific conditions
print("\nBREAK TEST BELOW\n")

prompt = "Enter city name: "
message = ""

# 'while True' statement will run forever unless stopped by 'break' 
while True:
    message = input(prompt)
    
    if message == 'quit':
        break
    else:
        print(message)

# CONTINUE in loops
# Can be used to return to the beginning of the loop
print("\n'CONTINUE' TEST BELOW\n")

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue # Using it here tells Python to ignore the rest of the code
                 # and start from the beginning of the loop
    print(current_number)

# Avoiding Infinite Loops
# This loop runs forever! To stop it, press CTR+C in the Terminal!
x = 1
while x <= 5:
    print(x)

# Check every WHILE loop after writing it in order to avoid infinite loops