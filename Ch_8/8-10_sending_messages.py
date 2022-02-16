# 8-10 Sending Messages
# Copy code from 8-9
# Write a function called send_messages() that prints each message and then
# moves it into new list sent_messages. 
# Print both lists after calling the function to verify it works correctly. 
def show_message(messages):
    print("List of messages:")
    for msg in messages:
        print(f"\t{msg}") # Using \t to make the list indented (looks nice)

def send_messages(listname, sent_messages):
    while listname:
        current_message = listname.pop()
        print(f"Now moving message: '{current_message}'...")
        sent_messages.append(current_message)

short_msg_list = ['be right there', 'maybe later', 'gonna grab a beer now', \
    'it costs 400.000 dollars to fire this weapon for 12 seconds']
sent_messages = []

# Now to call the functions
send_messages(short_msg_list, sent_messages)
show_message(short_msg_list)
show_message(sent_messages)