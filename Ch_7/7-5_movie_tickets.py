# 7-5 Movie Tickets
# Ticket price changes based on person's age:
# - under 3 years old -> FREE
# - between 3-12 -> $10
# - over 12 -> $15

# Write a loop asking user about their age, then print the ticket's price
prompt = "Please type in your age: "
age = ""

# NOTE: I'm using 'age' variable for setting up the WHILE loop in order to
# avoid infinite loop here - the book does not specify if it should be an
# infinite loop or not, so I'm guessing the latter is the desired outcome. 
while age == "":
    age = input(prompt)
    age = int(age)

    if age < 3:
        print("The ticket is free!")
    elif age >= 3 and age <= 12:
        print("Ticket cost: $10.")
    elif age > 12:
        print("Ticket costs $15.")