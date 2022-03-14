# Python Standard Library
# A set of modules provided with every Python installation

# randint
# Takes two arguments (numbers) and returns a random one from the given
# range. 
# Basically an RNG!
from random import randint
print(randint(0, 420))

# choice()
# Takes a random element from a tuple/list
from random import choice

players = ['vacool', 'blue', 'emce', 'coffeecatto']
first_player = choice(players)
print(first_player)