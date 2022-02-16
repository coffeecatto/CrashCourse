# Chapter 8
# Storing functions in modules and using them

# XXX: Importing an Entire Module
# First, create a separate .py file with a written function
# Filename: pizza.py 
import pizza

# Write the module's namefile first, then the function's name
# (separated by a single dot)
pizza.make_pizza('large', 'pepperoni', 'salami', 'cheese', 'jalapeno')

# NOTE: There is no need to import a whole file - it is possible to import
# only chosen functions from a specified file
from pizza import make_pizza

make_pizza('smol', 'pineapple', 'onions', 'tuna', 'eggs')

# In such cases, there is no need to specify namefile in front of function's 
# name, since we've already imported a specific function (or functions), so
# Python already knows what we mean

# NOTE: It is also possible to import functions while simultaneously giving
# them another call name
from pizza import make_pizza as gib_pitca

gib_pitca('medium', 'tabasco', 'chicken', 'cheese', 'carolina reaper')

# NOTE: Similar thing can be done for modules
import pizza as pp

pp.make_pizza('xxl', 'cheese')

# NOTE: It is also possible to import ALL functions while using FROM statement,
# but this can mess stuff up if Python encounters overlapping variable names etc
from pizza import *

make_pizza('smol', 'pineapple', 'onions', 'tuna', 'eggs')
