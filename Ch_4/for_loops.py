# Chapter 4 - 'for' Loops!

# General file for testing stuff from this Chapter.

# Create a list first
magicians = ['copperfield', 'vernon', 'hermann']

# Now create a 'for' loop 
for magician in magicians:
    print(magician)

# NOTE: typing 'magician' after 'for' apparently makes a variable out of it. Does it remember its last value?

print(f"\nLast 'magician' value: {magician}")

# It does! Yay!
# NOTE: By default, a 'for' loop will go through all the items in a list.

# Using a loop to create a separate message for each item in the list

print("\nAutomated messages go here:")

for magician in magicians:
    print(f"That's a bloody good magic trick, {magician.title()}!")

# Anything put in the indent will be a part of the loop. For example, multiple messages per person are possible thanks to this.

print ("\nMultiple messages per person:")

for magician in magicians:
    print(f"Nice trick, dear {magician.title()}!")
    print(f"Can you do the trick with disappearing cards next, {magician.title()}?\n")

# Anything put after the indented part (so basically, further, non-indented stuff) is not a part of the loop. 
# The following message, for example, is outside of the loop, since it is not indented.

print("Thanks, nice tricks guys!")

# Unnecessary indents can break the code, so it's important to be careful about this. 
# Although VSCodium seems to indent stuff automatically, so it shouldn't be much of an issue - at least for now. 
# In any case, incorrect indents will either be visible through weird program behavior, or by causing errors - Python will tell what's going in in the latter case. 

