# 6-4 Glossary 2

# Store five programming words I've learned about in previous chapters
# in the dictionary. Store their meaning as values. 
# Then add five more pairs to the dictionary to check if the code will
# take them into consideration the next time it is run.

prog_words = {
    'for': 'used for loops',
    'if': 'used for tests',
    'list comprehension': 'used to create calculated lists',
    'styling': 'used to make code more readable',
    'comment': 'very important for remembering what is going on',
    'set': 'used to check contents while omitting duplicate entries',
    'boolean': 'used to assign True/False values only',
    'del': 'used for deleting entries in lists/dictionaries',
    'pop': 'used to remove entries from lists while moving them somewhere else',
    'cocaine': 'used for increasing efficiency and speed'
}

for word in prog_words:
    print(f"'{word}' is {prog_words[word]}.")