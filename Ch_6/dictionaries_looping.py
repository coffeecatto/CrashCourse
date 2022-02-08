# Chapter 6
# Dictionaries and loops

# Looping through key-values pairs
# To check for items (i.e. key-values pairs), use method .items()
# Similarly, to check only for keys, use .keys(), and .values() for values

# .items()
user_0 = {
    'username': 'vacool',
    'first': 'grzegorz',
    'last': 'wu',
}
print(user_0)

for key, value in user_0.items():
    print(f"\nKey: {key.title()}")
    print(f"Value: {value.title()}")

# Another example
print("\nAnother example")
fav_langs = {
    'kacper': 'python',
    'dariusz': 'python',
    'grzegorz': 'uninstall',
    'jakub': 'react',
    'steve': 'swift', # It's a good practice to include comma at the end
    }

for name, lang in fav_langs.items():
    print(f"{name.title()}'s favorite language is {lang.title()}.")

# .keys()
print("\n.keys() method")

fav_langs = {
    'kacper': 'python',
    'dariusz': 'python',
    'grzegorz': 'uninstall',
    'jakub': 'react',
    'steve': 'swift', # It's a good practice to include comma at the end
    }

for key in fav_langs.keys():
    print(key.title())

# NOTE: Python goes for KEYS first, so in such cases, using .keys() method
#       is not necessary. Outcome will be the same with and without it!

# In loops, currently 'active' key can be used to retrieve its value
print("\nRetrieving value from active keys")

friends = ['kacper', 'grzegorz']
for name in fav_langs:
    print(name.title())
    if name in friends:
        language = fav_langs[name].title()
        print(f"Hi {name.title()}, your fav language is {language}!")

# NOTE: The above print would also work if I didn't define 'language', 
#       but used 'fav_langs[name].title()' in the print itself. 

# Looping in a particular order
# This is similar to lists
print("\nLooping sorted dictionary")

for name in sorted(fav_langs):
    print(name.title())

# .values()
print("\n.values() method")

# This will print ALL values in a dictionary
for lang in fav_langs.values():
    print(lang.title())

# If I want to avoid repeat entries, I have to use 'set' thingy
# NOTE: Set can be applied to lists too. 
print("'Set' print")
for lang in set(fav_langs.values()):
    print(lang.title())

# Sets can also be 'created' by using braces - similarly to creating a 
# dictionary, but without using ':' to assign values to keys. 
print("\nCreated set")
superset = {'python', 'python', 'ruby', 'rust', 'ruby', 'uninstall'}
print(superset)