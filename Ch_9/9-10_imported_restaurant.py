# 9-10 Imported Restaurant

# Store 'Restaurant' class in a module, then import it here
# and create an instance to prove that stuff works.

# NOTE: I could probably import the class straight from exercise 9-1, but
# dashes in the filename seem to break the import process. Ehh. 

from ch9_modules import Restaurant

hot_noodles = Restaurant('Hot Noodles', 'asian food')

# Testing functions
hot_noodles.describe_restaurant()
hot_noodles.open_restaurant()