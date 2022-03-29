# Chapter 10

# Storing Data & JSONs

# json.dump() and json.load()
import json

numbers = [2, 4, 6, 7, 9, 21, 42]
filename = r'json/numbers.json'

with open(filename, 'w') as f:
    json.dump(numbers, f)

# Import data from file
with open(filename) as f:
    imported_numbers = json.load(f)
    
print(imported_numbers)