# 9-11 Imported Admin

# Import User, Privileges and Admin classes from one file, then 
# create an Admin instance and print show_privileges() to check if
# everything is in order. 

# Importing from the general module file
from ch9_modules import User, Privileges, Admin

# Creating an admin instance
superuser = Admin('Superfly', 'Johnson', 42, 'male', 'reddit mod', 0)

# Print privileges
superuser.privileges.show_privileges()