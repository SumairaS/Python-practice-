"""
add_user_to_group
"""
import subprocess

 

def add_user_to_group(username, group_name):

    try:

        # Use the 'usermod' command to add the user to the group

        subprocess.check_call(['sudo', 'usermod', '-aG', group_name, username])

        print(f"User '{username}' added to group '{group_name}' successfully.")

    except subprocess.CalledProcessError as e:

        print(f"Error: {e}")

    except Exception as e:

        print(f"An unexpected error occurred: {str(e)}")

 

if __name__ == "__main__":

    username = input("Enter the name of the user: ")

    group_name = input("Enter the name of the group: ")

    

    add_user_to_group(username, group_name)