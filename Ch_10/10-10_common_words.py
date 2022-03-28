# 10-10 Common Words

# Get a few text files with a lot of words (I'll use the ones I already have 
# from previous exercises). 
# Write a program that reads these files and counts how many times the word
# 'the' appears in each file. 
# Use a space after 'the' so it doesn't count words like 'there' etc. 

filenames = [r'text_files/aliceNOT.txt', r'text_files/siddhartha.txt', 
             r'text_files/moby_dick.txt', r'text_files/little_women.txt',
             r'text_files/alice.txt']

def count_words(filename, word):
    """Counts how many times a given word appears in a text file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"ERROR: File {filename} not found.")
    else:
        count = contents.lower().count(word)
        print(f"'{word}' appears {count} times in file {filename}!")

for filename in filenames:
    count_words(filename, 'the ')