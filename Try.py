"""
Your module description
"""
try:

    result = 10 / 0  # This will raise a ZeroDivisionError (a subclass of ArithmeticError)

except ArithmeticError as e:

    # Access the error message using the args attribute

    error_message = e.args[0]

    print(f"ArithmeticError message: {error_message}")