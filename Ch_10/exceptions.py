# Chapter 10

# Exceptions - TRY-EXCEPT blocks

# Use this stuff to keep the program running even if things break along
# the way (should be careful with this, obviously)
try:
    print(5/0)
except ZeroDivisionError:
    print("Yeah, no, please do not try to divide by zero.")
    
# USING EXCEPTIONS TO PREVENT CRASHES
print("Provide to numbers for division.")
print("Type 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("ERROR: Hey, stop trying to divide by zero!")
    except ValueError:
        print("ERROR: Are you trying to divide with letters?")
    else:
        print(f"\nResult: {answer}")
        
# FILENOTFOUNDERROR EXCEPTION
filename = r'aliceNOT.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"File {filename} not found. Are you sure it exists?")
    
# ANALYZING TEXT
# split() can be used to build a list from words in a string
title = "Alice in Wonderland"
title.split()
print(title)

# Counting how many words there are in Alice in Wonderland

def count_words(filename):
    """Counts the amount of words in a given file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"File {filename} not found. Are you sure it exists?")
    else:
        # Time to count words
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} contains {num_words} words!")
    
filename = r'text_files/alice.txt'
count_words(filename)

# Using it in a loop with a list
print("\nLoop-dee-doo time\n")
filenames = [r'text_files/aliceNOT.txt', r'text_files/siddhartha.txt', 
             r'text_files/moby_dick.txt', r'text_files/little_women.txt',
             r'text_files/alice.txt']

for filename in filenames:
    count_words(filename)

# NOTE: Thanks to the 'except' block, the code does not stop running after
# encountering an error immediately with the first file. 

# FAILING SILENTLY
# PASS statement can be used to tell Python to do absolutely nothing. 
try:
    print(5/0)
except ZeroDivisionError:
    pass