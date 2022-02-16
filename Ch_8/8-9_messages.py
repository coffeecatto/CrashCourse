# 8-9 Messages
# Make a list of short messages, then create a function that prints
# each message
def show_message(messages):
    print("List of messages:")
    for msg in messages:
        print(f"\t{msg}") # Using \t to make the list indented (looks nice)

short_msg_list = ['be right there', 'maybe later', 'gonna grab a beer now', \
    'it costs 400.000 dollars to fire this weapon for 12 seconds']

show_message(short_msg_list)