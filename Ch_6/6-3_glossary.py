# 6-3 Glossary

# Store five programming words I've learned about in previous chapters
# in the dictionary. Store their meaning as values. 

prog_words = {
    'for': 'used for loops',
    'if': 'used for tests',
    'list comprehension': 'used to create calculated lists',
    'styling': 'used to make code more readable',
    'comment': 'very important for remembering what is going on',
}

for word in prog_words:
    print(f"'{word}' is {prog_words[word]}.")