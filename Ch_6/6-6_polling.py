# 6-6 Polling

# Copying code from the book's 'favorite_languages.py'...

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# Make a list of people who will participate in the poll. 
# Include some of the names from the dictionary.

poll_participants = ['grzegorz', 'kacper', 'edward', 'patryk', 'jen']

# Create a message loop. If a person is already in the dictionary, create a 
# message thanking them for participating. 
# If they are not already in the dictionary, invite them to the poll. 

for participant in poll_participants:
    if participant in favorite_languages:
        print(f"Dear {participant.title()}, thank you for your input!")
    else:
        print(f"Dear {participant.title()}, PARTICIPATE IN THE POLL DANG IT!")