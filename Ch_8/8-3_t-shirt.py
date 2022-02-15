# 8-3 T-Shirt
# Write a function called make_shirt() that accepts size and the text of
# a message that should be printed on the shirt.
# Then, call the function twice: one time using pos args, second time
# using key args. 
def make_shirt(text_size, text_contents):
    """Display information about text printed on a shirt."""
    text_size = int(text_size)
    
    print(f"The message will be printed in font size {text_size}, with the "
    "following text:")
    print(f"\t{text_contents}")

# Pos args call
make_shirt('12', 'Happy birthday you old bastard!')

# Key args
make_shirt(text_size = '16', text_contents = 'PARTY TIME')