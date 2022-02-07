# 5-2 More Tests

# Have at least one True and one False variants for each following test. 

# 1. Tests for equality and inequality with strings. 

print("1. Equality, Inequality")

game = 'Tetris'

if game == 'Tetris':
    print("The game is Tetris!")
if game != 'Minecraft':
    print("The game is certainly not Minecraft (thank the gods...)")

# 2. Test using the .lower() method

print("\n2. Using .lower() in test")

game = 'Tetris'

if game.lower() == 'tetris':
    print("Lowercase test works!")
if game.lower() != 'minecraft':
    print("This line should print if result is false!")

# 3. Numerical tests involving ==, !=, >, <, >= and <=

print ("\n3. Numerical tests with ==, !=, >, <, >= and <=")

ammo = 21

print(ammo == 21)
print(ammo == 20)
print(ammo != 20)
print(ammo != 21)
print(ammo > 20)
print(ammo > 21)
print(ammo < 22)
print(ammo < 21)
print(ammo >= 21)
print(ammo >= 22)
print(ammo <= 21)
print(ammo <= 20)

# 4. Tests using the 'and', 'or' keywords

print("\n4. Tests using 'and', 'or'")

# AND
# True
ammo = 21
gun = 'glock'

if ammo == 21 and gun == 'glock':
    print("Gun is fully loaded.")
else:
    print("You can reload.")

# False
ammo = 9
gun = 'glock'

if ammo == 21 and gun == 'glock':
    print("Gun is fully loaded.")
else:
    print("You can reload.")

# OR

# TRUE
temperature = '-6'
cold_wind = True

if temperature <= '-6' or cold_wind == True:
    print("You'll catch a cold if you stay outside.")

# FALSE
temperature = '21'
cold_wind = False

if temperature <= '-6' or cold_wind == True:
    print("You'll catch a cold if you stay outside.")
else:
    print("Quite a warm day today, eh?")

# 5. Is an item on the list

print("\n5. Testing 'in'")

milks = ['soy', 'cow', 'almond']

print('soy' in milks)
print('oat' in milks)

# 6. Is an item NOT on the list

print("\n6. Testing 'not in'")

milks = ['soy', 'cow', 'almond']

print('oat' not in milks)
print('soy' not in milks)
