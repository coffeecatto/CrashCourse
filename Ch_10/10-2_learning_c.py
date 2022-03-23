# 10-2 Learning C

# replace() can be used to replace words in strings. 
# For example, replace ('dog', 'cat') will replace all instances of dogs with
# cats. 

# Read each line from the learning_python.txt, replace 'Python' with something
# else, then print the modified message. 
# This has to print all lines from the file.

filename = r'text_files\learning_python.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.replace('Python', 'Soviet Russia').rstrip())
        # Now that's a combo I did not expect to work for some reason