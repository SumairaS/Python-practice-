"""
Installing update OS packages/repositories  
"""
import subprocess

 

def run_yum_update():

    try:

        # Run the 'sudo yum update -y' command

        subprocess.check_call(['sudo', 'yum', 'update', '-y'])

        print("Yum update completed successfully.")

    except subprocess.CalledProcessError as e:

        print(f"Error: {e}")

    except Exception as e:

        print(f"An unexpected error occurred: {str(e)}")

 

if __name__ == "__main__":

    run_yum_update()