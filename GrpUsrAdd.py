"""
Your module description
"""

import os

 

# Define the username and group name

username = "user_to_add"

groupname = "group_to_add_to"

 

# Add the user to the group (requires superuser privileges)

os.system(f"sudo usermod -aG {groupname} {username}")

print(f"User '{username}' has been added to the group '{groupname}'.")