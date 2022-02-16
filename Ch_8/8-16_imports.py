# 8-16 Imports
# Copy code from a previous program that uses one function into a separate
# file, then use all import methods in here

# Standard import
print("Standard import:")

import sandvich
sandvich.make_sandwich('ham')

# from module_name import function_name
print("\nfrom module_name import function_name:")

from sandvich import make_sandwich
make_sandwich('jalapeno', 'cheese')

# from module_name import function_name as fn
print("\nfrom module_name import function_name as fn:")

from sandvich import make_sandwich as gib_kanapka
gib_kanapka('kielbasa sausage', 'onions')

# import module_name as mn
print("\nimport module_name as mn")

import sandvich as tf
tf.make_sandwich('garlic', 'onions')

# from module_name import *
print("\nfrom module_name import *")

from sandvich import *
make_sandwich('yes', 'no')