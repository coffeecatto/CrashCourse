# Chapter 10

# Writing to files

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("123 ASD !@# textfile write test!")
    # NOTE: Python can only write strings to a file.
    # In case of numbers, they'll have to be converted to plain strings first.

# NOTE 2: Looks like Python will write to file in the same manner as it 
# 'prints' stuff to the terminal (for example: if I want stuff to be in
# a new line in the file, then I'll need to use the '\n' thingy). 

with open(filename, 'w') as file_object:
    file_object.write("123 ASD !@# textfile write test!")
    file_object.write("\tTab test!")
    file_object.write("\nNew line test!")

# APPENDING TO A FILE
# Basically, adding stuff without erasing already existing contents!

with open(filename, 'a') as file_object:
    file_object.write("\nHello world! Or something!")