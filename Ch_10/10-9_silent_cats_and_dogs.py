# 10-9 Silent Cats and Dogs

# Modify 10-8 so that it fails silently if either file is missing.

textfiles = [r'text_files/cats.txt', r'text_files/dogs.txt']

for file in textfiles:
    try:
        with open(file) as f:
            pet_names = f.read()
            print(f"File {file} contains the following names: \n{pet_names}")
    except FileNotFoundError:
        pass