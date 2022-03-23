# 10-1 Learning Python

# Store a few lines that summarize what I've learned about Python, in a
# separate text file called learning_python.txt.
# Then make the program read the lines with the following methods:
# - by reading the entire file
# - by looping over the file object
# - by storing lines in a list first

filename = r'text_files\learning_python.txt'

# Reading the entire file
print("1. Reading the entire file:")
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

# Looping over the file object
print("\n2. Looping over the file object:")
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip()) # strips the blank lines

# Storing lines in a list first
print("\n3. Storing lines in a list:")
with open(filename) as file_object:
    lines_list = file_object.readlines()
    for line in lines_list:
        print(line.rstrip())


# NOTE: .txt files with 'UTF-8 with Signature' encoding give some weird
# characters at the beginning of the output. 
# Switching to plain UTF-8 or ANSI solves this issue.