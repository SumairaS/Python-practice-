"""
Run time Error

When we excute the program if something goes wrong 

"""
try:

    # Code that may raise exceptions

    x = int(input("Enter a number: "))

    result = 10 / x

    

    # Additional code that may raise exceptions

    y = int(input("Enter another number: "))

    result = result / y

except ValueError:

    # Handling the ValueError (invalid input)

    print("Invalid input. Please enter a valid number.")

except ZeroDivisionError:

    # Handling the ZeroDivisionError (division by zero)

    print("Error: Division by zero is not allowed.")

except Exception as e:

    # Handling any other unexpected exceptions

    print(f"An error occurred: {e}")

else:

    # Code to execute if no exceptions occurred

    print(f"Result: {result}")

finally:

    # Code that always executes, for cleanup or resource release

    print("Cleanup or resource release")

 

# Code after the try-except block

print("End of program")