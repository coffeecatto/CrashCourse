# Chapter 10
# Files and Exceptions

# NOTE: Had to enable 'Python > Terminal: Execute In File Dir' first, otherwise
# VSCodium tried to find the file in the parent folder of the exercises
# (i.e. it tried to look for the file in 'CrashCourse' folder, not in 'Ch_10')
with open('text_files\pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

# Using absolute paths (as variables to make things easier)
# NOTE: Using 'r' in front converts the following to a raw string.
# If I do not do that, Python throws a OSError: [Errno 22]. 
# From what I gather, this is because by default, Python reads stuff like
# '/f' as form feed characters or something. 
# Also, people recommend importing path from pathlib in order to solve
# this and make the code more portable at the same time. 
file_path = r'F:\Programowanie\git\CrashCourse\Ch_10\text_files\pi_digits.txt'

with open(file_path) as file_object:
    contents = file_object.read()
print(contents)

# READING LINE BY LINE
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())
        
# Making a list of lines from a file
the_million_digits_file = r'text_files\pi_million_digits.txt'
with open(the_million_digits_file) as file_object:
    lines = file_object.readlines() # readlines reads each line and stores it
                                    # in a list

# Working with file's contents
pi_string = ''
for line in lines:
    pi_string += line.strip() # strips all the empty spaces

print(pi_string[:52])
print(len(pi_string))

# Large files: ONE MILLION DIGITS and finding your birthday date in Pi
birthday = input("Enter your birthday date as mmddyy format:")
if birthday in pi_string:
    print("Your birthday is present in the first million digits of Pi!")
else:
    print("Nope, your birthday is not in the first million digits of Pi.")