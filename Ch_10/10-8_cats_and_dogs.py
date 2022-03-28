# 10-8 Cats and Dogs

# Make two files with three names each in them: cats.txt and dogs.txt. 
# Read these files and print their contents. 
# Write it in a TRY-EXCEPT block that accounts for FileNotFoundError error. 

textfiles = [r'text_files/cats.txt', r'text_files/dogs.txt']

for file in textfiles:
    try:
        with open(file) as f:
            pet_names = f.read()
            print(f"File {file} contains the following names: \n{pet_names}")
    except FileNotFoundError:
        print(f"ERROR: Couldn't find the following file: {file}.")