# 9-12 Multiple Modules

# Same as 9-11, but User class has to be stored in a seperate file from
# Privileges and Admin classes. 

# from user_basemodule import User # <- apparently code works without this
from user_additional import Privileges, Admin

# Creating an admin instance
superuser = Admin('Superfly', 'Johnson', 42, 'male', 'reddit mod', 0)

# Print privileges, info
superuser.describe_user()
superuser.privileges.show_privileges()