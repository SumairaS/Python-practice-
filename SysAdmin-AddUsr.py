"""
Add users 
"""
import os
def new_user(): 
    confirm = "N" 
    while confirm != "Y": 
        username = input("Enter the name of the user to add: ") 
        print("Use the username '" + username + "'? (Y/N)")
        confirm = input().upper()
        os.system("sudo adduser " + username)
        print(f"user added",username)
new_user()

import os

def remove_user():

    confirm = "N" 

    while confirm != "Y": 

        username = input("Enter the name of the user to remove: ") 

        print("Remove the user : '" + username + "'? (Y/N)") 

        confirm = input().upper()

        os.system("sudo userdel -r " + username)
        
        print(f"removed",username)

        
remove_user()