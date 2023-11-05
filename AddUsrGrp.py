"""
USer added to grp by Arpita
"""

import os

 

# Define the username and group name

username = "userX"

groupname = "ec2-user"

 

# Add the user to the group (requires superuser privileges)

os.system(f"sudo usermod -aG {groupname} {username}")

print(f"User '{username}' has been added to the group '{groupname}'.")