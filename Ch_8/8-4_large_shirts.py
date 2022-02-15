# 8-4 Large Shirts
# NOTE: Use code from 8-3. 
# Modify the function so that default values are specified. 
# Then print with default values, next medium size, then all custom values. 
def make_shirt(text_size = 'large', text_contents = 'I love Python!'):
    """Display information about text printed on a shirt."""
    
    print(f"The message will be printed in {text_size} text, with the "
    "following contents:")
    print(f"\t{text_contents}\n")

# Default print
make_shirt()

# Medium size print
make_shirt('medium')

# All custom print
make_shirt('small', 'POG')