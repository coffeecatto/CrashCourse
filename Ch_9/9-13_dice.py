# 9-13 Dice

# Make a Die class with one attribute - sides. Default value: 6. 
# Create a method called roll_die() - it should print a random number, from 1 
# to the number of sides that the die has. 
# Make a 6 sided die and roll it 10 times. 
# Make a 10 and 20 sided dice and roll each 10 times.

class Die:
    """RNG for rolling dice. Number of sides can be specified."""
    
    def __init__(self, sides):
        """Checks for number of sides of a die (6 by default)."""
        self.sides = sides
    
    def roll_die(self, times): # Will print each roll result in a new line.
        """Rolling dice. Prints result at the end of a roll."""
        from random import randint
        self.times = times
        
        while times != 0:
            roll_result = randint(1, self.sides)
            times += -1
            
            print(f"Result: {roll_result}.")
    
    def roll_die_list(self, times): # Stores all rolls in a list, then prints. 
        """Rolling dice. Prints a list with results at the end of a roll."""
        from random import randint
        self.times = times
        
        results_list = []
        
        while times != 0:
            roll_result = randint(1, self.sides)
            results_list.append(roll_result)
            times += -1
            
        print(f"Results: {results_list}.")

        
# Testing if stuff works
print("Rolling D6!")
d6 = Die(6)
d6.roll_die(10)

print("\nRolling D10!")
d10 = Die(10)
d10.roll_die(10)

print("\nRolling D20!")
d20 = Die(20)
d20.roll_die(10)

# Created roll_die_list method, testing if it works (should print results
# as a list, instead of printing each roll result in a separate line)
print("\nRolling D6!")
d6.roll_die_list(10)

print("\nRolling D10!")
d10.roll_die_list(10)

print("\nRolling D20!")
d20.roll_die_list(10)